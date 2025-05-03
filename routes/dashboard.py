from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from models import NotaFiscalResposta
from typing import List
import sqlite3

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

@router.get("/dashboard", response_model=List[NotaFiscalResposta])
def consultar_notas(token: str = Depends(oauth2_scheme)):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT data_emissao, chave, cliente_cpf_cnpj, valor_total FROM notas_fiscais")
    rows = cursor.fetchall()
    conn.close()
    return [
        NotaFiscalResposta(
            data=row[0],
            chave=row[1],
            cliente_cpf_cnpj=row[2],
            valor_total=row[3]
        ) for row in rows
    ]
