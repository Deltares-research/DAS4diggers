# DAS4diggers

[![License: MIT](https://img.shields.io/pypi/l/imod)](https://choosealicense.com/licenses/mit)
[![Lifecycle: experimental](https://lifecycle.r-lib.org/articles/figures/lifecycle-experimental.svg)](https://lifecycle.r-lib.org/articles/stages.html)
[![Formatting: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/charliermarsh/ruff)

Detecting digging animals with fiber optic acoustic sensing

## Installation process
The installation uses package manager pixi, for installation options see https://pixi.sh/latest/

To install pixi on windows, in powershell type:
```
winget install prefix-dev.pixi
```
Now clone DAS4diggers to your local drive using:
```
git clone https://github.com/Deltares-research/DAS4diggers.git
```
Then navigate into that folder with:
```
cd DAS4diggers
```
To create a conda enviroment and install DAS4diggers in it type:
```
pixi install
```

## Update DAS4diggers
To update DAS4diggers with the latest version from github, open a shell in the DAS4diggers folder and:
```
git pull
```
And the same as with installation type:
```
pixi install
```

## Tutorial
Activate the DAS4diggers_env in a command prompt and type 
```
pixi run notebook
```

## Contributing

You can contribute by testing, raising issues and making pull requests. Some general guidelines:

- Use new branches for developing new features or bugfixes. Use prefixes such as feature/ bugfix/ experimental/ to indicate the type of branch
- Add unit tests (and test data) for new methods and functions. We use pytest.
- Add Numpy-style docstrings
- Use Black formatting with default line lenght (88 characters)
- Update requirement.txt en environment.yml files if required

## License
MIT license
