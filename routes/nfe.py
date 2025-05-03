from fastapi import APIRouter, HTTPException, Depends
from models import NotaFiscal
from utils import hash_senha
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime
import sqlite3

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

@router.post("/emitir_nota")
def emitir_nota(nota: NotaFiscal, token: str = Depends(oauth2_scheme)):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    valor_total = 0
    for codigo in nota.produtos:
        cursor.execute("SELECT valor FROM produtos WHERE codigo = ?", (codigo,))
        result = cursor.fetchone()
        if not result:
            raise HTTPException(status_code=404, detail=f"Produto com código {codigo} não encontrado")
        valor_total += result[0]

    chave = f"NFE{datetime.now().timestamp()}"
    data_emissao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("INSERT INTO notas_fiscais (data_emissao, chave, cliente_cpf_cnpj, valor_total) VALUES (?, ?, ?, ?)",
                   (data_emissao, chave, nota.cliente_cpf_cnpj, valor_total))
    conn.commit()
    conn.close()

    return {"mensagem": "Nota fiscal emitida com sucesso", "chave": chave, "valor_total": valor_total}
