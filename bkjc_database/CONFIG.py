database_type = "ncdhotstrip"
systemDatabase = ["master", "model", "msdb", "tempdb"]
baseUrl = "mssql+pymssql://ARNTUSER:ARNTUSER@127.0.0.1:1433/{}?charset=utf8"
echo: bool = False
beforeInit = True
databaseCheckInfo = {}  # 数据库正确性验证字典
drive = "sqlserver"
databaseList = ['DWDiagnostics', 'DWConfiguration', 'DWQueue', 'Classifier', 'SteelRecord', "ConfigCenter"]
