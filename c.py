from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

html = urlopen("http://doohaproject.tistory.com/category/%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8")
bsObj = BeautifulSoup(html,"html.parser")
Location = bsObj.find("span",{"class":"imageblock"}).find("a")['href']
print(Location)
urlretrieve(Location, "first.zip")

