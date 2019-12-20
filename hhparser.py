import re
#
#   HHParser класс предназначен для обработки описаний вакансий полученных с сайта hh.ru
#   В каждом описании вакансии парсер определяет какие технологии были востребованы и
#   возвращает их список
#

class HHParser():
    def __init__(self):
        self._l_found_technology = []
        self._s_description = ""

    def parse(self, job_description: str) -> list:
        self._s_description = job_description
        self._clean_trash()
        self._clean_html()
        self._find_technology()
        return self._l_found_technology

    def _clean_trash(self) -> None:
        """
            Метод для очистки описания от символов, которые на являются буквами английского алфавита
        """
        re_cleanr = re.compile('[\W_]+')
        self._s_description = re_cleanr.sub(" ", self._s_description )

    def _clean_html(self) -> None:
        """
            Метод для очистки описания от html тагов
        """
        re_cleanr = re.compile('<.*?>')
        self._s_description = re.sub(re_cleanr, '', self._s_description)

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
