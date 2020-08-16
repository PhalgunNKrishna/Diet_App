class Result:
    def __init__(self, url, page_title):
        self.url = url
        self.title = page_title

# following code taken from geeksforgeeks and stackoverflow: find url later 


try:
    from bs4 import BeautifulSoup
    from googlesearch import search
    import lxml
    import urllib 
except ImportError:
    print("One or more modules not imported")

cal = input("How many calories do you want your meal to have?")
prot = input("How many grams of protein do you want your meal to have?")
carb = input("How many grams of carbohydrates do you want your meal to have?")
fat = input("How many grams of fat do you want your meal to have?")
pref = input("What preferences do you have (e.g. keto, vegan, nut allergy ...)")

query = pref + "meal with " + cal + "calories " + prot + "grams of protein " + carb + "grams of carbohydrates " + fat + "grams of fat" 

count = 1
for url in search(query, tld="co.in", num=5, stop=5, pause=2):
    if count == 1:
        page = BeautifulSoup(urllib.request.urlopen(url), "lxml")
        res1 = Result(url, page.title.string)
    elif count == 2:
        page = BeautifulSoup(urllib.request.urlopen(url), "lxml")
        res2 = Result(url, page.title.string)
    elif count == 3:
        page = BeautifulSoup(urllib.request.urlopen(url), "lxml")
        res3 = Result(url, page.title.string)
    elif count == 4:
        page = BeautifulSoup(urllib.request.urlopen(url), "lxml")
        res4 = Result(url, page.title.string)
    else:
        page = BeautifulSoup(urllib.request.urlopen(url), "lxml")
        res5 = Result(url, page.title.string)
    count += 1

print(res1.title)
print(res2.title)
print(res3.title)
print(res4.title)
print(res5.title)


