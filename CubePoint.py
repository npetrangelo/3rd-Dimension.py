class CubePoint:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def makePoint(coords):
		return CubePoint(coords[0], coords[1], coords[2])

	def translate(self, dx, dy, dz):
		self.x += dx
		self.y += dy
		self.z += dz

	def getMatrix(self):
		return [self.x, self.y, self.z]
