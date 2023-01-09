import streamlit as st
from streamlit_option_menu import option_menu
from apps import (
    summarizer_app,
    home
    )

with st.sidebar:
        selected = option_menu(
            menu_title = "Navigation",
            options = ["Home", "Summarizer App"],
            icons = ["house-door", "body-text"],
            menu_icon = "list",
            default_index = 0,
            )

def main():
    if selected == "Home":
        home.app()
    if selected == "Summarizer App":
        summarizer_app.app()
    return



if __name__ == "__main__":
    main()