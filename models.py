from datetime import date, timedelta

class UnableToWorkException(Exception):
    pass

class Employee:

    def safe_email(self, email):
        file = 'emails.txt'
        f1 = open(file, 'a')
        f1.write(str(self.email) + '\n')
        f1.close()

    def validate_email(self):
        file = 'emails.txt'
        f2 = open(file, 'r')
        for email in f2:
            if email == self.email:
                raise ValueError('this email already exists')

    def __init__(self, name, fullname, email, zp):
        self.name = name
        self.fullname = fullname
        self.email = email
        self.validate_email()
        self.zp = zp

    def work(self):
        return f"I come to the office"

    def check_selary(self, zp):
        now = date.today()
        month_start = date(now.year, now.month, 1)
        diff = (now - month_start).days + 1
        count_sell = zp * diff
        return count_sell

    def check_salary_apgr(self, zp):
        now = date.today()
        month_start = date(now.year, now.month, 1)
        weekend = [5, 6]
        diff = (now - month_start).days + 1
        day_count = 0
        for day in range(diff):
            if (month_start + timedelta(day)).weekday() not in weekend:
                day_count += 1
        return day_count

    def __gt__(self, other):
        return self.zp > other.zp

    def __ge__(self, other):
        return self.zp >= other.zp

    def __lt__(self, other):
        return self.zp < other.zp

    def __le__(self, other):
        return self.zp <= other.zp

    def __eq__(self, other):
        return self.zp == other.zp

    def __ne__(self, other):
        return self.zp != other.zp

    @property
    def full_info(self):
        return f"{self.__class__.__name__}, {self.name}, {self.fullname}, {self."

class Recruiter(Employee):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def work(self):
        parent_work1 = super().work()
        return f"I come to the office and start to hiring"

    def __str__(self):
        return (f'Recruter: {self.name}')


class Programmer(Employee):

    def __init__(self, name, email, zp, tech_stack):
        super().__init__(name, email, zp)
        self.tech_stack = tech_stack

    def work(self):
        parent_work2 = super().work()
        return f"I come to the office and start to coding"

    def __str__(self):
        return f'Programmer: {self.name}'

    def comp_tech(self, tech_another):
        if len(self.tech_stack) > len(tech_another.tech_stack):
            comp = '>'
        elif len(self.tech_stack) < len(tech_another.tech_stack):
            comp = '<'
        else:
            comp = '='

        return (f'Tech stack of {self.name} {comp} tech stack of {tech_another.name}')

    def alfa_pr(*args):
        tech_stack_for_alfa = set()
        for i in args:
            tech_stack_for_alfa = tech_stack_for_alfa.union(set(i.tech_stack))

        alfa_pr = Programmer('Proframer 3', 'pr3@gamail.com', 100, list(tech_stack_for_alfa))
        return alfa_pr


class Candidate:

    def __init__(self, full_name, email, technologies, main_skill, main_skill_grade):
        self.full_name = full_name
        self.email = email
        self.technologies = technologies
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    def work(self):
        raise UnableToWorkException('I’m not hired yet, lol')


class Vacancy:

    def __init__(self, title, main_skill, main_skill_level):
        self.title = title
        self.main_skill = main_skill
        self.main_skill_level = main_skill_level
