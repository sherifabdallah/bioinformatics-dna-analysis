# Bioinformatics-Dna
DNA nucleotide count web app

## Table of Content
- [Bioinformatics Dna](#Bioinformatics-Dna)
  * [Tools](#tools)
  * [How to run](#how-to-run)
  * [URL](#URL)
  * [Author](#author)

## Tools
1. Python
2. Streamlit
3. Pandas
4. Altair
5. Pillow


## How to run
* Enter the directory where the script is located then type the following to the console
```sh
$ git clone https://github.com/sherifabdallah/bioinformatics-dna-analysis bioinformatics-dna-analysis
```

* Install Python 3.8 venv, pip and compiler
```sh
$ sudo apt-get install python3.8 python3.8-venv python3-venv
```

* Create a virtual environment to install dependencies in and activate it:

```sh
$ python3.8 -m venv venv
$ source venv/bin/activate
```

* Then install the dependencies:

```sh
(venv)$ cd bioinformatics-dna-analysis
(venv)$ python -m pip install --upgrade pip
(venv)$ python -m pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.


* Finally run The App:
```sh
(venv)$ python -m streamlit run main.py
```
* And navigate to `http://127.0.0.1:8501`.



## Author
[Sherif Abdullah](https://github.com/sherifabdallah)
