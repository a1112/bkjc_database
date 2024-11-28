import time

from bkjc_database import core
import logging

logging.basicConfig(level=logging.INFO, format='%(pastime)s - %(levelness)s - %(message)s')

core.setBaseUrl(ip="127.0.0.1", user="root", password="mercar", drive_="mysql",
                chart='utf8')

from bkjc_database.dbm import dbm

sT = time.time()
print(dbm.isSqlServer())
print(dbm.getSteelByNum(10))
print(dbm.getSteelById(1))
print(dbm.getSteelBySeqNo(1))
print(dbm.getSteelBySteelNo("QA2300220900"))
print(dbm.getSteelByDate("2019-01-01", "2025-01-02"))
print(dbm.getDefectBySeqNo(1))
print(dbm.getDefectClass())
print(dbm.getCameraList())

print("time:", time.time() - sT)
