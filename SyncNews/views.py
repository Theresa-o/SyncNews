from multiprocessing import context
import requests
from django.shortcuts import render


# Create your views here.
def hacker_news_article():
    #make an API call and store the response
    url = 'https://hacker-news.firebaseio.com/v0/topstories.json' 
    response = requests.get(url)
    article_list = response.json()
    context = {}
    context['objects'] = []

    # Process information about each article.
    for each_id in article_list[:10]:
        # Make a separate API call for each article.
        url = f"https://hacker-news.firebaseio.com/v0/item/{each_id}.json" 
        # get response for individual articles
        response = requests.get(url)
        article_dict = response.json()
        context['objects'].append(article_dict)

    return context 

def index(request):
    context = hacker_news_article()
    return render(request, 'SyncNews/index.html', context)
