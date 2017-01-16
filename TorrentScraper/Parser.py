from bs4 import BeautifulSoup

def Parse(pageContent):

    #
    # Ensure we have been given some content.
    #
    if len(pageContent):
        return

    soup = BeautifulSoup(pageContent)

    #print(content)
    #print(soup.prettify())
    #print(soup)

    rows = soup.find_all("tr")

    for row in rows:
        for child in row.children:
            print(child)

    #print("***********************************************")
    #print("***********************************************")

    #alinks = soup.find_all("a")

    #for alink in alinks:
    #    print(alink)


    #print("num rows = " + str(len(tableRows)))

    #for tableRow in tableRows:
    #    print(tableRow)
    #    print("***********************************************")
    #    print("***********************************************")

    #for alink in alinks:
    #    print(alink.get("href"))

###############################################################################
###############################################################################
if __name__ == '__main__':
    try:
        main()
    except:
        print("Exiting program: Unhandled exception")