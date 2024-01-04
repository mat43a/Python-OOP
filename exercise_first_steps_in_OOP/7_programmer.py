class Programmer:
    def __init__(self, name: str, language: str, skills: int):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name, language, skill_earned):
        if language == self.language:
            self.skills += skill_earned
            return f'{self.name} watched {course_name}'
        return f'{self.name} does not know {language}'

    def change_language(self, new_language, skill_needed):
        if self.skills >= skill_needed:
            if self.language != new_language:
                previous_language = self.language
                self.language = new_language
                return f'{self.name} switched from {previous_language} to {new_language}'

            return f'{self.name} already know {new_language}'

        return f'{self.name} needs {skill_needed - self.skills} more skills'
