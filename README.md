# CJKfuzz

[![Supported Python Versions](https://img.shields.io/pypi/pyversions/cjkfuzz)](https://pypi.org/project/cjkfuzz/) [![PyPI version](https://badge.fury.io/py/cjkfuzz.svg)](https://badge.fury.io/py/cjkfuzz)

## Prerequisites

- Python 3.9+

## Installation

### From PyPI

```shell
pip install cjkfuzz
```

### From Source

```shell
pip install git+https://github.com/eddielin0926/cjkfuzz.git
```

## Usage

```python
from cjkfuzz import fuzz
fuzz.ratio('你好', '你好嗎?')
```

## License

This project is licensed under the terms of the [MIT License](LICENSE)
