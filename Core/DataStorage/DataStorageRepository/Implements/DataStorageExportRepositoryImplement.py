from Core.DataStorage.DataStorageRepository.Template.DataStorageRepositoryTemplate import DataStorageRepositoryTemplate

class DataStorageExportRepositoryImplement(DataStorageRepositoryTemplate):
    def insertData(self, dados) -> str:
        """
        Sobrescrição com os parametros de exportação para inserir no banco

        :param dados: dataframe enviado pela camada de serviço
        :type dados: pd.DataFrame

        :return: Mensagem de sucesso ou erro.
        :rtype: str
        """
        
        sql = """
            INSERT INTO tb_export 
            (codigo_ano, codigo_mes, codigo_ncm, codigo_unidade, codigo_pais, estado_origem, codigo_via_transporte, codigo_unidade_receita_federal_embarque, quantidade_produto, peso_kilo, valor_mercadoria) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
	
        return self.persistData(dados, sql)
