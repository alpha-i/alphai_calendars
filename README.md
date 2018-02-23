# Alpha-I Calendars

A library to extends pandas market calendar with calendars not related to the market

## Setup Development Environment

### Create conda environment
```bash
$ conda create -n calendars python=3.5
$ source activate calendars
```

### Install dependencies

```bash
$ pip install -U setuptools --ignore-installed --no-cache-dir
$ pip install -r dev-requirements.txt --src $CONDA_PREFIX
```

### Usage
```python
import alphai_calendars as mcal

mcal.get_calendar('GYMUK')

```

### Running the test suite
```bash
pytest tests/
```

### Credits

This library is based on [pandas_market_calendar](https://readthedocs.org/projects/pandas-market-calendars/)
