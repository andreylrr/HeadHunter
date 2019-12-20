import unittest
import hhparser

s_test = "<p><strong>Middle Java Developer на проект разработки платформы  BPS(bpsuite.com).</strong></p> <p>Компания <strong>Astarus</strong> \
 занимается разработкой ПО, основным направлением компании является \
 разработка бизнес решений на платформе Java/ Spring + SAP. За время работы \
 мы разработали ПО, которым уже пользуются такие компании как Авиакомпания \
 SWISS, Lufthansa, SwissPost, British Telecommunications, Starbucks, \
 Университет Цюриха и другие.</p> <p>В связи с развитием Компании и \
 увеличением количества проектов будем рады рассмотреть Middle \
 Java-разработчиков в нашу дружную команду.</p> <p><strong>В кандидатах нам \
  интересно:</strong><br />1. Опыт разработки на Java 8 от 2-х лет;</p> <p>2.\
 Твердые знания и опыт работы со Spring, ORM (Hibernate), JPA, JSTL, JSP;</p>\
 <p>3. Опыт работы с реляционными БД (MS SQL);</p> <p>4. Хорошие знания HTML, \
  CSS, Jаvаsсriрt (библиотека JQuery);</p> <p>5. Умение давать оценку \
 трудозатрат;</p> <p>6. Умение выполнять разработку в выбранный срок;</p> \
 <p>7. Понимание вопросов безопасности при разработке Web-приложений;</p> \
 <p>8. Умение составлять документацию на программный продукт.</p> \
 <p><strong>Будет плюсом:</strong><br />Владение английским языком на уровне\
 чтения документации и ведения переписки.</p> <p><strong>Мы \
 предлагаем:</strong></p> <p><strong>✔ </strong>Интересную для Вас заработную\
  плату в виде оклада + квартальные премии по результатам работы на \
 проекте;</p> <p><strong>✔</strong> Корпоративное обучение английскому языку, \
 стажировки, онлайн-конференции, курсы повышения квалификации и участие в \
 крупных профильных конференциях;</p> <p><strong>✔</strong> Работу в уютном и \
 стильном офисе в центральной части города (БЦ &quot;Парус Плаза&quot;);</p> \
 <p><strong>✔</strong> Комфортные условия работы: 2 монитора, мягкие кресла, \
 кондиционер, комната отдыха, настольный теннис и тренажеры, полностью \
 оборудованная удобная кухня;</p> <p><strong>✔</strong> График работы 5 дней \
 в неделю 8 часов в день;</p> <p><strong>✔</strong> Добровольное медицинское \
 страхование с возможностью оплаты стоматологии и фитнес-клуба;</p> \
 <p><strong>✔</strong> Отличный коллектив и разнообразные корпоративные \
 мероприятия.</p>"


class HHParser_TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.hh_parser = hhparser.HHParser()
        self.hh_parser._s_description = s_test

    def test_clean_html(self):
        self.hh_parser._clean_html()
        self.assertEqual(-1, self.hh_parser._s_description.find("<"))
        self.assertEqual(-1, self.hh_parser._s_description.find(">"))

    def test_clean_trash(self):
        self.hh_parser._clean_html()
        self.hh_parser._clean_trash()

    def test_find_technology(self):
        self.hh_parser._clean_html()
        self.hh_parser._clean_trash()
        self.hh_parser._find_technology()
        self.assertEqual(12, len(self.hh_parser._l_found_technology))


if __name__ == '__main__':
    unittest.main()
