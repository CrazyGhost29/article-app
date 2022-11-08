import requests
from bs4 import BeautifulSoup

test_url = 'https://www.heise.de/news/Stable-Diffusion-Stability-AI-auf-Kurs-mit-101-Millionen-US-Dollar-Finanzierung-7313243.html'
test_url2 = 'https://medium.com/a-microbiome-scientist-at-large/why-cant-babies-drink-water-13b22c7ac721'
test_url3 = 'https://www.pressebox.de/pressemitteilung/cosys-ident-gmbh/digitalisierung-der-logistik-mit-mobilen-scannern/boxid/1133995'
test_url4 = 'https://venturebeat.com/security/report-password-fatigue-compromises-employee-productivity-security-and-well-being/'
test_url5 = 'https://www.bigdata-insider.de/5-tipps-um-ein-unternehmen-ki-ready-zu-machen-a-2097e733d0a1af77fa479439ce70a534/'
test_url6 = 'https://www.inpactmedia.com/karriere/arbeitswelt-der-zukunft/hybrides-arbeiten-win-win-situation-fuer-alle'
test_url7 = 'https://www.behoerden-spiegel.de/2022/10/21/non-visible-data-gewinnt-nato-innovation-challenge/'
test_url8 = 'https://omr.com/de/daily/diese-ki-systeme-veraendern-die-welt-der-bilder-fuer-immer-und-damit-auch-das-marketing/'
# REQUEST UNSUCCESSFUL test_url9 = 'https://t3n.de/news/stable-diffusion-ki-kritik-1507584/'
test_url10 = 'https://1e9.community/t/microsoft-soll-wegen-einer-programmier-ki-verklagt-werden-die-mit-open-source-code-trainiert-wurde/18127'
test_url11 = 'https://techcrunch.com/2022/10/20/generally-intelligent-secures-cash-from-openai-vets-to-build-capable-ai-systems/?guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmRlLw&guce_referrer_sig=AQAAAH6oYtHGron4VRxizrj96Fujg4mazdhmMRkSuCb76zXRQZVD1-JRZCA8zKdShCPfKRu5iY9LWnGhk28WwIaRqsAOmpQ_pbP3N_EnUoLe9zSuP_xzm1imx9eFPdh8BEn40Di7lRh0lJGP5CmBoITYTPqQf_-E5zuYydE6ytMANH3e&guccounter=2'
test_url12 = 'https://www.marktechpost.com/2022/10/21/microsoft-ai-research-introduces-deepspeed-mii-a-new-open-source-python-library-from-deepspeed-that-speeds-up-20000-widely-used-deep-learning-models/'
test_url13 = 'https://www.it-zoom.de/dv-dialog/e/big-data-integration-31379/'
# PAYWALL test_url14 = 'https://www.handelsblatt.com/technik/it-internet/insight-innovation-der-moerder-und-sein-digitaler-zwilling-wie-neue-technologie-verbrecher-jagt/28754514.html'
test_url15 = 'https://www.windkraft-journal.de/2022/10/19/fugro-liefert-rwe-geodaten-vom-geplanten-offshore-windpark-dogger-bank-sued/180730'
test_url16 = 'https://www.meinbezirk.at/graz/c-wirtschaft/mit-geodaesie-wird-man-zum-klimawandel-spezialist_a5631211'
test_url17 = 'https://www.security-insider.de/so-funktioniert-devsecops-fuer-sap-a-ba98d03cb2e4158ba6318f0711b27aa8/'
test_url18 = 'https://enterprisersproject.com/article/2022/10/digital-transformation-mlops-best-practices'
test_url19 = 'https://www.computerweekly.com/blog/CW-Developer-Network/API-series-OctoML-ML-APIs-need-to-take-a-lesson-from-their-ancestors'
test_url20 = 'https://www.wiwo.de/technologie/digitale-welt/software-wachstum-in-der-cloud-sap-uebertrifft-die-erwartungen-der-analysten/28765820.html'
test_url21 = 'https://analyticsindiamag.com/can-text-to-image-ai-learn-ethics-or-is-the-future-doomed%EF%BF%BC/'
test_url22 = 'https://www.infoq.com/news/2022/08/meta-blenderbot3-chatbot/'
test_url23 = 'https://www.kdnuggets.com/2022/08/benefits-natural-language-ai-content-creators.html'
test_url24 = 'https://www.kommune21.de/meldung_39436_gn'
test_url25 = 'https://www.volksfreund.de/pr/presseportal/wgic-unterstuetzt-intergeo-als-strategischer-partner_aid-75900063'
# REQUEST UNSUCCESSFUL test_url26 = 'https://www.golem.de/news/anzeige-data-engineering-und-data-science-mit-python-2208-167872.html'
test_url27 = 'https://uelzener-presse.de/2022/08/26/wie-kann-man-sich-auf-data-analytics-umorientieren/'
test_url28 = 'https://www.unite.ai/machine-learning-vs-data-science-key-differences/'
test_url29 = 'https://www.springerprofessional.de/reporting/investor-relations/esap-plattform-fuer-unternehmensdaten-startet-erst-2026/23369244'
test_url30 = 'https://www.saarbruecker-zeitung.de/pr/presseportal/teradata-stellt-vantagecloud-lake-vor_aid-75960389'
test_url31 = 'https://www.cloudcomputing-insider.de/was-ist-azure-global-infrastructure-a-aed226e32dbcb7e9a556ccc4982f335c/'
test_url32 = 'https://www.boersennews.de/nachrichten/artikel/dgap-news-bwi-optimiert-sap-nutzung-mit-usu-software-asset-management/3850711/'
test_url33 = ''
test_url34 = ''
test_url35 = ''
test_url36 = ''
test_url37 = ''
test_url38 = ''
test_url39 = ''
test_url40 = ''
test_url41 = ''
test_url42 = ''


class TextScraper:

    def __init__(self):
        pass

    def getdata(self, url):
        r = requests.get(url)
        htmldata = r.text
        #print(htmldata)
        soup = BeautifulSoup(htmldata, 'html.parser')
        scraped_lines = []
        #1
        if "heise.de" in url:
            for data in soup.find('div', {"class":"article-content"}).find_all("p" or "b", recursive = False):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "Heise"
            title = soup.find('h1', class_='a-article-header__title').get_text(strip=True)
        #2
        elif "pressebox.de" in url:
            for data in soup.find('div', {"itemprop":"articleBody"}).find_all(text = True, recursive = False):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "Pressebox"
            title = soup.find('h1', class_='cmb-10').get_text(strip=True)
        #3
        elif "bigdata-insider.de" in url:
            for data in soup.find('article', {"class":"inf-article-detail"}).find_all('p', {"class":"inf-text--medium-sec"}, recursive = False):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "Bigdata Insider"
            title = soup.find('span', class_='inf-no-margin').get_text(strip=True)
        #4
        elif "venturebeat.com" in url:
            for data in soup.find('div', {"class":"article-content"}).find_all("p", recursive=False):
                if data.em:
                    continue
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "Venturebeat"
            title = soup.find('h1', class_='article-title').get_text(strip=True)
        #5
        elif "medium.com" in url: # auf not membership testen
            for data in soup.find('div', class_='hz ia ib ic id').find_all("p", class_="pw-post-body-paragraph", recursive=False):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "Medium"
            title = soup.find('div', class_='hz ia ib ic id').div.find('h1', class_='pw-post-title').get_text(strip=True)
        #6
        if "inpactmedia.com" in url:
            for data in soup.find('div', {"class":"text-content"}).find_all("p", recursive = False):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "Inpactmedia"
            title = soup.find('h1', class_='page-title').get_text(strip=True)
        #7
        if "behoerden-spiegel.de" in url:
            for data in soup.find('div', {"class":"td-post-content"}).find_all("p", recursive = False):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "Behörden Spiegel"
            title = soup.find('h1', class_='entry-title').get_text(strip=True)
        #8
        if "omr.com" in url:
            for data in soup.find('div', {"class":"post-content"}).find_all("p", recursive = False):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "OMR"
            title = soup.find('h1', class_='text-h3').get_text(strip=True)
        #9 --- der Request kommt an den cookie einstellungen nicht vorbei
        if "t3n.de" in url:
            scraped_lines = ["REQUEST UNSUCCESSFUL"]
            domain = "t3n"
            title = "None"
            print("Titel: " + title)
        #10
        if "1e9.community" in url:
            for data in soup.find_all("p")[:-2]:
                if data.em:
                    continue
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "1E9 Community"
            title = soup.find('h1').get_text(strip=True)
        #11
        if "techcrunch.com" in url:
            for data in soup.find('div', {"class":"article-content"}).find_all("p", recursive = False):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "TechCrunch"
            title = soup.find('h1', class_='article__title').get_text(strip=True)
            print("Titel: " + title)
        #12
        if "marktechpost.com" in url:
            for data in soup.find('div', {"class":"td-post-content"}).find_all("p", recursive = False):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "MARKTECHPOST"
            title = soup.find('div', class_='td-post-header').find('h1').get_text(strip=True)
            print("Titel: " + title)
        #13
        if "it-zoom.de" in url:
            for data in soup.find('div', class_="news-text-wrap").find_all("p", class_="bodytext"):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "IT-ZOOM"
            title = soup.find('h1', itemprop='headline').get_text(strip=True)
            print("Titel: " + title)
        #14 --- PAYWALL
        if "handelsblatt.com" in url:
            scraped_lines = ["PAYWALL"]
            domain = "Handelsblatt"
            title = soup.find('span', class_='vhb-headline--onecolumn').get_text(strip=True)
            print("Titel: " + title)
        #15 --- Text Deutsch und englisch...
        if "windkraft-journal.de" in url:
            for data in soup.find('div', class_="post_content").find_all("p", recursive=False):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "Windkraft-Journal"
            title = soup.find('h1', class_='entry-title').get_text(strip=True)
            print("Titel: " + title)
        #16
        if "meinbezirk.at" in url:
            for data in soup.find('div', id='content-main').find_all("p", recursive=True)[:-3]:
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "MeinBezirk.at"
            title = soup.find('h1').get_text(strip=True)
            print("Titel: " + title)
        #17
        elif "security-insider.de" in url:
            for data in soup.find('article', {"class":"inf-article-detail"}).find_all('p', {"class":"inf-text--medium-sec"}, recursive = False):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "Security Insider"
            title = soup.find('span', class_='inf-no-margin').get_text(strip=True)
            print("Titel: " + title)
        #18
        elif "enterprisersproject.com" in url:
            for data in soup.find('div', {"class":"text-formatted"}).find_all('p', recursive = False):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "The Enterprises Project"
            title = soup.find('span', class_='field--name-title').get_text(strip=True)
            print("Titel: " + title)
        #19
        elif "computerweekly.com" in url:
            for data in soup.find('section', {"id":"content-body"}).find_all('p'):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "ComputerWeekly.com"
            title = soup.find('h1', class_='main-article-title').get_text(strip=True)
            print("Titel: " + title)
        #20
        elif "wiwo.de" in url:
            for data in soup.find('div', {"class":"o-article__content"}).find_all('p', recursive=True):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "WirtschaftsWoche"
            title = soup.find('h2', class_='c-headline--article').get_text(strip=True)
            print("Titel: " + title)
        #21
        elif "analyticsindiamag.com" in url:
            for data in soup.find_all('p'):
                if data.span:
                    continue
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "aim"
            title = soup.find('h1', class_='elementor-heading-title').get_text(strip=True)
            print("Titel: " + title)
        #22
        elif "infoq.com" in url:
            for data in soup.find('div', {"class":"article__data"}).find_all('p', recursive=False):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "InfoQ"
            title = soup.find('h1', class_='heading').get_text(strip=True)
            print("Titel: " + title)
        #23
        elif "kdnuggets.com" in url:
            for data in soup.find('div', id="post-").find_all('p', recursive=False):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "KD nuggets"
            title = soup.find('h1', id='title').get_text(strip=True)
            print("Titel: " + title)
        #24
        elif "kommune21.de" in url:
            for data in soup.find('div', {"class":"meldungText"}):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "Kummune 21"
            title = soup.find('h1', class_='meldungTitel').get_text(strip=True)
            print("Titel: " + title)
        #25
        elif "volksfreund.de" in url:
            for data in soup.find_all('p', class_="text", recursive=True):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "Volksfreund"
            title = soup.find('span', class_='park-article__headline').get_text(strip=True)
            print("Titel: " + title)
        #26 --- der Request kommt an den cookie einstellungen nicht vorbei
        elif "golem.de" in url:
            scraped_lines = ["REQUEST UNSUCCESSFUL"]
            domain = "golem.de"
            title = "None"
            print("Titel: " + title)
        #27
        elif "uelzener-presse.de" in url:
            for data in soup.find('article', {"class":"small single p-3"}).find_all('p', recursive=True)[:-2]:
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "Uelzener Presse"
            title = soup.find('h1', class_='title').get_text(strip=True)
            print("Titel: " + title)
        #28
        elif "unite.ai" in url:
            for data in soup.find('div', {"id":"mvp-content-main"}).find_all('p', recursive=False):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "UNITE.AI"
            title = soup.find('h1', class_='entry-title').get_text(strip=True)
            print("Titel: " + title)
        #29
        elif "springerprofessional.de" in url:
            for data in soup.find('div', {"class":"rich-text mtl"}).find_all('p', recursive=False):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "Springer Professional"
            title = soup.find('h1').get_text(strip=True)
            print("Titel: " + title)
        #30
        elif "saarbruecker-zeitung.de" in url:
            for data in soup.find('div', class_='park-section').find_all('p', recursive=True):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "Saarbrücker Zeitung"
            title = soup.find('span', class_='park-article__headline').get_text(strip=True)
            print("Titel: " + title)
        #31
        elif "cloudcomputing-insider.de" in url:
            for data in soup.find('article', {"class":"inf-article-detail"}).find_all('p', {"class":"inf-text--medium-sec"}, recursive = False):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "Cloudcomputing Insider"
            title = soup.find('span', class_='inf-no-margin').get_text(strip=True)
            print("Titel: " + title)
        #32
        elif "boersennews.de" in url:
            for data in soup.find('table', border="0").find_all('p', recursive=True):
                if data.br :
                    continue
                if data.i :
                    break
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "börsenNEWS.de"
            title = soup.find('h1', class_='balance-ragged-lines').get_text(strip=True)
            print("Titel: " + title)
        #33
        elif "wiwo.de" in url:
            for data in soup.find('div', {"class":"o-article__content"}).find_all('p', recursive=-1):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "WirtschaftsWoche"
            title = soup.find('h2', class_='c-headline--article').get_text(strip=True)
            print("Titel: " + title)
        #34
        elif "wiwo.de" in url:
            for data in soup.find('div', {"class":"o-article__content"}).find_all('p', recursive=-1):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "WirtschaftsWoche"
            title = soup.find('h2', class_='c-headline--article').get_text(strip=True)
            print("Titel: " + title)
        #35
        elif "wiwo.de" in url:
            for data in soup.find('div', {"class":"o-article__content"}).find_all('p', recursive=-1):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "WirtschaftsWoche"
            title = soup.find('h2', class_='c-headline--article').get_text(strip=True)
            print("Titel: " + title)
        #36
        elif "wiwo.de" in url:
            for data in soup.find('div', {"class":"o-article__content"}).find_all('p', recursive=-1):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "WirtschaftsWoche"
            title = soup.find('h2', class_='c-headline--article').get_text(strip=True)
            print("Titel: " + title)
        #37
        elif "wiwo.de" in url:
            for data in soup.find('div', {"class":"o-article__content"}).find_all('p', recursive=-1):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "WirtschaftsWoche"
            title = soup.find('h2', class_='c-headline--article').get_text(strip=True)
            print("Titel: " + title)
        #38
        elif "wiwo.de" in url:
            for data in soup.find('div', {"class":"o-article__content"}).find_all('p', recursive=-1):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "WirtschaftsWoche"
            title = soup.find('h2', class_='c-headline--article').get_text(strip=True)
            print("Titel: " + title)
        #39
        elif "wiwo.de" in url:
            for data in soup.find('div', {"class":"o-article__content"}).find_all('p', recursive=-1):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "WirtschaftsWoche"
            title = soup.find('h2', class_='c-headline--article').get_text(strip=True)
            print("Titel: " + title)
        #40
        elif "wiwo.de" in url:
            for data in soup.find('div', {"class":"o-article__content"}).find_all('p', recursive=-1):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "WirtschaftsWoche"
            title = soup.find('h2', class_='c-headline--article').get_text(strip=True)
            print("Titel: " + title)
        #41
        elif "wiwo.de" in url:
            for data in soup.find('div', {"class":"o-article__content"}).find_all('p', recursive=-1):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "WirtschaftsWoche"
            title = soup.find('h2', class_='c-headline--article').get_text(strip=True)
            print("Titel: " + title)
        #42
        elif "wiwo.de" in url:
            for data in soup.find('div', {"class":"o-article__content"}).find_all('p', recursive=-1):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "WirtschaftsWoche"
            title = soup.find('h2', class_='c-headline--article').get_text(strip=True)
            print("Titel: " + title)
        


        else:
            for data in soup.find_all('p'):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            shortlink = url.split('/')
            shortlink = shortlink[2].split('.')
            if 'www' not in shortlink:
                domain = shortlink[0].capitalize()
            else:
                domain = shortlink[1].capitalize()
            title = (soup.find('h1').get_text(strip=True) + " !!!Seite nicht eingepflegt!!!")

        
        #print("\n\n".join(scraped_lines))
            
        return "\n".join(scraped_lines), title, domain

#TextScraper.getdata(TextScraper, 'https://venturebeat.com/security/report-u-s-businesses-experience-42-cyberattacks-per-year/')