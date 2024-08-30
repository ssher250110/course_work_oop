from json import JSONDecodeError

from settings import DATA_VACANCIES_PATH
from src.func_utils import get_instances_hh, get_instances_sj, sorted_vacancies_salary, convert_to_instance
from src.work_data import JsonSaver


def main():
    user_name_vacancy = input("Введите название вакансии: ")
    user_quantity_vacancies = int(
        input("Сколько вакансий искать (максимальное количество вакансий 100, по умолчанию 10): "))
    if 0 < user_quantity_vacancies <= 100:
        user_quantity_vacancies = user_quantity_vacancies
    else:
        user_quantity_vacancies = 10

    hh_instances = get_instances_hh(user_name_vacancy, user_quantity_vacancies)
    sj_instances = get_instances_sj(user_name_vacancy, user_quantity_vacancies)

    while True:
        user_file = input("1 - перезаписать файл новыми вакансиями\n"
                          "2 - добавить в файл вакансии\n"
                          "3 - продолжить\n")
        saver = JsonSaver(DATA_VACANCIES_PATH)
        if user_file == "1":
            sorted_instances = sorted_vacancies_salary(hh_instances + sj_instances)
            saver.create_vacancies_file(sorted_instances)
            break
        elif user_file == "2":
            sorted_instances = sorted_vacancies_salary(hh_instances + sj_instances)
            saver.add_vacancies_file(sorted_instances)
            break
        elif user_file == "3":
            break
        else:
            print("Неправильный ввод")
            continue

    vacancies_file = saver.get_vacancies_file()
    display_vacancies = convert_to_instance(vacancies_file)
    for vacancy in display_vacancies:
        print(vacancy)

    while True:
        user_delete_vacancies = input("Удалить вакансии с отсутствующей зарплатой?\n"
                                      "1 - нет\n"
                                      "2 - да\n")
        if user_delete_vacancies == "1":
            break
        elif user_delete_vacancies == "2":
            saver.delete_vacancies_zero_salary()
            break
        else:
            continue

    vacancies_file = saver.get_vacancies_file()
    display_vacancies = convert_to_instance(vacancies_file)
    for vacancy in display_vacancies:
        print(vacancy)

    while True:
        user_vacancies = input("1 - очистить файл?\n"
                               "2 - завершить работу программы?\n")
        if user_vacancies == "1":
            saver.delete_vacancies_file()
            break
        elif user_vacancies == "2":
            break
        else:
            print("Ошибка ввода")
            continue


if __name__ == '__main__':
    main()
