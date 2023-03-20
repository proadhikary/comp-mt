#pip install pyter3 numpy pandas stramlit nltk
import nltk
# nltk.set_proxy('http://172.16.199.20:8080')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

import os
import pyter
import numpy as np
import pandas as pd
import streamlit as st
from pathlib import Path
from nltk import word_tokenize
from nltk.translate.meteor_score import meteor_score
from nltk.translate.bleu_score import SmoothingFunction, corpus_bleu, sentence_bleu
st.set_page_config(page_title='COMP-MT', page_icon='head.png', layout="centered", initial_sidebar_state="auto", menu_items=None)
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)


def bleu(ref, gen):
    ref_bleu = []
    gen_bleu = []
    for l in gen:
        gen_bleu.append(l.split())
    for i,l in enumerate(ref):
        ref_bleu.append([l.split()])
    cc = SmoothingFunction()
    score_bleu = corpus_bleu(ref_bleu, gen_bleu, weights=(0, 1, 0, 0), smoothing_function=cc.method4)
    return score_bleu

def ter(ref, gen):
    if len(ref) == 1:
        total_score =  pyter.ter(gen[0].split(), ref[0].split())
    else:
        total_score = 0
        for i in range(len(gen)):
            total_score = total_score + pyter.ter(gen[i].split(), ref[i].split())
        total_score = total_score/len(gen)
    return total_score


#main code states here
with st.columns(3)[1]:
     st.image("head.png")

st.markdown("<h1 style='text-align: center;'>COMPMT: Automatic Evaluation</h1>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center;'> Enter you scholar id || Insert the file as `gold.txt` & `pred.txt` || Click on Submit", unsafe_allow_html=True)

with st.form(key="Form :", clear_on_submit = True):
    id = st.text_input("Scholar ID")
    File = st.file_uploader(label = "Upload file", accept_multiple_files=True, type=["txt"])
    Submit = st.form_submit_button(label='Submit')
try:
    os.mkdir(id)
except:
    pass

if Submit :
    for File in File:
        save_folder = id
        save_path = Path(save_folder, File.name)
        with open(save_path, mode='wb') as w:
            w.write(File.getvalue())

    # if save_path.exists():
    #     st.success(f'Files are successfully saved!')

    ref = open("%s/gold.txt" %id, "r")
    ref = ref.readlines() 
    gen = open("%s/pred.txt"%id, "r")
    gen = gen.readlines() 

    for line in zip(ref, gen):
        refm = word_tokenize(line[0])
        genm = word_tokenize(line[1])
        m_score = meteor_score([refm], genm)

    for i,l in enumerate(gen):
        gen[i] = l.strip()

    for i,l in enumerate(ref):
        ref[i] = l.strip()
        
    ter = ter(ref, gen)
    bleu = bleu(ref, gen)
    meteor = m_score
    result = [bleu, ter, meteor]
    with open("%s/result.txt"%id, "w") as output:
        output.write(str(result))

    resultdf = pd.DataFrame(result).T
    resultdf.columns = ['BLEU', 'TER', 'METEOR']
    hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
    st.markdown("<h4 style='text-align: center;'>Scores</h4>", unsafe_allow_html=True)
    st.markdown(hide_table_row_index, unsafe_allow_html=True)
    st.table(resultdf)

st.markdown("<small><p style='text-align: center;'>Developed by: Pro! </p><small>", unsafe_allow_html=True)

