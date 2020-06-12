from typing import List, Optional

from fastapi import APIRouter

from data import Todo, OpcoesDeStatus
from model import ModeloDoItem, ModeloDoItemResposta

router = APIRouter()

todo = Todo()


@router.get("/")
async def hello_world():
    """
    View raiz, retorna {'ola': 'mundo'}
    """
    return {"hello": "world"}


@router.get("/", response_model=List[ModeloDoItemResposta])
async def todo_list(status: Optional[OpcoesDeStatus] = None):
    """
    View que retorna lista de itens
    """
    if status is not None:
        return todo.filtrar(status=status)
    return todo.todo


@router.get("/{id_do_item}", response_model=List[ModeloDoItemResposta])
async def get_item_todo(id_do_item: int):
    """
    View que mostra um item a fazer pelo id
    """
    return todo.pegar(id_do_item)


@router.post("/", response_model=List[ModeloDoItem], status_code=201)
async def todo_add(todo_insert: ModeloDoItem):
    """
    View que insere item na lista todo
    """
    return todo.inserir(todo_insert.dict())
