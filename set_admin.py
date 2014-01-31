import bcrypt, argparse, requests, json
from settings import SERVER_NAME

if __name__ == '__main__':
  # parse command line arguments
  parser = argparse.ArgumentParser()
  parser.add_argument("username", help="username")
  parser.add_argument("password", help="password")
  args = parser.parse_args()
  # api url + endpoint
  url = 'http://%s/accounts' % SERVER_NAME
  # delete accounts
  # TODO: no authentication on api yet (howto init w/o admin account?)
  print requests.delete(url)
  # generate bcrypt hashed password
  hashed = bcrypt.hashpw(args.password, bcrypt.gensalt())
  print hashed
  payload = {'username': args.username, 'password': hashed}
  headers = {'content-type': 'application/json'}
  print requests.post(url, data=json.dumps(payload), headers=headers)
