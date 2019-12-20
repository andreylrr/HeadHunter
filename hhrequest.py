import requests as req
import hhparser as hp
"""
     Класс HHRequest осуществляет обращение к сайту hh.ru с помощью api  
     для поиска вакансий по указанной тематики и обрабатывает 
     найденные объявления для получения списка требуемых технологий.
"""

class HHRequest():
    def __init__(self):
        self._s_search_pattern = ""
        self._l_ignore_terms = []
        self._s_url = ""
        self._l_urls_vacancies = []
        self._o_parser = hp.HHParser()

    def set_search_pattern(self, pattern: str) -> None:
        self._s_search_pattern = pattern

    def set_url(self, url: str) -> None:
        self._s_url = url

    def get_urls_vacancies(self) -> list:
        if not self._s_url:
            raise ValueError('Не задан адрес сайта.')

        if not self._s_search_pattern:
            raise ValueError('Не заданы критерии поиска.')

        i_page_number = 1
        while True:
            j_params = {'text': self._s_search_pattern,
                        'page': i_page_number,
                        'per_page': 100
            }

            j_result = req.get(self._s_url, params=j_params).json()

            for j_item in j_result['items']:
                self._l_urls_vacancies.append(j_item['url'])

            if j_result["page"] >= j_result["pages"] - 1:
                break
            else:
                i_page_number += 1
        return self._l_urls_vacancies

    def process_url(self, url: str) -> list:
        j_result = req.get(url).json()
        return self._o_parser.parse(j_result['description'])

    def load_ignore_terms(self, file_name: str) -> None:
        pass
