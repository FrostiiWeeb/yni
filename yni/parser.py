from typing import List, Optional, Dict

from .header import Header


class Yni:
    def __init__(self) -> None:
        self.variables: Dict[str, Header] = {}
