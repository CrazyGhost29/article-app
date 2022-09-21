from mailbox import linesep
import requests
from bs4 import BeautifulSoup

test_url = 'https://www.focus.de/panorama/welt/abschied-queen/aktuelle-entwicklungen-im-newsticker-harry-feiert-traurigen-geburtstag-mega-operation-vor-queen-begraebnis_id_142949737.html'
test_url2 = 'https://medium.com/a-microbiome-scientist-at-large/why-cant-babies-drink-water-13b22c7ac721'
test_url3 = 'https://www.transfermarkt.de/mazraoui-bdquo-war-ein-sehr-guter-start-von-mir-beim-fc-bayern-ldquo-ndash-spielte-264-von-900-minuten/view/news/411376'
test_url4 = 'https://venturebeat.com/security/report-password-fatigue-compromises-employee-productivity-security-and-well-being/'


class TextScraper:

    def __init__(self):
        pass

    def getdata(self, url):
        r = requests.get(url)
        htmldata = r.text
        soup = BeautifulSoup(htmldata, 'html.parser')
        scraped_lines = []
        if soup.find('div', {"class":"article-content"}) is not None:
            for data in soup.find('div', {"class":"article-content"}).find_all("p" or "b", recursive = False):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
        
        elif soup.find('div', {"itemprop":"articleBody"}) is not None:
            for data in soup.find('div', {"itemprop":"articleBody"}).find_all(text = True, recursive = False):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
        
        elif soup.find('article', {"class":"inf-article-detail"}) is not None:
            for data in soup.find('article', {"class":"inf-article-detail"}).find_all('p', {"class":"inf-text--medium-sec"}, recursive = False):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)

        
        #print("\n\n".join(scraped_lines))
            
        return "\n".join(scraped_lines)


#TextScraper.getdata(TextScraper, 'https://venturebeat.com/security/report-u-s-businesses-experience-42-cyberattacks-per-year/')