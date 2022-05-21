"""Contain keys for twitter API"""

from easydict import EasyDict

detailsDict = EasyDict()

detailsDict.keysDict = EasyDict()
detailsDict.keysDict.TWITTER_APP_KEY = ''
detailsDict.keysDict.TWITTER_APP_SECRET = ''
detailsDict.keysDict.TWITTER_KEY = ''
detailsDict.keysDict.TWITTER_SECRET = ''

detailsDict.queries = EasyDict()
detailsDict.queries.KEYWORD = 'KEYWORD/S HERE'
detailsDict.queries.COUNT = 10000

detailsDict.db = EasyDict()
detailsDict.db.URL = 'mongodb://127.0.0.1:27017/'
detailsDict.db.DATABASE = 'DATABASE_NAME'
detailsDict.db.COLLECTION = 'COLLECTION_NAME'