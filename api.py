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

app = Eve(auth=BCryptAuth)
Bootstrap(app)
app.register_blueprint(eve_docs, url_prefix='/docs')
