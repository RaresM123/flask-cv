from typing import Optional, List

from pydantic import BaseModel


class PersonalInfoResponse(BaseModel):
	first_name: str
	last_name: str
	email: str
	mobile: str
	linkedin: Optional[str] = None
	description: Optional[str] = None


class ExperienceResponse(BaseModel):
	position: str
	start_year: Optional[int] = None
	end_year: Optional[int] = None
	company: str
	description: Optional[str] = None


class EducationResponse(BaseModel):
	university: str
	degree: str
	start_date: Optional[int] = None
	end_date: Optional[int] = None
	grade: Optional[float] = None


class LanguageResponse(BaseModel):
	language: str
	level: str


class SkillResponse(BaseModel):
	skill: str
	level: str


class CVResponse(BaseModel):
	personal_info: PersonalInfoResponse
	experience: List[ExperienceResponse]
	education: List[EducationResponse]
	languages: List[LanguageResponse]
	skills: List[SkillResponse]
