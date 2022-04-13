import requests
from bs4 import BeautifulSoup
import json


url = "https://en.wikipedia.org/wiki/History_of_Mexico"


def fixed(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    all_passages = soup.find("p")  # returns a list of all paragraphs

    cited_passages = all_passages.find_all("sup", class_ = "reference")  # returns a list of cited paragraphs

    uncited_list = []
    for passage in all_passages:
        if passage not in cited_passages:
            uncited_list.append(passage.get_text())

    return uncited_list


"""
This function will return an integer of number of passages that need citation in the url.
"""
def get_citations_needed_count(url):
    data = fixed(url)

    uncited_passages = len(data)

    return uncited_passages



"""
This function will return a formatted string of each uncited passage in the right order.
"""
def get_citations_needed_report(url):
    data = fixed(url)

    # array = []
    for i in data:
        print(f"citation is needed for: '{i}' passage")
        print("_"*50)

 

    # with open("uncited_passages.json", "w") as f:
    #     content = json.dumps(array)
    #     f.write(content)
    


if __name__ == "__main__":
    print(get_citations_needed_count(url))
    get_citations_needed_report(url)
