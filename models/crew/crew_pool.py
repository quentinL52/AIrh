from crewai import Crew, Process
import json
from .agents import cv_analyzer_agent, job_offer_analyzer_agent, report_generator_agent, cv_parser_agent, skills_extractor_agent, experience_extractor_agent, project_extractor_agent, education_extractor_agent, ProfileBuilderAgent, informations_personnelle_agent
from .tasks import analyze_cv_task, analyze_job_offer_task, generate_report_task, task_parsing, task_extract_skills, task_extract_experience, task_extract_projects, task_extract_education, task_build_profile, task_extract_informations

def interview_analyser(conversation):
    crew_analyse= Crew(
        agents=[report_generator_agent],
        tasks=[generate_report_task],
        process=Process.sequential,
        verbose=False
    )
    result = crew_analyse.kickoff()
    return result

def analyse_cv(cv_content: str) -> json:
    crew = Crew(
        agents=[            
            informations_personnelle_agent,
            cv_parser_agent,
            skills_extractor_agent,
            experience_extractor_agent,
            project_extractor_agent,
            education_extractor_agent,

            ProfileBuilderAgent
            
        ],
        tasks=[
            task_extract_informations,
            task_parsing,
            task_extract_skills,
            task_extract_experience,
            task_extract_projects,
            task_extract_education,
            task_build_profile
            
        ],
        verbose=True
    )
    result = crew.kickoff(inputs={"cv_content": cv_content})
    return result
