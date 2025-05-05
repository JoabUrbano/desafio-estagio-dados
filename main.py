from Core.DownloadData.DownloadDataController import DownloadDataController
from Core.DataStorage.DataStorageController import DataStorageController

#downloadDataController = DownloadDataController()
#downloadDataController.downloadDataExportImportFull()

dataStorageController = DataStorageController()
#print(dataStorageController.dataStorageServiceExport())
print(dataStorageController.dataStorageServiceImport())
