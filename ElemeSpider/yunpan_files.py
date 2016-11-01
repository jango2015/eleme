import requests
import json
file_list_url ="http://c-t.yunpan.360.cn/file/list" #type=2&t=0.9921613916353091&order=asc&field=file_name&path=%2F&page=0&page_size=300&ajax=1
file_download_url="http://c-t.yunpan.360.cn/file/download"  #nid=13983973164922515&fname=%2FJOB%20www.lagou.com.txt&ajax=1
headers = {
            "Accept":"*/*",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Connection":"keep-alive",
            # "Content-Length":"91",
            "Content-type":"application/x-www-form-urlencoded UTF-8",
            "Cookie":"__guid=91251416.3086305693651073500.1477022817026.9539; __huid=101nfbTUxnm0B4BNiWVu%2BfgAAbS9ij7h15tA2k6Zm2ay0%3D; Q=u%3Dfntryl_001%26n%3D%26le%3DL3caZwN4ZPH0ZUAcozRhL29g%26m%3D%26qid%3D802009908%26im%3D1_t00df551a583a87f4e9%26src%3Dpcw_cloud%26t%3D1; T=s%3D40bb00defdbab0659ad3822dfb11dcd3%26t%3D1477973358%26lm%3D%26lf%3D1%26sk%3Dd5a8f1b4ef47d9e102322b617b53e197%26mt%3D1477973358%26rc%3D%26v%3D2.0%26a%3D0; token=3030998290.55.29069719.802009908.1477973360; SEC_INFO_802009908=c-t.yunpan.360.cn; count=3",
            "Host":"c-t.yunpan.360.cn",
            "Origin":"http://c-t.yunpan.360.cn",
            "Referer":"http://c-t.yunpan.360.cn/my/index/",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36",
            "X-Requested-With":"XMLHttpRequest",}
file_list_payload ={"type":"2","t":"0.9921613916353091","order":"asc","field":"file_name","page":0,"page_size":300,"ajax":1}
download_payload={"ajax":1}
replace_fields=["loginFlag","page","errmsg","errno","listType","field","order","type","previewSign","fileNum","data","oriName","path","nid","date","isDir","isFav","oriSize","size","scid","preview","hasThumb","thumb","fhash","fileType","fmtime"]
yunpan_dir_list=[]
yunpan_file_list = []
savepath ="D:\\workspace\yunpan_2016_jango"
def file_list_post(path="/"):
    file_list_payload["path"] = path
    print(file_list_payload)
    r = requests.post(url=file_list_url,data=json.dumps(file_list_payload),headers =headers )
    rcs = r.content.decode("utf8","ignore")
    st = replace_with_fields(rcs).replace(",{}","").replace(",mtime",",'mtime'").replace("true","True").replace("false","False").replace('&"nid"=','&nid=').replace('&"size"=','&size=').replace('dev"type"=','devtype=').replace('""preview"Sign"','"previewSign"').strip()
    # print(st)
    # print(type(st))
    j = eval(st)
    # print(j)
    # print(type(j))
    errno = j["errno"]
    fileNum = j["fileNum"]
    if errno =='0' and fileNum >0:
        datalist = j["data"]
        for dataitem in datalist:
            # print(dataitem)
            isDir = False
            try:
                isDir = dataitem["isDir"]
            except KeyError:
                print("********* this  is a file ***********")
            if isDir:
                dir_model = class_dir()
                dir_model.isDir = isDir
                dir_model.nid =dataitem["nid"]
                dir_model.oriName = dataitem["oriName"]
                dir_model.path = dataitem["path"]

                class_dir_model = dir_model.__dict__

                create_dir(path)
                # file_list_post(path=dir_model.path)

                yunpan_dir_list.append(class_dir_model)
            else:
                file_model = class_file()
                file_model.fhash = dataitem["fhash"]
                file_model.nid = dataitem["nid"]
                file_model.path =dataitem["path"]
                file_model.oriName =dataitem["oriName"]
                class_file_model = file_model.__dict__
                yunpan_file_list.append(class_file_model)
                #
                # file_json = json.dumps(class_file_model)
                # write_str(file_json)



import time
def create_dir(path):
    import os
    current_save_path =savepath+path
    print(current_save_path)
    if os.path.exists(current_save_path) ==False:
        os.mkdir(current_save_path)

        # print(len(datalist))
        # str_rc = str(r.content).replace("b","")
        # print(str_rc)

def write_str(content,current_file_list_json_path):
    import io
    f = open(current_file_list_json_path,"a")
    f.write(content)
    f.close()

class class_dir:
    isDir =False
    oriName=''
    path=''
    nid=''
class class_file:
    oriName =''
    path =''
    fhash =''
    nid =''

def replace_with_fields(content):
    if len(content) ==0:
        return ''
    str_content = str(content)
    if len(replace_fields)>0:
        for field in replace_fields:
            # print(field)
            str_content = str_content.replace(field,'"'+field+'"')

    return str_content
class yunpan_response:
    loginFlag =""
    page =0,
    errmsg =''
    errno=''
    listType=''
    field=''
    order=''
    type=''
    previewSign=''
    fileNum=''
    data =[]
class fileOrdir:
    oriName=''
    path=''
    nid =''
    date=''
    isDir=False,
    isFav ="",
    oriSize=''
    size=''
    scid =''
    preview=''
    hasThumb= '',
    thumb=''
    fhash=''
    fileType=''
    fmtime=''
    mtime=''




if __name__ =="__main__":
    file_list_post()
    len_dir = len(yunpan_dir_list)
    print(len_dir)
    print(len(yunpan_file_list))
    file_json = json.dumps(yunpan_file_list)

    current_file_list_json_path = savepath + "/op_log" + "1"+ ".json"  #path.replace('/', '')
    # print(path)
    write_str(file_json, current_file_list_json_path)
    if len_dir > 0:
        for yunpan_dir_item in yunpan_dir_list:
            print(yunpan_dir_item)
            # print(type(yunpan_dir_item))
            item_path = yunpan_dir_item["path"]
            print("*************************************************8item_path:"+item_path+"********************************************************")
            # return
            file_list_post( path= item_path)