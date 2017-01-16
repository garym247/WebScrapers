from bs4 import BeautifulSoup
import Gig

RippingUrlPageOne = r"http://www.rippingrecords.com/tickets.php?month={0}"
RippingUrlPageOther = r"http://www.rippingrecords.com/tickets.php?page={0}&month={1}"

RippingUrlPageNov = r"http://www.rippingrecords.com/tickets.php?month=11"


class RippingPage(object):
    """description of class"""

    def __init__(self, content):
        self.hasFollowingPage = False

        soup = BeautifulSoup(content)

        gigTable = self.FindGigTable(soup)
        self.gigs = None

        if gigTable is not None:
            self.gigs = self.ExtractGigsFromTable(gigTable)                
        else:
            print("Could not find the Gigs table")

    def HasFollowingPage(self):
        return self.hasFollowingPage

    def GetGigs(self):
        return self.gigs

    def FindGigTable(self, soup):
        allTables = soup.find_all('table')

        print(type(allTables))
        print(len(allTables))

        for table in allTables:
            if table.get("class") is not None:
                #print("class = {0}".format(table["class"]))
                #print("class = {0}".format(table["class"][0]))

                if table["class"][0] == "collapse":
                    return table
            else:
                print("no class")
            return None

    def ExtractGigsFromTable(self, gigTable):
        allRows = gigTable.find_all('tr')
        print(type(allRows))

        gigs = []
        for row in allRows:
            print(row)
            gig = self.ExtractGigFromRow(row)
            gigs.append(gig)

        return gigs

    def ExtractGigFromRow(self, row):
        allCols = row.find_all('td')
        print(len(allCols))
        gig = Gig.Gig()
        for col in allCols:
            #print(col)
            #print(col.text)
            if col.get("class") is not None:
                colClass = col["class"][0]
                if colClass == "date":
                    gig.SetDate(col.text.strip())
                elif colClass == "ticket":
                    gig.SetAct(col.text.strip())
                elif colClass == "venue":
                    gig.SetVenue(col.text.strip())
                elif colClass == "city":
                    gig.SetLocation(col.text.strip())
                elif colClass == "price":
                    gig.SetPrice(col.text.strip())
        return gig

