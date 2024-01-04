# Monitoring system

## Requirements


* [Requirements file](requirements.txt)
* Python 3.10.13v (Anaconda)
* Mysql DB

## To start
1. Install dependecies


``` bash
$ cd mqtt-test
$ pip install -r requirements.txt
```

2. Create a database and a table (Mysql)
3. [Change the .env file](src/connections/db/.env)
3. To launch the project, run the following commands:


``` bash
$ cd mqtt-test/src
$ python init.py
```