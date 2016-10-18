import os
from common import get_content_by_url
from mongoservice import Insert
# from Geohash import geohash
import Geohash
eleme_cities ='https://mainsite-restapi.ele.me/shopping/v1/cities'

restaurant_category ='https://mainsite-restapi.ele.me/shopping/v2/restaurant/category?latitude=31.21551&longitude=121.44695' #by gps

pois_nearby ='https://mainsite-restapi.ele.me/v2/pois?extras%5B%5D=count&geohash=wtw3sjq6n6um&keyword=世纪大道&limit=20&type=nearby'

restaurant_gps_nearby ='https://mainsite-restapi.ele.me/shopping/restaurants?extras%5B%5D=activities&geohash=wtw3syjydf6&latitude=31.23526&limit=24&longitude=121.50582&offset=0'  #offset : pagesize geohash: geo hashcode


filepath =os.path.abspath("./city/eleme_cities_withGeohash.json")
def get_cities():
   content = get_content_by_url(eleme_cities)
   data =content.decode("utf8","ignore")
   obj =eval(data)
   print(sorted(obj.keys()))
   f = open(filepath, 'a')
   s = str(obj)
   f.write(s)
   f.close()
   for item in sorted(obj.keys()):
       cities =[]
       key = item
       item_list = obj[item]
       print(key)
       print(item_list)
       print("\n")
       for city in item_list:
           print(city)
           eleme_city = ElemeCities_Item()
           eleme_city.or_id = city["id"]
           eleme_city.meta = key
           eleme_city.abbr = city["abbr"]
           eleme_city.latitude = city["latitude"]
           eleme_city.longitude = city["longitude"]
           eleme_city.name = city["name"]
           eleme_city.pinyin = city["pinyin"]
           # eleme_city.geohash =geohash.encode(eleme_city.latitude,eleme_city.longitude,precision=12)
           eleme_city.geohash =Geohash .encode(eleme_city.latitude,eleme_city.longitude)
           print("\n")
           v= eleme_city.__dict__
           print(v)
           cities.append(v)
       Insert(cities, "Spider_Eleme_Cities_WithGeoHash")



class ElemeCities_Item:
    or_id = ''
    meta =''
    abbr= ''
    latitude =''
    longitude =''
    name =''
    pinyin = ''
    geohash =''


if __name__ == '__main__':
    get_cities()