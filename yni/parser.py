import re
from typing import Dict, Any

from .header import Header, BaseClass


HEADER_REGEX = re.compile("^#(.*)")
KEY_VALUE_REGEX = re.compile("(.*?):(.*)")


class Yni(BaseClass):
    def __init__(self) -> None:
        self.variables: Dict[str, Header] = {}

    @classmethod
    def from_string(cls, string: str):
        ret = {}
        current_header = ret

        for line in string.splitlines():
            if line == "":
                continue
            if line.startswith("#"):
                match = HEADER_REGEX.search(line)
                name = match.group(1)
                current_header = ret[name] = {}
            elif line in ["[", "]"]:
                pass
            else:
                match = KEY_VALUE_REGEX.search(line)
                key, value = match.group(1), match.group(2)
                key = key.strip("\t")
                value = value.strip(" ")
                if value.startswith("env("):
                    try:
                        import dotenv
                    except ImportError:
                        raise Exception("python-dotenv library is needed for env(..., ...)")
                    value = value[4:-1]
                    filename, keyname = value.split(",")
                    filename = filename.strip(" ")
                    keyname = keyname.strip(" ")
                    value = dotenv.get_key(filename, keyname)
                current_header[key] = value

        yni = cls()
        for header, attributes in ret.items():
            yni.variables[header] = Header(header, attributes)
        return yni

    @classmethod
    def from_file(cls, filename: str):
        with open(filename, "r") as f:
            return cls.from_string(f.read())

    def __repr__(self):
        return repr(self.variables)

    def __getitem__(self, name: str):
        return self.variables[name]

    def __setitem__(self, name: str, value: Any):
        self.variables[name] = value
