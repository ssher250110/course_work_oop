class Vacancy:
    """
    Класс для работы с одной вакансией
    """

    __slots__ = [
        "__vacancy_name",
        "description",
        "address",
        "date_published",
        "__salary_from",
        "__salary_to",
        "currency",
        "__url",
    ]

    def __init__(
            self,
            vacancy_name: str,
            description: str,
            address: str,
            date_published: int | str,
            salary_from: int | None,
            salary_to: int | None,
            currency: str | None,
            url: str,
    ):
        """
        :param vacancy_name: название вакансии
        :param description: описание вакансии
        :param address: город вакансии
        :param date_published: дата публикации
        :param salary_from: зарплата от
        :param salary_to: зарплата до
        :param currency: валюта
        :param url: сайт вакансии
        """
        self.__vacancy_name = vacancy_name
        self.description = description
        self.address = address
        self.date_published = date_published
        self.__salary_from = self.validate_salary(salary_from)
        self.__salary_to = self.validate_salary(salary_to)
        self.currency = self.validate_currency(currency)
        self.__url = url

    @property
    def vacancy_name(self):
        return self.__vacancy_name

    @property
    def salary_from(self):
        return self.__salary_from

    @salary_from.setter
    def salary_from(self, value):
        self.__salary_from = value

    @property
    def salary_to(self):
        return self.__salary_to

    @salary_to.setter
    def salary_to(self, value):
        self.__salary_to = value

    @property
    def url(self):
        return self.__url

    @staticmethod
    def validate_salary(salary):
        """
        Метод для преобразования зарплаты
        :param salary: зарплата
        :return: зарплату
        """
        if salary is None or salary == 500000:
            return 0
        return salary

    @staticmethod
    def validate_currency(currency):
        """
        Метод для преобразования валюты
        :param currency: валюта
        :return: валюту
        """
        if currency is None or currency in ("rub", "RUR"):
            return "руб."
        return currency

    def avg_salary(self):
        """
        Получение средней зарплаты вакансии
        :return: среднее значение зарплаты
        """
        return (self.salary_from + self.salary_to) / 2

    def __eq__(self, other):
        if self.avg_salary() == 0:
            return False
        if other.avg_salary() == 0:
            return False
        return self.avg_salary() == other.avg_salary

    def __gt__(self, other):
        if self.avg_salary() == 0:
            return False
        if other.avg_salary() == 0:
            return True
        return self.avg_salary() > other.avg_salary()

    def print_salary(self):
        """
        Метод для корректного отображения зарплаты для пользователя
        :return: корректное отображение зарплаты
        """
        if self.salary_from == 0 and self.salary_to == 0:
            return "не указана"
        elif self.salary_from == 0 and self.salary_to != 0:
            return f"до {self.salary_to} {self.currency}"
        elif self.salary_from != 0 and self.salary_to == 0:
            return f"от {self.salary_from} {self.currency}"
        else:
            return f"от {self.salary_from} до {self.salary_to} {self.currency}"

    def __str__(self):
        """
        Метод вывода информации пользователю
        :return: информацию о вакансии
        """
        return (
            f"Название вакансии: {self.vacancy_name}\n"
            f"{self.description}\n"
            f"Город: {self.address}\n"
            f"Дата публикации: {self.date_published}\n"
            f"Зарплата: {self.print_salary()}\n"
            f"Ссылка на вакансию: {self.url}\n"
        )

    def to_dict(self):
        """
        Метод для сохранения вакансии из экземпляра класса
        :return:
        """
        return {
            "vacancy_name": self.vacancy_name,
            "description": self.description,
            "address": self.address,
            "date_published": self.date_published,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "currency": self.currency,
            "url": self.url,
        }


class HeadHunterVacancy(Vacancy):
    platform_name = "HH"

    def __str__(self):
        """
        Метод вывода информации пользователю
        :return: информацию о вакансии
        """
        return (
            f"HeadHunter\n"
            f"Название вакансии: {self.vacancy_name}\n"
            f"{self.description}\n"
            f"Город: {self.address}\n"
            f"Дата публикации: {self.date_published}\n"
            f"Зарплата: {self.print_salary()}\n"
            f"Ссылка на вакансию: {self.url}\n"
        )

    def to_dict(self):
        vacancy_dict = super().to_dict()
        new_vacancy_dict = {"platform_name": self.platform_name} | vacancy_dict
        # vacancy_dict["platform_name"] = self.platform_name
        return new_vacancy_dict


class SuperJobVacancy(Vacancy):
    platform_name = "SJ"

    def __str__(self):
        """
        Метод вывода информации пользователю
        :return: информацию о вакансии
        """
        return (
            f"SuperJob\n"
            f"Название вакансии: {self.vacancy_name}\n"
            f"{self.description}\n"
            f"Город: {self.address}\n"
            f"Дата публикации: {self.date_published}\n"
            f"Зарплата: {self.print_salary()}\n"
            f"Ссылка на вакансию: {self.url}\n"
        )

    def to_dict(self):
        vacancy_dict = super().to_dict()
        new_vacancy_dict = {"platform_name": self.platform_name} | vacancy_dict
        # vacancy_dict["platform_name"] = self.platform_name
        return new_vacancy_dict
