import time

from bkjc_database import core
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

core.setBaseUrl(ip="127.0.0.1", user="ARNTUSER", password="ARNTUSER", drive_="sqlserver",
                chart='utf8')

from bkjc_database.dbm import dbm
print(dbm.getSteelByNum(10))

sT=time.time()
print(dbm.isSqlServer())
print(dbm.getSteelByNum(10))
print(dbm.getSteelById(221111)[0][1].ID)
print(dbm.getSteelBySeqNo(221111))
print(dbm.getSteelBySteelNo("3A15150400"))
print(dbm.getSteelByDate("2019-01-01", "2025-01-02"))
print(dbm.getDefectBySeqNo(1))
print(dbm.getDefectClass())
print(dbm.getCameraList())
print("time:",time.time()-sT)
