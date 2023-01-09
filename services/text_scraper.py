import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By

test_url = 'https://www.heise.de/news/Stable-Diffusion-Stability-AI-auf-Kurs-mit-101-Millionen-US-Dollar-Finanzierung-7313243.html'
test_url2 = 'https://medium.com/a-microbiome-scientist-at-large/why-cant-babies-drink-water-13b22c7ac721'
test_url3 = 'https://www.pressebox.de/pressemitteilung/cosys-ident-gmbh/digitalisierung-der-logistik-mit-mobilen-scannern/boxid/1133995'
test_url4 = 'https://venturebeat.com/security/report-password-fatigue-compromises-employee-productivity-security-and-well-being/'
test_url5 = 'https://www.bigdata-insider.de/5-tipps-um-ein-unternehmen-ki-ready-zu-machen-a-2097e733d0a1af77fa479439ce70a534/'
test_url6 = 'https://www.inpactmedia.com/karriere/arbeitswelt-der-zukunft/hybrides-arbeiten-win-win-situation-fuer-alle'
test_url7 = 'https://www.behoerden-spiegel.de/2022/10/21/non-visible-data-gewinnt-nato-innovation-challenge/'
test_url8 = 'https://omr.com/de/daily/diese-ki-systeme-veraendern-die-welt-der-bilder-fuer-immer-und-damit-auch-das-marketing/'
test_url9 = 'https://t3n.de/news/stable-diffusion-ki-kritik-1507584/'
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
test_url26 = 'https://www.golem.de/news/anzeige-data-engineering-und-data-science-mit-python-2208-167872.html'
test_url27 = 'https://uelzener-presse.de/2022/08/26/wie-kann-man-sich-auf-data-analytics-umorientieren/'
test_url28 = 'https://www.unite.ai/machine-learning-vs-data-science-key-differences/'
test_url29 = 'https://www.springerprofessional.de/reporting/investor-relations/esap-plattform-fuer-unternehmensdaten-startet-erst-2026/23369244'
test_url30 = 'https://www.saarbruecker-zeitung.de/pr/presseportal/teradata-stellt-vantagecloud-lake-vor_aid-75960389'
test_url31 = 'https://www.cloudcomputing-insider.de/was-ist-azure-global-infrastructure-a-aed226e32dbcb7e9a556ccc4982f335c/'
test_url32 = 'https://www.boersennews.de/nachrichten/artikel/dgap-news-bwi-optimiert-sap-nutzung-mit-usu-software-asset-management/3850711/'
test_url33 = 'https://esut.de/2022/11/fachbeitraege/37565/it-news-digital-work-arbeit-ist-eine-taetigkeit-kein-ort/'
test_url34 = 'https://www.computerwoche.de/a/openai-veroeffentlicht-dall-e-api,3613165'
test_url35 = 'https://www.unesco.org/en/articles/ai-decoded-new-online-course-seeks-demystify-artificial-intelligence-all'
test_url36 = 'https://www.itp.net/infrastructure/cloud/alibaba-cloud-debuts-new-open-source-platform-to-speed-up-innovations'
test_url37 = 'https://www.elektrotechnik.vogel.de/neue-richtlinie-fuer-big-data-anwendungen-veroeffentlicht-a-d30b89abfebc097050373c516b293260/'
test_url38 = 'https://www.boerse-express.com/news/articles/datenintegration-und-etl-prozess-mit-interaktiven-landkarten-und-geo-analysen-mehrwert-aus-unternehmensdaten-holen-521077'
test_url39 = 'https://idw-online.de/de/news804284'
test_url40 = 'https://www.egovernment.de/optimierte-stadtplanung-dank-geodatenbasierter-digitaler-zwillinge-a-90c920d65563128fc08ab653a202003e/'
test_url41 = 'https://www.datacenter-insider.de/die-sicherheit-der-softwarelieferketten-ruecken-in-den-fokus-a-0f1b07fb0b148de96997452469ccf69a/'
test_url42 = 'https://www.bmi.bund.de/SharedDocs/pressemitteilungen/DE/2022/11/digital-souveraen-in-der-cloud.html'
test_url43 = 'bwi.de'
test_url44 = 'https://www.zdnet.de/88405279/ki-als-entwicklerhilfe-nicht-ausgereift/'
test_url45 = 'https://www.riffreporter.de/de/technik/kuenstliche-intelligenz-meta-cicero-diplomacy-algorithmen-deep-learning'
test_url46 = 'https://www.technologyreview.com/2022/11/25/1063707/ai-minecraft-video-unlock-next-big-thing-openai-imitation-learning/'
test_url47 = 'https://www.storage-insider.de/was-sind-big-data-a-388663abd5c0ab8c99d323ee7529e1d9/'
test_url48 = 'https://www.konstruktionspraxis.vogel.de/unternehmen-nutzen-digitalisierung-vor-allem-fuer-optimierung-a-4d791ebf388d5182af60186ad84168e6/'
test_url49 = 'https://www.informationweek.com/big-data/developerweek-enterprise-sorting-out-big-data-to-empower-ai'
test_url50 = 'https://www.boeckler.de/de/pressemitteilungen-2675-digitale-kontrolle-diskriminierungsschutz-haftungsfragen-44947.htm'
test_url51 = 'https://www.bmbf.de/bmbf/shareddocs/bekanntmachungen/de/2022/11/2022-11-28-Bekanntmachung-Digitale-Geosysteme.html'
test_url52 = 'https://www.thw.de/SharedDocs/Meldungen/DE/Pressemitteilungen/international/2022/11/pressemitteilung_002_kongo.html'
test_url53 = 'https://www.notebookcheck.com/Banana-Pi-BPI-M6-Alternative-zum-Raspberry-Pi-mit-starker-KI-Leistung-eMMC-Speicher-und-PCIe.670330.0.html'
test_url54 = 'https://www.sciencenews.org/article/brain-implant-reads-peoples-thoughts?fbclid=IwAR0I4mAl7DepRVu1HaGyuO24kK42BE3hAY7cPVTdntAMBZd7duLA2-KyXqQ'
test_url55 = 'https://www.silicon.de/41702900/wie-ki-devops-prozesse-optimieren-kann'
test_url56 = 'https://www.ip-insider.de/was-sind-microservices-und-wo-liegen-ihre-vorteile-a-46f9d950db50006737242a5df93f7159/'
test_url57 = 'https://www.presseportal.de/pm/166985/5378932'
test_url58 = ''
test_url59 = ''
test_url60 = ''
test_url61 = ''
test_url62 = ''

# chromedriver_autoinstaller.install()
selenium_list = ["computerwoche.de", "t3n.de", "golem.de", "itp.net"]
chrome_options = Options()
def get_driver():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


class TextScraper:

    def __init__(self):
        pass

    def getdata(self, url):
        if any(dom in url for dom in selenium_list):
            print("Selenium")
            chrome_options.add_argument("--headless")
            # driver = webdriver.Chrome(options=chrome_options)
            driver = get_driver()
        else:
            print("Request")
            r = requests.get(url)
            htmldata = r.text
            # print(htmldata)
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
        elif "inpactmedia.com" in url:
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
        elif "behoerden-spiegel.de" in url:
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
        elif "omr.com" in url:
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
        elif "t3n.de" in url:
            driver.get(url)
            driver.implicitly_wait(1)
            driver.switch_to.frame("sp_message_iframe_735176")
            driver.find_element(By.XPATH, "//*[@title='Zustimmen']").click()
            driver.implicitly_wait(1)
            driver.switch_to.parent_frame()
            data = driver.find_elements(By.XPATH,  "//*[@id='main-content']/div/div/p")
            print(len(data))
            for element in data:
                if element.text == "":
                    continue
                scraped_lines.append(element.text)
            domain = "t3n"
            title = driver.find_element(By.XPATH, '//*[@id="article"]/h2').text
            driver.quit()
            print("Titel: " + title)
        #10
        elif "1e9.community" in url:
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
        elif "techcrunch.com" in url:
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
        elif "marktechpost.com" in url:
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
        elif "it-zoom.de" in url:
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
        elif "handelsblatt.com" in url:
            scraped_lines = ["PAYWALL"]
            domain = "Handelsblatt"
            title = soup.find('span', class_='vhb-headline--onecolumn').get_text(strip=True)
            print("Titel: " + title)
        #15 --- Text Deutsch und englisch...
        elif "windkraft-journal.de" in url:
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
        elif "meinbezirk.at" in url:
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
        #26 Klappt mit Selenium
        elif "golem.de" in url:
            driver.get(url)
            driver.implicitly_wait(1)
            driver.switch_to.frame("sp_message_iframe_689342")
            driver.find_element(By.XPATH, "//*[@title='Zustimmen und weiter']").click()
            driver.implicitly_wait(1)
            driver.switch_to.parent_frame()
            data = driver.find_elements(By.XPATH,  "//*[@class='formatted']/p")
            print(len(data))
            for element in data:
                if element.text == "":
                    continue
                scraped_lines.append(element.text)
            domain = "Golem"
            title = driver.find_element(By.XPATH, "//*[@class='dh1 head5']").text
            driver.quit()
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
        elif "esut.de" in url:
            for data in soup.find('div', {"class":"td-post-content"}).find_all('p', recursive=False):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "ES&T"
            title = soup.find('h1', class_='entry-title').get_text(strip=True)
            print("Titel: " + title)
        #34 KLAPPT MIT SELENIUM
        elif "computerwoche.de" in url:
            driver.get(url)
            driver.switch_to.frame("sp_message_iframe_735670")
            driver.find_element(By.XPATH, "//*[@title='Ablehnen']").click()
            driver.switch_to.default_content()
            data = driver.find_elements(By.XPATH,  "//div[@class='col-md-9 col-lg-10 idgGalleryWidthHelper']/p")
            for element in data:
                if element.text == "":
                    continue
                scraped_lines.append(element.text)
            domain = "Computerwoche"
            title = driver.find_element(By.XPATH, '//div[@class="col-md-12"]/h1[1]').text
            driver.quit()
            print("Titel: " + title)
        #35
        elif "unesco.org" in url:
            for data in soup.find('div', {"class":"field--name-field-paragraphs"}).find_all('p', recursive=True):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        scraped_lines.append(refined_space)
            domain = "Unesco"
            title = soup.find('h1', class_='title article-title').get_text(strip=True)
            print("Titel: " + title)
        #36 SELENIUM!
        elif "itp.net" in url:
            driver.get(url)
            driver.implicitly_wait(1)
            data = driver.find_elements(By.XPATH,  "//*[@class='entry-content']/p")
            print(len(data))
            for element in data:
                if element.text == "":
                    continue
                scraped_lines.append(element.text)
            domain = "ITP"
            title = driver.find_element(By.XPATH, "//h1").text
            driver.quit()
            print("Titel: " + title)
        #37
        elif "elektrotechnik.vogel.de" in url:
            for data in soup.find_all('p', class_='inf-text--medium-sec', recursive=True):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "Elektrotechnik"
            title = soup.find('span', class_='inf-headline-1').get_text(strip=True)
            print("Titel: " + title)
        #38
        elif "boerse-express.com" in url:
            for data in soup.find('article', {"id":"video-tag-article"}).find_all('p', recursive=False):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "boerse-express"
            title = soup.find('div', class_="size-8 no-float").find('h3').get_text(strip=True)
            print("Titel: " + title)
        #39
        elif "idw-online.de" in url:
            for data in soup.find('div', {"class":"blueline-top add-padding-h"}).find_all('p', recursive=False):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 50:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "idw"
            title = soup.find('div', class_="blueline-top add-padding-h").find('h4').get_text(strip=True)
            print("Titel: " + title)
        #40
        elif "egovernment.de" in url:
            for data in soup.find_all('p', class_="inf-text--medium-sec", recursive=True):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 10:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "eGovernment"
            title = soup.find('span', class_='inf-headline-1').get_text(strip=True)
            print("Titel: " + title)
        #41
        elif "datacenter-insider.de" in url:
            for data in soup.find('article', {"class":"inf-article-detail"}).find_all('p', {"class":"inf-text--medium-sec"}, recursive = False):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "Datacenter Insider"
            title = soup.find('span', class_='inf-no-margin').get_text(strip=True)
            print("Titel: " + title)
        #42
        elif "bmi.bund.de" in url:
            scraped_lines = ["ACCESS DENIED"]
            domain = "BMI Bund"
            title = "403 Forbidden"
            print("Titel: " + title)
        #43
        elif "bwi.de" in url:
            scraped_lines = ["ACCESS DENIED"]
            domain = "BWI Intern"
            title = "403 Forbidden"
            print("Titel: " + title)
        #44
        elif "zdnet.de" in url:
            for data in soup.find('div', {"id":"articleContent"}).find_all('p', recursive=False):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "ZDNET"
            title = soup.find('h1').get_text(strip=True)
            print("Titel: " + title)
        #45
        elif "riffreporter.de" in url:
            for data in soup.find('div', {"id":"articleBg"}).find_all('p', recursive=2)[:-1]:
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "RiffReporter"
            title = soup.find('h2', class_='MuiTypography-root').get_text(strip=True)
            print("Titel: " + title)
        #46
        elif "technologyreview.com" in url:
            for div in soup.find_all('div', {"class":"gutenbergContent__content--1FgGp"}):
                for data in div.find_all("p", recursive=False):
                    raw = data.get_text(strip=True)
                    refined_l = raw.lstrip()
                    refined_r = refined_l.rstrip()
                    refined_space = refined_r.replace("  ", "")
                    if len(refined_space.split()) > 5:
                        if "\n" not in refined_space.split():
                            #print("***: "+refined_space)
                            scraped_lines.append(refined_space)
            domain = "MIT Technology Review"
            title = soup.find('h1', class_='contentArticleHeader__title--rp01p').get_text(strip=True)
            print("Titel: " + title)
        #47
        elif "storage-insider.de" in url:
            for data in soup.find('article', {"class":"inf-article-detail"}).find_all('p', {"class":"inf-text--medium-sec"}, recursive = False):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "Storage Insider"
            title = soup.find('span', class_='inf-no-margin').get_text(strip=True)
            print("Titel: " + title)
        #48
        elif "konstruktionspraxis.vogel.de" in url:
            for data in soup.find_all('p', class_='inf-text--medium-sec', recursive=True):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "Konstruktionspraxis"
            title = soup.find('span', class_='inf-headline-1').get_text(strip=True)
            print("Titel: " + title)
        #49
        elif "informationweek.com" in url:
            for data in soup.find('div', {"class":"article-content"}).find_all('p', recursive=2):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "InformationWeek"
            title = soup.find('h1', class_='article-title').get_text(strip=True)
            print("Titel: " + title)
        #50
        elif "boeckler.de" in url:
            for data in soup.find('div', {"class":"hbs-article__content"}).find_all('p', recursive=False):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 10:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "Hans Böckler Stiftung"
            title = soup.find('h2', class_='hbs-article__headline').get_text(strip=True)
            print("Titel: " + title)
        #51
        elif "bmbf.de" in url:
            scraped_lines = ["ACCESS DENIED"]
            domain = "BMBF Bund"
            title = "403 Forbidden"
            print("Titel: " + title)
        #52
        elif "thw.de" in url:
            scraped_lines = ["ACCESS DENIED"]
            domain = "THW Bund"
            title = "403 Forbidden"
            print("Titel: " + title)
        #53
        elif "notebookcheck.com" in url:
            for data in soup.find_all('p', class_="bodytext", recursive=1):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "Notebookcheck"
            title = soup.find('h1').get_text(strip=True)
            print("Titel: " + title)
        #54
        elif "sciencenews.org" in url:
            for data in soup.find('div', {"class":"rich-text"}).find_all('p', recursive=False):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "ScienceNews"
            title = soup.find('h1').get_text(strip=True)
            print("Titel: " + title)
        #55
        elif "silicon.de" in url:
            for data in soup.find('div', {"class":"entry-content"}).find_all('p', recursive=False):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "WirtschaftsWoche"
            title = soup.find('h1', class_='entry-title').get_text(strip=True)
            print("Titel: " + title)
        #56
        elif "ip-insider.de" in url:
            for data in soup.find('article', {"class":"inf-article-detail"}).find_all('p', {"class":"inf-text--medium-sec"}, recursive = False):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "IP Insider"
            title = soup.find('span', class_='inf-no-margin').get_text(strip=True)
            print("Titel: " + title)
        #57
        elif "presseportal.de" in url:
            for data in soup.find('div', {"class":"card"}).find_all('p', class_=None, recursive=False):
                raw = data.get_text(strip=True)
                refined_l = raw.lstrip()
                refined_r = refined_l.rstrip()
                refined_space = refined_r.replace("  ", "")
                if len(refined_space.split()) > 5:
                    if "\n" not in refined_space.split():
                        #print("***: "+refined_space)
                        scraped_lines.append(refined_space)
            domain = "Presseportal"
            title = soup.find('h1').get_text(strip=True)
            print("Titel: " + title)
        #58
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
            title = soup.find('h1').get_text(strip=True)
            print("Titel: " + title)
        #59
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
        #60
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
        #61
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
        #62
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