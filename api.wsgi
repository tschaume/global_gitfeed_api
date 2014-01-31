activate_this = '/home/patrick/public/api.the-huck.com/env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
import logging, sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(1,'/home/patrick/public/api.the-huck.com')
from api import app
