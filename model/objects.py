from dataclasses import dataclass


@dataclass
class Object:
    object_id: int
    classification: str
    continent: str
    country: str
    curator_approved: int
    dated: str
    department: str
    medium: str
    nationality: str
    object_name: str
    restricted: int
    rights_type: str
    role: str
    room: str
    style: str
    title: str

    def __hash__(self):
        return hash(self.object_id)