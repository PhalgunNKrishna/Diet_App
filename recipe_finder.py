class Result:
    def __init__(self, url, page_title):
        self.url = url
        self.title = page_title

# following code taken from geeksforgeeks and stackoverflow: find url later 
try:
    from googlesearch import search
    from urrlib2 import urlopen
    from lxml.html import parse
except ImportError:
    print("One or more modules not imported")

cal = input("How many calories do you want your meal to have?")
prot = input("How many grams of protein do you want your meal to have?")
carb = input("How many grams of carbohydrates do you want your meal to have?")
fat = input("How many grams of fat do you want your meal to have?")
pref = input("What preferences do you have (e.g. keto, vegan, nut allergy ...)")

query = pref + "meal with " + cal "calories " + prot + "grams of protein " + carb + "grams of carbohydrates " + fat + "grams of fat" 

count = 1
for i in search(query, tld="co.in", num=5, stop=5, pause=2):
    if count == 1:
        res1 = Result()
    elif count == 2:
        res2 = Result()
    elif count == 3:
        res3 = Result()
    elif count == 4:
        res4 = Result()
    else:
        res5 = Result()
    count += 1



