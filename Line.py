class Line:

	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2

	def Draw(self, canvas, cam):
		pt1 = cam.project(self.p1)
		pt2 = cam.project(self.p2)
		self.p1.Draw(canvas, cam)
		self.p2.Draw(canvas, cam)
		canvas.create_line(pt1[0], pt1[1], pt2[0], pt2[1])

	def midpoint(self):
		x = (self.p1.x + self.p2.x) / 2
		y = (self.p1.y + self.p2.y) / 2
		z = (self.p1.z + self.p2.z) / 2

		return CubePoint(x, y, z)

	def makeIntersection(self, zPlane):
		zPercent = (zPlane - self.p1.z) / (self.p2.z - self.p1.z)
		x = zPercent * (self.p2.x - self.p1.x) + self.p1.x
		y = zPercent * (self.p2.y - self.p1.y) + self.p1.y

		if (zPlane > self.p1.z and zPlane < self.p2.z) or (zPlane < self.p1.z and zPlane > self.p2.z):
			return CubePoint(x, z, zPlane)
		else:
			return None