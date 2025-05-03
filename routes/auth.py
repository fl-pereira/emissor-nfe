from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
import sqlite3
from models import Usuario
from utils import hash_senha

router = APIRouter()

@router.post("/cadastro")
def cadastrar_usuario(usuario: Usuario):
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        senha_hash = hash_senha(usuario.senha)
        cursor.execute("INSERT INTO usuarios (cnpj, email, senha) VALUES (?, ?, ?)",
                       (usuario.cnpj, usuario.email, senha_hash))
        conn.commit()
        conn.close()
        return {"mensagem": "Usuário cadastrado com sucesso."}
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="E-mail já cadastrado.")

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    senha_hash = hash_senha(form_data.password)
    cursor.execute("SELECT * FROM usuarios WHERE email = ? AND senha = ?",
                   (form_data.username, senha_hash))
    usuario = cursor.fetchone()
    conn.close()
    if usuario:
        return {"access_token": form_data.username, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=400, detail="Credenciais inválidas")
