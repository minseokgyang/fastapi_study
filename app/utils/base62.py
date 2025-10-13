import string
from typing import Final

class Base62:
    BASE: Final[str] = string.digits + string.ascii_letters
    BASE_LEN: Final[int] = len(BASE)

    @classmethod
    def encode(cls, num:int) -> str:
        if num < 0:
            raise ValueError(f"{cls}.encode()need positive integer but you passed: {num}")

        if num == 0:
            return cls.BASE[0]

        result = []
        while num:
            num, remainder = divmod(num, cls.BASE_LEN)
            result.append(cls.BASE[remainder])
        return "".join(result)
