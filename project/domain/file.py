from dataclasses import dataclass
from uuid import UUID
from datetime import datetime


@dataclass(frozen=True)
class FileId:
    value: UUID

@dataclass(frozen=True)
class Metadata:
    path: str
    created_a: datetime = None
    updated_at: datetime = None

class File:
    def __init__(self, id: FileId, metadata: Metadata, name: str):
        self._id = id
        self._name = name
        self._metadata = metadata

    @property
    def id(self) -> FileId:
        return self._id

    @property
    def extracted_text(self) -> str:
        return self._extracted_text
    
    @property
    def metadata(self) -> Metadata:
        return self._metadata
    
    @property
    def name(self) -> str:
        return self._name
    
    def set_extracted_text(self, text: str):
        self._extracted_text = text