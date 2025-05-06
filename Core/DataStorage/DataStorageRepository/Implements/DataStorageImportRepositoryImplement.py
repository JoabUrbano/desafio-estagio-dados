from Core.DataStorage.DataStorageRepository.Template.DataStorageRepositoryTemplate import DataStorageRepositoryTemplate

class DataStorageImportRepositoryImplement(DataStorageRepositoryTemplate):
    """
    Implementação que cuida dos dados de importação
    """
    def insertData(self, dados) -> str:
        """
        Sobrescrição com os parametros de importação para inserir no banco

        Args:
            data (pd.DataFrame): DataFrame tratado enviado pela camada de serviço.

        Returns:
            str: Mensagem de sucesso ou erro.
        """
        
        sql = """
            INSERT INTO tb_import 
            (codigo_ano, codigo_mes, codigo_ncm, codigo_unidade, codigo_pais, estado_destino, codigo_via_transporte, codigo_unidade_receita_federal_desembarque, quantidade_produto, peso_kilo, valor_mercadoria, valor_frete, valor_seguro)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
	
        return self.persistData(dados, sql)
