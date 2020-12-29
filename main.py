from Item import Item
item1 = Item(13, 12, 2020, "monitor", 93.0, "college")

item1.print_item()

# I want to save each month as a text file

# item_file = open('item_file.txt', 'r')
# item_file.close()


from datetime import datetime

current_year = datetime.today().year
current_day = datetime.today().day
current_month = datetime.today().month

print(current_year)
print(current_day)
print(current_month)




# Python project to keep better track of my finances and become a more experienced programmer.
