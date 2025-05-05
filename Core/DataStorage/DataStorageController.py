from Core.DataStorage.DataStorageService.Template.DataStorageTemplate import DataStorageTemplate
from Core.DataStorage.DataStorageService.Implements.DataStorageServiceImportImplements import DataStorageServiceImportImplements

class DataStorageController:
    def __init__(self):
        """
        Método construtor que instância todos os objetos services
        """
        self.dataStorageServiceExportImplements = DataStorageTemplate("./data/EXP_COMPLETA.csv", 25)
        self.dataStorageServiceImportImplements = DataStorageServiceImportImplements("./data/IMP_COMPLETA.csv", 25)
    
    def dataStorageServiceExport(self):
        """
        Método que chama o objeto para tratar as exportações completas
        """
        self.dataStorageServiceExportImplements.loadDada()
    
    def dataStorageServiceImport(self):
        """
        Método que chama o objeto para tratar as importações completas
        """
        self.dataStorageServiceImportImplements.loadDada()
