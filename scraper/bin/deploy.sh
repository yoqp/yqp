#!/bin/sh
set -e

echo '----- [scraper] RUN deploy'

#cd scraper

# ECRへのログインと変数準備
$(aws ecr get-login --region ap-northeast-1 --no-include-email)
REPOSITORY_URI=REPOSITORY_URI

IMAGE_TAG=dev-$(date '+%Y%m%d%H%M%S')
LATEST_TAG='develop'

# イメージをタグ付けしてpush
docker build -t $REPOSITORY_URI:$LATEST_TAG .
docker tag $REPOSITORY_URI:$LATEST_TAG $REPOSITORY_URI:$IMAGE_TAG
docker push $REPOSITORY_URI:$LATEST_TAG
docker push $REPOSITORY_URI:$IMAGE_TAG
