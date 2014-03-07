Buildbot-Nine-Demo
==================

Heroku app to host the buildbot nine demo

This serves as an example on how to deploy buildbot nine on Heroku, and also has simple configuration to show new features of buildbot nine.

- new ForceScheduler UI: in demo1.py is configured a complex forcescheduler
- new Trigger UI: the master.cfg implements multiple triggers to show how it works in the UI.

The project includes a buildbot.tac file which starts a master and a slave in the same twistd process.

The project can use any db as configured in heroku variables (sqlite, mysql or postgre). At free tier level of service, it looks like sqlite is much faster, but remember it is not persistent, and will be reset when the app is redeployed, restarted, or sleeped.

In order to avoid sleeping, the application is doing "self ping". This is because Heroku is stopping the application if it serves no http requests for more than one hour. This would cause the loss of the db, so we try to avoid that by instanciating a TimerService, which pings the application every 30min.

How to deploy
=============

- https://devcenter.heroku.com/articles/quickstart
- please read and understand the heroku python tutorial before starting this one.
- deploy the app normally with git push in your heroku git URL

- run once the db upgrade:

    heroku run buildbot upgrade-master master

- set the variables (`heroku config:set`):
    - `DBURL`: url to your database, including user and password (optional)
    - `buildbotURL`: url to your heroku application. e.g: http://buildbot-nine-demo.herokuapp.com/
    - `PING_DELAY`: the number of seconds between self wakeup pings (optional)

- you can now make sure everything looks good using

    heroku logs

Publishing changes to buildbot
==============================
The application includes a copy of buildbot, so that we can show features not yet merged into upstream.
You can edit `.gitmodules` in order to point to your own fork of buildbot. Then update your environment:

    git submodule init
    git submodule update


Running it locally
==================
In order to test your change the best is to run the app locally.
You will have to install the following packages on your system:

   - python
   - python-virtualenv
   - node.js + npm (use `ppa:chris-lea/node.js` on ubuntu)
   - bower ( `npm install -g bower`)
   - grunt-cli ( `npm install -g grunt-cli`)

Then the app can be run locally with:

    virtualenv sandbox
    . sandbox/bin/activate
    pip install `cat requirements_dev.txt`
    foreman start

Deploy you changes
==================

As Heroku python environment does not include a version of npm and bower, it is not capable of building automatically the web app upon deployment. This is why a pre-compiled version of the web app and plugins is included in the app base repository.
In order to update the pre-compiled environment:

    cd built_frontend
    ./update.sh
    (then commit the changes, and deploy them)

if you made changes to buildbot, dont forget to commit the `git submodule` pointer to buildbot

    git commit buildbot
