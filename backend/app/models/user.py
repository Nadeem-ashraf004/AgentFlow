from datetime import datetime
from uuid import UUID , uuid4

from sqlalchemy import  String, DateTime ,func, Boolean

from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base 


class User(Base):

      __tablename__ = "users"

      id : Mapped[UUID] = mapped_column(
            primary_key=True, 
            default=uuid4,
            )
      full_name : Mapped[str] = mapped_column(
            String(100),
            nullable=False,
      )
      email : Mapped[str] = mapped_column(
            String(100),
            nullable=False,
      )
      password_hash : Mapped[str] = mapped_column(
            String(255),
            nullable= False,
      )
      is_active : Mapped[bool] =mapped_column(
            Boolean,
            default=True,
            nullable=False,

      )
      created_at : Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            server_default=func.now(),
            nullable=False
      )
      updated_at : Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            server_default=func.now(),
            onupdate=func.now(),
            nullable=False
      )

        
