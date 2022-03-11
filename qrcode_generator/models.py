from dataclasses import dataclass
from uuid import UUID


@dataclass
class ImageCode:
    id: UUID
    name: str
    value: str
    image: str
