# GRAPH CALC (or TBD)


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
4) create graphs in django shell (default output dir: `./data/generated-graphs`)

```
python3 manage.py shell
```

- To create an RMAT graph with 1024 nodes, 1024 edges:
```
>>> from generators import kron
>>> kron.generate_and_save_graph(1024, 1024)
```   
