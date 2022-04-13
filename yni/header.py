from typing import Any, Dict, List
from dataclasses import dataclass, field


class BaseClass:
    attributes: Dict[str, Any]

    def __getitem__(self, name: str):
        return self.attributes[name]
    def __setitem__(self, name: str, value: Any):
        self.attributes[name] = value

    def __getattribute__(self, __name: str) -> Any:
        if __name in super().__getattribute__("attributes"):
            return super().__getattribute__("attributes")[__name]
        return super().__getattribute__(__name)

    def __setattr__(self, __name: str, __value: Any) -> None: # this one dies
        if __name in super().__getattribute__("attributes"):
            super().__getattribute__("attributes")[__name] = __value
            return
        return super().__setattr__(__name, __value)

@dataclass
class Header(BaseClass):
    name: str
    attributes: Dict[str, Any] = field(default_factory=dict)
    children: "List[Child]" = field(default_factory=list)

@dataclass
class Child(BaseClass):
    parent: Header
    name: str
    attributes: Dict[str, Any] = field(default_factory=dict)