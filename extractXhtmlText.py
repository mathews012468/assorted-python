from bs4 import BeautifulSoup
import re

with open("/Users/mathewsoto/Library/Containers/com.apple.BKAgentService/Data/Documents/iBooks/Books/1581182804.ibooks/OPS/content1.xhtml") as f:
    source_html = f.read()

soup = BeautifulSoup(source_html, "html.parser",)
# print( soup.body.get_text(separator="\n", strip=True) )
#find all elements with the id = page{number}
pageNumberRegex = re.compile(r"^page[0-9]+")
for pageElement in soup.find_all(id=pageNumberRegex):
    print(pageElement.parent.text, end="\n\n")
# for child in soup.body.children:
#     print(child.name, child.attrs, child.text, end="\n\n")