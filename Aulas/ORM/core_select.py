from sqlalchemy import select
from core import user_table, engine

selecione = select([user_table])

# for x in selecione.execute():


print(x for x in selecione.execute)