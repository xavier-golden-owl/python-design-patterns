class RoundPeg:
	def __init__(self, radius):
		self.__radius = radius

	def getRadius(self):
		return self.__radius


class RoundHole:
	def __init__(self, radius):
		self.__radius = radius

	def getRadius(self):
		return self.__radius

	def fit(self, peg: RoundPeg):
		return self.getRadius() >= peg.getRadius()


class SquarePeg:
	def __init__(self, width):
		self.__width = width

	def getWidth(self):
		return self.__width

class SquarePegAdapter(RoundPeg):
	def __init__(self, squarePeg):
		self.__squarePeg = squarePeg

	def getRadius(self):
		return self.__squarePeg.getWidth() * (2 ** 0.5) / 2


if __name__ == '__main__':
	roundHold	= RoundHole(2)

	print(roundHold.fit(RoundPeg(2)))

	print(roundHold.fit(SquarePegAdapter(SquarePeg(2))))

	print(roundHold.fit(SquarePegAdapter(SquarePeg(4))))
