# This pattern can be used for converting API response into a useful format.
# Could also be used for configuration object.

from typing import List, Dict, Optional

from pydantic import BaseModel


class Params1(BaseModel):
    param1: List[int]
    param2: Optional[List[str]]
    param3: bool = False
    param4: int = 701

    @staticmethod
    def from_dict(data):
        params = Params1(**data)
        return params


if __name__ == "__main__":
    data = {"param1": ["1", 2]}
    params = Params1.from_dict(data)
    print(params)  # param1=[1, 2] param2=None param3=False param4=701
