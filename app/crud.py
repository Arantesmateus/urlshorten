import secrets
from sqlalchemy.orm import Session
from app import models, schemas

def generate_short_code(length: int = 6) -> str:
    "Gera uma string aleatória segura com letras e números."
    #Using url_safe to return an URL without bad characteres
    return secrets.token_urlsafe(length)[:length]

def get_url_by_code(db: Session, short_code: str):
    "Busca a URL curta no banco de dados"
    return db.query(models.URL).filter(models.URL.short_code == short_code).first()

def create_short_url(db: Session, url_schema: schemas.URLCreate) -> models.URL:
    "Gera o código, garante que ele é o único e salvo no banco"
    while True:
        code = generate_short_code()
        db_existing = get_url_by_code(db, short_code=code)
        if not db_existing:
            break
    db_url = models.URL(
        original_url=str(url_schema.original_url),
        short_code=code,
        expires_at=url_schema.expires_at
    )

    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url