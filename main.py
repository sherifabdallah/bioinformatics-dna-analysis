import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image

# image = Image.open('dna_logo.png')
# st.image(image)


st.title('Bioinformatics DNA')

st.write("""
# DNA Nucleotide Count Web App

This app counts the nucleotide composition of query DNA!

***
""")

# Input text box

st.header('Enter DNA sequence')

sequence_input = ">DNA query \n GAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)

# prints input DNA sequence

# st.header('INPUT (DNA Query)')
# sequence

# DNA nucleotide

st.write("***")

# Dna nucliotide count

st.header('OUTPUT (DNA Nucleotide Count)')

# Print Dectionry
st.subheader('1. Print Dictionary')

def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C')),
    ])
    return d

X = DNA_nucleotide_count(sequence)

X_label = list(X)
x_values = list(X.values())

X

### 2. Print text

st.subheader('2. Print text')

st.write('There are ' + str(X['A']) + ' adenine (A)')
st.write('There are ' + str(X['T']) + ' thymine (T)')
st.write('There are ' + str(X['G']) + ' guanine (G)')
st.write('There are ' + str(X['C']) + ' cytosine (C)')

### 3. Display DataFrame

st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns= {'index':'nucleotide'})
st.write(df)

### 4. Display Bar Chart

st.subheader('4. Display Bar Chart')

p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)

p = p.properties(
    width=alt.Step(80)
)
st.write(p)


hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


