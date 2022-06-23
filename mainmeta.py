from bs4 import BeautifulSoup
import requests
import random

url_link = 'https://belmeta.com'
vac_lst = []

#````````````````````````````````````````````````````````````````````
def resp(url):
    global vacancy
    timeout = random.randint(0,5)
    resp = requests.get(url, timeout)
    soup = BeautifulSoup(resp.text, 'lxml')
    vacancy = soup.find_all('article', class_=('job','job no-logo'))

    for j in vacancy:
        global vac_detail
        vac_detail = {}

# город вакансии
        city = j.find('div', class_='job-data region').get_text().strip()
        vac_detail['город'] = city
# имя вакансии и добавление ее в словарь
        name_vac = j.find('div', class_='title-wrap').get_text().strip()
        vac_detail['название_вакансии'] = name_vac
# название компании
        company = j.find('div', class_='job-data company').get_text().strip()
        vac_detail['компания'] = company
# размер зарплаты
        try:
            salary = j.find('div', class_='job-data salary').get_text().strip()
            vac_detail['зарплата'] = salary
        except Exception as e:
            vac_detail['зарплата'] = 'заработная плата не указана'
# краткое описание вакансии
        try:
            description = j.find('div', class_='desc').get_text().strip()
            vac_detail['описание_вакансии'] = description
        except Exception as e:
            vac_detail['описание_вакансии'] = 'описание отсутствует'

# все добавляем в список
        vac_lst.append(vac_detail)

# на печать все вакансии
    for i in vac_lst:
        print('`' * 70)
        for key, value in i.items():
            print(key, ':', value)

#````````````````````````````````````````````````````````````````````
def city_vac():
# парсим вакансии по городам, ввод от пользователя
    while True:
        print()
        user_city = input('Введите название города >>> ').strip()
        time_vac = input('''    Введите время размещения вакансии,
    1 за 24 часа
    3 за 3 дня
    7 за 7 дней
    ```````````````````````````````````````
    9.Выход в главное меню
>>> ''').strip()
        if time_vac == '9':
            break
        else:
            url_link = 'https://belmeta.com/vacansii?q=&l=' + user_city + '&df=' + time_vac
            resp(url_link)

#````````````````````````````````````````````````````````````````````
def catalog_vac():
    pass

#````````````````````````````````````````````````````````````````````
def type_vac():
    pass

#````````````````````````````````````````````````````````````````````
def popular_vac():
    pass

#```меню`````````````````````````````````````````````````````````````
def main():
    while True:
        print('''   Тип поиска вакансий:
    1.Вакансии по городам
    2.Вакансии по рубрикам (в процессе)
    3.Вакансии по типам (в процессе)
    4.Популярные вакансии (в процессе)
    ```````````````````````````````````````
    9.Выход из программы
''')
        user_option = input('>>> ')
        if user_option == '1':
            city_vac()
        elif user_option == '2':
            catalog_vac()
        elif user_option == '3':
            type_vac()
        elif user_option == '4':
            popular_vac()

        elif user_option == '9':
            break

#````````````````````````````````````````````````````````````````````
if __name__ == "__main__":
    main()
    