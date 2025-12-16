from dotenv import load_dotenv
load_dotenv()  # 🔑 THIS WAS MISSING

from fastapi import FastAPI
from pydantic import BaseModel
from etl.load.db_connection import get_db_connection
from etl.load.loaders import upsert_rows

app = FastAPI()

class TitanicPassenger(BaseModel):
    passenger_ref: int
    name: str
    sex: str
    age: float | None = None
    pclass: int
    fare: float | None = None
    embarked: str | None = None
    survived: bool


@app.post("/register-passenger")
def register_passenger(p: TitanicPassenger):
    row = {
        "passenger_ref": p.passenger_ref,
        "name": p.name,
        "sex": p.sex,
        "age": p.age,
        "fare": p.fare,
        "survived": p.survived
    }

    with get_db_connection() as conn:
        conn.autocommit = True   # 🔑 CRITICAL LINE

        print("DB HOST:", conn.info.host)
        print("DB NAME:", conn.info.dbname)

        upsert_rows(conn, "passengers", [row])



    return {"status": "inserted"}
