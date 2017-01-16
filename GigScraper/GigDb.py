import sqlite3
import datetime

SqlCreateGigTable = "CREATE TABLE IF NOT EXISTS gigs (act TEXT, venue TEXT, location TEXT)"
SqlFindGig = "SELECT COUNT(*) FROM gigs WHERE act = '{0}' AND venue = '{1}' AND location = '{2}'"
SqlAddGig = "INSERT INTO gigs (act, venue, location) VALUES (?, ?, ?)"

class GigDb(object):
    """description of class"""
    def __init__(self, dbPath):
        print("Opening database : {0}".format(dbPath))
        self.dbPath = dbPath
        self.dbConn = sqlite3.connect( self.dbPath )
        self.dbConn.execute(SqlCreateGigTable)

    def Close(self):
        print("Closing database : {0}".format(self.dbPath))
        self.dbConn.close()

    def AddGigs(self, gigs):
        print("Number of gigs to add = {0}".format(len(gigs)))
        for gig in gigs:
            print("Adding gig = {0}".format(gig))
            AddGig(self, gig)

    def GigExists(self, gig):
        sqlCount = SqlFindGig.format(gig.act, gig.venue, gig.location)
        
        cursor = self.dbConn.cursor()
        cursor.execute(sqlCount)
        result=cursor.fetchone()
        cursor.close()

        return True if result[0] else False

    def AddGig(self, gig):
        if not self.GigExists(gig):
            now = datetime.datetime.now()
            dateAdded = datetime.datetime.now().strftime('%Y-%m-%d')

            cursor = self.dbConn.cursor()
            cursor.execute(SqlAddGig, (gig.act, gig.venue, gig.location))
            self.dbConn.commit()
            cursor.close()

            self.ReportGigAdded("Gig Added", gig)

    def ReportGigAdded(self, action, gig):
        print("{0} : {1}, {2}, {3}".format(action, gig.act, gig.venue, gig.location) )



