from app.database import SessionLocal, engine
from app import models, schemas, crud

db = SessionLocal()
url_data = schemas.URLCreate(original_url="https://www.google.com")
try:
    crud.create_short_url(db, url_schema=url_data)
    print("Success")
except Exception as e:
    import traceback
    traceback.print_exc()
