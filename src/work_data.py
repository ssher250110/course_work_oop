import json
from abc import ABC, abstractmethod

from src.work_vacancy import Vacancy


class Saver(ABC):
    def __init__(self, path):
        self.path = path
        with open(self.path, "w") as file:
            json.dump([], file)

    @abstractmethod
    def add_vacancies(self, vacancies: list[Vacancy]) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_vacancies(self, queries=None) -> list[dict]:
        raise NotImplementedError

    @abstractmethod
    def delete_vacancies(self, query=None) -> None:
        raise NotImplementedError


class JsonSaver(Saver):

    def add_vacancies(self, vacancies: list[Vacancy]) -> None:
        """
        Добавление вакансий в файл json
        :param vacancies: список экземпляров класса вакансий
        """
        vacancies_json = [vacancy.to_dict() for vacancy in vacancies]
        with open(self.path, encoding="utf-8") as file:
            old_vacancies: list[dict] = json.load(file)
        old_vacancies.extend(vacancies_json)
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(old_vacancies, file, ensure_ascii=False, indent=4)

    def get_vacancies(self, queries=None) -> list[dict]:
        """
        Получение вакансий из файла json
        :param queries: необходимый запрос данных
        """
        with open(self.path, encoding="utf-8") as file:
            all_vacancies: list[dict] = json.load(file)
        vacancies = []
        # for vacancy in all_vacancies:
        #     if all(vacancy.get(field) == query for field, query in queries.items()):
        #         vacancies.append(vacancy)

        for field, query in queries.items():
            for vacancy in all_vacancies:
                if vacancy[field] == query:
                    vacancies.append(vacancy)
        return vacancies

    def delete_vacancies(self, query=None) -> None:
        pass
