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
