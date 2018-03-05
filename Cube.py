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
		for face in self.faces:
			face.Draw(canvas, p)

	def reset(self):
		self.center = CubePoint(0, 0, 0)
		for i in range(1):
			for j in range(1):
				for k in range(1):
					self.pts[i][j][k] = CubePoint(i*self.length - self.length/2, j*self.length - self.length/2, k*self.length - self.length/2)

	def updateCenter(self):
		xSum = 0
		ySum = 0
		xSum = 0

		for i in [0, 1]:
			for j in [0, 1]:
				for k in [0, 1]:
					xSum += self.pts[i][j][k].x
					ySum += self.pts[i][j][k].y
					zSum += self.pts[i][j][k].z

		self.center = CubePoint(xSum/8, ySum/8, zSum/8)

	def updateLines(self):
		self.edges = []

		for i in [0, 1]:
			for j in [0, 1]:
				for k in [0, 1]:
					if (i + 1 < 2):
						self.edges.append(Line(self.pts[i][j][k], self.pts[i+1][j][k]))
					if (j + 1 < 2):
						self.edges.append(Line(self.pts[i][j][k], self.pts[i][j+1][k]))
					if (k + 1 < 2):
						self.edges.append(Line(self.pts[i][j][k], self.pts[i][j][k+1]))

	def updateFaces(self):
		updateLines(self)
		self.faces = []

		for i in [0, 1]:
			for j in [0, 1]:
				for k in [0, 1]:
					if (i+1 < 2 and j+1 < 2):
						self.faces.append(Face.makeFace([ self.pts[i][j][k], self.pts[i+1][j][k], self.pts[i+1][j+1][k], self.pts[i][j+1][k] ]))

					if (j+1 < 2 and k+1 < 2):
						self.faces.append(Face.makeFace([ self.pts[i][j][k], self.pts[i][j+1][k], self.pts[i][j+1][k+1], self.pts[i][j][k+1] ]))

					if (i+1 < 2 and k+1 < 2):
						self.faces.append(Face.makeFace([ self.pts[i][j][k], self.pts[i+1][j][k], self.pts[i+1][j][k+1], self.pts[i][j][k+1] ]))

	def getIntersection(self, zPlane):
		intersection = []
		for face in self.faces:
			line = face.getIntersection(zPlane)
			if line is not None:
				intersection.add(line)

		return Intersection2D(intersection)

	def updateIntersections(self, zPlane):
		self.intersections = []
		for face in self.faces:
			intersection = face.getIntersection(zPlane)
			if intersection is not None:
				self.intersections.append(intersection)

	def DrawIntersections(self, canvas, cam):
		if len(self.intersections) is not 0:
			print(intersections)
			for intersection in self.intersections:
				intersection.Draw(canvas, cam)

	def translate(self, x, y, z):
		for i in [0, 1]:
			for j in [0, 1]:
				for k in [0, 1]:
					self.pts[i][j][k].translate(x, y, z)
		updateCenter()

	def setZ(self, z):
		for i in [0, 1]:
			for j in [0, 1]:
				for k in [0, 1]:
					self.pts[i][j][k] = CubePoint(self.pts[i][j][k].x, self.pts[i][j][k].y, (self.pts[i][j][k].z - center.z) + z)
		updateCenter()

	def rotateX(self, a):
		for i in [0, 1]:
			for j in [0, 1]:
				for k in [0, 1]:
					self.pts[i][j][k].rotateX(a, self.center)

	def rotateY(self, a):
		for i in [0, 1]:
			for j in [0, 1]:
				for k in [0, 1]:
					self.pts[i][j][k].rotateY(a, self.center)

	def rotateZ(self, a):
		for i in [0, 1]:
			for j in [0, 1]:
				for k in [0, 1]:
					self.pts[i][j][k].rotateZ(a, self.center)

