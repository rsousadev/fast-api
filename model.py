from typing import Optional
from data import OpcoesDeStatus
from pydantic import BaseModel


class ModeloDoItem(BaseModel):
    id: int
    titulo: str
    status: Optional[OpcoesDeStatus]


class ModeloDoItemResposta(ModeloDoItem):
    id: int