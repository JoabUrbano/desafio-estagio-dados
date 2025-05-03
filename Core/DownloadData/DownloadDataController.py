from Core.DownloadData.Implement.DownloadDataExportImportFull import DownloadDataExportImportFull

class DownloadDataController:
    def __init__(self):
        self.downloadDataExportImportFullService = DownloadDataExportImportFull()
    
    def downloadDataExportImportFull(self):
        self.downloadDataExportImportFullService.makeRequest()