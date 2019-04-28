# ДЗ. Урок 3. Применение объектов в работе с вебом
# 1. Написать функцию получения IATA-кода города из его названия, используя API Aviasales.
from json import loads              # импортируем loads из json
from requests import get      		# импортируем метод get из модуля requests
from googletrans import Translator  # импортируем Translator из googletrans для определения языка введённого текста
                                    # Подробности здесь https://pypi.org/project/googletrans/

def iata_code_city(city):
    translator = Translator()
    langv = translator.detect(city).lang # определяем язык, ниже формируем ссылку
    link = f'http://autocomplete.travelpayouts.com/places2?term={city}&locale={langv}&types[]=city'
    web_page = get(link)       # с помощью метода get() отправляем get запрос на страницу по адресу link
    page_text = web_page.text  # получаем текст веб-страницы
    city_data = loads(page_text) # заргужаем данные JSON формата в city_data
    if city_data: # если есть данные в city_data, то ниже получаем список iata кодов
        iata_list = [city_dict['code'] for city_dict in city_data if city_dict['name'].lower() == city.lower()]
        if iata_list:                           # если список iata кодов не пуст
            return '%s' % ', '.join(iata_list)  # возвращаем 1 код или несколько через запятую
    else:
        return None # если нет данных в city_data - [], то возвращаем None
    return None     # если ничего не найдено, то возвращаем None


if __name__ == '__main__':
    print('Получение IATA-кода города из его названия, используя API Aviasales.')
    print('Поддерживаемые языки / Supported Languages: ar, bg, cs, da, de, el, en, es, fa, fi, fr, he, hi, hr,')
    print('hu, id, it, ja, ka, ko, lt, lv, ms, nl, no, pl, pt, ro, ru, sk, sl, sr, sv, th, tl, tr, uk, vi.')
    print('Рекомендуемые языки / Recommended Languages: ru, en.')
    city_name = input('Введите название города / Enter the name of the city: ')
    print(f'IATA-код города / IATA-city code:                     {iata_code_city(city_name)}')