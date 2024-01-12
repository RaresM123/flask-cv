import json

import click
from flask import Blueprint

from cv_parser.json_parser import JsonParser
from flaskr import serializer
from flaskr.exceptions import commands_exception
from flaskr.utils import CV_JSON_PATH_1, CV_PDF_PATH_1

cli_bp = Blueprint('cv', __name__)


@cli_bp.cli.command("all")
@commands_exception
def cv_info():
	"""
	Command for printing in console the entire cv
	:return:
	"""
	json_parser = JsonParser(cv_path=CV_JSON_PATH_1)
	json_parser.parse()
	cv = serializer.CVResponse(**json_parser.__dict__).model_dump_json(indent=4)
	click.echo(cv)


@cli_bp.cli.command("personal")
@commands_exception
def personal_info():
	"""
	Command for printing in console the personal information
	:return:
	"""
	json_parser = JsonParser(cv_path=CV_JSON_PATH_1)
	json_parser.parse()
	cv = serializer.PersonalInfoResponse(**json_parser.personal_info).model_dump_json(indent=4)
	click.echo(cv)


@cli_bp.cli.command("education")
@commands_exception
def education_info():
	"""
	Command for printing in console the education information
	:return:
	"""
	json_parser = JsonParser(cv_path=CV_JSON_PATH_1)
	json_parser.parse()
	cv = json.dumps([serializer.EducationResponse(**e).model_dump() for e in json_parser.education], indent=4)
	click.echo(cv)


@cli_bp.cli.command("experience")
@commands_exception
def experience_info():
	"""
	Command for printing in console the experience information
	:return:
	"""
	json_parser = JsonParser(cv_path=CV_JSON_PATH_1)
	json_parser.parse()
	cv = json.dumps([serializer.ExperienceResponse(**e).model_dump() for e in json_parser.experience], indent=4)
	click.echo(cv)


@cli_bp.cli.command("languages")
@commands_exception
def languages_info():
	"""
	Command for printing in console the languages information
	:return:
	"""
	json_parser = JsonParser(cv_path=CV_JSON_PATH_1)
	json_parser.parse()
	cv = json.dumps([serializer.LanguageResponse(**l).model_dump() for l in json_parser.languages], indent=4)
	click.echo(cv)


@cli_bp.cli.command("skills")
@commands_exception
def skills_info():
	"""
	Command for printing in console the skills information
	:return:
	"""
	json_parser = JsonParser(cv_path=CV_JSON_PATH_1)
	json_parser.parse()
	cv = json.dumps([serializer.SkillResponse(**s).model_dump() for s in json_parser.skills], indent=4)
	click.echo(cv)

