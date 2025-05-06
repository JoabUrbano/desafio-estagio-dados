from Core.DataStorage.DataStorageService.Template.DataStorageTemplate import DataStorageTemplate
from Core.DataStorage.DataStorageService.Implements.DataStorageServiceImportImplements import DataStorageServiceImportImplements

from Core.DataStorage.DataStorageRepository.Implements.DataStorageExportRepositoryImplement import DataStorageExportRepositoryImplement
from Core.DataStorage.DataStorageRepository.Implements.DataStorageImportRepositoryImplement import DataStorageImportRepositoryImplement

class DataStorageController:
    """
    Controlador que instância os objetos das implementações de DataStorageTemplate
    da camada de serviço e instância também as implementações dos seus respectivos
    repositorys, para persistir os dados.
    """
    def __init__(self):
        """
        Construtor que instância todos os objetos services e repositorys, e passa
        como parametro para os objetos da camada de serviço o caminho para os dados
        e o objeto repository correspondente para persistir os dados
        """
        self.dataStorageExportRepositoryImplement = DataStorageExportRepositoryImplement()
        self.dataStorageServiceExportImplements = DataStorageTemplate("./data/EXP_COMPLETA.csv", self.dataStorageExportRepositoryImplement)
        
        self.dataStorageImportRepositoryImplement = DataStorageImportRepositoryImplement()
        self.dataStorageServiceImportImplements = DataStorageServiceImportImplements("./data/IMP_COMPLETA.csv", self.dataStorageImportRepositoryImplement)
    
    def dataStorageServiceExport(self):
        """
        Chama o objeto da camada de serviço que trata as exportações completas

        :return: Mensagem de sucesso ou erro.
        :rtype: str
        """
        return self.dataStorageServiceExportImplements.loadDada()
    
    def dataStorageServiceImport(self):
        """
        Chama o objeto da camada de serviço que trata as importações completas

        :return: Mensagem de sucesso ou erro.
        :rtype: str
        """
        return self.dataStorageServiceImportImplements.loadDada()
