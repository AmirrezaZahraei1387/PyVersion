# PyVersion

A cross Platform tool for doing basic version management and comparison.

### Loading Version

In order to start work with the versions, we first need to load
them. You can either use the normal __init__ or the fromstr 
class method.

```python
import Vmanager

version = Vmanager.PyVersion(4, 3, 2, 1)
```

```python
import Vmanager

version = Vmanager.PyVersion().fromstr("5.4.4.2")
```

### Using Comparison Operators

the comparison operators are all overloaded
and so can be used with the versions.

```python
import Vmanager

v_1 = Vmanager.PyVersion().fromstr("5.4.4.2")
v_2 = Vmanager.PyVersion().fromstr("5.7.4")

print(v_1 == v_2)  # False
print(v_1 != v_2)  # True
print(v_1 >= v_2)  # False
print(v_1 <= v_2)  # True
print(v_1 > v_2)  # False
print(v_1 < v_2)  # True
```

### Resizing

Resizing can be used to add some trailing version numbers to the
end of the version. for example version 4.8 can get 4 trailing
zeros and become 4.8.0.0.0.0.

```python
import Vmanager

v_1 = Vmanager.PyVersion().fromstr("5.4.4.2")

v_1.resize(2, 0)
print(v_1)  # 5.4.4.2.0.0
```

The last argument is optional. it defines what value should be
used, and it is defaulted to zero.

You can also give negative numbers as the trailing version number.
In this case instead of adding it will remove the version numbers.

```python
import Vmanager

v_1 = Vmanager.PyVersion().fromstr("5.4.4.2")

v_1.resize(-2, 0)
print(v_1)  # 5.4
```

### Other Useful Functionalities

insertend(): Inserting a value to the end of the version.

insertfront(): Inserting a value to the beginning of the version.

pop(): removing a number at a specific index

[]: getting and setting the value by giving a key

removeRedundant(): removing the redundant trailing values.
first parameter is the number of trailing values, and the
second one is the value should be considered.

isunder(): check if one version is under another one or not.
it has a parameter to set how much it need to check. it is
defaulted to zero.

normalize(): it will get to versions as input and then resize them,
so they will  have a similar size. then it returns them.



