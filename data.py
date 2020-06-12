from enum import Enum
from typing import List, Dict, Any, Union
from enum import Enum


class OpcoesDeStatus(str, Enum):
    a_fazer = 'A Fazer'
    fazendo = 'Fazendo'
    feito = 'Feito'

Item = Dict[str, Union[int, str, OpcoesDeStatus]]

class Todo:
    todo: List[Item] = [
        {"id": 1, "titulo": "Fazer Live", "descricao": "Fazer live no canal do edu", "status": OpcoesDeStatus.a_fazer},
        {"id": 2, "titulo": "Ligar Straming", "status": OpcoesDeStatus.a_fazer},
        {"id": 3, "titulo": "Pentear Cabelo", "status": OpcoesDeStatus.a_fazer},
    ]
    id_atual = 3

    def listar(self):
        self.todo

    def inserir(self, item: Dict[str, Any]) -> Item:
        self.id_atual += 1
        item['id'] = self.id_atual
        self.todo.append(item)
        return item

    def pegar(self, item_id: int) -> Item:
        item = filter(lambda x:x['id'] == id, self.todo)
        return list(item)[0]

    def filtrar(self, status:OpcoesDeStatus) -> List[Item]:
        return list(filter(lambda x: x['status'] == status, self.todo))