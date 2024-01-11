from cv_parser.base_parser import BaseParser
import json

from cv_parser.exceptions.parser_read_exception import JsonReadException


class JsonParser(BaseParser):

	cv_path: str
	cv_content: dict

	def __init__(self, cv_path):
		self.cv_path = cv_path
		self.cv_content = {}

	def get_content(self):
		try:
			with open(self.cv_path, "r") as f:
				self.cv_content = json.load(f)
		except Exception as e:
			raise JsonReadException

	def get_personal_info(self):
		self.personal_info = self.cv_content.get("personal_info", None)

	def get_education(self):
		self.education = self.cv_content.get("education", None)

	def get_skills(self):
		self.skills = self.cv_content.get("skills", None)

	def get_languages(self):
		self.languages = self.cv_content.get("languages", None)

	def get_experience(self):
		self.experience = self.cv_content.get("experience", None)



















