SERVER_NAME = '127.0.0.1:5000'

MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_USERNAME = 'user'
MONGO_PASSWORD = 'user'
MONGO_DBNAME = 'apitest'
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

schema = {
  'project': {
    'type': 'string',
    'minlength': 3,
    'maxlength': 20,
    'required': True,
  },
  'message': {
    'type': 'string',
    'minlength': 5,
    'required': True,
  },
  'datetime': {
    'type': 'datetime',
    'required': True,
  },
}

commits = {
  'cache_control': 'max-age=10,must-revalidate',
  'cache_expires': 10,
  'schema': schema
}

DOMAIN = {
  'commits': commits,
}
