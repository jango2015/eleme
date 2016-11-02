import requests
import json
file_list_url ="http://c-t.yunpan.360.cn/file/list" #type=2&t=0.9921613916353091&order=asc&field=file_name&path=%2F&page=0&page_size=300&ajax=1
                                                    #type=1&t=0.3559999934034921&order=asc&field=file_name&path=%2F12306%2F&page=0&page_size=300&ajax=1
                                                    #type=1&t=0.615957312383044&order=asc&field=file_name&path=%2F12306%2F&page=0&page_size=300&ajax=1
file_download_url="http://c-t.yunpan.360.cn/file/download"  #nid=13983973164922515&fname=%2FJOB%20www.lagou.com.txt&ajax=1
# headers = {
#             "Accept":"*/*",
#             "Accept-Encoding":"gzip, deflate",
#             "Accept-Language":"zh-CN,zh;q=0.8",
#             "Connection":"keep-alive",
#             # "Content-Length":"91",
#             "Content-type":"application/x-www-form-urlencoded UTF-8",
#             "Cookie":"__guid=91251416.3086305693651073500.1477022817026.9539; __huid=101nfbTUxnm0B4BNiWVu%2BfgAAbS9ij7h15tA2k6Zm2ay0%3D; SEC_INFO_802009908=c-t.yunpan.360.cn; test_cookie_enable=null; Q=u%3Dfntryl_001%26n%3D%26le%3DL3caZwN4ZPH0ZUAcozRhL29g%26m%3D%26qid%3D802009908%26im%3D1_t00df551a583a87f4e9%26src%3Dpcw_cloud%26t%3D1; T=s%3D3b0b1e33752a31cd3fa494cd32ab258e%26t%3D1478069158%26lm%3D%26lf%3D1%26sk%3D2da7b7be4da2e788300d3d2ab579075f%26mt%3D1478069158%26rc%3D%26v%3D2.0%26a%3D0; token=3030998290.55.e79095a3.802009908.1478069158; count=13",
#             "Host":"c-t.yunpan.360.cn",
#             "Origin":"http://c-t.yunpan.360.cn",
#             # "Referer":"http://c-t.yunpan.360.cn/my/index/",
#              "Referer":"http://c-t.yunpan.360.cn/my/?sid=#",
#             "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36",
#             "X-Requested-With":"XMLHttpRequest",}

headers ={
        "Host":" c-t.yunpan.360.cn",
        "Connection":" keep-alive",
        "Cache-Control":" max-age=0",
        "Accept":" text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Upgrade-Insecure-Requests":" 1",
        "User-Agent":" Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36",
        "Accept-Encoding":" gzip, deflate, sdch",
        "Accept-Language":" zh-CN,zh;q=0.8",
        "Cookie":" __guid=91251416.3086305693651073500.1477022817026.9539; __huid=101nfbTUxnm0B4BNiWVu%2BfgAAbS9ij7h15tA2k6Zm2ay0%3D; SEC_INFO_802009908=c-t.yunpan.360.cn; Q=u%3Dfntryl_001%26n%3D%26le%3DL3caZwN4ZPH0ZUAcozRhL29g%26m%3D%26qid%3D802009908%26im%3D1_t00df551a583a87f4e9%26src%3Dpcw_cloud%26t%3D1; T=s%3D3b0b1e33752a31cd3fa494cd32ab258e%26t%3D1478069158%26lm%3D%26lf%3D1%26sk%3D2da7b7be4da2e788300d3d2ab579075f%26mt%3D1478069158%26rc%3D%26v%3D2.0%26a%3D0; token=3030998290.55.e79095a3.802009908.1478069158; test_cookie_enable=null; count=18"
}
file_list_payload ={"type":"1","t":"0.615957312383044","order":"asc","field":"file_name","path":"/","page":0,"page_size":300,"ajax":1}
download_payload={"ajax":1}
replace_fields=["loginFlag","page","errmsg","errno","listType","field","order","type","previewSign","fileNum","data","oriName","path","nid","date","isDir","isFav","oriSize","size","scid","preview","hasThumb","thumb","fhash","fileType","fmtime"]

dir_path_list = []
used_path_list=[]
savepath ="D:\\workspace\yunpan_2016_jango"
current_file_list_json_path = savepath + "/op_log" + "1" + ".json"  # path.replace('/', '')
dirs_log_path=savepath + "/op_log_dirs" + "1" + ".json"
def file_list_post(path="/12306/"):
    # file_list_payload["path"] = path
    file_list_payload.update({"path":path})
    file_list_payload["nid"]="14495613079423672"
    headers.update({"Referer":"http://c-t.yunpan.360.cn/my/?sid=#"+path})
    print(file_list_payload)
    print("\r\t")
    r = requests.post(url=file_list_url,data=json.dumps(file_list_payload),headers =headers )
    rcs = r.content.decode("utf8","ignore")
    st = replace_with_fields(rcs).replace(",{}","").replace(",mtime",",'mtime'").replace("true","True").replace("false","False").replace('&"nid"=','&nid=').replace('&"size"=','&size=').replace('dev"type"=','devtype=').replace('""preview"Sign"','"previewSign"').strip()
    # print(st)
    # return
    # print(type(st))
    j = eval(st)
    print(j)
    return
    # print(type(j))
    yunpan_dir_list = []
    yunpan_file_list = []
    print("---------------------------------path:"+path+" start--------------------------------------------------------\r\t\n\n")
    errno = j["errno"]
    fileNum = j["fileNum"]
    if errno =='0' and fileNum >0:
        datalist = j["data"]
        for dataitem in datalist:
            # print(dataitem)
            isDir = 0
            try:
                isDir = dataitem["isDir"]
                # print(isDir)
                print("++++++++++++++++++++++++++++isDir:"+str(isDir)+"+++++++++++++++++++++++++++++++++++++++++++")
            except KeyError:
                isDir = 0
            if isDir ==1:
                dir_model = class_dir()
                dir_model.isDir = isDir
                dir_model.nid =dataitem["nid"]
                dir_model.oriName = dataitem["oriName"]
                dir_model.path = dataitem["path"]

                class_dir_model = dir_model.__dict__
                print(dir_model.path)
                dir_path_list.append(dir_model.path)
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

                f = open(current_file_list_json_path,"a")
                f.write(str(class_file_model)+"\r\t\n\n")
                f.close()
                #
                # file_json = json.dumps(class_file_model)
                # write_str(file_json)

    print(yunpan_dir_list)
    # unrepeat_dir_path_list =list(yunpan_dir_list)
    # print(unrepeat_dir_path_list)
    # len_dirpath = len(unrepeat_dir_path_list)
    # # print(path)
    # # write_str(file_json, current_file_list_json_path)
    # df = open(dirs_log_path,"a")
    # df.write(str(unrepeat_dir_path_list)+"\r\t\n\n")
    # df.close()
    # if len_dirpath > 0:
    #     for yunpan_dir_item in unrepeat_dir_path_list:
    #         print(yunpan_dir_item)
    #         if  yunpan_dir_item not in used_path_list:
    #             # break
    #             # print(type(yunpan_dir_item))
    #             # item_path = yunpan_dir_item["path"]
    #             _vpath = yunpan_dir_item["path"]
    #             create_dir(path=_vpath)
    #             file_list_post(path=_vpath)
    #             used_path_list.append(yunpan_dir_item)





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
    # _vpath ="%2FABP%E4%BA%A4%E6%B5%81%E4%BC%9A%2F"
    # file_list_post(_vpath)
    # len_dir = len(yunpan_dir_list)
    # file_json = json.dumps(yunpan_file_list)

    # print("---------------------------------path:" + item_path + " end --------------------------------------------------------\r\t\n\n\r\t\n\n")