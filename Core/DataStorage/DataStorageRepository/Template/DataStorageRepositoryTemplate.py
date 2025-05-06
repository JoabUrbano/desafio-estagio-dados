import pymysql
import pandas as pd

from dotenv import load_dotenv
import os
load_dotenv()

class DataStorageRepositoryTemplate:
    """
    Template geral do repository que será sobrescrito
    """
    def __init__(self):
        """
        Construtor que carrega as variaveis de ambiente com as informações do banco
        """
        self.host = os.getenv("DB_HOST")
        self.port = int(os.getenv("DB_PORT", 3306))
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB_DATABASE")

    def insertData(self, dados: pd.DataFrame) -> str:
        """
        Método a ser sobrescrito com os parametros do dataframe para inserir no banco
        e a montagem do comando SQL INSERT.

        Args:
            data (pd.DataFrame): DataFrame tratado enviado pela camada de serviço.

        Returns:
            str: Mensagem de sucesso ou erro.
        """
        sql = ""
        return self.persistData(dados, sql)
    
    def persistData(self, dados, sql) -> str:
        """
        Chama o comando SQL INSERT montado no passo anterior para inserir os dados
        no banco, mas por se tratar de uma grande quantidade de dados, essa inserção
        é feita em blocos de 3000 dados por vez para não sobrecarregar o banco.

        Args:
            data (pd.DataFrame): DataFrame tratado enviado pela camada de serviço.
            sql (str): Comando INSERT sql para inserir os dados no banco.

        Returns:
            str: Mensagem de sucesso ou erro.

        Errors:
            AttributeError: Se o objeto `dados` não for um DataFrame válido.
            ValueError: Se houver problemas na conversão dos dados para tuplas.
            pymysql.err.OperationalError: Se houver erro na conexão com o banco de dados.
            pymysql.err.ProgrammingError: Se o comando SQL estiver incorreto.
            pymysql.err.IntegrityError: Se houver violação de integridade no banco.
            pymysql.MySQLError: Para quaisquer outros erros relacionados ao MySQL.
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

