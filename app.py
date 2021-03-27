from models import Programmer
from models import Recruiter
from models import Candidate
from models import Vacancy
from models import UnableToWorkException

def main():

    recr_1 = Recruiter('Vika', 'viktoria@gmail.com', 24)
    emp_2 = Programmer('Sophia', 'Soph@gmail.com', 30, ['Python', 'SQL', 'CSS', 'PostgreSQL'])
    emp_3 = Programmer('Vlad', 'Vlad@gmail.com', 500, ['Python', 'GitHub', 'Java'])
    cand_1 = Candidate('Valentin Zal', '@gmail.com', ['SQL', 'Java'], 'English', 'Magister')
    cand_2 = Candidate('Valentin Zal', '@gmail.com', ['SQL', 'Java'], 'English', 'Magister')
    cand_3 = Candidate('Valentin Zal', '@gmail.com', ['SQL', 'Java'], 'English', 'Magister')
    vak_1 = Vacancy('Programmer', ['C++', 'C#'], 'Midle')
    vak_2 = Vacancy('Desiner', ['Figma', 'C#'], 'Midle')

if __name__ == '__main__':
    try:
        main()
    except(ValueError, UnableToWorkException) as err:
        exc = sys.exc_info()[2]
        traceback1 = traceback.format_tb(exc)[0]
        error_class = err.__class__.__name__
        error_message = f'{datetime.now()}: {error_class}, Traceback: {traceback1}'
        filename = './logs.txt'
        f = open(filename, 'a')
        f.write(str(error_message) + '\n')
        f.close()
