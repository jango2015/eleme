from urllib.request import Request,urlopen
import urllib.parse
import requests

def get_content_by_url(url):
    req = Request(url)
    resp = urlopen(req)
    content = resp.read()
    # data = content.decode("gbk")
    return content

def get_content_by_url_utf8(url):
    req = Request(url)
    resp = urlopen(req)
    content = resp.read()
    data = content.decode("utf-8")
    return data

def get_response_by_url(url):
    resp = requests.get(url)
    content = resp.content.decode('utf-8')
    return content

def get_response_by_url_with_headers(url):
    headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
               "Accept-Encoding": "gzip, deflate, sdch",
               "Accept-Language": "zh-CN,zh;q=0.8",
               "Connection": "keep-alive",
               "Host":"m.dianping.com",
               "Upgrade-Insecure-Requests":1,
               "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"
               }
    resp = requests.get(url,headers =headers)
    content = resp.content.decode('utf-8')
    return content

def post_response_by_url_with_headers(url):
    headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
               "Accept-Encoding": "gzip, deflate, sdch",
               "Accept-Language": "zh-CN,zh;q=0.8",
               "Connection": "keep-alive",
               "Host":"m.dianping.com",
               "Upgrade-Insecure-Requests":1,
               "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"
               }
    resp = requests.post(url,headers =headers)
    content = resp.content.decode('utf-8')
    return content
def get_response_by_url_with_headers(url,headers):
    resp = requests.post(url,headers =headers)
    content = resp.content.decode('utf-8')
    return content

def get_content(url):
    values = {'wd': 'python',
              'opt-webpage': 'on',
              'ie': 'gbk'}
    url_values = urllib.parse.urlencode(values)
    url_values = url_values.encode(encoding='UTF-8')
    req = urllib.request.Request(url, url_values)
    # req = Request(url)
    resp = urlopen(req)
    content = resp.read()
    # data = content.decode('gbk')
    # print(data)
    return content

'''
HTML特殊字符编码对照表 http://www.jb51.net/onlineread/htmlchar.htm
HTML特殊字符编码  替换  '''
def html_content_without_special_chars(html_content):
    special_chars =["&#914;","&#917;","&#920;","&#923;","&#926;","&#929;","&#933;","&#936;","&#946;","&#949;","&#952;","&#955;","&#958;","&#961;","&#964;","&#967;","&#977;","&#8226;","&#8243;","&#8472;","&#8482;","&#8593;","&#8596;","&#8657;","&#8660;","&#8707;","&#8712;","&#8719;","&#8727;","&#8734;","&#8870;","&#8747;","&#8773;","&#8801;","&#8834;","&#8838;","&#8855;","&#8968;","&#8971;","&#9827;","&#160;","&#163;","&#166;","&#169;","&#172;","&#175;","&#178;","&#181","&#62;","&#9728;","&#9729;","&#9730;","&#9731;","&#9732;","&#9733;","&#9734;","&#9735;","&#9736;","&#9737;","&#9738;","&#9739;","&#9740;","&#9741;","&#9742;","&#9743;","&#9744;","&#9745;","&#9746;","&#9747;","&#9748;","&#9749;","&#9750;","&#9751;","&#9752;","&#9753;","&#9754;","&#9755;","&#9756;","&#9757;","&#9758;","&#9759;","&#9760;","&#9761;","&#9762;","&#9763;","&#9764;","&#9765;","&#9766;","&#9767;","&#9768;","&#9769;","&#9770;","&#9771;","&#9772;","&#9773;","&#9774;","&#9775;","&#9776;","&#9777;","&#9778;","&#9779;","&#9780;","&#9781;","&#9782;","&#9783;","&#9784;","&#9785;","&#9786;","&#9787;","&#9788;","&#9789;","&#9790;","&#9791;","&#9792;","&#9793;","&#9794;","&#9795;","&#9796;","&#9797;","&#9798;","&#9799;","&#9800;","&#9801;","&#9802;","&#9803;","&#9804;","&#9805;","&#9806;","&#9807;","&#9808;","&#9809;","&#9810;","&#9811;","&#9812;","&#9813;","&#9814;","&#9815;","&#9816;","&#9817;","&#9818;","&#9819;","&#9820;","&#9821;","&#9822;","&#9823;","&#9824;","&#9825;","&#9826;","&#9827;","&#9828;","&#9829;","&#9830;","&#9831;","&#9832;","&#9833;","&#9834;","&#9835;","&#9836;","&#9837;","&#9838;","&#9839;","&#9840;","&#9841;","&#9842;","&#9843;","&#9844;","&#9845;","&#9846;","&#9847;","&#9848;","&#9849;","&#9850;","&#9851;","&#9852;","&#9853;","&#9854;","&#9855;","&#9856;","&#9857;","&#9858;","&#9859;","&#9860;","&#9861;","&#9862;","&#9863;","&#9864;","&#9865;","&#9866;","&#9867;","&#9868;","&#9869;","&#9870;","&#9871;","&#9872;","&#9873;","&#9874;","&#9875;","&#9876;","&#9877;","&#9878;","&#9879;","&#9880;","&#9881;","&#9882;","&#9883;","&#9884;","&#9885;","&#9886;","&#9887;","&#9888;","&#9889;","&#9890;","&#9891;","&#9892;","&#9893;","&#9894;","&#9895;","&#9896;","&#9897;","&#9898;","&#9899;","&#9900;","&#9901;","&#9902;","&#9903;","&#9904;","&#9905;","&#9906;","&#9907;","&#9908;","&#9909;","&#9910;","&#9911;","&#9912;","&#9913;","&#9914;","&#9915;","&#9916;","&#9917;","&#9918;","&#9919;","&#9920;","&#9921;","&#9922;","&#9923;","&#9924;","&#9925;","&#9926;","&#9927;","&#9928;","&#9929;","&#9930;","&#9931;","&#9932;","&#9933;","&#9934;","&#9935;","&#9936;","&#9937;","&#9938;","&#9939;","&#9940;","&#9941;","&#9942;","&#9943;","&#9944;","&#9945;","&#9946;","&#9947;","&#9948;","&#9949;","&#9950;","&#9951;","&#9952;","&#9953;","&#9954;","&#9955;","&#9956;","&#9957;","&#9958;","&#9959;","&#9960;","&#9961;","&#9962;","&#9963;","&#9964;","&#9965;","&#9966;","&#9967;","&#9968;","&#9969;","&#9970;","&#9971;","&#9972;","&#9973;","&#9974;","&#9975;","&#9976;","&#9977;","&#9978;","&#9979;","&#9980;","&#9981;","&#9982;","&#9983;"]
    html =str(html_content)
    for special_char in special_chars:
        pos = html.find(special_char)
        if pos >-1:
            html = html.replace(special_char," ")
    return  html

def class_to_dict(obj):
    '''把对象(支持单个对象、list、set)转换成字典'''
    is_list = obj.__class__ == [].__class__
    is_set = obj.__class__ == set().__class__

    if is_list or is_set:
        obj_arr = []
        for o in obj:
            # 把Object对象转换成Dict对象
            dict = {}
            dict.update(o.__dict__)
            obj_arr.append(dict)
        return obj_arr
    else:
        dict = {}
        dict.update(obj.__dict__)
        return dict
