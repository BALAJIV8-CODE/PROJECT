from autoscraper import AutoScraper

url = 'https://www.randomlists.com/email-addresses'

wanted_list = ("[a-zA-Z0-9]+@+[a-zA-Z0-9]+[a-zA-Z]")

scraper = AutoScraper()

# Here we can also pass html content via the html parameter instead of the url (html=html_content)
ans = re.compile(wanted_list)
result = scraper.build(url, ans)
print(result)

