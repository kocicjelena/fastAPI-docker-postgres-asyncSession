import os
import sys
from os import path
#from core.config import CONFIG_ROOT

#from ..app.core.db import Base, async_engine

from . import Base, async_engine

def create_all():
    import inspect
    import importlib

    if True:
        import full.core.models as model_module
        
#        model_module = importlib.import_module('core.orm.models')
        for _name in dir(model_module):
            if not _name.startswith('__'):
                _class = getattr(model_module, _name)
                if inspect.isclass(_class):
                    globals().update({_name: _class})

    Base.metadata.create_all(async_engine)


def alembic_create_all():
    from alembic.config import Config
    from alembic import command
    os.chdir('/app/db')
    alembic_cfg = Config('alembic.ini')
   
    
   
    if command.show(alembic_cfg, "head") is None:
        command.revision(alembic_cfg, autogenerate=True, message='initial')
    command.upgrade(alembic_cfg, "head")
    os.chdir('..')


if __name__ == '__main__':
    create_all()
    # alembic_create_all()
