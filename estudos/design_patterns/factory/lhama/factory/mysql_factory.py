from usecase import UseCase
from databases import MysqlRepository


class MySqlFactory:
    
    @staticmethod
    def create() -> UseCase:
        return UseCase(MysqlRepository())