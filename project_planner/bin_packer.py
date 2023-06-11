from typing import Callable, Generic, TypeVar

T = TypeVar("T")


class Bin(Generic[T]):
    def __init__(
        self, capacity: float, padding: float = 0, sizer: Callable[[T], float] = float
    ):
        self.items: list[T] = []
        self.capacity = capacity
        self.sizer = sizer
        self.padding = padding

    def add(self, item: T):
        self.items.append(item)
        self.capacity -= self.sizer(item)
        self.capacity -= self.padding

    def fits(self, item: T) -> bool:
        return self.sizer(item) <= self.capacity

    def __iter__(self):
        return iter(self.items)


class BinPacker(Generic[T]):
    def __init__(
        self, capacity: float, padding: float = 0, sizer: Callable[[T], float] = float
    ):
        """
        Creates a BinPacker for bins of the given capacity
        containing items of type T.

        sizer is an optional function which, which given an
        item of type T, returns its size. By default, this
        is just float(), as the expectation is that this
        will be used with numerical values most of the time.

        padding allows for additional spacing between items,
        such as to represent the kerf of a saw blade when
        planning cuts to boards.
        """
        self.capacity = capacity
        self.sizer = sizer
        self.padding = padding

    def pack(self, items: list[T]) -> list[Bin[T]]:
        """
        Uses a first-fit decreasing algorithm to approximate a
        solution to the bin packing problem. Given a list of
        items, allocates them into no more than 1.7x the minimum
        number of bins with the given capacity.
        """
        bins: list[Bin[T]] = []
        for item in sorted(items, reverse=True):
            for bin in bins:
                if bin.fits(item):
                    bin.add(item)
                    break
            else:
                bin = Bin[T](self.capacity, sizer=self.sizer, padding=self.padding)
                if bin.fits(item):
                    bin.add(item)
                    bins.append(bin)
                else:
                    raise ValueError("item exceeds maximum bin capacity")
        return bins
