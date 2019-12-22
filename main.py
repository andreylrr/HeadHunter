import hhrequest as hr
import hhparserdescription as hp
import pickle as pic
import requests as re
import pprint as pp
import hhparserdescription as hp
import hhparser_key_skills as hk

d_terms_dictionary = dict()
s_url = 'https://api.hh.ru/vacancies'
s_search = 'java developer'


o_pars_description = hp.HHParserDescription()
o_pars_key_skills = hk.HHParserKeySkills()
o_hhrequest = hr.HHRequest(o_pars_description)

o_hhrequest.set_url(s_url)
o_hhrequest.set_search_pattern(s_search)

l_urls = o_hhrequest.get_urls_vacancies()
for s_url in l_urls:
    l_terms = o_hhrequest.process_url(s_url)
    print(s_url)
    for s_term in l_terms:
        if s_term in d_terms_dictionary:
            d_terms_dictionary[s_term] += 1
        else:
            d_terms_dictionary[s_term] = 1

print(sorted(d_terms_dictionary.items(), key=lambda x: x[1], reverse=True))

with open(s_search + '.pickle', 'wb') as f:
    pic.dump(d_terms_dictionary, f)
