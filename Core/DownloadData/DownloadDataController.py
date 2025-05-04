from Core.DownloadData.Implement.DownloadDataExportImportFull import DownloadDataExportImportFull

class DownloadDataController:
    def __init__(self):
        """
        Método construtor que cria os objetos service
        """
        self.downloadDataExportImportFullService = DownloadDataExportImportFull()
    
    def downloadDataExportImportFull(self):
        """
        Método que chama o objeto de DownloadDataExportImportFull
        """
        self.downloadDataExportImportFullService.makeRequest()