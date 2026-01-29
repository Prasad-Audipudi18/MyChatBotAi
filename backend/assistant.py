from langchain_google_genai import ChatGoogleGenerativeAI
from utils.config import get_system_prompt
from user_profile import USER_PROFILE

def get_personal_answer(user_input):
    q = user_input.lower()

    if "name" in q:
        return f"My name is {USER_PROFILE['name']}."

    if "resume" in q:
        # Build a full resume string
        resume = f"{USER_PROFILE['summary']}\n\nExperience:\n"
        exp = USER_PROFILE['experience']
        resume += f"{exp['role']} at {exp['company']} ({exp['duration']}, {exp['location']})\n"
        resume += f"{exp['description']}\n"
        resume += "Modules: " + ", ".join(exp['modules']) + "\n\n"
        resume += "Skills:\nFrontend: " + ", ".join(USER_PROFILE['skills']['frontend']) + "\n"
        resume += "Other Skills: " + ", ".join(USER_PROFILE['skills']['other_skills']) + "\n\n"
        resume += "Education:\n"
        for edu in USER_PROFILE['education']:
            resume += f"{edu['degree']}, {edu['institution']} ({edu['year']}) - {edu['score']}\n"
        resume += "\nProjects:\n"
        for p in USER_PROFILE['projects']:
            resume += f"{p['name']} ({p['type']}): {p['description']}\nTechnologies: {', '.join(p['technologies'])}\n\n"
        resume += "Currently Learning: " + ", ".join(USER_PROFILE['currently_learning']['modules'])
        return resume

    if "education" in q or "qualification" in q:
        edu_text = ""
        for edu in USER_PROFILE['education']:
            edu_text += f"{edu['degree']}, {edu['institution']} ({edu['year']}) - {edu['score']}\n"
        return edu_text.strip()

    if "skill" in q:
        skills = USER_PROFILE['skills']
        return f"Frontend: {', '.join(skills['frontend'])}\nOther Skills: {', '.join(skills['other_skills'])}"

    if "experience" in q:
        exp = USER_PROFILE['experience']
        exp_text = f"{exp['role']} at {exp['company']} ({exp['duration']}, {exp['location']})\n"
        exp_text += f"{exp['description']}\nModules: {', '.join(exp['modules'])}"
        return exp_text

    if "project" in q:
        proj_text = ""
        for p in USER_PROFILE['projects']:
            proj_text += f"{p['name']} ({p['type']}): {p['description']}\nTechnologies: {', '.join(p['technologies'])}\n\n"
        return proj_text.strip()

    if "learning" in q or "modules" in q:
        modules = USER_PROFILE['currently_learning']['modules']
        return f"Currently learning these modules: {', '.join(modules)}"

    return "No valid response."


class ChatAssistant:
    def __init__(self, api_key=None):
        self.api_key = api_key
        if not self.api_key:
            raise ValueError("GOOGLE_API_KEY missing")
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-3-flash-preview",
            google_api_key=self.api_key,
            temperature=0.2
        )
        self.history = []

    def add_to_history(self, role, content):
        self.history.append({"role": role, "content": content})
        if len(self.history) > 10:
            self.history.pop(0)

    def get_conversation_context(self):
        return [{"role": "system", "content": get_system_prompt()}] + self.history

    def chat(self, user_input):
        personal = get_personal_answer(user_input)
        if personal:
            self.add_to_history("assistant", personal)
            return personal

        self.add_to_history("user", user_input)
        context = self.get_conversation_context()
        resp = self.llm.invoke(context)
        text = resp.content
        self.add_to_history("assistant", text)
        return text

def answer_query(query, assistant=None):
    if assistant is None:
        raise ValueError("Assistant not initialized")
    return assistant.chat(query)
