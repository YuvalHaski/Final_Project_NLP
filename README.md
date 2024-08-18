# Final_Project_NLP

Literature Review on NLP Using SCOPUS Data

Overview
This project involves conducting a comprehensive literature review on Natural Language Processing (NLP) using data retrieved from the SCOPUS academic database. The objective is to analyze and summarize trends in NLP-related research over the past decade.

Tasks
Data Retrieval:

Develop a Python program to interface with the SCOPUS API.
Retrieve academic papers that mention "NLP" in the title, keywords, or abstract from the last 10 years.
Extract metadata including the title, authors, journal, keywords, publication year, and abstract.
Preprocessing:

Perform text preprocessing tasks including tokenization, lemmatization, and stop words removal.
Frequent Term Analysis:

Use TF-IDF to identify the most frequent terms.
Visualize the results using bar charts and word clouds.
Word2Vec Analysis:

Apply Word2Vec to find the most frequent terms.
Autoencoder Analysis:

Use an Autoencoder to identify the most important terms.
Comparison of Results:

Compare the results obtained from TF-IDF, Word2Vec, and Autoencoder analyses.
Named Entity Recognition (NER):

Implement an NER algorithm to extract named entities.
Exploratory Data Analysis (EDA):

Conduct EDA to identify trends, such as the number of papers published per year and the most prolific authors.
Trend Analysis:

Identify the most frequent terms or concepts and analyze their trends over the past 10 years.
Find highly interdependent terms or concepts.
Summarization:

Summarize the abstracts of the retrieved papers.
Topic Modeling:

Use a GPT model for topic modeling through question answering.
Comparison of Trends:

Compare the trends identified in the frequent term analysis with those from the topic modeling.
Review Article:

Write a review article summarizing the trends in academic publications related to NLP.
Requirements
Python 3.x
Access to the SCOPUS API
Libraries: requests, json, csv, nltk, gensim, tensorflow/keras, matplotlib, wordcloud
Usage
Clone the repository.
Install the required libraries using pip install -r requirements.txt.
Run the main script to retrieve data and perform analyses.
License
This project is licensed under the MIT License.
