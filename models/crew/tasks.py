from crewai import Task
from .agents import report_generator_agent, cv_parser_agent, skills_extractor_agent, experience_extractor_agent, project_extractor_agent, education_extractor_agent, ProfileBuilderAgent, informations_personnelle_agent
'''
analyze_cv_task = Task(
    description=(
        "Analyser le contenu du CV suivant : \n\n"
        "Identifier les compétences techniques, les soft skills, les expériences professionnelles marquantes, "
        "la formation et tout autre élément pertinent pour une évaluation de candidature."
    ),
    expected_output=(
        "Un résumé structuré des points clés du CV, incluant sections distinctes pour compétences, "
        "expériences (avec dates et responsabilités principales), formation, soft skills."
    ),
    agent=cv_analyzer_agent
)

analyze_job_offer_task = Task(
    description=(
        "Analyser le contenu de l'offre d'emploi suivante : \n\n"
        "{job_offer}\n\n"
        "Identifier le titre du poste, les responsabilités principales, les compétences requises (techniques et comportementales), "
        "l'expérience exigée, et les informations sur l'entreprise si disponibles."
    ),
    expected_output=(
        "Un résumé structuré des exigences et caractéristiques du poste, incluant responsabilités, "
        "compétences must-have et nice-to-have, et niveau d'expérience attendu."
    ),
    agent=job_offer_analyzer_agent)'''


generate_report_task = Task(
    description=(
        "En utilisant l'analyse de la conversation, rédiger un rapport synthétique. "
        "Ce rapport doit évaluer l'adéquation générale du candidat (basé sur ses réponses) pour le poste (basé sur l'offre). "
        "le rapport doit evaluer la correspondance des réponses avec les quéstions et évaluer les capacités techniques et sa communication. "
        "Soyez objectif et factuel."
    ),
    expected_output=(
        "Un rapport final structuré en sections : \n"
        "1. Score global (évalué sur l'adequation et les réponse du candidat).\n"
        "2. Points fort et point faible : détaille les point forts et faible du candidat avec des arguments.\n"
        "3. Axes d'amélioration : reprend les point faible du candidat et lui donne des pistes pour s'ameliorer.\n"
        "4. Evaluation detaillé : detaille precisement l'evalution du candidat (adequation technique, communication). \n"
    ),
    agent=report_generator_agent,
)

# cv_parser_agent
task_parsing = Task(
    description=(
        "Analyser le texte brut du CV suivant :\n\n{cv_content}\n\n"
        "Identifier les sections présentes **exactement comme elles apparaissent**. "
        "Ne pas inférer de sections manquantes. Répondre uniquement avec les noms de sections trouvées dans le texte."
    ),
    agent=cv_parser_agent,
    input_keys=["cv_content"],
    expected_output="Une liste des titres de sections présents dans le texte du CV (ex: ['informations_personnelles','Expérience Professionnelle', 'Formation', 'Compétences', 'Projets'])."
)

task_extract_skills = Task(
    description=(
        "Voici le contenu du CV :\n\n{cv_content}\n\n"
        "Extraire uniquement les compétences mentionnées explicitement dans le texte du CV. "
        "Séparer les hard skills (techniques) et les soft skills (comportementales) en analysant les listes ou phrases les contenant. "
        "Ne rien inventer. Ne pas déduire de compétences à partir d'un poste ou d'une expérience implicite."
        "identifie clairement les compétences, et n'en exlue aucune"
    ),
    agent=skills_extractor_agent,
    input_keys=["cv_content"],
    expected_output="Un dictionnaire JSON 'Compétences' avec deux clés : 'hard_skills' et 'soft_skills', contenant uniquement des listes de compétences présentes dans le texte."
)

task_extract_experience = Task(
    description=(
        "Voici le contenu du CV :\n\n{cv_content}\n\n"
        "Extraire chaque expérience professionnelle clairement identifiable dans le texte du CV. "
        "Pour chaque expérience, indiquer : le titre du poste, l'entreprise, les dates (si disponibles) et les responsabilités ou réalisations. "
        "Ne pas compléter ou deviner des informations absentes. Ignorer les expériences floues ou non structurées."
        "Ne confond pas les expériences avec les projets."
        "Identifie clairement les expériences professionnelles, et ne considére pas les etudes ou formations comme des expériences professionnelles."
    ),
    agent=experience_extractor_agent,
    input_keys=["cv_content"],
    expected_output="Un dictionnaires JSON Expérience 'Professionnelle' avec 5 clés : 'title', 'company', 'start_date', 'end_date', 'responsibilities' (liste)."
)

task_extract_projects = Task(
    description=(
        "Voici le contenu du CV :\n\n{cv_content}\n\n"
        "Identifier les projets mentionnés dans le texte du CV, qu'ils soient professionnels ou personnels. "
        "Inclure uniquement ceux clairement décrits. Pour chaque projet, extraire : le titre, les rôles, les technologies, et les résultats. "
        "Ne pas inférer ni inventer des projets à partir de postes ou compétences implicites."
        "Identifie clairement les projets, et ne considére pas les expériences professionnelles comme des projets."
        "Ne considére pas les études, formations ou alternances comme des projets."
    ),
    agent=project_extractor_agent,
    input_keys=["cv_content"],
    expected_output="Un dictionnaire JSON 'Projets' avec deux listes : 'professional' et 'personal', chaque élément étant un projet avec 'title', 'role', 'technologies', 'outcomes'."
)

task_extract_education = Task(
    description=(
        "Voici le contenu du CV :\n\n{cv_content}\n\n"
        "Extraire uniquement les formations et diplômes mentionnés explicitement dans le texte du CV. "
        "Inclure : diplôme, établissement, dates de début et fin si disponibles. Ne pas inventer de dates ou d'intitulés. "
        "Ignorer les formations non nommées ou imprécises."
        "Identifie clairement les formations et ne confond pas les formations avec les expériences professionnelles, ni les projets."
    ),
    agent=education_extractor_agent,
    input_keys=["cv_content"],
    expected_output="Un dictionnaires JSON 'Formation' avec : 'degree', 'institution', 'start_date', 'end_date'."
)

task_extract_informations = Task(
    description=(
        "Voici le contenu du CV :\n\n{cv_content}\n\n"
        "Votre tâche est d'extraire les informations de contact du candidat. Ces informations se trouvent généralement au début ou à la fin du CV, souvent sous une section intitulée 'CONTACT'.\n"
        "Extrayez précisément :\n"
        "- Le **Nom complet**.\n"
        "- L'**Adresse e-mail**.\n"
        "- Le **Numéro de téléphone**.\n"
        "- La **Localisation** (ville ou région).\n"
        "\nRetournez une liste de dictionnaires JSON 'informations_personnelles' avec les clés : 'nom', 'email', 'numero_de_telephone', 'localisation'. Si une information n'est pas présente, mettez la valeur à `null`."
        "toutes les informations devront etre normalisées, principalement le nom si il est en majuscule en titre."
    ),
    agent=informations_personnelle_agent,
    input_keys=["cv_content"],
    expected_output="Un dictionnaire JSON 'informations_personnelles' contenant le nom, l'email, le numéro de téléphone et la localisation du candidat."
)

task_build_profile = Task(
    description=(
        "Créer un profil structuré pour le candidat en récupérant les informations extraites par les agents précédents. "
        "Le profil doit inclure les informations personnelles, les compétences, expériences, projets et formations sous forme de JSON."
    ),
    agent=ProfileBuilderAgent,
    context=[
        task_extract_skills,
        task_extract_experience,
        task_extract_projects,
        task_extract_education,
        task_extract_informations
    ],
    expected_output= "retourne uniquement les dictionnaire JSON, sans en tete de fichier.Générer uniquement le contenu JSON brut pour la clé 'candidat', SANS aucun encadrement JSON (par exemple, pas de `{}` externes, pas de `json`, pas de ```json```). Le résultat doit être directement le dictionnaire pour 'candidat', encodé en UTF-8, sans apostrophes, ni caractères spéciaux.",
    output_file= f"data/cv_profile.json"
)