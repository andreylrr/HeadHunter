import requests as r
import pprint as p
import json as j


s_url = 'https://api.hh.ru/vacancies'
i_page = 1
l_url = []

while True:
    j_params = {'text': 'java developer',
              'page': i_page}
    j_result = r.get(s_url,params=j_params).json()

    for j_item in j_result['items']:
        l_url.append(j_item['url'])

    if j_result["page"] >= j_result["pages"] - 1:
        break
    else:
        i_page += 1

    print(f'Processing page number {i_page}..')


for s_url in l_url:
    j_result = r.get(s_url).json()
    p.pprint(j_result['description'])
    print(type(j_result['description']))

# Из описания надо выделить только технологии. Признаки: 1. Английское слово полность 2. Начинается с заглавной буквы


# TODO Все найденные слова должны быть помещены в словарь. Если термина нет в словаре, то он добавляется и счетчик усатанвливается в 1
# TODO Если термин присутствует в словаре, то счетчик увеличивается на едениу.


