from Core.DownloadData.Implements.DownloadDataExportImportFull import DownloadDataExportImportFull

class DownloadDataController:
    """
    Classe controladora que instância os objetos das implementações de DownloadData
    e chama seu fluxo de ações.
    """
    def __init__(self):
        """
        Construtor que cria os objetos da camada de Service de DownloadData
        """
        self.downloadDataExportImportFullService = DownloadDataExportImportFull()
    
    def downloadDataExportImportFull(self):
        """
        Chamada do fluxo do objeto de DownloadDataExportImportFull que baixará
        tanto dos dados de exportação quanto importações completos e utilizando NCM
        """
        self.downloadDataExportImportFullService.makeRequest()