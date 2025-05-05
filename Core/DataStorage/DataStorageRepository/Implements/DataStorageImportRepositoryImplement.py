from Core.DataStorage.DataStorageRepository.Template.DataStorageRepositoryTemplate import DataStorageRepositoryTemplate

class DataStorageImportRepositoryImplement(DataStorageRepositoryTemplate):
    def insertData(self, dados) -> str:
        """
        Sobrescrição com os parametros de importação para inserir no banco

        :param dados: dataframe enviado pela camada de serviço
        :type dados: pd.DataFrame

        :return: Mensagem de sucesso ou erro.
        :rtype: str
        """
        
        sql = """
            INSERT INTO tb_import 
            (codigo_ano, codigo_mes, codigo_ncm, codigo_unidade, codigo_pais, estado_destino, codigo_via_transporte, codigo_unidade_receita_federal_desembarque, quantidade_produto, peso_kilo, valor_mercadoria, valor_frete, valor_seguro)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
	
        return self.persistData(dados, sql)
