SERVER_NAME = '127.0.0.1:5000'

MONGO_HOST = 'localhost'
MONGO_PORT = 27017
#MONGO_USERNAME = 'user'
#MONGO_PASSWORD = 'user'
#MONGO_DBNAME = 'apitest'
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

DATE_FORMAT = '%c'
PUBLIC_METHODS = ['GET']
PUBLIC_ITEM_METHODS = ['GET']

DOMAIN = {
  'accounts': {
    'schema': {
      'username': {
        'type': 'string',
        'minlength': 5,
        'required': True
      },
      'password': {
        'type': 'string',
        'required': True
      }
    }
  },
  'gitcommits': {
    'datasource': {
      'default_sort': [('datetime',1)],
    },
    'schema': {
      'project': {
        'type': 'objectid',
        'required': True,
        'data_relation': {
          'resource': 'projects',
          'field': '_id',
          'embeddable': True
        }
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
  },
  'gitprojects': {
    'additional_lookup': {
      'url': 'regex("[\w]+")',
      'field': 'name'
    },
    'schema': {
      'name': {
        'type': 'string',
        'minlength': 3,
        'maxlength': 20,
        'required': True,
        'unique': True,
      },
    }
  }
}
