#!/bin/bash
sh convert.sh
branch=$(git symbolic-ref HEAD | sed -e 's,.*/\(.*\),\1,')
#cd plank && python plank.py && python plank_lead.py  cd ../
git pull origin $branch
git add .
current="`date +'%Y-%m-%d %H:%M:%S'`"
msg="Updated: $current"
cd plank && python plank.py && python plank_lead.py  cd ../
git commit -m "wip $branch $msg"
git push origin $branch

