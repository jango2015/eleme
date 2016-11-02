import requests
import bs4
from common import  get_response_by_url_with_headers

base_yunpan_url="http://c-t.yunpan.360.cn/my/?sid=#"
root_sid ="/"

headers ={
        "Host":" c-t.yunpan.360.cn",
        "Connection":" keep-alive",
        "Cache-Control":" max-age=0",
        "Accept":" text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Upgrade-Insecure-Requests":" 1",
        "User-Agent":" Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36",
        "Accept-Encoding":" gzip, deflate, sdch",
        "Accept-Language":" zh-CN,zh;q=0.8",
        "Cookie":" __guid=91251416.3086305693651073500.1477022817026.9539; __huid=101nfbTUxnm0B4BNiWVu%2BfgAAbS9ij7h15tA2k6Zm2ay0%3D; SEC_INFO_802009908=c-t.yunpan.360.cn; Q=u%3Dfntryl_001%26n%3D%26le%3DL3caZwN4ZPH0ZUAcozRhL29g%26m%3D%26qid%3D802009908%26im%3D1_t00df551a583a87f4e9%26src%3Dpcw_cloud%26t%3D1; T=s%3D3b0b1e33752a31cd3fa494cd32ab258e%26t%3D1478069158%26lm%3D%26lf%3D1%26sk%3D2da7b7be4da2e788300d3d2ab579075f%26mt%3D1478069158%26rc%3D%26v%3D2.0%26a%3D0; token=3030998290.55.e79095a3.802009908.1478069158; test_cookie_enable=null; count=15"
}

def get_yunpan_files_by_url(sid = root_sid):
    url = base_yunpan_url+sid
    str_html = get_response_by_url_with_headers(url=url,headers=headers)
    print(str_html)



if __name__ =="__main__":
    get_yunpan_files_by_url()




