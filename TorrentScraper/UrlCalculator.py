# https://thepirateboat.eu/recent
# https://thepirateboat.eu/recent/1
# https://thepirateboat.eu/recent/2
# top100 
# music           https://thepirateboat.eu/top/101
# audiobooks      https://thepirateboat.eu/top/102
# flac            https://thepirateboat.eu/top/104
# movies          https://thepirateboat.eu/top/201
# hd movies       https://thepirateboat.eu/top/207
# hd tv shows     https://thepirateboat.eu/top/208
# music videos    https://thepirateboat.eu/top/203



#recentTorrentsPage = "http://pirateproxy.ws/recent"
#recentTorrentsPage = "http://baytorrent.nl/recent"
#recentTorrentsPage = "http://baytorrent.nl/recent"


maxPagesToOpen = 1

class UrlCalculator(object):
    """description of class"""

    ###########################################################################
    ###########################################################################
    def __init__(self, baseUrl, numPages):
        self.baseUrl = baseUrl
        self.numPages = numPages

    ###########################################################################
    ###########################################################################
    def GetUrls(self):
        return self.GetUrlsStub()

    ###########################################################################
    ###########################################################################
    def GetUrlsStub(self):
        urls = [
            "https://thepirateboat.eu/top/101" ]
        return urls

    ###########################################################################
    ###########################################################################
    def GetUrlsReal(self):
        urls = []

        for i in range(0, numPages):
            #
            # The first recent torrents page is "http://pirateproxy.ws/recent"
            # Subsequent torrent pages are "http://pirateproxy.ws/recent/<page number>"
            #
            if i == 0:
                url = baseUrl + "/recent"
            else:
                url = baseUrl + "/recent/" + str(i)

            urls.append(url)

        return urls
