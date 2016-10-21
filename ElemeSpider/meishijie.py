from common import get_response_by_url
from mongoservice import Insert,get_by_pinyin,get_all
from bs4 import BeautifulSoup
from pinyin import PinYin
_cid = 160
base_url = "http://www.meishij.net/shiliao.php?cid="
s_pinyin = PinYin()
s_pinyin.load_word()

'''获取 理疗分类'''
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
        d = s_pinyin.hanzi2pinyin_split(string=s,split=" ")
        l0 = d.replace(' ','')
        # l1  = d.strip()
        # print(dd["href"])
        # print(dd.string)
        # print(l0)

        meishijie_shiliao_fenlei = meishijie_shiliao_parant_category()
        meishijie_shiliao_fenlei.cid =_cid +index
        index+=1
        if cid == 160 :
            meishijie_shiliao_fenlei.category_pinyin="jibingtiaoli"
            meishijie_shiliao_fenlei.category_cn='疾病调理'
        # elif cid== 190:
        #     meishijie_shiliao_fenlei.category_pinyin="jibingtiaoli"
        #     meishijie_shiliao_fenlei.category_cn='疾病调理'
        meishijie_shiliao_fenlei.cnName=dd.string
        meishijie_shiliao_fenlei.pinyin = l0
        meishijie_shiliao_fenlei.url = dd["href"]

        class_meishijie_shiliao_fenlei = meishijie_shiliao_fenlei.__dict__
        meishijie_shiliao_Categories.append(class_meishijie_shiliao_fenlei)
    '''获取该分类食材 start
    '''
    get_meishijie_shiliao_shicai_yi(cid,meishijie_shiliao_fenlei.category_pinyin) #适宜食材
    get_meishijie_shiliao_shicai_ji(cid,meishijie_shiliao_fenlei.category_pinyin) #禁忌食材
    '''
    获取该分类食材 end
    '''
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
获取食材 start
'''

'''适宜食材  start'''
shicai_base_url = "http://www.meishij.net/"
def get_meishijie_shiliao_shicai_yi(cid = _cid,category_pinyin=""):
    url=base_url+str(cid)
    html = get_html_by_url(url)
    soup = BeautifulSoup(html)
    # shiyi_shicai = soup.li.next_siblings
    soup_shiyi_shicais = soup.findAll(id="yi_more")

    shicai_type =''
    shicai_type_name=''
    shicai_remark =''
    shiliao_shicais =[]
    for soup_shiyi_shicai in soup_shiyi_shicais:
        shicai_type=soup_shiyi_shicai["class"][0]
        shicai_type_name = soup_shiyi_shicai.string
        remark_spans = soup_shiyi_shicai.next_sibling
        yi_shicais = soup_shiyi_shicai.next_sibling.next_sibling.next_sibling

        for remark_span in remark_spans:
            # print(remark_span)
            shicai_remark = shicai_remark+remark_span.string+"\n\t "
        for shicai_li in yi_shicais:
            for a in shicai_li:
                # print(a)
                # print(type(a))
                if shicai_li.string is not None:
                    if shicai_li.string !="\n":
                        shiliao_shicai = meishijiie_shiliao_shicai()
                        shiliao_shicai.cid = cid
                        shiliao_shicai.category_pinyin = category_pinyin
                        shiliao_shicai.cnName = shicai_li.string
                        shiliao_shicai.remark = shicai_remark
                        shiliao_shicai.type = shicai_type
                        shiliao_shicai.type_name = shicai_type_name
                        shiliao_shicai.url =shicai_base_url+shiliao_shicai.cnName
                        d = s_pinyin.hanzi2pinyin_split(string=shiliao_shicai.cnName, split=" ")
                        l0 = d.replace(' ', '')
                        shiliao_shicai.pinyin = l0
                        imgs = a.select("img")
                        for img in imgs:
                            shiliao_shicai.img_url = img["src"]
                        class_shiliao_shicai = shiliao_shicai.__dict__
                        print(class_shiliao_shicai)
                        shiliao_shicais.append(class_shiliao_shicai)
                    # img = shicai_li.find_all("img")
                    # print(img)

    Insert(shiliao_shicais,"Meishijie_shiliao_shicais")
'''
适宜食材 end
 '''


'''禁忌食材 start'''
def get_meishijie_shiliao_shicai_ji(cid = _cid,category_pinyin=""):
    url = base_url + str(cid)
    html = get_html_by_url(url)
    soup = BeautifulSoup(html)
    # shiyi_shicai = soup.li.next_siblings
    soup_shiyi_shicais = soup.findAll(id="ji_more")

    shicai_type = ''
    shicai_type_name = ''
    shicai_remark = ''
    shiliao_shicais = []
    for soup_shiyi_shicai in soup_shiyi_shicais:
        shicai_type = soup_shiyi_shicai["class"][0]
        shicai_type_name = soup_shiyi_shicai.string
        remark_spans = soup_shiyi_shicai.next_sibling
        print(soup_shiyi_shicai.next_sibling.next_sibling)
        ji_shicais = soup_shiyi_shicai.next_sibling.next_sibling.next_sibling

        for remark_span in remark_spans:
            # print(remark_span)
            shicai_remark = shicai_remark + remark_span.string + "\n\t "
        for shicai_li in ji_shicais:
            # for a in shicai_li:
                # print(a))
            shicai_li_string = str(shicai_li.string).strip()
            print()
            if shicai_li.string is not None:
                if shicai_li.string != "\n" and len(shicai_li_string)>0:
                    shiliao_shicai = meishijiie_shiliao_shicai()
                    shiliao_shicai.cid = cid
                    shiliao_shicai.category_pinyin = category_pinyin
                    shiliao_shicai.cnName = shicai_li.string
                    shiliao_shicai.remark = shicai_remark
                    shiliao_shicai.type = shicai_type
                    shiliao_shicai.type_name = shicai_type_name
                    shiliao_shicai.url = shicai_base_url + shiliao_shicai.cnName
                    try:
                        d = s_pinyin.hanzi2pinyin_split(string=shiliao_shicai.cnName,split=' ')
                        l0 = d.replace(' ', '')
                        shiliao_shicai.pinyin = l0
                    except :
                        import traceback
                        # traceback.print_exc()
                    imgs = shicai_li.select("img")
                    for img in imgs:
                        shiliao_shicai.img_url = img["src"]
                    class_shiliao_shicai = shiliao_shicai.__dict__
                    # print(class_shiliao_shicai)
                    shiliao_shicais.append(class_shiliao_shicai)
                    # img = shicai_li.find_all("img")
                    # print(img)

    Insert(shiliao_shicais, "Meishijie_shiliao_shicais")
'''禁忌食材 end'''

'''
获取食材 end
'''


'''base'''
def get_html_by_url(url):
    sohtml =get_response_by_url(url)
    html =str(sohtml).encode("utf-8")
    return html

'''食疗及美食分类'''
class meishijie_shiliao_parant_category:
    cid =''
    category_pinyin =''
    category_cn = ''
    cnName=''
    pinyin=''
    url=''

'''食疗 适宜食材/禁忌食材'''
class meishijiie_shiliao_shicai:
    cid =''
    category_pinyin=''
    cnName=''
    pinyin=''
    img_url=''
    url=''
    remark=''
    type =''  '''type : yi适宜食材  type:ji ：禁忌食材'''
    type_name =''

'''菜谱、中医保健、养生妙方'''
class meishijie_shiliao_cai_menu:
    cid = ''
    category_pinyin = ''


'''获取 菜谱、中医保健、养生妙方'''
cai_menu_types ={"caipu":"菜谱","zhongyibaojian":"中医保健","yangshengmiaofang":"养生妙方"}
cai_menu_types_st ={"caipu":"3","zhongyibaojian":"1","yangshengmiaofang":"2"}
def get_cai_menus(cid=_cid,page_num=1,cai_menu_types_st="3"):
     url = base_url+str(cid)+"&sortby=update&st="+cai_menu_types_st
     html = get_html_by_url(url)
     soup = BeautifulSoup(html)

     total_page =0
     total_page_nums = soup.select(".gopage form",)
     for total_page_num in total_page_nums:
         page_text= str(total_page_num.get_text()).replace('页','').replace('共','').replace('到第','').replace('，','').strip()
         # print(page_text)
         # print(len(page_text))
         total_page = int(page_text)
         print(total_page)
         # print(type(total_page_num))

     cai_menu_lists = soup.select(".listtyle1_list .listtyle1")
     for cai_menu_list in cai_menu_lists:
         print((cai_menu_list))





if __name__ == '__main__':
    # get_meishijie_categories()
    # get_meishijie_shiliao_shicai_yi()
    # get_meishijie_shiliao_shicai_ji()
    get_cai_menus()