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

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app = Eve(auth=BCryptAuth)
  Bootstrap(app)
  app.register_blueprint(eve_docs, url_prefix='/docs')
  app.run(host='127.0.0.1', port=port, debug=True)
