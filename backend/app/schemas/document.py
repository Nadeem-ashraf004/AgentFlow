from datetime  import datetime
from pydantic import BaseModel, ConfigDict

class DicumentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id : str
    file_name : str
    file_type : str
    status : str
    created_at : datetime

class DocumentUploadReque(BaseModel):
    document_id : str
    file_name : str
    status : str
    
   

