import streamlit as st
import spacy
from spacy import displacy
from dateparser.search import search_dates
import re

# --- Page Configuration ---
st.set_page_config(
    page_title="ClauseScope",
    page_icon="⚡",
    layout="wide",
)

# --- Custom CSS for High-Energy UI ---
custom_css = """ 
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&display=swap');

    body {
        font-family: 'Poppins', sans-serif;
        color: #FFFFFF; /* White text */
        background-color: #000000; /* Black background */
    }
    .stApp {
        background-color: #000000;
    }
    h1, h2, h3 {
        color: #0052FF; /* Brighter Electric Blue */
        font-weight: 700; /* Bold */
    }
    h2 {
        border-bottom: 2px solid #0052FF; /* Brighter Electric Blue separator */
        padding-bottom: 10px;
        margin-top: 40px;
    }
    .stButton>button {
        border: 2px solid #DFFF00; /* Neon Yellow border */
        border-radius: 25px; /* Rounded */
        background-color: #DFFF00; /* Neon Yellow background */
        color: #000000; /* Black text */
        font-weight: 700; /* Bold */
        padding: 12px 24px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #000000; /* Black background on hover */
        color: #DFFF00; /* Neon Yellow text on hover */
    }
    .stTextArea textarea {
        background-color: #1a1a1a;
        color: #FFFFFF;
        border: 2px solid #0052FF; /* Brighter Electric Blue */
        border-radius: 15px;
    }
    mark {
        background-color: #DFFF00; /* Neon Yellow */
        color: #000000; /* Black text */
        padding: 0.2em 0.4em;
        border-radius: 0.3em;
    }
    .stSpinner > div > div {
        border-top-color: #0052FF; /* Brighter Electric blue spinner */
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Load the pre-trained English model
@st.cache_resource
def load_spacy_model():
    return spacy.load("en_core_web_sm")

nlp = load_spacy_model()

def extract_clauses_and_dates(text):
    """
    Extracts clauses using dependency parsing and dates using dateparser.
    """
    # Clause extraction with spaCy
    doc = nlp(text)
    clauses = []
    for sent in doc.sents:
        root = sent.root
        subject = next((child for child in root.children if "subj" in child.dep_), None)
        obj = next((child for child in root.children if "obj" in child.dep_), None)
        if subject and obj:
            clauses.append(f"{subject.text} {root.text} {obj.text}")

    # Date extraction with dateparser
    date_tuples = search_dates(text)
    dates = [date_str for date_str, _ in date_tuples] if date_tuples else []
    
    return clauses, dates

def highlight_text(text):
    """
    Generates an HTML string with highlighted entities using both spaCy and dateparser.
    """
    # First, get all entities from spaCy
    doc = nlp(text)
    highlighted_html = displacy.render(doc, style="ent", jupyter=False)

    # Then, find dates with dateparser and override highlighting for them
    date_tuples = search_dates(text)
    if date_tuples:
        for date_str, _ in date_tuples:
            # Use regex to replace the found date string with a marked version
            highlighted_html = re.sub(f"(?<!<mark>){re.escape(date_str)}(?!</mark>)", f"<mark>{date_str}</mark>", highlighted_html)

    return highlighted_html

st.title("ClauseScope – AI-powered Contract Clause & Date Extractor")

# Section 1: Full Contract Analysis
st.header("1. Analyze Full Contract")
contract_text = st.text_area("Paste Full Contract Text Here", "", height=300, label_visibility="collapsed")

if st.button("Analyze Full Contract"):
    if contract_text:
        with st.spinner('Analyzing...'):
            clauses, dates = extract_clauses_and_dates(contract_text)
            st.subheader("Extracted Clauses")
            if clauses:
                for clause in clauses:
                    st.write(f"- {clause}")
            else:
                st.info("No clauses found.")

            st.subheader("Extracted Dates (using dateparser)")
            if dates:
                for date in dates:
                    st.write(f"- {date}")
            else:
                st.info("No dates found.")
    else:
        st.warning("Please paste the contract text above to analyze.")

# Section 2: Snippet Highlighter
st.header("2. Highlight a Specific Snippet")
snippet_text = st.text_area("Paste a Snippet to Highlight", "", height=150, label_visibility="collapsed")

if st.button("Highlight Snippet"):
    if snippet_text:
        with st.spinner('Highlighting...'):
            highlighted_html = highlight_text(snippet_text)
            st.subheader("Highlighted Snippet")
            st.markdown(highlighted_html, unsafe_allow_html=True)
    else:
        st.warning("Please paste a snippet above to highlight.")
