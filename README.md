# PowerdByIllia
Software Switch

### To create python classes based on yang models:

First, install virtualenv:
```
pip install virtualenv
```

Then, run it:
```
source env/bin/activate
```
Install pyangbind and pyang:
```
pip install pyang pyangbind
```

To create python classes based on yang models, run:
```
export PYBINDPLUGIN=`path/to/project/env/bin/python -c \
> 'import pyangbind; import os; print ("{}/plugin".format(os.path.dirname(pyangbind.__file__)))'`
```
- mac:
```
pyang -p templates/yang_models/ --plugindir $PYBINDPLUGIN -f pybind -o templates/yang_py/sw_mac_table.py templates/yang_models/mac-table.yang
```
- interface:
```
pyang --plugindir $PYBINDPLUGIN -f pybind -o templates/yang_py/sw_interface.py templates/yang_models/interface.yang
```


