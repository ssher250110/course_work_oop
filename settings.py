from pathlib import Path

BASIC_URL_HH = "https://api.hh.ru/vacancies"
BASIC_URL_SUPERJOB = "https://api.superjob.ru/2.0/vacancies/"

ROOT_PATH = Path(__file__).parent
DATA_VACANCIES_PATH = Path.joinpath(ROOT_PATH, "data_vacancies", "vacancies.json")
