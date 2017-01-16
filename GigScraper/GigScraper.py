import sys
import urllib.request
from bs4 import BeautifulSoup
import datetime
from RippingPage import RippingPage
from TktsScotlandPage import TktsScotlandPage
from Gig import Gig
from GigDb import GigDb

GigsDbPath = r"G:\MyStuffProgramming\Python\WebScrapers\GigScraper\Gigs.db"

def GetUrlContent(url):
    try:
        with urllib.request.urlopen(url, None, 5) as response:
            content = response.read()
            return content
    except urllib.request.URLError:
        print("...failed")
        return ""
    except:
        print("...caught an unhandled exception (OpenUrl)")
        return ""
 
def SaveContent(path, content):
    soup = BeautifulSoup(content)
    print(soup.prettify)

    prettifiedText = soup.prettify()
    print(type(prettifiedText))

    sampleFile = open(r'G:\MyStuffProgramming\Python\RippingScrape\ripping_nov.txt', 'w')
    sampleFile.write(prettifiedText)
    sampleFile.close()

def main():
    
    #now = datetime.datetime.now()
    #currentMonth = now.month
    #print(now)
    #print(currentMonth)
    #for month in range(currentMonth, 12 + 1):
        #print(month)
        #url = rippingUrlPageOne.format(month)
    #content = GetUrlContent(RippingUrlPageNov)
    #SaveContent(r'G:\MyStuffProgramming\Python\RippingScrape\ripping_nov.txt', content)

    gig1 = Gig("band1", "venue1", "edinburgh", "0-0-0", "0")
    gig2 = Gig("band2", "venue2", "edinburgh", "0-0-1", "1")
    gig3 = Gig("band3", "venue3", "edinburgh", "0-0-1", "1")

    print(gig1)
    print(gig2)

    gigDb = GigDb(GigsDbPath)

    gigDb.AddGig(gig1)
    gigDb.AddGig(gig2)
    gigDb.AddGig(gig3)


    print("gig1 exists = {0}".format(gigDb.GigExists(gig1)))
    print("gig2 exists = {0}".format(gigDb.GigExists(gig2)))
    print("gig3 exists = {0}".format(gigDb.GigExists(gig3)))

    return


    sampleFile = open(r'G:\MyStuffProgramming\Python\RippingScrape\ripping_nov.txt', 'r')
    sampleContent = sampleFile.read()


    print("Retrieving gigs from....", end="")  
    gigDb = GigDb(GigsDbPath)

    # Get the gigs from Ripping Records
    print("Ripping Records")
    rippingPage = RippingPage(sampleContent)
    gigs = rippingPage.GetGigs()
    gigDb.AddGigs(gigs)

    # Get the gigs from Tickets Scotland
    print("                        Tickets Scotland")
    tktsScotlandPage = TktsScotlandPage()
    gigs = tktsScotlandPage.GetGigs()
    gigDb.AddGigs(gigs)

    gigDb.Close()

    print("Finished")

if __name__ == "__main__":
    try:
        main()
    except:
        print("Unexpected error: ", sys.exc_info()[0])
        print("Exiting program: Unhandled exception")
