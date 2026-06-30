from fastapi.responses import RedirectResponse
from fastapi import status, HTTPException, FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import engine, get_db
from app import models, schemas, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="URL Shortener")

#1. Endpoint to shorten the URL
@app.post("/shorten", response_model=schemas.URLResponse, status_code=status.HTTP_201_CREATED)
def shorten_url(url_data: schemas.URLCreate, db: Session = Depends(get_db)):
    return crud.create_short_url(db=db, url_schema=url_data)


#2. Endpoint to redirect
@app.get("/{short_code}")
def redirect_to_original(short_code: str, db: Session = Depends(get_db)):
    db_url = crud.get_url_by_code(db=db, short_code=short_code)

    if not db_url:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Link encurtado não encontrado.'
        )

    return RedirectResponse(url=db_url.original_url)
