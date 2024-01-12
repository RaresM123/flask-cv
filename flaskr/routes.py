from flask import Blueprint, jsonify
from cv_parser.json_parser import JsonParser
from flaskr.exceptions import http_exception
from flaskr.utils import CV_JSON_PATH_1
from flaskr.cache import cache
import flaskr.serializer as serializer
from flask_pydantic import validate

bp = Blueprint('cv_info', __name__, url_prefix="/cv")


@bp.route("/", methods=['GET'])
@http_exception
@validate()
def get_cv():
	"""
	Route for retrieving all information from the cv
	:return: json format response
	"""
	cached_json_parser = cache.get("cached_json_parser")
	if not cached_json_parser:
		json_parser = JsonParser(cv_path=CV_JSON_PATH_1)
		json_parser.parse()
		cache.set("cached_json_parser", json_parser)
		return jsonify({
			"status_code": 200,
			"result": serializer.CVResponse(**json_parser.__dict__).model_dump()
		})

	return jsonify({
		"status_code": 200,
		"result": serializer.CVResponse(**cached_json_parser.__dict__).model_dump()
	})


@bp.route("/personal", methods=['GET'])
@http_exception
@validate()
def get_personal_info():
	"""
	Route for retrieving personal information from the cv
	:return: json format response
	"""

	cached_json_parser = cache.get("cached_json_parser")
	if not cached_json_parser:
		json_parser = JsonParser(cv_path=CV_JSON_PATH_1)
		json_parser.parse()
		cache.set("cached_json_parser", json_parser)
		return {
			"status_code": 200,
			"result": serializer.PersonalInfoResponse(**json_parser.personal_info).model_dump()
		}
	return {
		"status_code": 200,
		"result": serializer.PersonalInfoResponse(**cached_json_parser.personal_info).model_dump()
	}


@bp.route("/experience", methods=['GET'])
@http_exception
@validate()
def get_experience():
	"""
	Route for retrieving experience information from the cv
	:return: json format response
	"""

	cached_json_parser = cache.get("cached_json_parser")
	if not cached_json_parser:
		json_parser = JsonParser(cv_path=CV_JSON_PATH_1)
		json_parser.parse()
		cache.set("cached_json_parser", json_parser)
		return {
			"status_code": 200,
			"result": [serializer.ExperienceResponse(**e).model_dump() for e in json_parser.experience]
		}

	return {
		"status_code": 200,
		"result": [serializer.ExperienceResponse(**e).model_dump() for e in cached_json_parser.experience]
	}


@bp.route("/education", methods=['GET'])
@http_exception
@validate()
def get_education():
	"""
	Route for retrieving education information from the cv
	:return: json format response
	"""

	cached_json_parser = cache.get("cached_json_parser")
	if not cached_json_parser:
		json_parser = JsonParser(cv_path=CV_JSON_PATH_1)
		json_parser.parse()
		cache.set("cached_json_parser", json_parser)
		return {
			"status_code": 200,
			"result": [serializer.EducationResponse(**e).model_dump() for e in json_parser.education]
		}

	return {
		"status_code": 200,
		"result": [serializer.EducationResponse(**e).model_dump() for e in cached_json_parser.education]
	}


@bp.route("/languages", methods=['GET'])
@http_exception
@validate()
def get_languages():
	"""
	Route for retrieving languages information from the cv
	:return: json format response
	"""

	cached_json_parser = cache.get("cached_json_parser")
	if not cached_json_parser:
		json_parser = JsonParser(cv_path=CV_JSON_PATH_1)
		json_parser.parse()
		cache.set("cached_json_parser", json_parser)
		return {
			"status_code": 200,
			"result": [serializer.LanguageResponse(**l).model_dump() for l in json_parser.languages]
		}

	return {
		"status_code": 200,
		"result": [serializer.LanguageResponse(**l).model_dump() for l in cached_json_parser.languages]
	}


@bp.route("/skills", methods=['GET'])
@http_exception
@validate()
def get_skills():
	"""
	Route for retrieving skills information from the cv
	:return: json format response
	"""

	cached_json_parser = cache.get("cached_json_parser")
	if not cached_json_parser:
		json_parser = JsonParser(cv_path=CV_JSON_PATH_1)
		json_parser.parse()
		cache.set("cached_json_parser", json_parser)
		return {
			"status_code": 200,
			"result": [serializer.SkillResponse(**s).model_dump() for s in json_parser.skills]
		}

	return {
		"status_code": 200,
		"result": [serializer.SkillResponse(**s).model_dump() for s in cached_json_parser.skills]
	}
