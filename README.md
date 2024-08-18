# Literature Review on NLP Using SCOPUS Data
 
## Overview
This project focuses on analyzing NLP-related research articles using various NLP techniques such as TF-IDF, Word2Vec, and Autoencoder. The project includes scripts for downloading data, processing it, and performing analysis.


## Setup Instructions
1. Clone the repository
2. Install the required packages
3. Obtain SCOPUS API credentials and update the configuration file.
4. Run the main script to retrieve data and perform analyses.


## Scripts
### `download_articles.py`
- **Purpose**: Fetches research articles from the SCOPUS API.
- **Usage**: Run the script with your API credentials to download the dataset.

### `hyperparameter_tuning_word2vec.ipynb`
- **Purpose**: Explores the impact of different vector sizes on Word2Vec model performance.
- **Usage**: Open the notebook and run the cells to see how changing vector sizes affects word pair similarities.

### `nlp.ipynb`
- **Purpose**: Analyzes the dataset using various NLP techniques to identify trends and key concepts.
- **Usage**: Run the notebook to perform text analysis and visualize the results.


## Requirements  
•	Python 3.x  
•	Access to the SCOPUS API  
•	Libraries: requests, json, csv, nltk, gensim, tensorflow/keras, matplotlib, wordcloud  
  
   
