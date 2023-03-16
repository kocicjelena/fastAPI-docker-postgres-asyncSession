# 
# from ..core import alembic

# alembic.alembic_create_all()


from fastapi import FastAPI



from core.orm import alembic

app = FastAPI()
#helper.create_all()
alembic.alembic_create_all()
