from web_scraper.scraper import get_citations_needed_count

def test_citations_count():
    url = ("https://en.wikipedia.org/wiki/History_of_Mexico")
    assert 24 == get_citations_needed_count(url)
