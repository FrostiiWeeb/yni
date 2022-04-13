from typing import Any, Dict, List, Optional, Tuple, Generic, TypeVar

from dataclasses import dataclass, field


@dataclass
class Header:
    name: str
    attributes: Dict[Any, Any] = field(default_factory=dict)
    children = field(default_factory=list)


@dataclass
class Child:
    parent: Header
    name: str
    attributes: Dict[Any, Any] = field(default_factory=dict)
