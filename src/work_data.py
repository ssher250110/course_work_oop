import json
import os
from abc import ABC, abstractmethod

from src.work_vacancy import Vacancy


class Saver(ABC):
    def __init__(self, path):
        self.path = path

    @abstractmethod
    def create_vacancies_file(self, vacancies: list[Vacancy]) -> None:
        raise NotImplementedError

    @abstractmethod
    def add_vacancies_file(self, vacancies: list[Vacancy]) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_vacancies_file(self) -> list[dict]:
        raise NotImplementedError

    @abstractmethod
    def delete_vacancies_file(self) -> None:
        raise NotImplementedError


class JsonSaver(Saver):

    def create_vacancies_file(self, vacancies: list[Vacancy]) -> None:
        """
        Перезапись вакансий в файл json
        :param vacancies: список экземпляров класса вакансий
        """
        vacancies_json = [vacancy.to_dict() for vacancy in vacancies]
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(vacancies_json, file, ensure_ascii=False, indent=4)

    def add_vacancies_file(self, vacancies: list[Vacancy]) -> None:
        """
        Добавление вакансий в файл json
        :param vacancies: список экземпляров класса вакансий
        """
        vacancies_json = [vacancy.to_dict() for vacancy in vacancies]
        with open(self.path, 'a', encoding="utf-8") as file:
            if os.stat(self.path).st_size == 0:
                json.dump(vacancies_json, file, ensure_ascii=False, indent=4)
            else:
                with open(self.path, "r", encoding="utf-8") as file:
                    old_vacancies: list[dict] = json.load(file)
                    old_vacancies.extend(vacancies_json)
                with open(self.path, "w", encoding="utf-8") as file:
                    json.dump(old_vacancies, file, ensure_ascii=False, indent=4)

    def get_vacancies_file(self) -> list[dict]:
        """
        Метод получения вакансий из файла json
        :return: список словарей вакансий
        """
        with open(self.path, "r", encoding="utf-8") as file:
            all_vacancies: list[dict] = json.load(file)
        return all_vacancies

    def delete_vacancies_file(self) -> None:
        """
        Метод удаления вакансий из файла json
        """
        with open(self.path, "w", encoding="utf-8") as file:
            file.write("")

    def delete_vacancies_zero_salary(self) -> None:
        """
        Метод удаляющий зарплаты у которых хоть один параметр равен 0
        """
        all_vacancies = self.get_vacancies_file()
        vacancies = [vacancy for vacancy in all_vacancies if vacancy["salary_from"] != 0 or vacancy["salary_to"] != 0]
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)
