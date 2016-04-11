# Key functions for python
Client size functions for writing into a D8-tree with Python.

##Usage example

```python
from keyfunctions import create_key,create_element_rand

obj = {'id': 1234, 'some':'thing'}
dimensions = [0.2,0.34,0.34,0.23]

key = create_key(dimensions,10)
rand = create_element_rand(obj.id)

session.execute("INSERT INTO d8tree(key,rand,obj) VALUES(?,?,?)",
    key,rand,obj)
```
