import twitter
import wikipedia

#get these from a config file
key = 'b7jZwU5ohwa8CSwjWLlgPryJD'
secret = 'a2gPwJ0lsMcJBtr6V1vvexslifP21hYB4CMS4jh1Q7CY7bmNGH'
token = '3379595800-QbyFbCxr2UeyRehGK2j2ZDKS5SZ57XRtpklpEtf'
token_secret = 'QSZcwcPaWmzsjUy86XhJs7vQrQHEmoQhRzFFnmFqqADH0'

def twitter_api():
    return twitter.Api(consumer_key=key,consumer_secret=secret,access_token_key=token, access_token_secret=token_secret)

API = twitter_api()

def search_twitter(concept):
    return API.GetSearch(concept)

def search_wiki(concept):
    return wikipedia.search(concept)

def search(concept):
    return type('search', (), {'twitter': search_twitter(concept), 'wiki': search_wiki(concept)})
