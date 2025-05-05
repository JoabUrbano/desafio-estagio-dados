import pandas as pd

class DataStorageTemplate:
    def __init__(self, path: str, repository):
        """
        Método construtor

        :param path: Caminho para o arquivo a ser lido
        :type path: str
        :param repository: Instância de RepositoryTemplate
        :type repository: RepositoryTemplate
        """
        self.path = path
        self.repository = repository

    def loadDada(self) -> str:
        """
        Método para abrir o arquivo .csv e coloca em um dataframe pandas

        :return: Mensagem de sucesso ou erro.
        :rtype: str

        :raises FileNotFoundError: Se o arquivo não for encontrado no caminho recebido.
        :raises UnicodeDecodeError: Se a codificação do arquivo for incompatível com 'utf-8'.
        :raises pandas.errors.ParserError: Se o conteúdo do CSV estiver mal formado.
        :raises OSError: Em caso de problemas ao acessar o arquivo.
        """
        try:
            data = pd.read_csv(
                self.path, sep=";", encoding="utf-8", escapechar="\n"
            )
            return self.VerifyDataExportImport(data)
            
        except Exception as e:
            return f"Erro ao abrir o arquivo: {e}."
        
    def VerifyDataExportImport(self, data: pd.DataFrame) -> str:
        """
        Método que trata as colunas do dataframe, trata as linhas com 
        informações nulas ou erradas
        
        :param data: Dataframe pandas contendo os dados do arquivo aberto
        :type data: pd.DataFrame

        :return: Mensagem de sucesso ou erro.
        :rtype: str
        """
        required_columns = [
            "CO_ANO", "CO_MES", "CO_NCM", "CO_UNID", "CO_PAIS",
            "SG_UF_NCM", "CO_VIA", "CO_URF", "QT_ESTAT", "KG_LIQUIDO", "VL_FOB"
        ]
        data = data.dropna(subset=required_columns)

        data = data[data['CO_NCM'].astype(str).str.len() <= 8]

        data["CO_ANO"] = pd.to_numeric(data["CO_ANO"], errors='coerce')
        data["CO_MES"] = pd.to_numeric(data["CO_MES"], errors='coerce')
        data["CO_NCM"] = pd.to_numeric(data["CO_NCM"], errors='coerce')
        data["CO_UNID"] = pd.to_numeric(data["CO_UNID"], errors='coerce')
        data["CO_PAIS"] = pd.to_numeric(data["CO_PAIS"], errors='coerce')
        data["CO_VIA"] = pd.to_numeric(data["CO_VIA"], errors='coerce')
        data["CO_URF"] = pd.to_numeric(data["CO_URF"], errors='coerce')
        data["QT_ESTAT"] = pd.to_numeric(data["QT_ESTAT"], errors='coerce')
        data["KG_LIQUIDO"] = pd.to_numeric(data["KG_LIQUIDO"], errors='coerce')
        data["VL_FOB"] = pd.to_numeric(data["VL_FOB"], errors='coerce')

        data = data[(data["CO_ANO"] >= 1997) & (data["CO_ANO"] <= 2100)]
        data = data[(data["CO_MES"] >= 1) & (data["CO_MES"] <= 12)]

        return self.VerifyDataImport(data)
    
    def VerifyDataImport(self, data: pd.DataFrame) -> str:
        """
        Método que trata as colunas especificas da importação a ser sobrescrito
        
        :param data: Dataframe pandas contendo os dados do arquivo aberto
        :type data: pd.DataFrame

        :return: Mensagem de sucesso ou erro.
        :rtype: str
        """
        return self.persistData(data)
    
    def persistData(self, data: pd.DataFrame) -> str:
        """
        Passa o dataframe para o repository persistir.

        Args:
            data (pd.DataFrame): DataFrame com os dados a tratar.

        Returns:
            str: Mensagem de sucesso ou erro.
        """
        return self.repository.insertData(data)
