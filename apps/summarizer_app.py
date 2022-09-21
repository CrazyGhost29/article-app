from services.text_scraper import TextScraper
from services.text_summarizer import TextSummarizer
import time
import numpy as np
import streamlit as st

summarizer = TextSummarizer()
scraper = TextScraper()

def app():
    st.title("Artikelzusammenfassung")

    

    #text = st.text_input("Text einfügen")
    input_url = st.text_input("URL einfügen")

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
        try:
            text = scraper.getdata(input_url)
        except Exception as error:
            st.error(f"URL konnte nicht umgewandelt werden...\nFehlercode: {error}")
        
        if text is not None:
            try:
                if configuration:
                    if summarization_type == "Sätze":
                        result_sens = summarizer.summarize_sens(text, selection_sens)
                        st.text_area("Anpassen:", value=result_sens, height=500)
                    elif summarization_type == "Ratio":
                        result_ratio = summarizer.summarize_ratio(text, selection_ratio)
                        st.text_area("Anpassen:", value=result_ratio, height=500)
                else:
                    result_sens = summarizer.summarize_sens(text, selection_sens)
                    st.text_area("Anpassen:", value=input_url + "\n\n" + result_sens, height=500)

                st.success("Zussammenfassung abgeschlossen!")

            except Exception as error:
                st.error(f"Artikel konnte nicht zusammengefasst werden...\nFehlercode: {error}")

        #progress_bar = st.progress(0)

        #for percent_complete in range(100):
            #time.sleep(0.05)
            #progress_bar.progress(percent_complete + 1)
        #test


    
    return