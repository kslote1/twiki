Intallation:

Get consumer keys and access tokens from twitter.
Fill them out in twitter_config.ini.
    
    cp twitter.ini.sample twitter.ini

make your virtual enviornment:

user@ubuntu:~/home$virtualenv virt
user@ubuntu:~/home$activate virt/bin/source

install all the packages:

(Source)user@ubuntu:~/home$virt/bin/pip install -r requirements.txt

Init the db

(Source)user@ubuntu:~/home$flask --app=twiki initdb

run the app

(Source)user@ubuntu:~/home$flask --app=twiki run

The app will be running at http://localhost:5000

You can log in with the temporary credentials

user:admin password: default
