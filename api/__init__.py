import os, bcrypt
from eve import Eve
from flask.ext.bootstrap import Bootstrap
from eve_docs import eve_docs
from eve.auth import BasicAuth

class BCryptAuth(BasicAuth):
  def check_auth(self, username, password, allowed_roles, resource, method):
    accounts = app.data.driver.db['accounts']
    account = accounts.find_one({'username': username})
    return (
      account and
      bcrypt.hashpw(password, account['password']) == account['password']
    )

accounts = {
  'public_methods': [],
  'public_item_methods': [],
  'schema': {
    'username': {
      'type': 'string',
      'minlength': 5,
      'required': True,
      'unique': True
    },
    'password': {
      'type': 'string',
      'required': True
    }
  }
}

gitcommits = {
  'datasource': {
    'default_sort': [('datetime',1)],
  },
  'schema': {
    'project': {
      'type': 'objectid',
      'required': True,
      'data_relation': {
        'resource': 'gitprojects',
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
    'sha1': {
      'type': 'string',
      'required': True,
    },
    'deletions': {
      'type': 'integer',
      'required': True,
    },
    'lines': {
      'type': 'integer',
      'required': True,
    },
    'insertions': {
      'type': 'integer',
      'required': True,
    },
    'files': {
      'type': 'integer',
      'required': True,
    },
  }
}

gitprojects = {
  'additional_lookup': {
    'url': 'regex("[\w]+")',
    'field': 'name'
  },
  'schema': {
    'name': {
      'type': 'string',
      'minlength': 3,
      'maxlength': 50,
      'required': True,
      'unique': True,
    },
  }
}

settings = {
  #'SERVER_NAME': '127.0.0.1:5000', # dev
  'SERVER_NAME': 'api.the-huck.com', # prod
  'MONGO_HOST': 'localhost',
  'MONGO_PORT': '27017',
  #'MONGO_USERNAME': 'user',
  #'MONGO_PASSWORD': 'user',
  'MONGO_DBNAME': 'apieve',
  'RESOURCE_METHODS': ['GET', 'POST', 'DELETE'],
  'ITEM_METHODS': ['GET', 'PATCH', 'PUT', 'DELETE'],
  'PUBLIC_METHODS': ['GET'],
  'PUBLIC_ITEM_METHODS': ['GET'],
  'CACHE_CONTROL': 'max-age=600',
  'CACHE_EXPIRES': 600,
  'DOMAIN': {
    'accounts': accounts,
    'gitcommits': gitcommits,
    'gitprojects': gitprojects
  }
}

app = Eve(auth=BCryptAuth, settings=settings)
Bootstrap(app)
app.register_blueprint(eve_docs, url_prefix='/docs')
