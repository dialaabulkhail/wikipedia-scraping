from web_scraper.scraper import get_citations_needed_count, get_citations_needed_report

def test_citations_count():
    url = ("https://en.wikipedia.org/wiki/History_of_Mexico")
    assert 24 == get_citations_needed_count(url)


def test_preceding_passage():
    url = ("https://en.wikipedia.org/wiki/History_of_Mexico")
    arr = ['The written ', 'history of Mexico', ' spans more than three millennia. First populated more than 13,000 years ago,', ' central and southern Mexico (termed ', 'Mesoamerica', ') saw the rise and fall of complex ', 'indigenous', ' civilizations. Mexico would later develop into a unique multicultural society. ', 'Mesoamerican', ' civilizations developed glyphic ', 'writing systems', ', recording the political history of conquests and rulers. Mesoamerican history prior to European arrival is called the prehispanic era or the ', 'pre-Columbian era', '. Following ', "Mexico's independence", ' from ', 'Spain', ' in 1821, political turmoil wracked the nation.  ', 'France', ', with the help of Mexican conservatives, seized control in the 1860s during the ', 'Second Mexican Empire', ', but was later defeated. Quiet prosperous growth was characteristic in the late 19th century but the ', 'Mexican Revolution', ' in 1910 brought a bitter civil war. With calm restored in the 1920s, economic growth was steady while population growth was rapid.\n']
    assert arr == get_citations_needed_report(url)
