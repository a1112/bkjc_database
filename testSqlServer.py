import time

import bkjc_database
from bkjc_database import core
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# core.setBaseUrl(ip="127.0.0.1", user="ARNTUSER", password="ARNTUSER", drive_="sqlserver",
#                 chart='utf8')
bkjc_database.CONFIG.database_type="Ncdplate"
core.setBaseUrl(ip="172.25.2.4２", user="root", password="nercar", drive_="mysql",
                chart='utf8')

from bkjc_database.dbm import dbm
print(dbm.getSteelByNum(100))

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
