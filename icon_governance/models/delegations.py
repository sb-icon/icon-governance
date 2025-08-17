from typing import Any, List, Optional

from pydantic import condecimal
from sqlalchemy.orm import declared_attr
from sqlmodel import Field, Session, SQLModel, create_engine


class Delegation(SQLModel, table=True):
    address: Optional[str] = Field(..., primary_key=True)
    prep_address: Optional[str] = Field(..., primary_key=True)
    value: condecimal(max_digits=28, decimal_places=0) = Field(nullable=False)
    last_updated_block: Optional[int] = Field(None)
    delegator: Optional[str] = Field(None, index=True)

    @declared_attr
    def __tablename__(cls) -> str:  # noqa: N805
        return "delegations"
