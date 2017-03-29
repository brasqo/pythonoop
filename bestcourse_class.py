class BestCourse:
	"""Qazi's website class test"""

	website = "http://cleverprogrammer.com"


	def __init__(self, name):
		"""initializing a name for qazi's courses"""
		self.name = name


python_course = BestCourse("Learn Python")
learn_command_line_course = BestCourse("Learn Command Line")

print(python_course.name)
print(BestCourse.website)

#object name.method
print(learn_command_line_course.name)

#class name.method
print(BestCourse.website)