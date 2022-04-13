from typing import Any, Dict, List
from dataclasses import dataclass, field


@dataclass
class Header:
    name: str
    attributes: Dict[str, Any] = field(default_factory=dict)
    children: "List[Child]" = field(default_factory=list)

    def __getitem__(self, name: str):
        return self.attributes[name]
    def __setitem__(self, name: str, value: Any):
        self.attributes[name] = value

    def __getattribute__(self, __name: str) -> Any: # WIP
        pass


@dataclass
class Child:
    parent: Header
    name: str
    attributes: Dict[str, Any] = field(default_factory=dict)

    def __getitem__(self, name: str):
        return self.attributes[name]
    def __setitem__(self, name: str, value: Any):
        self.attributes[name] = value
