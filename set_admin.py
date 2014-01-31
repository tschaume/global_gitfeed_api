import bcrypt, argparse, sys
from pymongo import MongoClient

if __name__ == '__main__':
  # parse command line arguments
  parser = argparse.ArgumentParser()
  parser.add_argument("username", help="username")
  parser.add_argument("password", help="password")
  args = parser.parse_args()
  # make connection to mongo client and get database
  client = MongoClient()
  db = client.apieve
  # get the database & accounts collection
  # check whether admin user already exists
  if db.accounts.find({"username": args.username}).count() > 0:
    print '%s account already in database!' % args.username
    sys.exit(0)
  # generate bcrypt hashed password & insert into collection
  hashed = bcrypt.hashpw(args.password, bcrypt.gensalt())
  admin = { "username": args.username, "password": hashed }
  print db.collection_names()
  db.accounts.insert(admin)
  print db.collection_names()
