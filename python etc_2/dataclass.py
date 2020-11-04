#!usr/bin/env/python3

from dataclasses import dataclass
from typing import Optional

@dataclass
class RateTimeDistance:
	rate: Optional[float] = None
	time: Optional[float] = None
	distance: Optional[float] = None

	def __post_init__(self) -> None:
		if self.rate is not None and self.time is not None:
			self.distance = self.rate * self.time
		elif self.rate is not None and self.distance is not None:
			self.time = self.distance / self.rate
		elif self.time is not None and self.distance is not None:
			self.rate = self.distance / self.time




r1 = RateTimeDistance(time=1, rate=2)
# r1.rate = 4 # to avoid this use @dataclass(frozen=True)
print(r1.distance)