
import requests

from bs4 import BeautifulSoup


URL ="https://en.wikipedia.org/wiki/History_of_Mexico"

def get_citations_needed_count(URL):

    page = requests.get(URL)

    soup = BeautifulSoup(page.content,'html.parser')

    all_results = soup.find_all('a', title = 'Wikipedia:Citation needed')

    return len(all_results)



def get_citations_needed_report(URL):

    page = requests.get(URL)

    soup = BeautifulSoup(page.content,'html.parser')

    all_results = soup.find_all('a', title = 'Wikipedia:Citation needed')

    all_results_clean = []


    for result in all_results:
        all_results_clean.append(f'Citation : {result.parent.parent.parent.text}')
        

    return (all_results_clean)




import json

file_content = json.dumps(get_citations_needed_report(URL))
with open('all_results_clean.json', 'w') as file:
    file.write(file_content)
    




print(get_citations_needed_count(URL))
print(get_citations_needed_report(URL))