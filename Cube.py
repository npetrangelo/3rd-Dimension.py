class Cube:

	def __init__(self, length):
		self.length = length
		self.center = CubePoint(0, 0, 0)
		self.pts = []
		self.edges = []
		self.faces = []
		self.intersections = []
		self.reset()
		self.updateCenter()
		self.updateLines()

	def Draw(self, canvas, cam):
		for face in faces:
			face.Draw(canvas, p)

	def reset(self):
		self.center = CubePoint(0, 0, 0)
		for i in range(1):
			for j in range(1):
				for k in range(1):
					pts[i][j][k] = CubePoint(i*self.length - self.length/2, j*self.length - self.length/2, k*self.length - self.length/2)

