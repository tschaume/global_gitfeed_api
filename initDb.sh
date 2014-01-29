#!/bin/bash
# do bulk insert into DB via API

HOST='127.0.0.1'
PORT='5000'

# insert projects first
DATA="'["
for p in `awk -F/ '{print $(NF-1)}' repolist.txt | tr '\n' ' '`; do
  DATA=$DATA'{"name":"'$p'"},'
done
DATA=${DATA%?}"]'"
echo $DATA
#curl -d $DATA -H 'Content-Type: application/json'  http://$HOST:$PORT/projects
#exit 1

# insert commits
DATA="'["
for repo in `head -1 repolist.txt`; do # TODO: replace with cat
  cd $repo
  project=`basename $PWD`
  log=$project.log
  [[ -e $log ]] && rm -v $log
  TZ=America/Los_Angeles git log --author='Patrick' --all --oneline --date=local --pretty=tformat:'%cd#%h#%s' >> $log
  while read commit; do
    IFS='#' read datetime sha1 message <<<"$commit"
    DATA=$DATA'{"project":"'$project'","message":"'$message'","datetime":"'$datetime'"},'
  done < $log
done
DATA=${DATA%?}"]'"

echo $DATA

#curl -d $DATA -H 'Content-Type: application/json'  http://$HOST:$PORT/commits
