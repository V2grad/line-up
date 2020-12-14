from typing import Any
import re

from sqlalchemy.ext.declarative import as_declarative, declared_attr

# https://fastapi.tiangolo.com/tutorial/sql-databases/
# Basically it automatically change class name to table name
# Base = declarative_base()
@as_declarative()
class Base:
    id: Any
    __name__: str
    # Generate __tablename__ automatically
    # Camal case to snake
    @declared_attr
    def __tablename__(cls) -> str:
        return re.sub(r'(?<!^)(?=[A-Z])', '_',  cls.__name__).lower()
