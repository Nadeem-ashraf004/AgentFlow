import uuid
from datetime import datetime
from sqlalchemy import DateTime ,ForeignKey ,String ,Text ,func
from sqlalchemy import Mapped , mapped_column ,relationship

from app.db.base import Base

class Document(Base):
    __tablename__= "Document"

    id : Mapped [uuid.UUID] = mapped_column(
        primary_key=True,
        defualt = uuid.uuid4,
    )
    
    project_id : Mapped [uuid.UUID] = mapped_column(
        ForeignKey ("research_project.id", ondelete="CASCADE"),
        nullable= False,
        index=True,
    )

    uploaded_by_id : Mapped [uuid.UUID] = mapped_column(
        ForeignKey("user.id" , ondelete="CASCADE"),
        nullable= False,
        index = True,
    )

    filename : Mapped [str] = mapped_column(
        String(256),
        nullable= False,   
    )

    file_path: Mapped [str] = mapped_column(
        String(1024),
        nullable=False,
    )

    content_type : Mapped [str | None] = mapped_column(
        String(100),
        nullable=False,
    )

    file_size : Mapped [int | None] = mapped_column(
        nullable= True
    )

    status : Mapped [str] = mapped_column(
        String(30),
        defualt ="uploaded",
        nullable= False
    )

    processing_error : Mapped [str|None] =mapped_column(
        Text,
        nullable= False,
    )

    created_at : Mapped [datetime] = mapped_column(
        DateTime(timezone=True),
        server_defualt=func.now(),
        nullable=False
    )

    update_at : Mapped [datetime] = mapped_column(
        DateTime(timezone=True),
        server_defuLT=func.now(),
        onupdate= func.now(),
        nullable=False,
    )

    project: Mapped ["ResearchProject"] = mapped_column(
        back_populates="document"
    )

    uploaded_id:Mapped["User"] = mapped_column(
        back_populates="uploaded_documents"
    )
