class PermutationGenerator(object):
	def __init__(self, length, radix):
		self.length = length
		self.radix = radix
		self.permutation = []
		while len(self.permutation) < length:
			self.permutation.append(0)
	def next(self):
		i = self.length - 1
		self.permutation[len(self.permutation) - 1] += 1
		while i >= 0:
			if self.permutation[i] == self.radix:
				self.permutation[i] = 0
				if i == 0:
					return None
				else:
					self.permutation[i - 1] += 1
			i -= 1
		return self.permutation
