class Item:

    def __init__(self, day, month, year, item_name, cost, category):
        self.day = day
        self.month = month
        self.year = year
        self.item_name = item_name
        self.cost = cost
        self.category = category

    def print_item(self):
        print("{0}/{1}/{2} {3} ${4} purchased for {5} ".
              format(self.day, self.month, self.year, self.item_name, self.cost, self.category))

