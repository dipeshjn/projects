API_KEY ='LVvfiheNsZffIVwFaXrs7nHN5'

API_SECRET ='Gb1HtXPZVOgLGHgHnWgS01y9OxvlQJ0Q5XpcVU9rkvh1Q51vU7'

ACCESS_TOKEN ='	780951174086168576-5oDyvi2lVZcEH48jzzJLyCfFO1mgQVd'

ACCESS_TOKEN_SECRET ='khtkj7pQhTfQT6hdIliVFiCfx5N8dtfW1IhqgLIhdq87z'

from twitter import Twitter, OAuth
import pprint

twitter_oauth = OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, API_KEY, API_SECRET)

#HTTP HEADERS

twitter = Twitter(auth = twitter_oauth)

results = twitter.search.tweets(q='fidget spinner', geography='28.6315 77.2167 20km')
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(results)

