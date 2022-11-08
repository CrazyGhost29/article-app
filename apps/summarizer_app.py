from services.text_scraper import TextScraper
from services.text_summarizer import TextSummarizer
from services.text_document import DocumentCreator
import numpy as np
import streamlit as st
from datetime import date

@st.cache(hash_funcs={"MyUnhashableClass": lambda _: None})
def load_summarizer():
    return TextSummarizer()
def load_scraper():
    return TextScraper()
def load_documetify():
    return DocumentCreator()

summarizer = TextSummarizer()
scraper = TextScraper()
document = DocumentCreator()

def app():
    st.title("Artikelzusammenfassung")

    topics = {}
    urls = {}
    domains = {}
    titles = {}
    texts = {}
    summarys = {}
    st.markdown("Benenne ein Thema und füge darunter bis zu 10 URL'S ein:")
    for x in range(10):
        if x == 0 or topics["header{}".format(x-1)] != "":
            topics["header{}".format(x)] = st.text_input("THEMA:", key="header{}".format(x))
            for y in range(10):
                if (y == 0 or urls["url{}_{}".format(x, y-1)] != "") and topics["header{}".format(x)] != "":
                    urls["url{}_{}".format(x, y)] = st.text_input(
                        "URL",
                        key="url{}_{}".format(x, y),
                        placeholder="{}. URL zum Thema {}".format(y+1, topics["header{}".format(x)]),
                        label_visibility="hidden"
                    )
                else: break
        else:
            break
    
    text_list = []
    st.markdown("""
    Wenn der Text nicht korrekt zusammengefasst wurde oder der Request nicht durch z.B. eine Paywall ging, kann ein Text hier eingefügt und zusammengefasst werden.
    Diese Zusammenfassungen müssen manuell in den Pressespiegel aufgenommen werden.
    """)
    for x in range(10):
        if x == 0 or text_list[x-1] != "":
            text_list.append(st.text_input("Text einfügen:", key="text{}".format(x)))
        else:
            break
            

    configuration = st.checkbox("Zusammenfassung konfigurieren", help="Standard sind 2 Sätze")

    selection_sens = 2
    selection_ratio = 0.1

    if configuration:
        summarization_type = st.radio(
            "Wählen aus nominaler und relativer Zusammenfassung",
            ["Sätze", "Ratio"]
        )
        if summarization_type == "Sätze":
            selection_sens = st.selectbox(
                "Anzahl an Sätzen:",
                [x+1 for x in range(9)]
            )
        if summarization_type == "Ratio":
            selection_ratio = st.selectbox(
                "Ratio:",
                [round(x+0.05, 2) for x in np.arange(0,0.5,0.05)]
            )

    if "clicked" not in st.session_state:
        st.session_state.clicked = False

    def callback():
        for t in range(len(topics)):
            for u in range(10):
                if "url{}_{}".format(t, u) in urls and urls["url{}_{}".format(t, u)] != "":
                    try:
                        texts["text{}{}".format(t, u)], titles["title{}_{}".format(t, u)], domains["domain{}_{}".format(t, u)] = scraper.getdata(urls["url{}_{}".format(t, u)])
                    except Exception as error:
                        st.error(f"Request konnte nicht durgeführt werden...\nFehlercode: {error}")

                    
                    try:
                        if configuration:
                            if summarization_type == "Sätze":
                                summarys["summary{}_{}".format(t, u)] = summarizer.summarize_sens(
                                    texts["text{}{}".format(t, u)],
                                    selection_sens
                                )
                            else:
                                summarys["summary{}_{}".format(t, u)] = summarizer.summarize_ratio(
                                    texts["text{}{}".format(t, u)],
                                    selection_ratio
                                )

                        else:
                            summarys["summary{}_{}".format(t, u)] = summarizer.summarize_sens(
                                texts["text{}{}".format(t, u)],
                                selection_sens
                            )
                    except Exception as error:
                        st.error(f"Artikel konnte nicht zusammengefasst werden...\nFehlercode: {error}")
        document.documentify(topics, titles, summarys, urls, domains)
        st.session_state.clicked = True
        return

    button = st.button("Pressespiegel erstellen", on_click = callback)

    if st.session_state.clicked:
        try:
            with open('services/Pressespiegel_{}.docx'.format(date.today().strftime("%d.%m.%Y")), 'rb') as file:
                doc_download = file.read()

                download_button_str = document.download_document(doc_download, 'Pressespiegel_{}.docx'.format(date.today().strftime("%d.%m.%Y")), 'Pressespiegel herunterladen')
                st.markdown(download_button_str, unsafe_allow_html=True)
        except Exception as error:
            st.error(f"Datei konnte nicht gefunden werden...\nFehlercode: {error}")
        
        for text_input in text_list:
            if text_input != "":
                try:
                    if configuration:
                        if summarization_type == "Sätze":
                            result_sens = summarizer.summarize_sens(text_input, selection_sens)
                            st.text_area("Zusammenfassung {} anpassen:".format(text_list.index(text_input)+1), value=result_sens, height=500)
                        elif summarization_type == "Ratio":
                            result_ratio = summarizer.summarize_ratio(text_input, selection_ratio)
                            st.text_area("Zusammenfassung {} anpassen:".format(text_list.index(text_input)+1), value=result_ratio, height=500)
                    else:
                        result_sens = summarizer.summarize_sens(text_input, selection_sens)
                        st.text_area("Zusammenfassung {} anpassen:".format(text_list.index(text_input)+1), value=result_sens, height=500)

                    st.success("Zussammenfassung abgeschlossen!")

                except Exception as error:
                    st.error(f"Artikel konnte nicht zusammengefasst werden...\nFehlercode: {error}")

    return