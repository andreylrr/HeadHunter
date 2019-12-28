import unittest
import hhparser_description

j_test = {'accept_handicapped': False,
 'accept_incomplete_resumes': False,
 'accept_kids': False,
 'address': {'building': '6с2',
             'city': 'Москва',
             'description': None,
             'lat': 55.692962,
             'lng': 37.65973,
             'metro': {'lat': 55.698333,
                       'line_id': '95',
                       'line_name': 'МЦК',
                       'lng': 37.648333,
                       'station_id': '95.531',
                       'station_name': 'ЗИЛ'},
             'metro_stations': [{'lat': 55.698333,
                                 'line_id': '95',
                                 'line_name': 'МЦК',
                                 'lng': 37.648333,
                                 'station_id': '95.531',
                                 'station_name': 'ЗИЛ'},
                                {'lat': 55.695,
                                 'line_id': '2',
                                 'line_name': 'Замоскворецкая',
                                 'lng': 37.664167,
                                 'station_id': '2.512',
                                 'station_name': 'Технопарк'}],
             'raw': 'Москва, Проектируемый проезд № 4062, 6с2',
             'street': 'Проектируемый проезд № 4062'},
 'allow_messages': True,
 'alternate_url': 'https://hh.ru/vacancy/35067558',
 'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=35067558',
 'archived': False,
 'area': {'id': '1',
          'name': 'Москва',
          'url': 'https://api.hh.ru/areas/1?host=hh.ru'},
 'billing_type': {'id': 'standard_plus', 'name': 'Стандарт плюс'},
 'branded_description': '\n'
                        '<style type="text/css">\n'
                        '.wrap_hh-wrapper h1,\n'
                        '.wrap_hh-wrapper h2,\n'
                        '.wrap_hh-wrapper h3,\n'
                        '.wrap_hh-wrapper h4,\n'
                        '.wrap_hh-wrapper h5,\n'
                        '.wrap_hh-wrapper h6,\n'
                        '.wrap_hh-wrapper p,\n'
                        '.wrap_hh-wrapper blockquote,\n'
                        '.wrap_hh-wrapper pre,\n'
                        '.wrap_hh-wrapper a,\n'
                        '.wrap_hh-wrapper abbr,\n'
                        '.wrap_hh-wrapper acronym,\n'
                        '.wrap_hh-wrapper address,\n'
                        '.wrap_hh-wrapper big,\n'
                        '.wrap_hh-wrapper cite,\n'
                        '.wrap_hh-wrapper code,\n'
                        '.wrap_hh-wrapper img,\n'
                        '.wrap_hh-wrapper ol,\n'
                        '.wrap_hh-wrapper ul,\n'
                        '.wrap_hh-wrapper li,\n'
                        '.wrap_hh-wrapper footer,\n'
                        '.wrap_hh-wrapper header {\n'
                        '    margin: 0;\n'
                        '    padding: 0;\n'
                        '    border: 0;\n'
                        '    font-size: 100%;\n'
                        '    font: inherit;\n'
                        '    vertical-align: baseline;\n'
                        '}\n'
                        '\n'
                        '.wrap_hh-clear {\n'
                        '    clear: both;\n'
                        '}\n'
                        '\n'
                        '.wrap_hh-wrapper footer,\n'
                        '.wrap_hh-wrapper header {\n'
                        '    display: block;\n'
                        '}\n'
                        '\n'
                        '.hht-vacancydescription {\n'
                        '    padding: 0px;\n'
                        '}\n'
                        '\n'
                        '.wrap_hh-wrapper .l-cell,\n'
                        '.wrap_hh-wrapper .l-paddings {\n'
                        '    padding: 0px;\n'
                        '}\n'
                        '\n'
                        '.wrap_hh-wrapper .b-vacancy-desc-wrapper {\n'
                        '    margin-top: 0px;\n'
                        '}\n'
                        '\n'
                        '.b-vacancy-desc {\n'
                        '    overflow: visible;\n'
                        '}\n'
                        '\n'
                        '.wrap_hh_content ol li b,\n'
                        '.wrap_hh_content ol li strong,\n'
                        '.wrap_hh_content ol li p b,\n'
                        '.wrap_hh_content ol li p strong,\n'
                        '.wrap_hh_content ul li b,\n'
                        '.wrap_hh_content ul li strong,\n'
                        '.wrap_hh_content ul li p b,\n'
                        '.wrap_hh_content ul li p strong {\n'
                        '    font-weight: normal;\n'
                        '    font-size: inherit!important;\n'
                        '    color: inherit!important;\n'
                        '    margin: 0!important;\n'
                        '    text-transform: none;\n'
                        '}\n'
                        '\n'
                        '.wrap_hh_content ol li p,\n'
                        '.wrap_hh_content ul li p,\n'
                        '.wrap_hh-small .wrap_hh_content ol li p,\n'
                        '.wrap_hh-small .wrap_hh_content ul li p {\n'
                        '    font-weight: normal;\n'
                        '    margin: 0;\n'
                        '}\n'
                        '\n'
                        '.wrap_hh_content p b,\n'
                        '.wrap_hh_content p strong {\n'
                        '    display: inline;\n'
                        '    margin: 0;\n'
                        '}\n'
                        '\n'
                        '.wrap_hh-wrapper {\n'
                        '    width: 100%;\n'
                        '    max-width: 690px;\n'
                        '    position: relative;\n'
                        '    word-break: normal;\n'
                        '    margin: 0px auto;\n'
                        '    position: relative;\n'
                        '    overflow: hidden;\n'
                        "    font-family: 'Arial', sans-serif;\n"
                        '    color: #35363b;\n'
                        '    font-size: 15px;\n'
                        '    line-height: 18px;\n'
                        '}\n'
                        '\n'
                        '.wrap_hh_header img {\n'
                        '    display: block;\n'
                        '    width: 100%;\n'
                        '}\n'
                        '.wrap_hh_content {\n'
                        '    padding: 5.2% 18% 7.6%;\n'
                        '    border-bottom: 14px solid #00bcf1;\n'
                        '    letter-spacing: 0.18px;\n'
                        '}\n'
                        '\n'
                        '.wrap_hh_content p,\n'
                        '.wrap_hh_content b,\n'
                        '.wrap_hh_content strong {\n'
                        '    display: block;\n'
                        '    font-size: 15px;\n'
                        '    line-height: 18px;\n'
                        '    margin: 5.4% 0 1.6%;\n'
                        '}\n'
                        '\n'
                        '.wrap_hh_content b, \n'
                        '.wrap_hh_content strong {\n'
                        '    font-size: 20px;\n'
                        '    line-height: 24px;\n'
                        '    color: #08b3ec;\n'
                        '}\n'
                        '.wrap_hh_content p:first-child,\n'
                        '.wrap_hh_content b:first-child,\n'
                        '.wrap_hh_content strong:first-child {\n'
                        '    margin-top: 0;\n'
                        '}\n'
                        '.wrap_hh_content ul,\n'
                        '.wrap_hh_content ul ul {\n'
                        '    list-style: none;\n'
                        '}\n'
                        '\n'
                        '.wrap_hh_content ol,\n'
                        '.wrap_hh_content ul {\n'
                        '    margin-left: 2.1%;\n'
                        '}\n'
                        '\n'
                        '.wrap_hh_content ul li,\n'
                        '.wrap_hh_content ol li {\n'
                        '    position: relative;\n'
                        '    font-size: 15px;\n'
                        '    line-height: 18px;\n'
                        '    margin-bottom: 12px;\n'
                        '}\n'
                        '\n'
                        '.wrap_hh_content ul > li:before {\n'
                        '    content: "\\2022";\n'
                        '    position: absolute;\n'
                        '    left: -2.1%;\n'
                        '    top: 0px;\n'
                        '    color: #a5adb3;\n'
                        '    font-size: 15px;\n'
                        '}\n'
                        '\n'
                        '/*Small*/\n'
                        '\n'
                        '.wrap_hh-small {\n'
                        '    font-size: 13px;\n'
                        '    line-height: 16px;\n'
                        '}\n'
                        '.wrap_hh-small .wrap_hh_header {\n'
                        '}\n'
                        '.wrap_hh-small .wrap_hh_content {\n'
                        '    padding: 8.8% 9.5% 10.5%;\n'
                        '    border-width: 7px;\n'
                        '    letter-spacing: 0.04px;\n'
                        '}\n'
                        '\n'
                        '.wrap_hh-small .wrap_hh_content b,\n'
                        '.wrap_hh-small .wrap_hh_content strong,\n'
                        '.wrap_hh-small .wrap_hh_content p {\n'
                        '    font-size: 13px;\n'
                        '    line-height: 16px;\n'
                        '    margin: 8.1% 0 2.5%;\n'
                        '}\n'
                        '\n'
                        '.wrap_hh-small .wrap_hh_content b,\n'
                        '.wrap_hh-small .wrap_hh_content strong {\n'
                        '    font-size: 18px;\n'
                        '    line-height: 22px;\n'
                        '}\n'
                        '.wrap_hh-small .wrap_hh_content p:first-child,\n'
                        '.wrap_hh-small .wrap_hh_content b:first-child,\n'
                        '.wrap_hh-small .wrap_hh_content strong:first-child {\n'
                        '    margin-top: 0;\n'
                        '}\n'
                        '\n'
                        '.wrap_hh-small .wrap_hh_content ol,\n'
                        '.wrap_hh-small .wrap_hh_content ul {\n'
                        '    margin-left: 3%;\n'
                        '}\n'
                        '\n'
                        '.wrap_hh-small .wrap_hh_content ul li,\n'
                        '.wrap_hh-small .wrap_hh_content ol li {\n'
                        '    font-size: 13px;\n'
                        '    line-height: 16px;\n'
                        '    margin-bottom: 10px;\n'
                        '}\n'
                        '\n'
                        '.wrap_hh-small .wrap_hh_content ul > li:before {\n'
                        '    left: -3%;\n'
                        '    top: 0px;\n'
                        '    font-size: 12px;\n'
                        '}\n'
                        '</style>\n'
                        ' \n'
                        '\n'
                        ' \n'
                        '    <div class="wrap_hh-wrapper wrap_hh-small">\n'
                        '        <div class="wrap_hh_header">\n'
                        '            <img '
                        'src="https://hhcdn.ru/ichameleon/132738.jpg" alt="">\n'
                        '        </div>\n'
                        '        <div class="wrap_hh_content">\n'
                        '\n'
                        '                    <p><strong>Кто мы:</strong></p> '
                        '<p>Мы – команда МоегоСклада. Уже больше 10 лет '
                        'развиваем и продаем веб-сервис, упрощающий жизнь '
                        'малому и среднему бизнесу. Помогаем вести складской '
                        'учет, управлять продажами и закупками, печатать '
                        'необходимые для ведения бизнеса документы.</p> <p>У '
                        'нас налажен и постоянно развивается процесс '
                        'разработки. Сделанные в первый день работы тикеты '
                        'могут уже завтра быть на проде. Продукт большой и '
                        'сложный, пользователи активно делятся пожеланиями. Мы '
                        'придумываем как реализовать полезный для людей '
                        'продукт – и делаем.</p> <p><strong>Кто '
                        'вы:</strong></p> <ul> <li> <p>Пишете на Java уже '
                        'больше полугода</p> </li> <li> <p>Знаете алгоритмы и '
                        'структуры данных</p> </li> <li> <p>Умеете писать '
                        'SQL-запросы</p> </li> <li> <p>Идеально, если работали '
                        'с EJB</p> </li> </ul> <p><strong>У нас '
                        'вы:</strong></p> <ul> <li> <p>Будете добавлять новые '
                        'и улучшать существующие функции сервиса: простой и '
                        'удобный интерфейс для продавцов, графики и аналитику '
                        'для руководителей (основной стек технологий: WildFly, '
                        'EJB, Hibernate, PostgreSQL) и писать интеграционные '
                        'тесты</p> </li> <li> <p>Будете разрабатывать '
                        'клиентскую часть веб-приложения (пользовательский '
                        'интерфейс и бизнес-логику) при помощи GWT и '
                        'UI-тесты</p> </li> </ul> <p><strong>Что '
                        'еще:</strong></p> <ul> <li> <p>Оформляем по ТК РФ с '
                        'первого дня</p> </li> <li> <p>Платим зарплату 100-140 '
                        'тысяч рублей (после налогов, на руки)</p> </li> <li> '
                        '<p>Обеспечиваем ультимативно гибкое начало рабочего '
                        'дня</p> </li> <li> <p>Заботимся о вашем комфорте в '
                        'нашем офисе в пяти минутах от метро Технопарк</p> '
                        '</li> <li> <p>Дарим фирменный мерч (футболки, '
                        'толстовки, кружки с собаками, и т.д.)</p> </li> <li> '
                        '<p>Терпим бюрократию только в виде заявлений на '
                        'отпуск и компенсацию обучения</p> </li> <li> '
                        '<p>Компенсируем оплату обедов и закупаем фрукты в '
                        'офис</p> </li> <li> <p>Компенсируем оплату обучения '
                        'по профилю и выдаем лицензию IDEA</p> </li> <li> '
                        '<p>И, конечно, подключаем к ДМС после окончания '
                        'испытательного срока</p> </li> </ul></div>\n'
                        '\n'
                        '        <div class="wrap_hh-clear">\n'
                        '            <!-- fix -->\n'
                        '        </div>\n'
                        '    </div>\n'
                        ' \n',
 'code': None,
 'contacts': None,
 'created_at': '2019-12-19T18:16:35+0300',
 'department': None,
 'description': '<p><strong>Кто мы:</strong></p> <p>Мы – команда МоегоСклада. '
                'Уже больше 10 лет развиваем и продаем веб-сервис, упрощающий '
                'жизнь малому и среднему бизнесу. Помогаем вести складской '
                'учет, управлять продажами и закупками, печатать необходимые '
                'для ведения бизнеса документы.</p> <p>У нас налажен и '
                'постоянно развивается процесс разработки. Сделанные в первый '
                'день работы тикеты могут уже завтра быть на проде. Продукт '
                'большой и сложный, пользователи активно делятся пожеланиями. '
                'Мы придумываем как реализовать полезный для людей продукт – и '
                'делаем.</p> <p><strong>Кто вы:</strong></p> <ul> <li> '
                '<p>Пишете на Java уже больше полугода</p> </li> <li> '
                '<p>Знаете алгоритмы и структуры данных</p> </li> <li> '
                '<p>Умеете писать SQL-запросы</p> </li> <li> <p>Идеально, если '
                'работали с EJB</p> </li> </ul> <p><strong>У нас '
                'вы:</strong></p> <ul> <li> <p>Будете добавлять новые и '
                'улучшать существующие функции сервиса: простой и удобный '
                'интерфейс для продавцов, графики и аналитику для '
                'руководителей (основной стек технологий: WildFly, EJB, '
                'Hibernate, PostgreSQL) и писать интеграционные тесты</p> '
                '</li> <li> <p>Будете разрабатывать клиентскую часть '
                'веб-приложения (пользовательский интерфейс и бизнес-логику) '
                'при помощи GWT и UI-тесты</p> </li> </ul> <p><strong>Что '
                'еще:</strong></p> <ul> <li> <p>Оформляем по ТК РФ с первого '
                'дня</p> </li> <li> <p>Платим зарплату 100-140 тысяч рублей '
                '(после налогов, на руки)</p> </li> <li> <p>Обеспечиваем '
                'ультимативно гибкое начало рабочего дня</p> </li> <li> '
                '<p>Заботимся о вашем комфорте в нашем офисе в пяти минутах от '
                'метро Технопарк</p> </li> <li> <p>Дарим фирменный мерч '
                '(футболки, толстовки, кружки с собаками, и т.д.)</p> </li> '
                '<li> <p>Терпим бюрократию только в виде заявлений на отпуск и '
                'компенсацию обучения</p> </li> <li> <p>Компенсируем оплату '
                'обедов и закупаем фрукты в офис</p> </li> <li> '
                '<p>Компенсируем оплату обучения по профилю и выдаем лицензию '
                'IDEA</p> </li> <li> <p>И, конечно, подключаем к ДМС после '
                'окончания испытательного срока</p> </li> </ul>',
 'driver_license_types': [],
 'employer': {'alternate_url': 'https://hh.ru/employer/208576',
              'id': '208576',
              'logo_urls': {'240': 'https://hhcdn.ru/employer-logo/2875813.png',
                            '90': 'https://hhcdn.ru/employer-logo/2875812.png',
                            'original': 'https://hhcdn.ru/employer-logo-original/608665.png'},
              'name': 'МойСклад',
              'trusted': True,
              'url': 'https://api.hh.ru/employers/208576?host=hh.ru',
              'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=208576&host=hh.ru'},
 'employment': {'id': 'full', 'name': 'Полная занятость'},
 'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'},
 'has_test': False,
 'hidden': False,
 'id': '35067558',
 'insider_interview': None,
 'key_skills': [{'name': 'Java'},
                {'name': 'Java EE'},
                {'name': 'SQL'},
                {'name': 'PostgreSQL'}],
 'name': 'Младший Java разработчик',
 'negotiations_url': None,
 'premium': False,
 'published_at': '2019-12-19T18:16:35+0300',
 'quick_responses_allowed': False,
 'relations': [],
 'response_letter_required': False,
 'response_url': None,
 'salary': {'currency': 'RUR', 'from': 100000, 'gross': False, 'to': 140000},
 'schedule': {'id': 'fullDay', 'name': 'Полный день'},
 'site': {'id': 'hh', 'name': 'hh.ru'},
 'specializations': [{'id': '1.221',
                      'name': 'Программирование, Разработка',
                      'profarea_id': '1',
                      'profarea_name': 'Информационные технологии, интернет, '
                                       'телеком'}],
 'suitable_resumes_url': None,
 'test': None,
 'type': {'id': 'open', 'name': 'Открытая'},
 'vacancy_constructor_template': None}


class HHParser_TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.hh_parser = hhparser_description.HHParserDescription()
        self.hh_parser._s_description = j_test['description']

    def test_clean_html(self):
        self.hh_parser._clean_html()
        self.assertEqual(-1, self.hh_parser._s_description.find("<"))
        self.assertEqual(-1, self.hh_parser._s_description.find(">"))

    def test_clean_trash(self):
        self.hh_parser._clean_html()
        self.hh_parser._clean_trash()
        self.assertEqual(1536, len(self.hh_parser._s_description))

    def test_find_technology(self):
        self.hh_parser._clean_html()
        self.hh_parser._clean_trash()
        self.hh_parser._find_technology()
        self.assertEqual(2, len(self.hh_parser._l_found_technology))


if __name__ == '__main__':
    unittest.main()
