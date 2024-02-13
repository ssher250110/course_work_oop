from datetime import datetime

from src.work_api import HHApiVacancies, SJApiVacancies
from src.work_vacancy import Vacancy, HeadHunterVacancy, SuperJobVacancy


def create_hh_instances(vacancies: list[dict]) -> list[Vacancy]:
    """
    Метод создания списка с экземплярами класса, вакансий HeadHunter
    :param vacancies: список вакансий
    :return: список экземпляров класса вакансий
    """
    return [
        HeadHunterVacancy(
            vacancy_name=vacancy["name"],
            description=[vacancy["snippet"]["requirement"].replace("<highlighttext>", "", ).replace(
                "</highlighttext>", "", ) if vacancy.get("snippet").get("requirement") else None][0],
            address=vacancy["area"]["name"],
            date_published=datetime.fromisoformat(vacancy["published_at"]).strftime("%d-%m-%Y %H:%M:%S"),
            salary_from=[vacancy["salary"]['from'] if vacancy.get("salary") else None][0],
            salary_to=[vacancy["salary"]['to'] if vacancy.get("salary") else None][0],
            currency=[vacancy["salary"]['currency'] if vacancy.get("salary") else None][0],
            url=vacancy["alternate_url"]
        )
        for vacancy in vacancies
    ]


def create_sj_instances(vacancies: list[dict]) -> list[Vacancy]:
    """
    Метод создания списка с экземплярами класса, вакансий SuperJob
    :param vacancies: список вакансий
    :return: список экземпляров класса вакансий
    """
    return [
        SuperJobVacancy(
            vacancy_name=vacancy["profession"],
            description=vacancy["candidat"],
            address=vacancy["client"]["town"]["title"],
            date_published=datetime.fromtimestamp(vacancy["date_published"]).strftime("%d-%m-%Y %H:%M:%S"),
            salary_from=vacancy["payment_from"],
            salary_to=vacancy["payment_to"],
            currency=vacancy["currency"],
            url=vacancy["link"]
        )
        for vacancy in vacancies
    ]


def sorted_vacancies_salary(vacancies: list[Vacancy]):
    """
    Сортировка вакансий по средней зарплате
    :param vacancies: список экземпляров класса вакансий
    """
    return sorted(vacancies, reverse=True)


def convert_to_instance(vacancies: list[dict]) -> list[Vacancy]:
    """
    Метод для конвертации списка с вакансиями обратно в список с экземплярами класса
    :param vacancies: список словарей с вакансиями
    :return: список экземпляров класса с вакансиями
    """
    instances = []
    for vacancy in vacancies:
        if vacancy["platform_name"] == "HeadHunter":
            del vacancy["platform_name"]
            instances.append(HeadHunterVacancy(**vacancy))
        elif vacancy["platform_name"] == "SuperJobs":
            del vacancy["platform_name"]
            instances.append(SuperJobVacancy(**vacancy))
    return instances


def get_instances_hh(name_vacancy, quantity_vacancy):
    hh_api = HHApiVacancies(name_vacancy)
    hh_vacancies = hh_api.get_vacancies(quantity_vacancy)
    hh_instances = create_hh_instances(hh_vacancies)
    return hh_instances


def get_instances_sj(name_vacancy, quantity_vacancy):
    sj_api = SJApiVacancies(name_vacancy)
    sj_vacancies = sj_api.get_vacancies(quantity_vacancy)
    sj_instances = create_sj_instances(sj_vacancies)
    return sj_instances
