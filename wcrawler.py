#LIBS
import sys
import requests
from bs4 import BeautifulSoup

#LISTS
TO_CRAWL = []
CRAWLED = set()

#REQUEST
def request(url):
    header = {"User-Agent": "browser"}
    #EXAMPLE: 'header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}'
    try:
        response = requests.get(url, headers=header)
        return response.text
    except KeyboardInterrupt:
        sys.exit(0)
    except:
        pass

#LINKS
def get_links(html):
    links = []
    try:
        soup = BeautifulSoup(html, "html.parser")
        tags_a = soup.find_all("a", href=True)
        for tag in tags_a:
            link = tag["href"]
            if link.startswith("http"):
                links.append(link)

        return links
    except:
        pass

#CRAWLER
def crawl():
    while 1:
        if TO_CRAWL:
            url = TO_CRAWL.pop()

            html = request(url)
            if html:
                links = get_links(html)
                if links:
                    for link in links:
                        if link not in CRAWLED and link not in TO_CRAWL:
                            TO_CRAWL.append(link)

                print("Crawling {}".format(url))

                CRAWLED.add(url)
            else:
                CRAWLED.add(url)
        else:
            print("Done")
            break

#MAIN
if __name__ == "__main__":
    url = sys.argv[1]
    TO_CRAWL.append(url)
    crawl()
