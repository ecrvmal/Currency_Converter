# CURRENCY CONVERTER CALCULATOR

The program provides API for currency calculation. 
HTTP  GET example: http://127.0.0.1:8000/api/rates?from=USD&to=RUB&value=4 
It request data from site https://api.api-ninjas.com  
and returns data as dict {"result": 386.69}

The test project 

## Stack

- Python > 3.7
  - requests
  - Django
  - django-ninja
  - Docker
  - docker-compose

## License:

MIT

## Run Program

1. install and run docker, docker-compose
2. cd to project directory
3. run 
```shell
docker-compose build
```
4. run 
```shell
docker-compose up -d
```
5. write in browser address-string(example): 
```shell
http://127.0.0.1:8000/api/rates?from=USD&to=RUB&value=4
```

## Listing program

PS D:\ecrvmal\Currency_Converter> docker-compose up\
[+] Running 1/0\
✔ Container currency_converter-app1-1  Created                     \                                               0.0s 
Attaching to currency_converter-app1-1 \
currency_converter-app1-1  | Watching for file changes with StatReloader \
currency_converter-app1-1  | Performing system checks... \
currency_converter-app1-1  | \
currency_converter-app1-1  | \
currency_converter-app1-1  | System check identified no issues (0 silenced). \
currency_converter-app1-1  | \
currency_converter-app1-1  | You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions. \
currency_converter-app1-1  | Run 'python manage.py migrate' to apply them. \
currency_converter-app1-1  | \
currency_converter-app1-1  | September 15, 2023 - 06:06:04 \
currency_converter-app1-1  | Django version 4.2.5, using settings 'config.settings' \
currency_converter-app1-1  | Starting development server at http://0.0.0.0:8000/\
currency_converter-app1-1  | Quit the server with CONTROL-C. \
currency_converter-app1-1  | \
currency_converter-app1-1  |\
