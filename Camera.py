class Camera:

	focalLength = 450
	orthoZoom = 3

	def __init__(self):
		self.x = 0.0
		self.y = 0.0
		self.z = -150.0
		self.phi = 0.0
		self.factor = 1.0

	def project(self, pt):
		image = transform(pt)

		projectionConstant = mix(focalLength / image.z, orthoZoom, self.factor)
		return (int(image.x * projectionConstant), int(image.y * projectionConstant))

	def getCubeColor():
		return "blue"

	def getIntersectionColor():
		return "cyan"

	def tranform(self, point):
		image = CubePoint(point.x, point.y, point.z)
		axis = CubePoint(0.0, 0.0, 0.0)

		image.rotateX(self.phi, axis)
		image.translate(-self.x, -self.y, -self.z)
		return image

	def rotate(self, dPhi):
		self.phi += dPhi

	def setRotation(self, phi):
		self.phi = phi

	def translate(self, dx, dy, dz):
		self.x += dx
		self.y += dy
		self.z += dz

	def setPosition(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def setProjectionFactor(self, factor):
		self.factor = factor

	def mix(a, b, factor):
		return (a*factor) + (b * (1 - factor))
