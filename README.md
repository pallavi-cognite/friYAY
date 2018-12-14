# friYAY
Backend for the FriYAY Application. Written in Django.

# Installation
`pip3 install -r requirements.txt`

# Running on Local
`python3 manage.py runserver`

# Connecting to DB
`./cloud_sql_proxy -instances=cognitedata-development:europe-west3:friyay=tcp:5432`

# deployment
`docker build -t eu.gcr.io/cognitedata-development/friyay-test:6 .`
`docker push eu.gcr.io/cognitedata-development/friyay-test:6`
Edit app.yaml with the new image
`kubectl apply -f app.yaml`

`user`
`cognite`
