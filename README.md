# PowerdByIllia
Software Switch

## How to run:
```bash
python -m app
```
for dev:
```bash
uvicorn app.__main__:app --reload
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
    "name": "str",
    "state": ""
}'
```

### To create python classes based on yang models:

First, install virtualenv:
```bash
pip install virtualenv
```

Then, run it:
```bash
source env/bin/activate
```
Install pyangbind and pyang:
```bash
pip install pyang pyangbind
```

To create python classes based on yang models, run from project directory:
```bash
export PYBINDPLUGIN=`path/to/project/env/bin/python -c \
> 'import pyangbind; import os; print ("{}/plugin".format(os.path.dirname(pyangbind.__file__)))'`
```
- mac:
```bash
pyang -p templates/yang_models/ --plugindir $PYBINDPLUGIN -f pybind -o templates/yang_py/sw_mac_table.py templates/yang_models/mac-table.yang
```
- interface:
```bash
pyang --plugindir $PYBINDPLUGIN -f pybind -o templates/yang_py/sw_interface.py templates/yang_models/interface.yang
```


