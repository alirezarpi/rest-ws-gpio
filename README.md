# rest-ws-gpio
Simple RESTful Web Service for Controling Raspberry pi GPIO(s)

This project is using JSON for communication and controling each gpio with '0' or '1' in 'data' value.

### Working with it

You can send POST request to http://url/api/ to control GPIO like this:

```
{
        "data": "101",
        "user": "Alireza"
}
```

And the Response is (201 Created):

```
{
    "id": 96,
    "data": "101",
    "user": "Alireza",
    "date": "2018-10-29T12:44:08.994750Z"
}
```

The response will be saved into postgreSQL database.

For authenticating users I used nginx auth_basic ( The project has no Authentication or Authorization ).

Or you can send GET request to get all of objects in the database.

**Note:** This project is not really recommended for production purposes due to its simplicity :)

###### _ARRC = AlirezaRpi Remote Control_
