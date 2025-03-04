from typing import Optional

from sqlmodel import (
    Field,
    SQLModel,
)

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name:str
    secret_name:str
    age: Optional[int] = None


hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
hero_2 = Hero(name="Spider-boy", secret_name="Pedro parqueador")
hero_3 = Hero(name="Rusty Man", secret_name="Tommy sharp", age=48)


print(hero_1)
print(hero_2)
print(hero_3)


