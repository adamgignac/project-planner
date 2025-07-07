import pathlib

import yaml
from pydantic import BaseModel


class Cut(BaseModel):
    """
    A Cut reprsents a piece that must be cut for the project.

    Count is optional (defaults to 1) but will allow for a more
    simple expression of repeated cuts (i.e. if your project
    requires numerous cuts of the same length, they can be
    combined into a single entry in the project manifest).
    """

    length: float
    count: int = 1


class ProjectComponent(BaseModel):
    """
    A ProjectComponent represents a particular material or type
    of board that needs to be cut into multiple pieces.

    Length should be the length of the board (e.g. for a board
    that comes in 8 foot lengths, where cuts will be measured
    in inches, the length is 96).

    Kerf is the width of the saw blade, to allow for cuts to be
    properly spaced - if 0.25 inches are lost to the kerf, then
    an 8-foot board can only yield 7 cuts that are exactly 12".
    """

    name: str
    length: float
    cuts: list[Cut]
    kerf: float = 0
    price: float = 0

    @property
    def segments(self):
        return sorted([i.length for i in self.cuts for j in range(i.count)])


class Project(BaseModel):
    """
    A Project contains a list of components.
    """

    name: str
    components: list[ProjectComponent]


def parse(p: pathlib.Path) -> Project:
    with open(p) as f:
        data = yaml.safe_load(f)
    return Project(**data)
