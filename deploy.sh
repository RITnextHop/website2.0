git pull
rm -rf db.sqlite3
python3.6 manage.py migrate
python3.6 manage.py migrate --run-syncdb
python3.6 manage.py loaddata Initial\ Data/initial_data.yaml
