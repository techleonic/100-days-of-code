from bs4 import BeautifulSoup
# import lxml
with open("website.html") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")
# soup = BeautifulSoup(content, "lxml")

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.a)

# find all tags
all_anchor = soup.find_all("a")

# text and aributes
for anchor in all_anchor:
    print(anchor.get_text())
    print(anchor.get("href"))

# find by tag and id
heading =  soup.find(name="h1",id="name")
print(heading)

#find by Class
section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

#find by multples selctions tags css
company_url = soup.select_one(selector="p a")
print(company_url)

#select one css method
name =  soup.select_one("#name")
print(name)

#selecting more than one
print(soup.select(".heading"))

