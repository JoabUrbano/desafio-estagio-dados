from Core.DataStorage.DataStorageService.Template.DataStorageTemplate import DataStorageTemplate
from Core.DataStorage.DataStorageService.Implements.DataStorageServiceImportImplements import DataStorageServiceImportImplements

from Core.DataStorage.DataStorageRepository.Implements.DataStorageExportRepositoryImplement import DataStorageExportRepositoryImplement
from Core.DataStorage.DataStorageRepository.Implements.DataStorageImportRepositoryImplement import DataStorageImportRepositoryImplement

class DataStorageController:
    def __init__(self):
        """
        Método construtor que instância todos os objetos services
        """
        self.dataStorageExportRepositoryImplement = DataStorageExportRepositoryImplement()
        self.dataStorageServiceExportImplements = DataStorageTemplate("./data/EXP_COMPLETA.csv", self.dataStorageExportRepositoryImplement)
        
        self.dataStorageImportRepositoryImplement = DataStorageImportRepositoryImplement()
        self.dataStorageServiceImportImplements = DataStorageServiceImportImplements("./data/IMP_COMPLETA.csv", self.dataStorageImportRepositoryImplement)
    
    def dataStorageServiceExport(self):
        """
        Método que chama o objeto para tratar as exportações completas

        :return: Mensagem de sucesso ou erro.
        :rtype: str
        """
        return self.dataStorageServiceExportImplements.loadDada()
    
    def dataStorageServiceImport(self):
        """
        Método que chama o objeto para tratar as importações completas

        :return: Mensagem de sucesso ou erro.
        :rtype: str
        """
        return self.dataStorageServiceImportImplements.loadDada()
