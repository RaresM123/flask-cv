# CV Flask Application

This application is used for exposing cv information through 2 methods:
1. As a Flask REST API
2. as a Flask CLI 

## Requirements

1. Install requirements of the project: `pip install -r requirements.txt` 

## Start Project
1. For REST API either run app.py or run makefile command: `make run-app`
2. For Flask CLI run `flask cv` command in terminal where you should see all available commands


## Testing
1. Unit Testing can be run by: `make run-tests`
2. For Api tests a pycharm plugin should pe installed and can be run from the interpreter(to be shown in live presentation)

## Description

There are 3 folders: 
1. `cv_data` where the test data is stored
2. `cv_parser` where all the classes regarding parsing the cv are
3. `flaskr` where the flask app is defined

### cv_data

Contains also json document and pdf documents(the last ones are there for validating a json read and for a unsuccessful try to parse cv information from pdf files - not very good parsers)


### cv_parser

Contains base model for parsing cv's. This was created for having the possibility to easily change the income source of the cv(either json, pdf, database)\
The other are implementations for the base class\
There is also an exceptions file that contains exceptions regarding reading and parsing the cv

### flaskr

Contains the app implementation:
1. `routes.py` contains the flask routes
2. `commands.py` contains the flask cli commands
3. `cache.py` contains the implementation for the cache. This one was used to cache cv information because it will not change that often and the processing can take a while in case of pdf parsing.
4. `exceptions.py` contains the implementation for different kind of errors and return json responses
5. `serializer.py` contains serialized classes to serialize the response and validate through pydantic

The routes: 

1. `/cv` will return the entire cv
2. `/cv/personal-info` will return personal info
3. `/cv/experience` will return experience info
4. `/cv/education` will return education info 
5. `/cv/skills` will return skills info
6. `/cv/languages` will return languages info