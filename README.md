# object-get

Use "." to get the value of a JSON object. Just like JavaScripthat gets the value of an object

## Install

```bash
pip install object-get
```

## Usage

```python
from object_get import get

obj = {
    'age': 18,
    'name': {
        'first': 'John',
        'last': 'Doe'
    },
    'languages': [
        'python',
        'java',
        ['c', 'c++'],
        ['js', 'javascript', 'typescript']
    ]
}

print(get(obj, 'age'))
# => 18

print(get(obj, 'weight'))
# => None

print(get(obj, 'weight', 100))
# => 100
```

```diff
- print(obj['name']['first'])
+ print(get(obj, 'name.first'))
# => John

- print(obj['name']['last'])
+ print(get(obj, 'name.last'))
# => Doe

- print(obj['languages'][0])
+ print(get(obj, 'languages[0]'))
# => python

- print(obj['languages'][2][1])
+ print(get(obj, 'languages[2][1]'))
# => c++

- print(obj['languages'][3][2])
+ print(get(obj, 'languages[3][2]'))
# => typescript
```