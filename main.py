import sys

import pyuseragents
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://stackoverflow.com/"
QUESTIONS_PYTHON_TAG = 'questions/tagged/python'
resp = requests.get(BASE_URL + QUESTIONS_PYTHON_TAG)
status = resp.status_code
soup = BeautifulSoup(resp.text, parser='lxml')
all_questions = soup.find('div', id='questions')
list_with_questions = all_questions.find_all('div', class_='s-post-summary--content')
#zagolovok_list_with_questions = list_with_questions.find_all('')

for i in list_with_questions:
    print(i.find('h3',class_="s-post-summary--content-title").text)


#
# print(list_with_questions)
# print()
# print(len(list_with_questions))