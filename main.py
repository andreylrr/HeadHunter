import requests as r
import pprint as p
import json as j


s_url = 'https://api.hh.ru/vacancies'
i_page = 1
j_params = {'text': 'java developer',
          'page': i_page}
j_result = r.get(s_url,params=j_params).json()


p.pprint(j_result)

for j_item in j_result['items']:
    p.pprint(j_item['url'])

#j_result_1 = r.get(j_items[0]['url']).json()
#p.pprint(j_result_1)
#p.pprint(j_items[0]['snippet']['requirement'])
