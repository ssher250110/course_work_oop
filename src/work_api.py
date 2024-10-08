import os
from abc import ABC, abstractmethod

import requests
from dotenv import load_dotenv

from settings import BASIC_URL_HH, BASIC_URL_SUPERJOB
from user_exceptions import ApiError

load_dotenv()


class ApiVacancies(ABC):
    """
    Абстрактный класс для получения вакансий через API
    """

    @abstractmethod
    def get_vacancies(self) -> list[dict]:
        """
        Абстрактный метод для получения вакансий
        :return: список вакансий в виде словарей
        """
        pass


class HHApiVacancies(ApiVacancies):
    """
    Класс для получения вакансий с сайта HeadHunter
    """

    def __init__(self, title_vacancy: str):
        """
        Инициализация атрибутов экземпляра класса
        :param title_vacancy: название вакансии для поиска
        """
        self.title_vacancy = title_vacancy
        self.params = {
            "text": self.title_vacancy,
            "search_field": "name",
            "order_by": "publication_time",
        }

    def get_vacancies(self, per_page: int = 10) -> list[dict]:
        """
        Получение необходимого кол-ва вакансий
        :param per_page: кол-во вакансий
        :return: список вакансий в виде словарей
        """
        self.params["per_page"] = per_page
        try:
            response_api_hh = requests.get(url=BASIC_URL_HH, params=self.params).json()["items"]
        except KeyError:
            raise ApiError()
        else:
            return response_api_hh


class SJApiVacancies(ApiVacancies):
    """
    Класс для получения вакансий с сайта SuperJob
    """

    def __init__(self, title_vacancy):
        """
        Инициализация атрибутов экземпляра класса
        :param title_vacancy: название вакансии для поиска
        """
        self.title_vacancy = title_vacancy
        self.params = {
            "keywords": [{"srws": 10, "skwc": "or", "keys": self.title_vacancy}]
        }

    def get_vacancies(self, count: int = 10):
        """
        Получение необходимого кол-ва вакансий
        :param count: кол-во вакансий
         :return: список вакансий в виде словарей
        """
        self.params["count"] = count
        try:
            headers = {"X-Api-App-Id": os.getenv("TOKEN_API_SUPERJOB")}
            response_api_sj = requests.get(url=BASIC_URL_SUPERJOB, json=self.params, headers=headers).json()["objects"]
        except KeyError:
            raise ApiError()
        else:
            return response_api_sj
