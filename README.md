# Redisearch Wikipedia Test

## Prerequisites

 - Redis server
 - A compiled `redisearch.so` module
 - Python 3 virtual env `pip install -r requirements.txt`

## Usage

Run Redis server

```bash
$ redis-server --loadmodule /path/to/redisearch.so
```

Load random articles from wikipedia (infinite loop, kill the process once you have enough):

```bash
$ python load_random.py
```

Search the index:

```python
from redisearch import Client

c = Client('wikipedia')
c.search('search term')
```
