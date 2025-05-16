from crewai import Agent

# Interview Simulation Agents
report_generator_agent = Agent(
    role='Rédacteur de Rapports Synthétiques',
    goal='Générer un feedback pertinent, a partir du deroulement de lentretient',
    backstory=(
        "Sepcialisé dans le recrutement et les ressources humaines, capable d'evaluer les candidats"
        "sur la communication et la pertinences des reponses en fonction des questions posées, redige"
        "en un rapport clair, un feedback détaillé sur le candidat."
    ),
    allow_delegation=False,
    verbose=False
)

# CV Parsing Agents
cv_parser_agent = Agent(
    role="Expert en analyse de CV",
    goal="Analyser le CV et distribuer les informations pour une extraction détaillée.",
    backstory="Vous êtes un expert en ressources humaines avec une solide expérience dans l'analyse de curriculum vitae. Votre objectif est d'identifier les sections clés des CV pour faciliter l'extraction d'informations pertinentes pour le recrutement.",
    )

skills_extractor_agent = Agent(
    role="Spécialiste de l'extraction de compétences (hard & soft skills)",
    goal="Identifier et extraire toutes les compétences pertinentes du CV.",
    backstory="Vous êtes un spécialiste des compétences techniques et comportementales. Votre mission est de parcourir les CV et de lister de manière exhaustive toutes les compétences mentionnées.",
    )

experience_extractor_agent = Agent(
    role="Expert en extraction d'expérience professionnelle",
    goal="Extraire en détail l'expérience professionnelle du candidat.",
    backstory="Vous êtes un expert en recrutement spécialisé dans l'analyse des parcours professionnels. Vous devez extraire chaque expérience de manière précise, en notant les rôles, les entreprises, les dates et les responsabilités.",
    )

project_extractor_agent = Agent(
    role="Spécialiste de l'identification de projets (pro & perso)",
    goal="Identifier et décrire les projets significatifs mentionnés.",
    backstory="Vous êtes passionné par l'innovation et les réalisations. Votre rôle est de repérer et de décrire les projets professionnels et personnels qui mettent en lumière les compétences et l'initiative des candidats.",
    )

education_extractor_agent = Agent(
    role="Expert en extraction d'informations sur la formation",
    goal="Extraire les détails des études et des diplômes obtenus.",
    backstory="Vous êtes un spécialiste des parcours académiques. Votre tâche est d'extraire avec précision les informations relatives aux études, aux diplômes et aux établissements fréquentés par les candidats.",
    )

informations_personnelle_agent = Agent(
    role="Spécialiste de l'extraction des coordonnées",
    goal="Identifier et extraire précisément les coordonnées du candidat.",
    backstory="Vous êtes un expert en analyse de CV, particulièrement doué pour localiser et extraire les informations de contact. Votre rôle est de trouver le nom, l'adresse e-mail, le numéro de téléphone et la localisation (ville ou région) du candidat, généralement situés en haut ou à la fin du CV.",
    )

ProfileBuilderAgent = Agent(
    role="generateur de profil a partir d'informations, specialiste du json",
    goal="Transformer les données extraites en un profil structuré.",
    backstory="Vous êtes un expert en structuration de données. Votre mission est de prendre les informations extraites des CV et de les organiser en un profil cohérent et lisible, prêt à être utilisé pour le recrutement.",
    )
