from common import *
from bs4 import BeautifulSoup
import os
vdisk_files_url = "http://vdisk.weibo.com/s/"
vdisk_files_code = "Cb1ItMmDIM8dQ"

current_download_url =""
save_file_dir =os.path.abspath("./v_disk_download_dirs/")
file_save_path =""
if os.path.exists(save_file_dir) == False:
    os.makedirs(save_file_dir)
current_save_file_dir= os.path.abspath("./v_disk_download_dirs/")

vdisk_dirs_path = os.path.abspath("./vdisk_dirs.json")
vdisk_files_path = os.path.abspath("./vdisk_files.json")
vdisk_file_download_log_path = os.path.abspath("./vdisk_file_download_logs.json")

file_formats =".pdf,.txt,.rar,.doc,.xls,.docx,.xlsx,.ppt,.pptx,.tar,.kdh,.jpg,.ace,.mp3,.av,.mpg,.mp4,.mv,.mov,.mht,.flv,.exe,.zip,.caj,.uvz,.chm,.djvu,.rm,.7z,"
vdisk_all_files =[]
def get_vdisk_files_by_code(code = vdisk_files_code,current_dir_path =save_file_dir):
    url = vdisk_files_url +code
    html = get_content_by_url_utf8(url)
    # print(html)
    html = html_content_without_special_chars(html)
    soup = BeautifulSoup(html)

    f_lists = soup.select("body .vd_main .filelist .sort_name_m .short_name")
    # print(f_lists)
    print(len(f_lists))
    vdisk_files =[]
    vdisk_dirs =[]
    for f_list in f_lists:
        # print(f_list)
        filename= str(f_list.string)
        pos = filename.rfind(".")
        # print(pos)
        file_format = filename[pos:]
        if pos >0 and file_formats.find(file_format.lower())>-1:
            # print(file_format)
            c_disk_file = vdisk_file()
            c_disk_file.name =html_content_without_special_chars(str(f_list.string))
            c_disk_file.url = f_list["href"]
            c_disk_file.title =html_content_without_special_chars(f_list["title"])
            class_vdisk_file = c_disk_file.__dict__
            # print(class_vdisk_file)
            vdisk_files.append(class_vdisk_file)
            vdisk_all_files.append(class_vdisk_file.copy())

            download_file_url = get_download_url_by_url(c_disk_file.url)
            current_download_url = c_disk_file.url
            st_logs = "___________________download file  url:"+current_download_url+"  开始下载 "+c_disk_file.title+"___________________________"
            print(st_logs)
            f = open(vdisk_file_download_log_path, "a")
            f.write(st_logs)
            f.close()
            import requests
            r = requests.get(download_file_url)
            with open(str(current_dir_path)+"/"+c_disk_file.title,"wb") as code:
                code.write(r.content)
            st_logs="****************************download file  url:"+current_download_url+" ********"+c_disk_file.title+"下载成功******************************************" +"\r\t"
            f  = open(vdisk_file_download_log_path,"a")
            f.write(st_logs)
            f.close()
        else:
            c_disk_dir = vdisk_dir()
            c_disk_dir.name = f_list.string
            c_disk_dir.url = f_list["href"]
            c_disk_dir.title = f_list["title"]
            pre_pos = c_disk_dir.url.rfind("/")+1
            la_poso = c_disk_dir.url.find("?")
            # subst = c_disk_dir.url[:pre_pos]
            c_disk_dir.code =c_disk_dir.url[pre_pos:la_poso]
            class_vdisk_dir = c_disk_dir.__dict__
            # print(class_vdisk_dir)
            vdisk_dirs.append(class_vdisk_dir)
    # print(vdisk_dirs)
    # print("\r\t")
    print(vdisk_files)
    print("\r\t")
    # if len(vdisk_files)>0:
    #     f_file = open(vdisk_files_path,"a")
    #     s = str(vdisk_files)
    #     f_file.write(s+","+"\r\t")
    #     f_file.close()
    # if len(vdisk_dirs) >0:
    #     f_file = open(vdisk_dirs_path, "a")
    #     s = str(vdisk_dirs)
    #     f_file.write(s+"\r\t")
    #     f_file.close()

    if len(vdisk_dirs) >0:
        for v_disk_dir in vdisk_dirs:
            print("\r\t")
            # print(v_disk_dir)
            print(v_disk_dir["name"])
            # return
            current_save_file_dir = current_save_file_dir +"/"+ str(v_disk_dir["name"])
            if os.path.exists(current_save_file_dir) ==False:
                os.makedirs(current_save_file_dir)
            print("***********************get code :"+v_disk_dir['code']+" *******************************")
            get_vdisk_files_by_code(code =v_disk_dir['code'],current_dir_path=current_save_file_dir)

def get_download_url_by_url(url):
    html = get_content_by_url_utf8(url)
    html = html_content_without_special_chars(html)
    # print(html)
    soup = BeautifulSoup(html)
    scripts = soup.select("script")
    print(len(scripts))
    # print(type(scripts))
    # print(scripts[8])
    vs_sc_data = str(scripts[8])
    # print(str(vs_sc_data))
    pre_po = vs_sc_data.rfind("fileDown.init(")
    la_po = vs_sc_data.rfind('"});')+2
    # _la_po = vs_sc_data
    file_download_info = vs_sc_data[pre_po:la_po].replace("fileDown.init(","")
    import json
    jo = json.loads(file_download_info)
    # print(file_download_info)
    print(jo)
    download_list_url = jo["download_list"]
    print(download_list_url)
    print(download_list_url[0])
    return  download_list_url[0]

        # for sc in script:
        #
        # if str(script).find("vdisk.pagedata") >-1:
        #     print("\r\t \r\t")



class vdisk_dir:
    title =''
    url =''
    name =''
    code =''

class vdisk_file:
    title =''
    url =""
    name =''


vdisk_All_files_path = os.path.abspath("./vdisk_all_files.json")
if __name__ =="__main__":
    get_vdisk_files_by_code()
    # print(len(vdisk_all_files))
    # if len(vdisk_all_files)>0:
    #     f_file = open(vdisk_All_files_path,"a")
    #     s = str(vdisk_all_files)
    #     f_file.write(s+"\r\t")
    #     f_file.close()
    # v_url ="http://vdisk.weibo.com/s/Cb1ItMmDIXelj?category_id=0&parents_ref=Cb1ItMmDIM8dQ"
    # get_download_url_by_url(v_url)
