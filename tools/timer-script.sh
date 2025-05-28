#!/bin/bash

FORCE=""
[ "$1" == "--force" ] && FORCE=true

cd /var/www/html/p24
BRANCH=$(git symbolic-ref --short HEAD)
CURRENT=$(git rev-parse HEAD)
git fetch origin
UPSTREAM=$(git rev-parse origin/$BRANCH)
if [ -n "$FORCE" -o "$CURRENT" != "$UPSTREAM" ]; then
    echo moving from $CURRENT to $UPSTREAM
    git reset --hard origin/$BRANCH
    make index html
    # the systemd jobs are already run as apache
    # chown -R apache:apache .
else
    echo no change from upstream on $CURRENT
fi
