from Core.DataStorage.DataStorageService.Implements.DataStorageServiceExportImplements import DataStorageServiceExportImplements

class DataStorageController:
    def __init__(self):
        self.dataStorageServiceExportImplements = DataStorageServiceExportImplements("./data/EXP_COMPLETA.csv", 25)
    
    def dataStorageServiceExport(self):
        self.dataStorageServiceExportImplements.loadDada()