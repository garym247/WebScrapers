import sys
import urllib.request
from optparse import OptionParser
from bs4 import BeautifulSoup
import UrlCalculator
import Writer

###############################################################################
###############################################################################
def getCommandLineOptions():
    parser = OptionParser()
    
    parser.add_option(
        "-b",
        "--baseurl",
        help="Specifies the base URL."
        )
    
    parser.add_option(
        "-n",
        "--numpages",
        help="Number of pages to scan."
        )

    parser.add_option(
        "-t",
        "--type",
        help="The type of torrents to retrieve."
        )

    parser.add_option(
        "-o",
        "--output",
        help="The output file."
        )

    validTypes = ["recent", "mp3", "flac", "vidother"]

    (options, args) = parser.parse_args();
    optionsDict = vars(options)

    # Extract the command line options from the dictionary providing default
    # values where needed.
    baseUrl = optionsDict["baseurl"] 
    numPages = 50 if optionsDict["numpages"] is None else int(optionsDict["numpages"])
    torrentType = "recent" if optionsDict["type"] is None else optionsDict["type"]
    outputFile = "output" if optionsDict["output"] is None else optionsDict["output"]

    # Check that we have a base url.
    if optionsDict["baseurl"] is None:
        print("A base URL has not been provided")

    # Check that we have a valid type.
    if optionsDict["type"] not in validTypes:
        print("Not a valid type")
    else:
        print("found valid type = " + optionsDict["type"] )

    return (baseUrl, numPages, torrentType, outputFile)

###############################################################################
###############################################################################
def OpenUrl(url):
    print("Attempting to open..." + url, end="")

    try:
        uf = urllib.request.urlopen(url, None, 5)
        content = uf.read()
    except urllib.request.URLError:
        print("...failed")
        return ""
    except:
        print("...caught an unhandled exception (OpenUrl)")
        return ""

    print("....success ({0} bytes read)".format(len(content)))

    return content

###############################################################################
###############################################################################
def ReadTestFile(filePath):
    file = open(filePath, 'r+')
    content = file.read()
    file.close()

    print(type(content))
    #print(content)

    bytesContent = bytes(content, 'utf-8')

    return bytesContent

###############################################################################
###############################################################################
def WriteTestFile(filePath, content):
    file = open(filePath, 'w+')
    print(type(content))

    decodedString = content.decode()

    file.write(decodedString)
    file.close()

###############################################################################
###############################################################################
def WriteLinks(filePath, links):
    file = open(filePath, 'w+')
    print(type(links))

    file.write(str(links))
    file.close()

###############################################################################
###############################################################################
def Parse(content):
    try:
        soup = BeautifulSoup(content)
        pretty = soup.prettify()
    
        #s = content.decode(errors='ignore')
        #s_ansii = s.encode(encoding ='ansii', errors='ignore')
        #print(s_ansii)

        mainContent = soup.find(id="main-content")

        rows = soup.find_all("tr")

        for child in rows[1].children:
            print("found child")
            for row in rows[1:]:
                category = row.td.center.a
                rowContents = row.contents
                for rowContent in row.contents:
                    if hasattr(rowContent, "td"):
                        print("row has data")
                    else:
                        print("row has NO data")

                categoryContents = category.contents
        #except AttributeError:
        #    print("Failed to extract data from row")

        numRows = len(rows)

        return

        print("********* a links *********")
        links = soup.find_all("a")

        print(type(links))

        x = len(links)

        #print("Number of links = " + str(len(links)))
        #for link in links:
        #    print("link = " + str(link))
    except UnicodeEncodeError as err:
        print("Caught a UnicodeEncodeError: {0}: ".format(err))
    except:
        print("Unexpected error in Parse() ", sys.exc_info()[0])


###############################################################################
###############################################################################
def main():

    content = ReadTestFile(r"g:\pirate_bay_test.htm")
    Parse(content)
    sys.exit()


    #(baseUrl, numPages, torrentType, outputFile) = getCommandLineOptions()

    print("Openning pages")

    urlCalculator = UrlCalculator.UrlCalculator("", 0)
    urls = urlCalculator.GetUrls()

    writer = Writer.Writer()

    for url in urls:
        content = OpenUrl(url)


        #WriteTestFile(r"g:\pirate_bay_test.htm", content)
        torrents = Parse(content)

        WriteLinks(r"g:\pirate_bay_links.txt", torrents)

        #Write(torrents)


###############################################################################
###############################################################################
if __name__ == '__main__':
    try:
        main()
    except:
        print("Unexpected error: ", sys.exc_info()[0])
        print("Exiting program: Unhandled exception")
