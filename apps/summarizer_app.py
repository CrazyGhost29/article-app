from services.text_scraper import TextScraper
from services.text_summarizer import TextSummarizer
import time
import numpy as np
import streamlit as st

@st.cache(hash_funcs={"MyUnhashableClass": lambda _: None})
def load_summarizer():
    return TextSummarizer()
def load_scraper():
    return TextScraper()

summarizer = TextSummarizer()
scraper = TextScraper()

def app():
    st.title("Artikelzusammenfassung")

    
    url_list = []
    text_list = []
    #text = st.text_input("Text einfügen")
    for x in range(5):
        if x == 0:
            input_url = st.text_input("URL einfügen", key = x)
            url_list.append(input_url)
        elif url_list[x-1] == "":
            break
        else:
            input_url = st.text_input("URL einfügen", key = x)
            url_list.append(input_url)
    
    for x in range(5):
        if x == 0:
            input_text = st.text_input("Text einfügen", key = x+5)
            text_list.append(input_text)
        elif text_list[x-1] == "":
            break
        else:
            input_text = st.text_input("Text einfügen", key = x+5)
            text_list.append(input_text)


    #input_url = st.text_input("URL einfügen")

    configuration = st.checkbox("Konfigurieren")

    selection_sens = 3
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

    status = 0

    if st.button("Zusammenfassen"):
        status = 1

    if status:
        st.warning("Bitte warten: Artikel wird zusammengefasst... Das kann einige Sekunden dauern.")

        #with st.spinner("lädt..."):
        #    time.sleep(3)
        for y in url_list:
            if y != "":
                try:
                    url_text = scraper.getdata(y)
                except Exception as error:
                    st.error(f"URL konnte nicht umgewandelt werden...\nFehlercode: {error}")
            
            
                try:
                    if configuration:
                        if summarization_type == "Sätze":
                            result_sens = summarizer.summarize_sens(url_text, selection_sens)
                            st.text_area("Anpassen:", value=y + "\n\n" + result_sens, height=500)
                        elif summarization_type == "Ratio":
                            result_ratio = summarizer.summarize_ratio(url_text, selection_ratio)
                            st.text_area("Anpassen:", value=y + "\n\n" + result_ratio, height=500)
                    else:
                        result_sens = summarizer.summarize_sens(url_text, selection_sens)
                        st.text_area("Anpassen:", value=y + "\n\n" + result_sens, height=500)

                    st.success("Zussammenfassung abgeschlossen!")

                except Exception as error:
                    st.error(f"Artikel konnte nicht zusammengefasst werden...\nFehlercode: {error}")

        for z in text_list:
            if z != "":
                try:
                    if configuration:
                        if summarization_type == "Sätze":
                            result_sens = summarizer.summarize_sens(z, selection_sens)
                            st.text_area("Anpassen:", value=result_sens, height=500)
                        elif summarization_type == "Ratio":
                            result_ratio = summarizer.summarize_ratio(z, selection_ratio)
                            st.text_area("Anpassen:", value=result_ratio, height=500)
                    else:
                        result_sens = summarizer.summarize_sens(z, selection_sens)
                        st.text_area("Anpassen:", value=result_sens, height=500)

                    st.success("Zussammenfassung abgeschlossen!")

                except Exception as error:
                    st.error(f"Artikel konnte nicht zusammengefasst werden...\nFehlercode: {error}")

        #progress_bar = st.progress(0)

        #for percent_complete in range(100):
            #time.sleep(0.05)
            #progress_bar.progress(percent_complete + 1)
        #test


    
    return