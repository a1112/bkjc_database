from typing import List
from NerCarDataBase.BaseImport import *
from NerCarDataBase.SqlBase import init
from NerCarDataBase.SqlTool import to_dict
from NerCarDataBase.core import beforeInit

from NerCarDataBase import core
from bkjc_database.NerCarDataBase.mysql.models.ncdplatedevice import Camera

from bkjc_database.property.DataBaseInterFace import DbItem
from config import serverDataBaseIp

core.setBaseUrl(ip=serverDataBaseIp, port=1433, user='root', password="nercar", drive_="mysql",
                chart='utf8')

from NerCarDataBase.mysql.models.ncdplatedevice import *

databaseName = "Ncdplatedevice"

engine: Engine
Base: automap_base
Session: sessionmaker
session: Session
inspector: Inspector
table_names: list


def dbInit():
    global engine, Base, Session, session, inspector, table_names
    engine, Base, Session, session, inspector = init(databaseName)
    table_names = inspector.get_table_names()


dbInit()
session.commit()

class DeviceDb(DbItem):
    def getCameraInfo(self):
        lastCamera: Camera
        cameraDict = {}

        for c in range(10):
            try:
                lastCamera = session.query(Camera).where(Camera.cam == c + 1)[-1]
                dicData = to_dict(lastCamera)
                dicData["isRun"] = True
                cameraDict[dicData['cam']] = dicData
            except:
                break
        return cameraDict


    def getLightInfo(self):
        light: Light
        lightDict = {}
        for c in range(10):
            try:
                lasttlight = session.query(Light)[-1]
                lasttlight=to_dict(lasttlight)
                lasttlight["isRun"]=True
                lightDict[str(lasttlight.LightNo)] = lasttlight
            except:
                break
        return lightDict


if __name__ == "__main__":

    print(getCameraInfo())
    print(getCameraInfo())
    print(getCameraInfo())
    light: Light
    lightList = []
    for c in range(10):
        try:
            lasttlight = session.query(Light)[-1]
            lightList.append(to_dict(lasttlight))
        except:
            break
    print(session.query(Light).count())
    print(len(lightList))
    print(lightList)
