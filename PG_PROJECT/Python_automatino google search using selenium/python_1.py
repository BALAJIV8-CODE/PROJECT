# python automation module using selenium
from selenium import webdriver


# get from user to search
topic2_Search = input('Enter the query in Google search : ')

# topic search
topic2_Search = topic2_Search.replace(' ' , '+')

# set chrome browser path
browser = webdriver.Chrome('chromedriver.exe')


for i in range(1):
    content = browser.get("http://google.com/search?q=" + topic2_Search + "&start" + str(i))


