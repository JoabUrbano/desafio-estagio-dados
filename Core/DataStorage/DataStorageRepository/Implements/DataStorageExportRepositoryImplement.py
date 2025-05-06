from Core.DataStorage.DataStorageRepository.Template.DataStorageRepositoryTemplate import DataStorageRepositoryTemplate

class DataStorageExportRepositoryImplement(DataStorageRepositoryTemplate):
    """
    Implementação que cuida dos dados de exportação
    """
    def insertData(self, dados) -> str:
        """
        Sobrescrição com os parametros de exportação para inserir no banco

        Args:
            data (pd.DataFrame): DataFrame tratado enviado pela camada de serviço.

        Returns:
            str: Mensagem de sucesso ou erro.
        """
        
        sql = """
            INSERT INTO tb_export 
            (codigo_ano, codigo_mes, codigo_ncm, codigo_unidade, codigo_pais, estado_origem, codigo_via_transporte, codigo_unidade_receita_federal_embarque, quantidade_produto, peso_kilo, valor_mercadoria) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
	
        return self.persistData(dados, sql)
