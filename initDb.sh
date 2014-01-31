#!/bin/bash
# do bulk insert into DB via API

HOST='127.0.0.1'
PORT='5000'

# delete all data
curl -X DELETE http://$HOST:$PORT/gitcommits
curl -X DELETE http://$HOST:$PORT/gitprojects

# insert projects first
echo "insert projects ..."
DATA="["
for p in `awk -F/ '{print $(NF-1)}' repolist.txt | tr '\n' ' '`; do
  DATA=$DATA'{"name":"'$p'"},'
done
DATA=${DATA%?}"]"
#echo $DATA | python -mjson.tool
curl -d @<(echo $DATA) -H 'Content-Type: application/json'  http://$HOST:$PORT/gitprojects

# generate commits data
echo "generate commits data ..."
DATA="["
for repo in `cat repolist.txt`; do
  cd $repo && echo $repo
  project=`basename $PWD`
  json=`curl -s http://$HOST:$PORT/gitprojects/$project | python -mjson.tool`
  id=`echo $json | grep _id | cut -d\" -f4`
  log=$project.log
  [[ -e $log ]] && rm -v $log
  TZ=America/Los_Angeles git log --author='Patrick' --all --oneline --date=local --pretty=tformat:'%cd#%h#%s' >> $log
  while read commit; do
    IFS='#' read datetime sha1 message <<<"$commit"
    DATA=$DATA'{"project":"'$id'","message":"'$message'","datetime":"'$datetime'"},'
  done < $log
  [[ -e $log ]] && rm -v $log
done
DATA=${DATA%?}"]"

# insert commits
#echo $DATA | python -mjson.tool
curl -d @<(echo $DATA) -H 'Content-Type: application/json'  http://$HOST:$PORT/gitcommits
