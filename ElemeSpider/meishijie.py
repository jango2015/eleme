from common import get_response_by_url
# from mongoservice import Insert,get_by_pinyin,get_all
from bs4 import BeautifulSoup

def get_meishijie_categories(cid = 160):
    url = "http://www.meishij.net/shiliao.php?st=3&cid="+str(cid)
    sohtml =get_response_by_url(url)
    html =str(sohtml).encode("utf-8")
    # print(html)


    # html = """
    # <html><head><title>The Dormouse's story</title></head>
    # <body>
    # <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
    # <p class="story">Once upon a time there were three little sisters; and their names were
    # <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
    # <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    # <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    # and they lived at the bottom of a well.</p>
    # <p class="story">...</p>
    # """
    # soup = BeautifulSoup(html)
    # print(soup)
    # print(soup.prettify())

    sop= BeautifulSoup(html)
    h = sop.prettify()
    # print( h )
    # head = sop.find('head')
    # print(head)
    p_categories = sop.findAll(attrs={'id':'listnav_ul'})[0]
    print(p_categories)
    dls = sop.findAll("dl",attrs={'class':"listnav_dl_style1"})
    for dl in dls:
        # print(dl)
        # print(dl.contents)
        # for category in dl.descendants :
        for category in dl.contents :
            # print(category)
            # print(category)
            print(category.string)



    # print(eval(dls))

if __name__ == '__main__':
    get_meishijie_categories()
