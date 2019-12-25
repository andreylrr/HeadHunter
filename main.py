import hhrequest as hr
import hhparserdescription as hp
import pprint as pp
import hhparserdescription as hp
import hhparser_key_skills as hk
import hhparser_salary as hs
import time
from tqdm import tqdm

d_terms_dictionary = dict()
s_url = 'https://api.hh.ru/vacancies?area=#'
s_search = 'python developer'


o_pars_description = hp.HHParserDescription()
o_pars_salary = hs.HHParserSalary()
o_pars_description.load_help_files("ignore_terms.txt","double_terms.txt")
o_pars_key_skills = hk.HHParserKeySkills()
o_hhrequest = hr.HHRequest(o_pars_description)

o_hhrequest.set_url(s_url)
try:
     o_hhrequest.set_region("Новосибирск")
except ValueError:
    print("Регион не найден.")

o_hhrequest.set_search_pattern(s_search)

l_urls = o_hhrequest.get_urls_vacancies()
i_number_vacancies = 0
for s_url in tqdm(l_urls):
    l_terms = o_hhrequest.process_url(s_url)
    for s_term in l_terms:
        if s_term in d_terms_dictionary:
            d_terms_dictionary[s_term] += 1
        else:
            d_terms_dictionary[s_term] = 1
    i_number_vacancies += 1
#print(f'Всего вакансий: {i_number_vacancies}')

o_hhrequest.set_parser(o_pars_salary)
l_salary = []
for s_url in l_urls:
    l_salary.append(o_hhrequest.process_url(s_url))

print(l_salary)

pp.pprint(sorted(d_terms_dictionary.items(), key=lambda x: x[1], reverse=True))

