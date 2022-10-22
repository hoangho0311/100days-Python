from bs4 import BeautifulSoup
import requests
# # import lxml
#
# with open("index.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
# print(soup.find_all("li"))
#

# respone = requests.get("https://daotao.vku.udn.vn/")
#
# soup = BeautifulSoup(respone.text, "html.parser")
# soup.select(selector=".item-list div ul li")
# article_text=soup.find(name="a").getText()
# # article_link=soup.find(name="a", rel="nofollow").get("href")
# # article_upvote=soup.find(class_="score").getText()
# print(article_text)

url ="https://www.empireonline.com/movies/features/best-movies-2/"
respone = requests.get(url)
soup = BeautifulSoup(respone.text,"html.parser")
data = soup.find(name="h3")
# movie_title = [movie.getText() for movie in data]
print(soup)