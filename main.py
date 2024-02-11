def main():
    hh_api = HHApiVacancies("python")
    hh_vacancies = hh_api.get_vacancies(5)
    hh_instances = create_hh_instances(hh_vacancies)
    hh_sorted_instances = sorted_vacancies_salary(hh_instances)
    for vac in hh_sorted_instances:
        print(vac)

    # sj_sort_vac = sorted_vacancies_date(hh_instances)
    # print()

    # sj_api = SJApiVacancies("linux")
    # sj_vacancies = sj_api.get_vacancies()
    # print()
    # sj_instances = SuperJobVacancy.create_sj_instances(sj_vacancies)
    # print()
    # sj_sort_vac = sorted_vacancies_date(hh_instances)
    # print()
    # for instancy in hh_instances:
    #     print(instancy)


if __name__ == '__main__':
    main()
