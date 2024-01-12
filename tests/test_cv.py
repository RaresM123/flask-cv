import pytest
from cv_parser.json_parser import JsonParser, JsonReadException
from flaskr.utils import CV_JSON_PATH_1, CV_PDF_PATH_1

TEST_DATA = {
	"personal_info": {
		"first_name": "Rares",
		"last_name": "Munteanu",
		"email": "raresmunteanu29@yahoo.com",
		"mobile": "+40763277778",
		"linkedin": "",
		"description": "Passionate software developer with almost 6 years of experience in Python"
	},
	"experience": [
		{
			"position": "senior software engineer",
			"start_year": 2022,
			"end_year": None,
			"company": "Lionstep",
			"description": "Process of rearchitecture from monolith to microservices"
		},
		{
			"position": "senior software engineer",
			"start_year": 2018,
			"end_year": 2022,
			"company": "Bitdefender",
			"description": "Implicated into process of vulnerability assessment"
		}
	],
	"education": [
		{
			"university": "Alexandru Ioan Cuza",
			"degree": "master",
			"start_date": "2020",
			"end_date": "2022",
			"grade": 9.50
		},
		{
			"university": "Alexandru Ioan Cuza",
			"degree": "licence",
			"start_date": "2017",
			"end_date": "2020",
			"grade": 9.25
		}
	],
	"languages": [
		{
			"language": "english",
			"level": "advanced"
		},
		{
			"language": "deutsch",
			"level": "beginner"
		}
	],
	"skills": [
		{
			"skill": "Python",
			"level": "expert"
		},
		{
			"skill": "Git",
			"level": "expert"
		},
		{
			"skill": "Flask",
			"level": "advanced"
		},
		{
			"skill": "SQL",
			"level": "advanced"
		},
		{
			"skill": "NoSQL",
			"level": "advanced"
		},
		{
			"skill": "microservices",
			"level": "advanced"
		}
	]
}


def test_all_cv():

	json_parser = JsonParser(cv_path=CV_JSON_PATH_1)
	json_parser.parse()
	assert type(json_parser.personal_info) == dict
	assert json_parser.personal_info == TEST_DATA.get("personal_info")


def test_all_cv_error():
	with pytest.raises(JsonReadException):
		json_parser = JsonParser(CV_PDF_PATH_1)
		json_parser.parse()

