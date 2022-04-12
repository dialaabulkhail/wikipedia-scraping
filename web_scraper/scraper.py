import requests
from bs4 import BeautifulSoup
import json


url = "https://en.wikipedia.org/wiki/History_of_Mexico"

"""
This function will return an integer of number of passages that need citation in the url.
"""
def get_citations_needed_count(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    all_passages = soup.find("p")  # returns a list of all paragraphs

    cited_passages = all_passages.find_all("sup", class_ = "reference")  # returns a list of cited paragraphs

    uncited_list = []
    for passage in all_passages:
        if passage not in cited_passages:
            uncited_list.append(passage.get_text())

    uncited_passages = len(uncited_list)

    return uncited_passages



"""
This function will return a formatted string of each uncited passage in the right order.
"""
def get_citations_needed_report(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    all_passages = soup.find("p")  

    cited_passages = all_passages.find_all("sup", class_ = "reference")  

    uncited_list = []
    for passage in all_passages:
        if passage not in cited_passages:
            uncited_list.append(passage.get_text())

    array = []
    for i in uncited_list:
        array.append(f"citation needed for '{i}' passage")

    with open("uncited_passages.json", "w") as f:
        content = json.dumps(array)
        f.write(content)
    


if __name__ == "__main__":
    # print(get_citations_needed_count(url))
    print(get_citations_needed_report(url))
