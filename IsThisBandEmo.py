from bs4 import BeautifulSoup
import requests

def check_is_emo(artist_name):

    resp = requests.get("http://isthisbandemo.com/?band={}".format(artist_name.replace(' ','+')))
    # print(resp.text)

    soup = BeautifulSoup(resp.text, 'html.parser')

    # Find all links on the page
    all_divs = soup.find_all('div')
    for div in all_divs:
        if div.get("class"):
            if div.get("class")[0] == "results":
                header_tag = div.find('h2')
                if header_tag:
                    emo_result = header_tag.text
    if emo_result is None:
        raise ValueError("emo_result is NULL")
        return None
    else:
        return emo_result

print(check_is_emo("primus"))