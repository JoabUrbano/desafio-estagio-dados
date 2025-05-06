from Core.DownloadData.Template.DownloadDataTemplate import DownloadDataTemplate

class DownloadDataExportImportFull(DownloadDataTemplate):
    """
    Implementação do template DownloadDataTemplate que
    sobrescreve o método construtor com as informações
    necessarias
    """
    def __init__(self):
        """
        Construtor sobrescrito para especificar o site e os arquivos
        que serão baixados
        """
        self.base_url = "https://www.gov.br"
        self.page_url = "https://www.gov.br/mdic/pt-br/assuntos/comercio-exterior/estatisticas/base-de-dados-bruta"
        self.filesToDownload = ['EXP_COMPLETA.zip', 'IMP_COMPLETA.zip']
        self.directory = "./data"
