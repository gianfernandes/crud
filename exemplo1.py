from sqlmodel import Session, SQLModel, create_engine 
from sqlalchemy import text

engine = create_engine("sqlite:///database.db")

with Session(engine) as session:
  statement = text("SELECT * FROM hero;")
  result = session.exec(statement)
  heroes =result.fetchall()
  for hero in heroes:
    print(hero)