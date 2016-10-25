from sqlalchemy import  Column,String,Integer,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import  declarative_base

from mongoservice import Insert

Base = declarative_base()

class MySql_Area(Base):
    __tablename__ ='sh_area'

    id = Column(Integer,primary_key= True)
    pid =Column(Integer)
    shortname = Column(String(100))
    name = Column(String(100))
    merger_name =Column(String(255))
    level = Column(Integer)
    pinyin = Column(String(100))
    code =Column(String(100))
    zip_code =Column(String(100))
    first = Column(String(50))
    lng = Column(String(100))
    lat = Column(String(100))

class Area:
    id= 0
    pid =0
    shortname=''
    name=''
    merger_name=''
    level=0
    pinyin=''
    code=''
    zip_code=''
    first=''
    lng=''
    lat=''

mysql_engine = create_engine("mysql+mysqlconnector://root:123456@localhost:3306/areas")
DBSession = sessionmaker(bind=mysql_engine)


def get_areas_from_Mysql():
    session = DBSession()
    areas = session.query(MySql_Area).all()
    itmes = []
    print(len(areas))
    for item in areas:
        class_item = item.__dict__
        # print(class_item)
        area = Area()
        area.id = class_item.get("id")
        area.pid = class_item.get("pid")
        area.shortname = class_item.get("shortname")
        area.name = class_item.get("name")
        area.merger_name = class_item.get("merger_name")
        area.level = class_item.get("level")
        area.pinyin = class_item.get("pinyin")
        area.code = class_item.get("code")
        area.zip_code = class_item.get("zip_code")
        area.first = class_item.get("first")
        area.lng = class_item.get("lng")
        area.lat = class_item.get("lat")
        class_area = area.__dict__
        # print(class_area)

        itmes.append(class_area)

        # Insert(class_item,'Spider_China_Areas')
        # lists.append(item.__dict__)
    Insert(itmes,"Spider_China_Areas")
    # print(areas[0].__dict__)


if __name__ == '__main__':
    get_areas_from_Mysql()