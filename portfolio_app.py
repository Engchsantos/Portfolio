import streamlit as st


# --- PAGE SETUP ---
sobre = st.Page(
    "views/sobre.py",
    title="Sobre",
    icon=":material/account_circle:",
)
predios = st.Page(
    "views/predios.py",
    title="Construção de Edifícios",
    icon=":material/apartment:",
)
residenciais = st.Page(
    "views/residenciais.py",
    title="Obras Residenciais",
    icon=":material/house:",
)
comerciais = st.Page(
    "views/comerciais.py",
    title="Obras Comerciais",
    icon=":material/storefront:",
)

pg = st.navigation(
    {
        "Info": [sobre],
        "Projetos": [predios, residenciais, comerciais],
    }
)


# --- SHARED ON ALL PAGES ---
st.logo("assets/logo.png")
st.sidebar.markdown("2024 - Feito por Carlos Santos")


# --- RUN NAVIGATION ---
pg.run()
