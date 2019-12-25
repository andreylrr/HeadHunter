import json
#
#   HHParserSalary класс предназначен для вакансий полученных с сайта hh.ru
#   В каждой вакансии парсер определяет зарплаты, если они указаны
#

class HHParserSalary():
    def __init__(self):
        self._l_found_salary = []
        self._s_type_vacancy = ""

    def parse(self, vacancy: json) -> list:
        self._get_vacancy_type(vacancy['description'])
        self._get_vacancy_type(vacancy['name'])

        if vacancy['salary']:
            return [self._s_type_vacancy,
                    vacancy['salary']['from'],
                    vacancy['salary']['to'],
                    vacancy['salary']['currency']]
        return []

    def _get_vacancy_type(self, vacancy: str):
        self._l_found_salary = []
        if "senior" in vacancy.lower():
            self._s_type_vacancy = "Senior"
        elif "junior" in vacancy.lower():
            self._s_type_vacancy = "Junior"
        elif "middle" in vacancy.lower():
            self._s_type_vacancy = "Middle"
        else:
            self._s_type_vacancy = "Unknown"




if __name__ == '__main__':
    pass
