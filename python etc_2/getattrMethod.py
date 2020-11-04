#!usr/bin/env/python3


class RTD_Solver:
	def __init__(
		self, *,
		rate: float = None,
		time: float = None,
		distance: float = None) -> None:

		if rate:
			self.rate = rate
		if time:
			self.time = time
		if distance:
			self.distance = distance

	def __getattr__(self, name: str) -> float:
		if name == "rate":
			return self.distance / self.time
		elif name == "time":
			return self.distance / self.rate
		elif name == "distance":
			return self.rate * self.time
		else:
			raise AttributeError(f"Can't compute {name}")


r1 = RTD_Solver(rate=6.25, distance=10.25)
print(r1.rate)


