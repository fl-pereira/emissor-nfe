from pydantic import BaseModel, EmailStr
from typing import List

class Usuario(BaseModel):
    cnpj: str
    email: EmailStr
    senha: str

class Cliente(BaseModel):
    nome: str
    cpf_cnpj: str
    endereco: str

class Produto(BaseModel):
    nome: str
    codigo: str
    valor: float

class NotaFiscal(BaseModel):
    cliente_cpf_cnpj: str
    produtos: List[str]

class NotaFiscalResposta(BaseModel):
    data: str
    chave: str
    cliente_cpf_cnpj: str
    valor_total: float
