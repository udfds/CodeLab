const puppeteer = require('puppeteer')

async function start() {

    // -----------------------------------------------------------------------------
    // Functions
    // -----------------------------------------------------------------------------

    async function loadMore(page, selector) {
        let moreButton = await page.$(selector);
        if (moreButton) {
            console.log('   -- Load more');
            await moreButton.click();
            await page.waitFor(selector, { timeout: 2000 }).catch(() => {
                console.log('   -- Timeout');
            });
            await loadMore(page, selector);
        }
    }

    async function getComments(page, selector) {
        let comments = await page.$$eval(selector, links => {
            return links.map(link => {
                return link.innerText
            });
        });

        return comments;
    }

    function usersCount(allMentions) {
        let usersByCount = {};
        allMentions.forEach(user => {
            usersByCount[user] = (usersByCount[user] || 0) + 1;
        });

        return usersByCount;
    }

    function usersSort(usersByCount) {
        let entries = Object.entries(usersByCount);

        return entries.sort((entryA, entryB) => { return entryB[1] - entryA[1] })
    }

    // -----------------------------------------------------------------------------
    // Actions
    // -----------------------------------------------------------------------------

    let browser = await puppeteer.launch();
    let page = await browser.newPage();

    console.log('   -- Go to page!');
    await page.goto('https://www.instagram.com/p/CDTXDdEF6WC/');
    await loadMore(page, '.dCJp8');

    let comments = await getComments(page, '.C4VMK span a');

    let result = usersSort(usersCount(comments));
    result.forEach(user => {
        if (user[1] > 1) {
            console.log('User:' + user[0] + ' - mentions:' + user[1]);
        }
    });

    browser.close();
}

start();