# PowerdByIllia
Software Switch

## How to run:
```bash
python -m app
```

>if you run it on linux, you need to run it as root

## How to push restconf requests:

Autorization is required.

>username: **_myusername_**,
password: **_mypassword_**

### State:
- state:Get
```
curl --location --request GET 'http://127.0.0.1:8000/restconf/state' \
--header 'Content-Type: application/yang.data+json' \
--header 'Authorization: Basic bXl1c2VybmFtZTpteXBhc3N3b3Jk' \
--data '{
    "name" : "str",
    "state" : ""
}'
```
- state:Put
```
curl --location --request PUT 'http://127.0.0.1:8000/restconf/state' \
--header 'Content-Type: application/yang.data+json' \
--header 'Authorization: Basic bXl1c2VybmFtZTpteXBhc3N3b3Jk' \
--data '{
    "name" : "str",
    "state" : "down or up"
}'
```

### Hostname:
- hostname:Get
```
curl --location --request GET 'http://127.0.0.1:8000/restconf/hostname' \
--header 'Content-Type: application/yang.data+json' \
--header 'Authorization: Basic bXl1c2VybmFtZTpteXBhc3N3b3Jk' \
--data '{
    "name" : ""
}'
```
- hostname:Put
```
curl --location --request PUT 'http://127.0.0.1:8000/restconf/hostname' \
--header 'Content-Type: application/yang.data+json' \
--header 'Authorization: Basic bXl1c2VybmFtZTpteXBhc3N3b3Jk' \
--data '{
    "name" : "str"
}'
```

### Mac Timer:

In request body you need to specify max_age in seconds. Even if it wont take it, there must be a field with any int value.
In return you will get timer in seconds.

- mac_timer:Get
```
curl --location --request GET 'http://127.0.0.1:8000/restconf/mac_timer' \
--header 'Content-Type: application/yang.data+json' \
--header 'Authorization: Basic bXl1c2VybmFtZTpteXBhc3N3b3Jk' \
--data '{
    "max_age" : "int"
}'
```
- mac_timer:Put
```
curl --location --request PUT 'http://127.0.0.1:8000/restconf/mac_timer' \
--header 'Content-Type: application/yang.data+json' \
--header 'Authorization: Basic bXl1c2VybmFtZTpteXBhc3N3b3Jk' \
--data '{
    "max_age" : "int"
}'
```

### Interface name:
- interface_name:Get
```
curl --location --request GET 'http://127.0.0.1:8000/restconf/interface_name' \
--header 'Content-Type: application/yang.data+json' \
--header 'Authorization: Basic bXl1c2VybmFtZTpteXBhc3N3b3Jk' \
--data '{
    "name": "",
    "state": "all or up or down"
}'
```
- interface_name:Put
```
curl --location --request PUT 'http://127.0.0.1:8000/restconf/interface_name' \
--header 'Content-Type: application/yang.data+json' \
--header 'Authorization: Basic bXl1c2VybmFtZTpteXBhc3N3b3Jk' \
--data '{
    "interface": "str",
    "name": "str"
}'
```