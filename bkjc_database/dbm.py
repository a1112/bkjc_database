from bkjc_database import CONFIG
if CONFIG.drive == "sqlserver":
    from .ss.dbi import SqlServer_3d0 as SqlObj
else:
    from .ms.dbi import Mysql_4d0 as SqlObj

dbm = SqlObj()
