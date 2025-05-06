import pandas as pd

class DataStorageTemplate:
    """
    Classe com a implementação geral do tratamento dos dados de exportação
    e importação, como os passos de tratar a exportação são todos comuns ao
    da importação, esse template já é o bastante para tratar exportação e terá
    um método reescrito para a importação.
    """
    def __init__(self, path: str, repository):
        """
        Construtor do template

        Args:
            path (str): Caminho para o arquivo csv.
            repository (str): Um objeto DataStorageRepositoryTemplate para persistir os dados.
        """
        self.path = path
        self.repository = repository

    def loadDada(self) -> str:
        """
        Abre o arquivo .csv e coloca em um dataframe pandas.

        Returns:
            str: Mensagem de sucesso ou erro.

        Errors:
            FileNotFoundError: Se o arquivo não for encontrado no caminho recebido.
            UnicodeDecodeError: Se a codificação do arquivo for incompatível com 'utf-8'.
            pandas.errors.ParserError: Se o conteúdo do CSV estiver mal formado.
            OSError: Em caso de problemas ao acessar o arquivo.
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
        Trata as colunas do dataframe, que são comuns a exportação e
        importação, eliminando dados nulos e forá dos intervalos especificados.
        
        Args:
            data (pd.DataFrame): DataFrame carregado na ultima etapa.

        Returns:
            str: Mensagem de sucesso ou erro.
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
        Trata as colunas especificas da importação, e será sobrescrito na
        implementação de importação.

        Args:
            data (pd.DataFrame): DataFrame com os dados verificados na etapa geral.

        Returns:
            str: Mensagem de sucesso ou erro.
        """
        return self.persistData(data)
    
    def persistData(self, data: pd.DataFrame) -> str:
        """
        Passa o dataframe para o repository persistir.

        Args:
            data (pd.DataFrame): DataFrame com os dados tratados para inserir no banco.

        Returns:
            str: Mensagem de sucesso ou erro.
        """
        return self.repository.insertData(data)
