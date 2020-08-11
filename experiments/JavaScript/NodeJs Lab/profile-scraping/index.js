const puppeteer = require("puppeteer");
const fs = require("fs");

(async () => {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  await page.goto("https://www.instagram.com/snn.krn/");

  const images = await page.evaluate(() => {
    //console.log("---------------------------------0");
    const imagePosts = document.querySelectorAll("article img");
    //console.log("---------------------------------1");
    const imagesList = [...imagePosts];
    //console.log("---------------------------------2");
    const list = imagesList.map(({ src }) => ({ src }));
    //console.log("---------------------------------3");

    return list;
  });

  fs.writeFile("instagram.json", JSON.stringify(images, null, 2), (error) => {
    if (error) throw new Error("Unknown error");
    console.log("Done");
  });

  //await page.screenshot({ path: "github2.png" });

  await browser.close();
})();
