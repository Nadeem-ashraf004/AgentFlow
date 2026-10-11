import uuid
from datetime import datetime
from sqlalchemy import DateTime , ForeignKey , Integer , String ,Text , func
from sqlalchemy.orm import Mapped , mapped_column , relationship

from app.db.base import Base

class ResearchQuery(Base):
    __tablename__ = "research_queries"

    id : Mapped [uuid.UUID] = mapped_column(
        primary_key=True,
        default= uuid.uuid4,
    )
    project_id : Mapped[uuid.UUID] = mapped_column(
        ForeignKey("research_project.id",ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    created_by_id : Mapped [uuid.UUID] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE"),
        nullable= False,
        index= True,
    )
    query_text : Mapped [str] = mapped_column(
        Text,
        nullable=False,
    )
    status : Mapped [str] = mapped_column(
        String(30),
        default="pending",
        nullable=False,
    )
    created_at : Mapped [datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
        )
    project : Mapped ["ResearchProject"] = mapped_column(
        back_populates = "research_quries",
    )
    runs : Mapped [list["ResearchRun"]] = relationship(
        back_populates="quries",
        cascade= "all , delete-orhan",
    )

    class ResearchRun(Base):
        __tablename__ = "research_run"

        id : Mapped [uuid.UUID] = mapped_column(
            primary_key= True,
            default=uuid.uuid4,
        )
        qurie_id : Mapped [uuid.UUID] = mapped_column(
            ForeignKey("research_queries.id")
        )
    
    