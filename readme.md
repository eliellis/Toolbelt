# Toolbelt
Toolbelt adds some pretty convenient abstraction to functional programming in Python

# Usage
```python
from Toolbelt.belt import Toolbelt
belt = Toolbelt()

@belt.map  # the map decorator should decorate your desired mapping function,
# and be called with the dataset to be mapped
def factorial(item):
    return item**item


@belt.reduce  # the reduce decorator should decorate your desired reduce function,
# and be called with the dataset to be reduced
def add(prev, next):
    return prev + next

if __name__ == '__main__':
    #calculate the factorial of numbers 0-100, then add them together, and print them out
    print(add(*factorial(*range(100))))

```

# Documentation

## Toolbelt#map(fn)
### fn(val, [key])
Just your regular old map, decorate your mapping function and call it with the data you'd like to change, or you can get creative with keyword arguments.

## Toolbelt#reduce(fn)
### fn(previous, next)
What to say? It's reduce like you know and love, give it your reduce function, and viola, out comes what you wanted.