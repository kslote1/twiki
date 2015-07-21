import twitter
from twitter import Api, TwitterError
from wikipedia import search, page, DisambiguationError
import wikipedia
import ConfigParser


#get these from a config file
def get_config():
    config = ConfigParser.ConfigParser()
    config.read('twitter.ini')
    return {'consumer_key': config.get('twitter', 'consumer_key'),
    'consumer_secret': config.get('twitter', 'consumer_secret'),
    'access_token_key': config.get('twitter', 'access_token_key'),
    'access_token_secret': config.get('twitter', 'access_token_secret')}

def twitter_api():
    config = get_config()
    return Api(consumer_key=config['consumer_key'],
               consumer_secret=config['consumer_secret'],
               access_token_key=config['access_token_key'],
               access_token_secret=config['access_token_secret'])

API = twitter_api()

def search_twitter(concept):
    results = []
    try:
        for result in API.GetSearch(concept):  
            results.append(type('tweet', (), {'text': result.text,
                                              'id': result.id,
                                              'user_name': result.user.screen_name,
                                              'user_url':result.user.url}))
    except TwitterError as e:
        pass
    return results

def search_wiki(concept):
    results = []
    for result in wikipedia.search(concept):
         try:
             wiki_page = page(result)
             results.append(type('wiki', (), {'url': wiki_page.url,
                                              'result': result,
                                              'summary': wiki_page.summary[:100] }))
         except DisambiguationError as e:
             #TO-DO: add all diambiguous search results recursivley? 
             pass
    return results

def tweet_url_from_obj(tweet):
    return "http://twitter.com/{0}/status/{1}".format(tweet.user.GetScreenName(), tweet.id)

def search(concept):
    return type('search', (), {'twitter': search_twitter(concept), 'wiki': search_wiki(concept)})
