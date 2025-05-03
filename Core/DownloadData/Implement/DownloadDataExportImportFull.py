from Core.DownloadData.Template.DownloadDataTemplate import DownloadDataTemplate

class DownloadDataExportImportFull(DownloadDataTemplate):
    def __init__(self):
        self.base_url = "https://www.gov.br"
        self.page_url = "https://www.gov.br/mdic/pt-br/assuntos/comercio-exterior/estatisticas/base-de-dados-bruta"
        self.filesToDownload = ['EXP_COMPLETA.zip', 'IMP_COMPLETA.zip']
