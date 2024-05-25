from bkjc_database.CONFIG import database_type
from bkjc_database.NerCarDataBase.mysql.models.ncdhotstripdefect import Camdefect1, Camdefect2
from bkjc_database.property.DataBaseInterFace import DbItem


class DefectDb(DbItem):
    def __init__(self):
        if database_type == "ncdhotstrip":
            self.databaseName = "ncdhotstripdefect"
        else:
            self.databaseName = "Ncdplatedefect"
        super().__init__(self.databaseName)

    def getDefectByDefectId(self, cameraId, defectId):
        with self.Session() as session:
            try:
                if cameraId == 1:
                    return session.query(Camdefect1).where(Camdefect1.defectID == defectId)[0]
                else:
                    return session.query(Camdefect2).where(Camdefect2.defectID == defectId)[0]
            except:
                session.rollback()
                return None

    def getLastDefect(self, cameraId):
        with self.Session() as session:
            try:
                if cameraId == 1:
                    return session.query(Camdefect1)[-1]
                else:
                    return session.query(Camdefect2)[-1]
            except:
                session.rollback()
                return None


Session = DefectDb().Session
