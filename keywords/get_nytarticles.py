import requests as req
import time
API_KEY='S9rAUUHmpGbOhJOspD57PLPwnM43H7MW' #insert your API_KEY 
TOPIC='Health'
articles = []
for i in range(10):
    url='https://api.nytimes.com/svc/search/v2/articlesearch.json?q='+TOPIC+'&api-key='+API_KEY+'&page='+str(i)
    response = req.get(url).json()

# Extract the necessary fields from the response.
    docs = response['response']['docs']
    for doc in docs:
        filteredDoc = {}
        filteredDoc['title'] = doc['headline']['main']
        filteredDoc['abstract'] = doc['abstract']
        filteredDoc['paragraph']=doc['lead_paragraph']

        articles.append(filteredDoc)

# Done to avoid hitting the API request limit.
    time.sleep(6)
articles[:10]