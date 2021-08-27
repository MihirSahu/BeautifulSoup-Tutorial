#This scrapes home.html

#Install beautiful soup and lxml
from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml') #To see soup object in easy to read format use soup.prettify()
    course_cards = soup.find_all('div', class_='card') #use .find() to find first instance of specified tag, .find_all() to find all specified tags

    for courses in course_cards:
        course_name = courses.h5.text
        course_price = courses.a.text.split()[-1]

        print('{name} costs {price}'.format(name=course_name, price=course_price))