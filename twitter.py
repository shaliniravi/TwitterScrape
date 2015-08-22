__author__ = 'Shalini'


from TwitterSearch import *
import csv

def get_tweets(query, max = 20000):
    # takes a search term (query) and a max number of tweets to find
    # gets content from twitter and writes it to a csv bearing the name of your query

    i = 0
    search = query

    with open(search+'.csv', 'wb') as outf:
        writer = csv.writer(outf)
        writer.writerow(['user','time','tweet','latitude','longitude'])
        try:
            tso = TwitterSearchOrder()
            tso.set_keywords([search])
            tso.set_language('en') # English tweets only

            ts = TwitterSearch(
                consumer_key = 'qPHhCyWFMCyNuJii6fhEytxAG',
                consumer_secret = 'bl8s3ICLCyhxx9n6q1ZDD1X9UAkdFy5Z0u4AkmUlPfcUvwcA4q',
                access_token = '140937790-ECvQr7J1tJziPyfd5GrHCzFxlN9R1PT5HbuEayDZ',
                access_token_secret = 'rlHrorLfvyGf2oxM46dg7Lw2k8VdahFDeGNd7bAIA64p0'
            )

            for tweet in ts.search_tweets_iterable(tso):
                lat = None
                long = None
                time = tweet['created_at']
                # UTC time when Tweet was created.
                user = tweet['user']['screen_name']
                tweet_text = tweet['text'].strip().encode('ascii', 'ignore')
                tweet_text = ''.join(tweet_text.splitlines())
                print i,time,
                if tweet['geo'] != None and tweet['geo']['coordinates'][0] != 0.0: # avoiding bad values
                    lat = tweet['geo']['coordinates'][0]
                    long = tweet['geo']['coordinates'][1]
                    print('@%s: %s' % (user, tweet_text)), lat, long
                else:
                    print('@%s: %s' % (user, tweet_text))

                writer.writerow([user, time, tweet_text, lat, long])
                i += 1
                if i > max:
                    return()

        except TwitterSearchException as e: # take care of all those ugly errors if there are some
            print(e)

query = raw_input ("Search for: ")
max_tweets = 20000
get_tweets(query, max_tweets)