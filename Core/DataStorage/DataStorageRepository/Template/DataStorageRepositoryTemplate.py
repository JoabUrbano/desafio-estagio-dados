import pymysql
import pandas as pd

from dotenv import load_dotenv
import os
load_dotenv()

class DataStorageRepositoryTemplate:

    def __init__(self):
        """
        Método construtor que pega as variaveis de ambiente com as informações do banco
        """
        self.host = os.getenv("DB_HOST")
        self.port = int(os.getenv("DB_PORT", 3306))
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB_DATABASE")

    def insertData(self, dados: pd.DataFrame) -> str:
        """
        Método a ser sobrescrito com os parametros do dataframe para inserir no banco

        :param dados: dataframe enviado pela camada de serviço
        :type dados: pd.DataFrame

        :return: Mensagem de sucesso ou erro.
        :rtype: str
        """
        sql = ""
        return self.persistData(dados, sql)
    
    def persistData(self, dados, sql) -> str:
        """
        Método para persistir os dados no banco

        :param dados: dataframe enviado pela camada de serviço
        :type dados: pd.DataFrame
        :param sql: Comando SQL para inserir os dados
        :type sql: str

        :return: Mensagem de sucesso ou erro.
        :rtype: str

        :raises AttributeError: Se o objeto `dados` não for um DataFrame válido.
        :raises ValueError: Se houver problemas na conversão dos dados para tuplas.
        :raises pymysql.err.OperationalError: Se houver erro na conexão com o banco de dados.
        :raises pymysql.err.ProgrammingError: Se o comando SQL estiver incorreto.
        :raises pymysql.err.IntegrityError: Se houver violação de integridade no banco.
        :raises pymysql.MySQLError: Para quaisquer outros erros relacionados ao MySQL.
        """
        batch_size: int = 3000
        try:
            with pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            ) as connection:
                with connection.cursor() as cursor:
                    total_rows = len(dados)
                    for start in range(0, total_rows, batch_size):
                        end = min(start + batch_size, total_rows)
                        batch = dados.iloc[start:end].to_records(index=False).tolist()
                        cursor.executemany(sql, batch)
                        connection.commit()
            return "Todos os dados foram inseridos com sucesso!"
        
        except pymysql.err.OperationalError as e:
            return f"Erro de conexão com o banco de dados: {e}"
        except pymysql.err.ProgrammingError as e:
            return f"Erro de SQL: {e}"
        except pymysql.err.IntegrityError as e:
            return f"Erro de integridade (ex: chave duplicada): {e}"
        except pymysql.MySQLError as e:
            return f"Erro MySQL: {e}"
        except Exception as e:
            return f"Erro inesperado: {e}"

