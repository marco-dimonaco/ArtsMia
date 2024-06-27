from dataclasses import dataclass
from model.objects import Object


@dataclass
class Connessione:
    obj1: Object
    obj2: Object
