import requests
from bs4 import BeautifulSoup
import os
import urllib.parse

class DownloadDataTemplate:
    def __init__(self):
        self.base_url = ""
        self.page_url = ""
        self.filesToDownload = []

    def makeRequest(self):
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
