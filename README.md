# Project Overview

This project is a data pipeline designed to extract, process, and analyze public discourse from government consultation platforms. It transforms unstructured citizen feedback into structured, actionable insights using a combination of web scraping and Large Language Models (LLMs).

## Description of tasks

-**Automated Extraction**: Download thousands of pdfs containing public votes using JavaScript. See [ScrappingScript.js](./scrappingScript.js). 

-**Data parsing**: Parse through each PDF to extract key information include ID, names, address, sentiment and comment using Pandas library in Python. See [main.py](./main.py) for the parsing code.

-**Semantic Analysis**: Use LLMs to perform sentiment analysis, and identify biased or biggoted comments. The code used for this can be found in [data_analysis.py](./data_analysis.py) and [data analysis for Sutton Planning a](./data_analysis_for_Sutton_Planning_application.ipynb).
