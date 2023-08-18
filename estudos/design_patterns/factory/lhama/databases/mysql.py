from typing import Dict
from interface import DatabaseInterface

class MysqlRepository(DatabaseInterface):
    
    def select_one(self) -> Dict:
        return {
            'sucesso': True,
            'data': 'olá mundo'
        }