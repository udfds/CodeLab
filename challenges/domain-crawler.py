import urllib.request

default_url = "https://elixir-lang.org"
pages_visited = []

def get_src(item):
    start = item.index('src="') + 5
    end = item.index('"', start)
    return item[start:end]

def get_href(item):
    start = item.index('href="') + 6
    end = item.index('"', start)
    return item[start:end]

def is_external(item):
    return 'http' in item

def clean_list(my_list):
    return list(dict.fromkeys(my_list))

def print_list(my_list):
    for item in my_list:
        print(" --", item)

def crawler(url):
    pages_visited.append(url)
    pages_visited.append(url + "/")

    # Request the page
    try:
        read_url = urllib.request.urlopen(url)
        bytes = read_url.read()

        # Get the content
        content = bytes.decode("utf8")
        read_url.close()
    except:
        print("Page ", url, " not available")
        return -1

    resources = []
    others = []
    pages = []
    links = []

    # Build the tag buffer
    for char in content:
        if char is '<':
            buffer = char
        elif char is '>':
            buffer += char
            if 'src="' in buffer:
                src = get_src(buffer)
                resources.append(src)
                continue

            if 'rel="' in buffer and '<link' in buffer:
                href = get_href(buffer)
                others.append(href)
                continue

            if 'href="/' in buffer:
                href = get_href(buffer)
                pages.append(href)
                continue

            if 'href="http' in buffer:
                href = get_href(buffer)
                links.append(href)
                continue

            buffer = ''
        else:
            buffer += char

    print("\n- Static assets in ", url)

    # Explore the resources
    resources = clean_list(resources)
    print_list(resources)

    # Explore the others
    others = clean_list(others)
    print_list(resources)

    print("\n- Pages in ", url)

    # Explore the pages
    pages = clean_list(pages)
    print_list(pages)

    # Explore links
    show_links = False
    if show_links is True:
        print("\n - Links in ", url)

        links = clean_list(links)
        print_list(links)

    # Crawler pages
    for item in pages:
        link = default_url + item
        if not link in pages_visited:
            crawler(link)


crawler(default_url)
