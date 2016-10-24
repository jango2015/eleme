from common import get_response_by_url
from mongoservice import Insert,get_by_pinyin,get_all
from bs4 import BeautifulSoup
from pinyin import PinYin
import  os
_cid = 160
base_url = "http://www.meishij.net/shiliao.php?cid="
s_pinyin = PinYin()
s_pinyin.load_word()

filepath =os.path.abspath("./1.json")
'''获取 理疗分类'''
def get_meishijie_categories(cid = _cid,category_pinyin='',category_cn=''):
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
        # if cid == 160 :
        #     meishijie_shiliao_fenlei.category_pinyin="jibingtiaoli"
        #     meishijie_shiliao_fenlei.category_cn='疾病调理'
        # elif cid== 190:
        #     meishijie_shiliao_fenlei.category_pinyin="jibingtiaoli"
        #     meishijie_shiliao_fenlei.category_cn='疾病调理'
        meishijie_shiliao_fenlei.category_pinyin=category_pinyin
        meishijie_shiliao_fenlei.category_cn=category_cn
        meishijie_shiliao_fenlei.cnName=dd.string
        meishijie_shiliao_fenlei.pinyin = l0
        meishijie_shiliao_fenlei.url = dd["href"]

        class_meishijie_shiliao_fenlei = meishijie_shiliao_fenlei.__dict__
        meishijie_shiliao_Categories.append(class_meishijie_shiliao_fenlei)
    Insert(meishijie_shiliao_Categories,collectionName='Meishijie_shiliao_Categories')

    '''获取该分类食材 start '''
    get_meishijie_shiliao_shicai_yi(cid,meishijie_shiliao_fenlei.category_pinyin) #适宜食材
    get_meishijie_shiliao_shicai_ji(cid,meishijie_shiliao_fenlei.category_pinyin) #禁忌食材
    '''获取该分类食材 end'''
    for st in dish_types_st:
        # print(st)
        # print(dish_types_st.get(st))
        get_dish_menus(cid,page_num=1,cai_menu_types_st=dish_types_st.get(st),category_pinyin=meishijie_shiliao_fenlei.category_cn)


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
    if (len(shiliao_shicais)>0):
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

    if (len(shiliao_shicais)>0):
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
class meishijie_shiliao_dish_menu:
    cid = ''
    dish_type =''
    dish_type_st=''
    dish_cn='' #菜名
    dish_pinyin='' #菜名 拼音
    link_url =''
    img_url=''
    cooking_remark ='' #烹饪 步骤数 /烹饪 时长
    page_num=0



'''获取 菜谱、中医保健、养生妙方'''
dish_types ={"3":"菜谱","1":"中医保健","2":"养生妙方"}
dish_types_st ={"caipu":"3","zhongyibaojian":"1","yangshengmiaofang":"2"}
def get_dish_menus(cid=_cid,page_num=1,cai_menu_types_st="3",category_pinyin=''):
     # print(dish_types[cai_menu_types_st])
     # return
     url = base_url+str(cid)+"&sortby=update&st="+cai_menu_types_st+"&page="+str(page_num)
     html = get_html_by_url(url)
     soup = BeautifulSoup(html)

     total_page =0
     total_page_nums = soup.select(".gopage form",)
     for total_page_num in total_page_nums:
         page_text= str(total_page_num.get_text()).replace('页','').replace('共','').replace('到第','').replace('，','').strip()
         # print(page_text)
         # print(len(page_text))
         total_page = int(page_text)
         # print(total_page)
         # print(type(total_page_num))
     cai_menu_lists = soup.select(".listtyle1_list .listtyle1 a")

     dish_menu_list =[]
     for cai_menu_list in cai_menu_lists:
         # print(cai_menu_list)
         dish_menu = meishijie_shiliao_dish_menu()
         dish_menu.link_url =cai_menu_list["href"]
         dish_menu.cid = cid
         dish_menu.dish_types_st = cai_menu_types_st
         dish_menu.dish_type =category_pinyin+dish_types.get(cai_menu_types_st)
         dish_menu.dish_cn = cai_menu_list["title"]
         img =cai_menu_list.find("img")
         dish_menu.img_url =img["src"]
         remarks = cai_menu_list.select(".c2 li")
         # print(remarks)
         for remark in remarks :
             # print(remark.string)
             dish_menu.cooking_remark+=remark.string +" \r\n"
         try:
             d = s_pinyin.hanzi2pinyin_split(string=dish_menu.dish_cn, split=' ')
             l0 = d.replace(' ', '')
             dish_menu.dish_pinyin = l0
         except:
             import traceback
             # traceback.print_exc()
         dish_menu.page_num = page_num
         dish_menu_item = dish_menu.__dict__
         dish_menu_list.append(dish_menu_item)
     print(dish_menu_list)
     f = open(filepath, 'a')
     s = str(dish_menu_list)
     f.write(s)
     f.close()
     if (len(dish_menu_list) > 0):
        Insert(dish_menu_list,"Mershijie_shiliao_dishmenus")
     page_num = page_num+1
     while (page_num <=total_page):
        # print(page)
        get_dish_menus(cid,page_num=page_num)
        break


def get_pinyin(str_cn):
    d = s_pinyin.hanzi2pinyin_split(str_cn,split=' ')
    l0 = d.replace(' ','')
    return  l0



def get_categiries_by_cid_range():

    '''
    疾病调理 cid
    '''
    jibintiaoli_cid_min = 160
    jibingtiaoli_cid_max = 196

    j_cn = '疾病调理'
    j_pinyin =get_pinyin(j_cn)
    # for index in range(jibintiaoli_cid_min,jibingtiaoli_cid_max+1):
    #     print(index)
    get_meishijie_categories(jibintiaoli_cid_min,category_pinyin=j_pinyin,category_cn=j_cn)
    '''
    功能性调理 cid
    '''
    gongnengxingtiaoli_cid_min = 198
    gongnengxingtiaoli_cid_max = 224
    g_cn = '功能性调理'
    g_pinyin = get_pinyin(g_cn)
    # for index in range(gongnengxingtiaoli_cid_min,gongnengxingtiaoli_cid_max+1):
    #     print(index)
    get_meishijie_categories(gongnengxingtiaoli_cid_min,category_pinyin=g_pinyin,category_cn=g_cn)
    '''
    脏腑调理 cid
    '''
    fuzhangtiaoli_cid_min = 226
    fuzhangtiaoli_cid_max = 251
    fuzhangtiaoli_cid_inc = 275
    f_cn ='腹脏调理'
    f_pinyin = get_pinyin(f_cn)
    # for index in range(fuzhangtiaoli_cid_min,fuzhangtiaoli_cid_max+1):
    #     print(index)
    #     get_meishijie_categories(index,category_pinyin=f_pinyin,category_cn=f_cn)

    get_meishijie_categories(fuzhangtiaoli_cid_inc,category_pinyin=f_pinyin,category_cn=f_cn)
    '''
    人群膳食 cid
    '''
    renqunshanshi_cid_min = 253
    renqunshanshi_cid_max = 267
    r_cn = '人群膳食'
    r_pinyin = get_pinyin(r_cn)
    # for index in range(renqunshanshi_cid_min,renqunshanshi_cid_max+1):
    #     print(index)
    get_meishijie_categories(renqunshanshi_cid_min,category_pinyin=r_pinyin,category_cn=r_cn)







if __name__ == '__main__':
    get_categiries_by_cid_range()
    # get_meishijie_categories()
        # print(dish_types_st.get(st))
    # get_meishijie_shiliao_shicai_yi()
    # get_meishijie_shiliao_shicai_ji()
    # get_dish_menus()