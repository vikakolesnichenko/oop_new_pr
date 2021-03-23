from models import Programmer
from models import Recruiter
from models import Candidate
from models import Vacancy


if __name__ == '__main__':

    print(__name__)

    recr_1 = Recruiter('Vika', 'viktoria@gmail.com', 24)
    emp_2 = Programmer('Sophia', 'Soph@gmail.com', 30,  ['Python', 'SQL', 'CSS', 'PostgreSQL'])
    emp_3 = Programmer('Vlad', 'Vlad@gmail.com', 500,  ['Python', 'GitHub', 'Java'])
    cand_1 = Candidate('Valentin Zal', '@gmail.com', ['SQL', 'Java'], 'English', 'Magister')
    cand_2 = Candidate('Valentin Zal', '@gmail.com', ['SQL', 'Java'], 'English', 'Magister')
    cand_3 = Candidate('Valentin Zal', '@gmail.com', ['SQL', 'Java'], 'English', 'Magister')
    vak_1 = Vacancy('Programmer', ['C++', 'C#'], 'Midle')
    vak_2 = Vacancy('Desiner', ['Figma', 'C#'], 'Midle')
