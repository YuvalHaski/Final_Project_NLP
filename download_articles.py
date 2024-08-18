import json
import requests
import csv
from datetime import datetime, timedelta
import threading
from queue import Queue
import time

API_KEY = '93957eb0a0aa8996a93f3908e17ecfde'

base_url = 'https://api.elsevier.com/content/search/scopus'
query = 'NLP'
date_range = 10

headers = {
    'X-ELS-APIKey': API_KEY,
    'Accept': 'application/json'
}


def fetch_data(start_year, end_year, results_queue):
    params = {
        'query': f'TITLE-ABS-KEY({query}) OR ABS({query})',
        'date': f'{start_year}-{end_year}',
        'start': 0,
        'count': 25,
    }

    thread_results = []

    while True:
        response = requests.get(base_url, headers=headers, params=params)

        if response.status_code == 429:
            print(f"Rate limit reached for years {start_year}-{end_year}. Waiting 5 seconds...")
            time.sleep(5)
            continue
        elif response.status_code != 200:
            print(f"Error: {response.status_code} for years {start_year}-{end_year}")
            print(response.text)
            break

        data = response.json()
        print(
            f"Receiving results {params['start']} to {params['start'] + params['count']} out of {data['search-results']['opensearch:totalResults']} for years {start_year}-{end_year}")
        entries = data['search-results']['entry']
        if not entries:
            break

        for entry in entries:
            abstract_url = next(
                (link.get('@href') for link in entry.get('link', []) if link.get('@ref') == 'full-text'), None)

            if abstract_url:
                abstract_response = requests.get(abstract_url, headers=headers).json()
                if 'full-text-retrieval-response' in abstract_response:
                    abstract = abstract_response['full-text-retrieval-response']['coredata'].get('dc:description', '')
                    keywords = ', '.join([keyword.get('$', '') for keyword in
                                          abstract_response['full-text-retrieval-response']['coredata'].get(
                                              'dcterms:subject', [])])
                    try:
                        authors = '# '.join([author.get('$', '') for author in
                                             abstract_response['full-text-retrieval-response']['coredata'].get(
                                                 'dc:creator', [])])
                    except Exception as e:
                        authors = None
                else:
                    abstract = ''
                    keywords = ''
                    authors = None
            else:
                abstract = ''
                keywords = ''
                authors = None

            result = {
                'title': entry.get('dc:title', ''),
                'authors': authors if authors else entry.get('dc:creator', ''),
                'journal': entry.get('prism:publicationName', ''),
                'keywords': keywords,
                'year': entry.get('prism:coverDate', '')[:4],
                'abstract': abstract
            }

            thread_results.append(result)

        params['start'] += params['count']

        if len(thread_results) >= int(data['search-results']['opensearch:totalResults']):
            break

    results_queue.put(thread_results)


def main():
    current_year = datetime.now().year
    start_year = current_year - date_range

    threads = []
    results_queue = Queue()

    for i in range(0, date_range, 2):
        thread_start_year = start_year + i
        thread_end_year = min(thread_start_year + 1, current_year)
        thread = threading.Thread(target=fetch_data, args=(thread_start_year, thread_end_year, results_queue))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    all_results = []
    while not results_queue.empty():
        all_results.extend(results_queue.get())

    # Remove duplicates based on title
    unique_results = {result['title']: result for result in all_results}.values()

    with open('nlp_papers.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'authors', 'journal', 'keywords', 'year', 'abstract'])
        writer.writeheader()
        writer.writerows(unique_results)

    print(f"Saved {len(unique_results)} unique results in 'nlp_papers.csv'")


if __name__ == "__main__":
    main()