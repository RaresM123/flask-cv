class BaseParser:

	personal_info: dict
	# list of dictionaries under form: {"position": "", "years_of_experience": int, "description": str }
	experience: list[dict]
	education: list[dict]
	languages: list[dict]
	skills: list[dict]

	def get_content(self):
		pass

	def get_personal_info(self):
		pass

	def get_experience(self):
		pass

	def get_education(self):
		pass

	def get_languages(self):
		pass

	def get_skills(self):
		pass

	def parse(self):
		self.get_content()
		self.get_skills()
		self.get_languages()
		self.get_education()
		self.get_experience()
		self.get_personal_info()



