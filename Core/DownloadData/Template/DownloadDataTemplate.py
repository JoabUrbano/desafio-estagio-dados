import requests
from bs4 import BeautifulSoup
import os
import urllib.parse
import zipfile

class DownloadDataTemplate:
    """
    Método construtor base que será sobrescrito
    """
    def __init__(self):
        self.base_url = ""
        self.page_url = ""
        self.filesToDownload = []
        self.directory = ""

    def makeRequest(self):
        """
        Método que faz a requisição para o site especificado e campura o
        HTML e cria a pasta onde será armazenado os downloads
        """
        response = requests.get(self.page_url)
        reqPage = BeautifulSoup(response.content, 'html.parser')
        os.makedirs("data", exist_ok=True)
        self.downloadFiles(reqPage)

    def downloadFiles(self, reqPage):
        """
        Método que procura e baixa apenas os arquivos filtrados
        """
        for a in reqPage.find_all('a', href=True):
            href = a['href']
            for fileName in self.filesToDownload:
                if fileName in href:
                    download_url = urllib.parse.urljoin(self.base_url, href)
                    file = fileName
                    print(f"Baixando: {file}")
                    file_response = requests.get(download_url)
                    with open(os.path.join("data", file), 'wb') as f:
                        f.write(file_response.content)

        print("Download finalizado.")
        self.unzipFiles()
    
    def unzipFiles(self):
        """
        Método que descompacta os arquivos baixados e apaga os zips
        """
        for nome_arquivo in os.listdir(self.directory):
            if nome_arquivo.endswith(".zip"):
                caminho_zip = os.path.join(self.directory, nome_arquivo)
                with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
                    zip_ref.extractall(self.directory)
                    print(f"Extraído: {nome_arquivo} para {self.directory}")
                os.remove(caminho_zip)
        
