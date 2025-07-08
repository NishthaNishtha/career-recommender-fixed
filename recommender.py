def recommend_careers(skills):
    roles = {
        "Python": ["Data Scientist", "Backend Developer"],
        "SQL": ["Data Analyst", "BI Analyst"],
        "Excel": ["Business Analyst"],
        "Power BI": ["Data Analyst"],
        "Prompt Engineering": ["AI Specialist", "LLM Trainer"]
    }
    recommendations = set()
    for skill in skills:
        recommendations.update(roles.get(skill, []))
    return list(recommendations)

def gpt_recommend_careers(skills):
    if not skills:
        return "No skills provided."
    return f"Based on your skills in {', '.join(skills)}, you may be a great fit for roles such as Data Scientist, AI Specialist, or Business Analyst."
