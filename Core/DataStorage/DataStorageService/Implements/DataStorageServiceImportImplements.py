from Core.DataStorage.DataStorageService.Template.DataStorageTemplate import DataStorageTemplate

import pandas as pd

class DataStorageServiceImportImplements(DataStorageTemplate):
        
    def VerifyDataImport(self, data: pd.DataFrame) -> str:
        """
        Sobrescreção do método para tratar as colunas exclusivas da importação
        que são as de valores de frete e seguro
        
        :param data: Dataframe pandas contendo os dados do arquivo aberto
        :type path: pd.DataFrame

        :return: Mensagem de sucesso ou erro.
        :rtype: str
        """
        required_columns = [
            "VL_FRETE", "VL_SEGURO"
        ]
        data = data.dropna(subset=required_columns)

        data["VL_FRETE"] = pd.to_numeric(data["VL_FRETE"], errors='coerce')
        data["VL_SEGURO"] = pd.to_numeric(data["VL_SEGURO"], errors='coerce')

        data = data[(data["VL_FRETE"] >= 0)]
        data = data[(data["VL_SEGURO"] >= 0)]

        return self.repository.insertData(data)

