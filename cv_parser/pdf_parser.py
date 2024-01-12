from cv_parser.base_parser import BaseParser
from resume_parser import resumeparse
from cv_parser.exceptions.parser_read_exception import PdfReadException


class PdfParser(BaseParser):

	cv_path: str
	cv_content: dict

	def __init__(self, cv_path):
		self.cv_path = cv_path
		self.cv_content = {}

	def get_content(self):
		"""
		This was an attempt to parse a pdf file, it seems that no free variant is good enough to be shown in a demo
		"""
		try:
			self.cv_content = resumeparse.read_file(self.cv_path)

		except Exception as e:
			raise PdfReadException



