import requests

url = "http://Webscrapingserver-env.eba-xjyfa7wc.us-east-2.elasticbeanstalk.com/yo"

file = open("webScraping/yahooFinanceScraperSolution1.py")
fileText = file.read()
file.close()

data = {"program": fileText}
page = requests.post(url, data=data)
print(page.content.decode('utf-8'))