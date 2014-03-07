cd ../buildbot/www
rm dist/*
python setup.py sdist
cd -
tar xzf ../buildbot/www/dist/*.gz
mkdir -p buildbot-www
cp -rf buildbot-www-*/* buildbot-www/
rm -rf buildbot-www-*
cd ../buildbot/www/codeparameter
rm dist/*
python setup.py sdist
cd -
tar xzf ../buildbot/www/codeparameter/dist/*.gz
mkdir -p buildbot-codeparameter
cp -rf buildbot-codeparameter-*/* buildbot-codeparameter/
rm -rf buildbot-codeparameter-*
git add buildbot-codeparameter buildbot-www

