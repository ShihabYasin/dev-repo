
A docker-compose file with 4 different flask python  services named "up", "collect" ,  "day_provider", month_provider. 

"up" is a GET rest api accessible from host at 7100 port with a json payload { "data": "value" } , value can be "day" or "month". 

"collect" ,  "day_provider" and  "month_provider" are not accessible from host machine. 

"up" calls "collect" service at its port 7101 that will provide current day or month based on "value" from json payload { "data": "value" }. "value" could be "day" or "month". If  "value" is "day" then "collect" service will call "day_provider" . If  "value" is "month" then "collect" service will call "month_provider" service. 

"collect" will communicate with "day_provider" service at its("day_provider" container) port 7102 or "month_provider" at its("month_provider" container) port 7103. 


"day_provider" will return a json like { "day": "name of the day of the week" }.  

"month_provider" will return a json like { "month": "name of themonth of the year" }. 

"collect" will return a json like:
{ 
"data": 
{"json data fetched from related provider service "}
}


# How to run: 
1. run fresh_build: in Makefile
2. Use postman GET:  http://localhost:7100/

```json
{
    "data": "month"
}
```

or

```json
{
    "data": "day"
}
```