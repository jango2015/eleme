

#http://api.map.baidu.com/geocoder/v2/?address=南昌市新建区新建大道760号&output=json&ak=BEh9E9oEt94ClOWC8foLb0t0IAF79Ce8
# 得到 经纬度坐标  {"status":0,"result":{"location":{"lng":115.83222249768369,"lat":28.69828993361852},"precise":1,"confidence":80,"level":"道路"}}
# 然后根据经纬度坐标进行获取具体的省份城市等信息
# http://api.map.baidu.com/geocoder/v2/?ak=BEh9E9oEt94ClOWC8foLb0t0IAF79Ce8&location=28.69828993361852,115.83222249768369&output=json&pois=1
# 得到结果为：
# {"status":0,"result":{"location":{"lng":115.83222249768366,"lat":28.69828995566995},"formatted_address":"江西省南昌市新建县新建大道762号","business":"",
#                       "addressComponent":{"country":"中国","country_code":0,"province":"江西省","city":"南昌市","district":"新建县","adcode":"360122","street":"新建大道","street_number":"762号","direction":"附近","distance":"3"},
#                       "pois":[{"addr":"新建大道549号附近","cp":" ","direction":"附近","distance":"48","name":"中国农业发展银行(新建区支行)","poiType":"金融","point":{"x":115.83198598282606,"y":28.698611910993674},"tag":"金融;银行","tel":"","uid":"53349ee3fd0ea91322026225","zip":""},
#                               {"addr":"新建大道716号","cp":" ","direction":"东","distance":"104","name":"新建区司法局","poiType":"政府机构","point":{"x":115.83128530452849,"y":28.698295075626885},"tag":"政府机构;行政单位","tel":"","uid":"a5097bfa0a226763f03cbac7","zip":""},
#                               {"addr":"新建县建设路与新建大道交汇处","cp":" ","direction":"西南","distance":"109","name":"花果山超市","poiType":"购物","point":{"x":115.83306394943767,"y":28.698738644869026},"tag":"购物;超市","tel":"","uid":"c8e8f63338a0f075ab0dd832","zip":""}
#                           ,{"addr":"新建大道555","cp":" ","direction":"附近","distance":"41","name":"新建区公安局交警大队公路巡警大队长堎中队","poiType":"政府机构","point":{"x":115.8321207286525,"y":28.69860399012132},"tag":"政府机构;公检法机构","tel":"","uid":"0c359826219be49bf82213e8","zip":""},
#                               {"addr":"新建大道555","cp":" ","direction":"附近","distance":"42","name":"新建区公安局交警大队长堎中队","poiType":"政府机构","point":{"x":115.8321207286525,"y":28.698611910993674},"tag":"政府机构;公检法机构","tel":"","uid":"652b52a4b1410f4ec7f50dec","zip":""},
#                               {"addr":"江西省南昌市新建区政法路36号1单元","cp":" ","direction":"东北","distance":"210","name":"新建区卫生局","poiType":"政府机构","point":{"x":115.8307193720574,"y":28.697273274966347},"tag":"政府机构;行政单位","tel":"","uid":"4eb3b533e594c975430245c6","zip":""},
#                               {"addr":"新建大道806","cp":" ","direction":"西","distance":"139","name":"嘉丰汽车修理厂","poiType":"汽车服务","point":{"x":115.83347716997213,"y":28.698326759207178},"tag":"汽车服务;汽车维修","tel":"","uid":"f2ca6ca6f66106aac4f025a3","zip":""},
#                               {"addr":"江西省南昌市新建县建设路226","cp":" ","direction":"南","distance":"199","name":"育苗幼儿园","poiType":"教育培训","point":{"x":115.83256089835224,"y":28.699839638885896},"tag":"教育培训;幼儿园","tel":"","uid":"01ff05897354e03ba2d230c1","zip":""},
#                               {"addr":"南昌市新建区","cp":" ","direction":"东北","distance":"224","name":"新建区疾病预防控制中心","poiType":"医疗","point":{"x":115.83038699901882,"y":28.697550508700105},"tag":"医疗;疾控中心","tel":"","uid":"b88931a51a0631a18e7727dd","zip":""},
#                               {"addr":"江西省南昌市新建县政法路","cp":" ","direction":"东北","distance":"211","name":"新建县卫生局宿舍","poiType":"房地产","point":{"x":115.8307103890023,"y":28.697281195940464},"tag":"房地产;住宅区","tel":"","uid":"aa473a645eef478deb12e439","zip":""}],
#                       "poiRegions":[],"sematic_description":"中国农业发展银行(新建区支行)附近48米","cityCode":163}}
# 手机号码归属地查询
# http://v.showji.com/Locating/showji.com2016234999234.aspx?m=15850781443&output=json&timestamp=1477386205760
from common import get_response_by_url
from bs4 import BeautifulSoup
from mongoservice import Insert
import os
restaurantid_range = range(293883,9999999999999+1)  # [2209,2855,2888,4335,5031,5699,6546,8563,8580,10554,11031,11310,11316,12225,12404 ,12625,12869,13040,13058,14261,14911,15596,15806,16160,]

err_decode_ids =[]
filepath =os.path.abspath("err_decode_restaurant_ids.json")
waimei_meituan_com_restaurant_url_web ="http://waimai.meituan.com/restaurant/"
waimei_meituan_com_restaurant_url_wap ="http://i.waimai.meituan.com/restaurant/"
def ping_waimai_meituan_restaurant_by_id(id):
    print("******"+str(id)+"*****")
    url_web = waimei_meituan_com_restaurant_url_web+str(id)
    url_wap = waimei_meituan_com_restaurant_url_wap + str(id)
    html =get_response_by_url(url_web)
    # print(html)
    soup = BeautifulSoup(html)
    # print(soup)
    noexits_soup = soup.select(".rest-info")
    is_restaurant_exist =len(noexits_soup) >0
    # print(is_restaurant_exist)
    if (is_restaurant_exist):
        model = effective_restaurant()
        model.id = id
        model.url_web = url_web
        model.url_wap = url_wap
        model.waimei_src = 'meituan'
        model.waimai_src_cn='美团外卖'

        class_model = model.__dict__
        print(class_model)
        print("-----------------------------id为:"+str(id)+"-----------------------------------")
        Insert(class_model,"effective_restaurants")

def ping_restaurant_by_idrange():
    for index in restaurantid_range:
        try:
            ping_waimai_meituan_restaurant_by_id(index)
        except:
            err_decode_ids.append(index)
            print(err_decode_ids)
            f = open(filepath, 'a')
            # s = str(err_decode_ids)
            s = str(","+str(index))
            f.write(s)
            f.close()
            continue
            # import traceback


class effective_restaurant:
    id =0
    url_web = ''
    url_wap =''
    waimei_src=''
    waimai_src_cn =''


eleme_shop_url_web ="https://www.ele.me/shop/"
eleme_shop_url_wap ="https://m.ele.me/shop/"

def ping_waimai_eleme_shop_by_id(id):
    print("******" + str(id) + "*****")
    url_web = eleme_shop_url_web + str(id)
    url_wap = eleme_shop_url_wap + str(id)
    html = get_response_by_url(url_web)
    # print(html)
    soup = BeautifulSoup(html)
    # print(soup)
    noexits_soup = soup.select(".shopguide-info-wrapper")
    is_restaurant_exist = len(noexits_soup) > 0
    # print(is_restaurant_exist)
    if (is_restaurant_exist):
        model = effective_restaurant()
        model.id = id
        model.url_web = url_web
        model.url_wap = url_wap
        model.waimei_src = 'eleme'
        model.waimai_src_cn = '饿了么'

        class_model = model.__dict__
        print(class_model)
        print("-----------------------------id为:" + str(id) + "-----------------------------------")
        # Insert(class_model, "effective_restaurants")

if __name__ =='__main__':
    # ping_waimai_meituan_restaurant_by_id(1)
    # ping_waimai_meituan_restaurant_by_id(210000)
    ping_restaurant_by_idrange()