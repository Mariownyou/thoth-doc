# Thoth doc: Dependency-free, lightweight docstring parser
![Thoth image](Thoth.svg.png =250x250)


## Installation
```bash
pip install thoth-doc
```

## Usage
```python
# code.py

def foo(bar: int, baz: str = "qux") -> None:
    """This is a docstring"""
    pass
```


```python
from thoth_doc import get_docstring

docstring = get_docstring("code.py", "foo")  # find docstring of foo in code.py
print(docstring)  # "This is a docstring"
```


## License
[MIT License](LICENSE)
