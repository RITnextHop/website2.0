#git pull
rm -rf db.sqlite3
python3.6 manage.py makemigrations
python3.6 manage.py migrate
python3.6 manage.py migrate --run-syncdb
python3.6 manage.py loaddata Initial\ Data/initial_data_v2.yaml
python3.6 manage.py loaddata Initial\ Data/nsic_data.yaml
python3.6 manage.py runserver 0.0.0.0:8000
