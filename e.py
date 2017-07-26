import os
from urllib.request import urlopen,urlretrieve
from bs4 import BeautifulSoup

downloadDir = "TistoryPicture"
baseUrl = "https://doohaproject.tistory.com/19"

def getAbsoluteUrl(source):
    if source.startswith("http://"):
        url = source
    else:
        url = "http:"+source
    return url

def DownloadDirectory(source, downloadDirectory):
    path = source.replace("http://","")
    path = path.split(".")[0]
    path = downloadDirectory+"/"+path

    print(path)
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(path)

    return path

html = urlopen(baseUrl)
bsObj = BeautifulSoup(html,"html.parser")
downloadList = bsObj.findAll("img")

for download in downloadList:
    if download.has_attr("filename"):
        cUrl = getAbsoluteUrl(download["src"])
        print(cUrl)
        urlretrieve(cUrl, download["filename"])