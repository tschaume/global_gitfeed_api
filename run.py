import os
from eve import Eve
from flask.ext.bootstrap import Bootstrap
from eve_docs import eve_docs

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app = Eve()
  Bootstrap(app)
  app.register_blueprint(eve_docs, url_prefix='/docs')
  app.run(host='127.0.0.1', port=port, debug=True)
