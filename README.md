# Python Tools And Libs

## Install package with PIPENV

```bash
export PIPENV_VENV_IN_PROJECT=1;
pipenv install --skip-lock;
```

## Run unittest
```bash
pipenv run python -m untitest tests/*;
```

or


```bash
pipenv shell;
python -m untitest tests/*;
```

## Use
from pyfatal.cassandra import Cassandra

