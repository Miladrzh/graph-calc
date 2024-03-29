# GRAPH CALC (or TBD)

## Requirements

1) `python3`
2) `swig` >= 4.1.0

## First time setup

1) in root dir, create new virtual environment, and activate
```
python3 -m venv ./venv
source ./venv/bin/activate 
```
2) install requirements
```
pip3 install -r requirements.txt
```
3) init models and db
```
python3 manage.py makemigrations
python3 manage.py migrate
```
<!-- - if you don't care about existing data
```
rm  storage/migrations/*
rm db.sqlite3
``` -->
4) create graphs in django shell (default output dir: `./data/generated-graphs`)

```
python3 manage.py shell
```

- e.g. In django shell, to create an RMAT graph with 1024 nodes, 1024 edges:
```
from generators import kron
kron.generate_graph(1024, 1024)
```   

- e.g. to run a benchmark test:
```
from workloads import test
test.run_test()
```
