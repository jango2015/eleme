from urllib.request import Request,urlopen
def get_content_by_url(url):
    req = Request(url)
    resp = urlopen(req)
    content = resp.read()
    # data = content.decode("gbk")
    return content

def get_content(url):
    req = Request(url)
    resp = urlopen(req)
    content = resp.read()
    print(content)
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
