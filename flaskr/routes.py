from flask import Blueprint
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

	cached_json_parser = cache.get("cached_json_parser")
	if not cached_json_parser:
		json_parser = JsonParser(cv_path=CV_JSON_PATH_1)
		json_parser.parse()
		cache.set("cached_json_parser", json_parser)
		return serializer.CVResponse(**json_parser.__dict__)

	return serializer.CVResponse(**cached_json_parser.__dict__)


@bp.route("/personal", methods=['GET'])
@http_exception
@validate()
def get_personal_info():

	cached_json_parser = cache.get("cached_json_parser")
	if not cached_json_parser:
		json_parser = JsonParser(cv_path=CV_JSON_PATH_1)
		json_parser.parse()
		cache.set("cached_json_parser", json_parser)
		return {
			"status_code": 200,
			"result": serializer.PersonalInfoResponse(**json_parser.personal_info)
		}
	return {
		"status_code": 200,
		"result": serializer.PersonalInfoResponse(**cached_json_parser.personal_info)
	}


@bp.route("/experience", methods=['GET'])
@http_exception
@validate()
def get_experience(cv_path: str = CV_JSON_PATH_1):

	cached_json_parser = cache.get("cached_json_parser")
	if not cached_json_parser:
		json_parser = JsonParser(cv_path=cv_path)
		json_parser.parse()
		cache.set("cached_json_parser", json_parser)
		return {
			"status_code": 200,
			"result": [serializer.ExperienceResponse(**e) for e in json_parser.experience]
		}

	return {
		"status_code": 200,
		"result": [serializer.ExperienceResponse(**e) for e in cached_json_parser.experience]
	}


@bp.route("/education", methods=['GET'])
@http_exception
@validate()
def get_education(cv_path: str = CV_JSON_PATH_1):

	cached_json_parser = cache.get("cached_json_parser")
	if not cached_json_parser:
		json_parser = JsonParser(cv_path=cv_path)
		json_parser.parse()
		cache.set("cached_json_parser", json_parser)
		return {
			"status_code": 200,
			"result": [serializer.EducationResponse(**e) for e in json_parser.education]
		}

	return {
		"status_code": 200,
		"result": [serializer.EducationResponse(**e) for e in cached_json_parser.education]
	}


@bp.route("/languages", methods=['GET'])
@http_exception
@validate()
def get_languages(cv_path: str = CV_JSON_PATH_1):

	cached_json_parser = cache.get("cached_json_parser")
	if not cached_json_parser:
		json_parser = JsonParser(cv_path=cv_path)
		json_parser.parse()
		cache.set("cached_json_parser", json_parser)
		return {
			"status_code": 200,
			"result": [serializer.LanguageResponse(**l) for l in json_parser.languages]
		}

	return {
		"status_code": 200,
		"result": [serializer.LanguageResponse(**l) for l in cached_json_parser.languages]
	}


@bp.route("/skills", methods=['GET'])
@http_exception
@validate()
def get_skills(cv_path: str = CV_JSON_PATH_1):

	cached_json_parser = cache.get("cached_json_parser")
	if not cached_json_parser:
		json_parser = JsonParser(cv_path=cv_path)
		json_parser.parse()
		cache.set("cached_json_parser", json_parser)
		return {
			"status_code": 200,
			"result": [serializer.SkillResponse(**s) for s in json_parser.skills]
		}

	return {
		"status_code": 200,
		"result": [serializer.SkillResponse(**s) for s in cached_json_parser.skills]
	}





