import math

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

	def Draw(self, canvas, cam):
		pt = cam.project(self)
		canvas.create_oval(pt[0], pt[1], pt[0] + 8, pt[1] + 8, fill=green)

	def getMatrix(self):
		return [self.x, self.y, self.z]

	def matrixMultiply(self, matrix):
		pt = [0.0, 0.0, 0.0]

		if (len(matrix[0] != 3)):
			raise IndexError('matrix needs to be 3 dimensional')

		for i in range(3):
			for j in range(3):
				pt[i] += self.getMatrix()[j] * matrix[i][j]

	def rotateX(self, a, axis):
		a *= math.pi / 180
		matrix = [[1.0, 0.0, 0.0], [0.0, math.cos(a), -math.sin(a)], [0.0, math.sin(a), math.cos(a)]]

		self.x -= axis.x
		self.y -= axis.y
		self.z -= axis.z
		rotation = matrixMultiply(matrix)
		self.x = rotation[0] + axis.x
		self.y = rotation[1] + axis.y
		self.z = rotation[2] + axis.z

	def rotateY(self, a, axis):
		a *= math.pi / 180
		matrix = [[math.cos(a), 0.0, math.sin(a)], [0.0, 1.0, 0.0], [-math.sin(a), 0.0, math.cos(a)]]

		self.x -= axis.x
		self.y -= axis.y
		self.z -= axis.z
		rotation = matrixMultiply(matrix)
		self.x = rotation[0] + axis.x
		self.y = rotation[1] + axis.y
		self.z = rotation[2] + axis.z

	def rotateZ(self, a, axis):
		a *= math.pi / 180
		matrix = [[math.cos(a), -math.sin(a), 0.0], [math.sin(a), math.cos(a), 0.0], [0.0, 0.0, 1.0]]

		self.x -= axis.x
		self.y -= axis.y
		self.z -= axis.z
		rotation = matrixMultiply(matrix)
		self.x = rotation[0] + axis.x
		self.y = rotation[1] + axis.y
		self.z = rotation[2] + axis.z
