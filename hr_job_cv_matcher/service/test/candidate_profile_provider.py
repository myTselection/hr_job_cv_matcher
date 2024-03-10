
from service.test.job_description_cv_provider import CV
from langchain.schema import Document
from model import CandidateProfile, EducationCareerJson, MatchSkillsProfileJson


def create_candidate_profile() -> CandidateProfile:
    source = "dummy.odf"
    return CandidateProfile(
        source=source,
        document=Document(page_content=CV, metadata={"source": source}),
        matched_skills_profile=MatchSkillsProfileJson(
            matching_skills=["Wordpress", "PHP", "HTML"],
            missing_skills=["Javascript", "Phigma"],
            social_skills=["Managing teams"]
        ),
        education_career_profile=EducationCareerJson(
            relevant_job_list=["Front End Developer", "Wordpress Administrator"],
            relevant_degree_list=["B. Tech"],
            years_of_experience=3
        )
    )


if __name__ == "__main__":
    from log_init import logger
    logger.info("Candidate profile: %s", create_candidate_profile())