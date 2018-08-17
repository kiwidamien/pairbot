# PairBot

Allows for selecting people at random from a list. Also includes a random list.

## Installation
```bash
python setup.py install
```

## Basic usage
```python
import pairbot

print(pairbot.get_pairs(pairbot.example_list, seed=42))
```

This returns 
```
[('Fred', 'Maryann'), ('The Professor', 'Gillian'), ('The Skipper', 'Ginger')]
```
