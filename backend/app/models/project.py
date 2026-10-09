import uuid
from datetime import datetime
from sqlalchemy import DateTime, ForeignKey , String , Text , func
from sqlalchemy import Mapped , mapped_column , relationship

from app.db.base import Base

class ResearchProject(Base):
    __tablename__="Research Project"

    id : Mapped [uuid.UUID] = mapped_column(
        primary_key = True,
        defualt = uuid.uuid4,
    )

    user_id : Mapped [uuid.UUID] = mapped_column(
        ForeignKey("user_id",ondelete="CASCADE"),
        nullable = False,
        index= True,
    )
    name : Mapped [str] = mapped_column(
        String(150),
        nullable = False,
    )
    description : Mapped [str] = mapped_column(
        Text,
        nullable = True,
    )
    status : Mapped [str] = mapped_column(
        String(30),
        defualt = "active",
        nullable = False
    )

    created_at : Mapped [datetime] = mapped_column(
        DateTime(timezone=True),
        server_defualt=func.now(),
        nullable = False,
    )

    update_at : Mapped [datetime] = mapped_column(
        DateTime(timezone=True),
        server_defualt = func.now(),
        nullable = False,
    )

    user : Mapped ["User"] = relationship(
        back_populates ="research_project",
    )

