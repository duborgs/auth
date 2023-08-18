from interface.database_inferface import DatabaseInterface
from typing import Type, Dict, Union

class UseCase():
    def __init__(self, repository: Type[DatabaseInterface]) -> None:
        self._repository = repository
        
    def do_something(self, data: bool) -> Union[Dict, None]:
        if data is True:
            repositoryResponse = self._repository.select_one()
            return repositoryResponse
        
        return None