import re
import json
#
#   HHParserKeySkills класс предназначен для обработки описаний вакансий полученных с сайта hh.ru
#   В каждом описании вакансии парсер определяет какие технологии были востребованы и
#   возвращает их список
#

class HHParserKeySkills():
    def __init__(self):
        self._l_found_technology = []
        self._s_description = ""

    def parse(self, vacancy: json) -> list:
        self._l_skills = vacancy['key_skills']
        if self._l_skills:
            print(type(self._l_skills[0]))
            self._find_technology()
        else:
            self._l_found_technology = []
        return self._l_found_technology

    def _find_technology(self) -> None:
        """
            Метод для определения ключевых слов по технологиям
        :return:
        """
        # Убираем русский текст
        l_tech = self._s_description.split()
        self._l_found_technology = [word for word in l_tech if not re.match("[А-Яа-я]", word)]
        # Убираем слова, которые не начинаются с большой буквы
        self._l_found_technology = [word for word in self._l_found_technology if word.istitle()]
        # Убираем повторы
        self._l_found_technology = list(set(self._l_found_technology))

if __name__ == '__main__':
    pass
