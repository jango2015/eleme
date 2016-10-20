from common import get_response_by_url
from mongoservice import Insert,get_by_pinyin,get_all
from bs4 import BeautifulSoup
from pinyin import PinYin
_cid = 160
base_url = "http://www.meishij.net/shiliao.php?st=3&cid="
def get_meishijie_categories(cid = _cid):
    url=base_url+str(cid)
    html =get_html_by_url(url)
    # print(html)
    # soup = BeautifulSoup(html)
    # print(soup)
    # print(soup.prettify())

    sop = BeautifulSoup(html)
    # h = sop.prettify()
    # print( h )
    # head = sop.find('head')
    # print(head)
    # p_categories = sop.findAll(attrs={'id':'listnav_ul'})[0]
    # print(p_categories)

    dds = sop.select(".listnav_dl_style1 dd a")
    print(len(dds))
    meishijie_shiliao_Categories=[]
    index =0
    for dd in dds:
        # print(dd)
        s = dd.string
        s_pinyin = PinYin()
        s_pinyin.load_word()
        d = s_pinyin.hanzi2pinyin_split(string=s,split=" ")
        l0 = d.replace(' ','')
        # l1  = d.strip()
        # print(dd["href"])
        # print(dd.string)
        # print(l0)

        meishijie_shiliao_fenlei = meishijie_shiliao_parant_category()
        meishijie_shiliao_fenlei.cid =_cid +index
        index+=1
        meishijie_shiliao_fenlei.category_pinyin="jibingtiaoli"
        meishijie_shiliao_fenlei.category_cn='疾病调理'
        meishijie_shiliao_fenlei.cnName=dd.string
        meishijie_shiliao_fenlei.pinyin = l0
        meishijie_shiliao_fenlei.url = dd["href"]
        # print(meishijie_shiliao_fenlei.__dict__)
        meishijie_shiliao_Categories.append(meishijie_shiliao_fenlei.__dict__)
        Insert(meishijie_shiliao_Categories,collectionName='Meishijie_shiliao_Categories')


    # dls = sop.findAll("dl",attrs={'class':"listnav_dl_style1"})
    # for dl in dls:
    #     # print(dl)
    #     # print(dl.contents)
    #     # for category in dl.descendants :
    #     for category in dl.contents :
    #         # print(category)
    #         print(category)
    #         print(category.string)


'''
base
'''
def get_html_by_url(url):
    sohtml =get_response_by_url(url)
    html =str(sohtml).encode("utf-8")
    return html

'''
食疗及美食分类
'''
class meishijie_shiliao_parant_category:
    cid =''
    category_pinyin =''
    category_cn = ''
    cnName=''
    pinyin=''
    url=''
'''
食疗 适宜食材
'''
class meishijiie_shiliao_shiyi_shicai:
    category_pinyin=''
    cnName=''
    pinyin=''
    img_url=''
    url=''
    remark=''


if __name__ == '__main__':
    get_meishijie_categories()
