import streamlit as st
import spacy
import pandas as pd
#from spacy_streamlit import visualize_tokens


st.set_page_config(page_title='EX-DATA from text')

def main():
    #st.markdown(f'<p style="color:#0C8B9B;font-size:45px;text-align:center;">WELCOME', unsafe_allow_html=True)
    st.markdown(
        f'<p style="color:#10ADC1;font-size:30px;text-align:center;"><strong>Data Extraction Using Machine Learning</strong></p>',unsafe_allow_html=True)
    st.sidebar.markdown(f'<p style="color:#10ADC1;font-size:45px;text-align:center;">WELCOME', unsafe_allow_html=True)

    st.sidebar.markdown(f'<p style="color:#04424A;font-size:50px;"><strong>EX-DATA</strong></p>',
                        unsafe_allow_html=True)
     


    st.title('Entrer votre texte')
    text_input = st.text_area("", "")

    st.title('les données extraites')
    if text_input != "" :
        prdnlp = spacy.load("preTrained_model")
        doc = prdnlp(text_input)
        for ent in doc.ents:
            
            st.markdown(f'<strong style="color:#0C8B9B;font-size:18px;"> {ent.label_}   ==>   </strong> {ent.text}', unsafe_allow_html=True)

    st.sidebar.title("Objectif")
    st.sidebar.info(
        "L'objectif est Extraction des informations à partir du texte non structuré . En effet, les données Qu'on veut extraits  sont :"
        " prenom, nom, adresse, email et numero de telephone  ")
          

if __name__ == "__main__" :
    main()