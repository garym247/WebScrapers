class Gig(object):
    """description of class"""

    def __init__(self, act, venue, location, date, price):
        self.act = act
        self.venue = venue
        self.location = location
        self.date = date
        self.price = price
    
    def __str__(self):
        return "act: {0}, venue: {1}, location: {2}, date: {3}, price: {4}".format(self.act, self.venue, self.location, self.date, self.price)

    @property
    def act(self):
        return self._act
    @act.setter
    def act(self, value):
        self._act = value

    @property
    def venue(self):
        return self._venue
    @venue.setter
    def venue(self, value):
        self._venue = value

    @property
    def location(self):
        return self._location
    @location.setter
    def location(self, value):
        self._location = value

    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, value):
        self._date = value

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        self._price = value

