class TorrentData(object):
    ###########################################################################
    ###########################################################################
    def __init__(self, category, subCategory, title, uploadDate, size, seeders = 0, leechers = 0):
        self.category = category
        self.subCategory = subCategory
        self.title = title
        self.uploadDate = uploadDate
        self.size = size
        self.seeders = seeders
        self.leechers = leechers
