# Food Craving Survey [![Build Status](https://travis-ci.org/jnthnrzr/food-craving-survey.svg?branch=master)](https://travis-ci.org/jnthnrzr/food-craving-survey) [![codecov](https://codecov.io/gh/jnthnrzr/food-craving-survey/branch/master/graph/badge.svg)](https://codecov.io/gh/jnthnrzr/food-craving-survey) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE) 
A website designed to record food craving scores from anonymous participants
for research.

## Setup
- Ensure correct versions of [Python](https://docs.python.org/3/) and [pip](https://pip.pypa.io/en/stable/) 
are installed:  
  `$ python --version` --> Python 3.6.1  
  `$ pip --version` --> pip 9.0.1 (python 3.6)
- Install virtualenv for python3 (see [Documentation](https://virtualenv.pypa.io/en/stable/) for 
details).
- Download source directory:  
`$ git clone https://github.com/jnthnrzr/food-craving-survey.git`
- Activate the virtualenv (exact command depends on OS, so consult 
documentation).
- Navigate to the Python backend directory:  
`$ cd backend/`
- Install dependencies from requirements.txt:  
`$ pip install -r requirements.txt`
- Run the backend server:  
`$ python backend.py`

## Running Tests and Coverage 
Using [py.test](https://docs.pytest.org/en/latest/) and [coverage](https://coverage.readthedocs.io/en/coverage-4.5.1/) from backend directory:  
`$ cd backend/`  
`$ pytest --cov=./`
