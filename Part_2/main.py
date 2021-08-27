#install beautifulsoup, lxml, and requests
from bs4 import BeautifulSoup
import requests

#Scrape the results shown when searching 'python' on timesjobs.com

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text #This only retrieves the text from the website

soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

for job in jobs:
    company_name = job.find('h3', class_= 'joblist-comp-name').text
    skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
    published_date = job.find('span', class_ = 'sim-posted').span.text

    print('''
        Company name: {name}
        Skills needed: {skill}
        Date published: {date}
    '''.format(name=company_name, skill=skills, date=published_date))