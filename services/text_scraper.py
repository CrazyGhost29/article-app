from mailbox import linesep
import requests
from bs4 import BeautifulSoup

test_url = 'https://www.focus.de/panorama/welt/abschied-queen/aktuelle-entwicklungen-im-newsticker-harry-feiert-traurigen-geburtstag-mega-operation-vor-queen-begraebnis_id_142949737.html'
test_url2 = 'https://medium.com/a-microbiome-scientist-at-large/why-cant-babies-drink-water-13b22c7ac721'

class TextScraper:

    def __init__(self):
        pass

    def getdata(self, url):
        r = requests.get(url)
        htmldata = r.text
        soup = BeautifulSoup(htmldata, 'html.parser')
        scraped_lines = []
        for data in soup.find_all('p'):
            raw = data.get_text()
            refined_l = raw.lstrip()
            refined_r = refined_l.rstrip()
            refined_space = refined_r.replace("  ", "")
            if len(refined_space.split()) > 5:
                #print("***: "+refined_space)
                scraped_lines.append(refined_space)
        
        print(type("\n".join(scraped_lines)))
            
        return "\n".join(scraped_lines)


#TextScraper.getdata(TextScraper, test_url2)