# coding=utf-8
#from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
#from urllib.error import URLError, HTTPError
import  urllib
from urllib2 import urlopen


class Wanimal:

    def __init__(self, page):
        self.page = page
        self.imgs = []

    def getPage(self, page):
        try:
            html = urlopen("http://wanimal1983.org/page/"+str(page))
            bsobj = BeautifulSoup(html, "html.parser")
            return bsobj
        except (URLError, HTTPError) as e:
            print (e)
            return None

    def getImages(self, page):
        print ("正在加载第%d页" % page)
        bsobj = self.getPage(page)
        imgTags = bsobj.findAll("div", {"class": "photo-sets"})
        self.imgs = []
        for imgTag in imgTags:
            for img in imgTag.findAll("img"):
                self.imgs.append(img)

    def download(self):
        for page  in range(36,self.page):
            self.getImages(page+1)
            for i in range(len(self.imgs)):
                print ("正在保存第%d个图片" % (i+1))
                path = str(page)+'_'+str(i)+".jpg"
                print (self.imgs[i].attrs["src"])
                urllib.urlretrieve(self.imgs[i].attrs["src"], "/Users/Topone/Desktop/untitled2/donw/"+path)

w = Wanimal(300000)
print (w.imgs)
w.download()


