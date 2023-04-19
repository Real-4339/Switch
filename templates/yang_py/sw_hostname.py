# -*- coding: utf-8 -*-
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import TypedListType
from pyangbind.lib.yangtypes import YANGBool
from pyangbind.lib.yangtypes import YANGListType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import ReferenceType
from pyangbind.lib.base import PybindBase
from collections import OrderedDict
from decimal import Decimal
from bitarray import bitarray
import six

# PY3 support of some PY2 keywords (needs improved)
if six.PY3:
  import builtins as __builtin__
  long = int
elif six.PY2:
  import __builtin__

class yc_switch_sw_hostname__switch(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module sw_hostname - based on the path /switch. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_path_helper', '_extmethods', '__hostname',)

  _yang_name = 'switch'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__hostname = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="hostname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:sw-hostname', defining_module='sw_hostname', yang_type='string', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return ['switch']

  def _get_hostname(self):
    """
    Getter method for hostname, mapped from YANG variable /switch/hostname (string)
    """
    return self.__hostname
      
  def _set_hostname(self, v, load=False):
    """
    Setter method for hostname, mapped from YANG variable /switch/hostname (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hostname is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hostname() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="hostname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:sw-hostname', defining_module='sw_hostname', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hostname must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="hostname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:sw-hostname', defining_module='sw_hostname', yang_type='string', is_config=True)""",
        })

    self.__hostname = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hostname(self):
    self.__hostname = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="hostname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:sw-hostname', defining_module='sw_hostname', yang_type='string', is_config=True)

  hostname = __builtin__.property(_get_hostname, _set_hostname)


  _pyangbind_elements = OrderedDict([('hostname', hostname), ])


class sw_hostname(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module sw_hostname - based on the path /sw_hostname. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_path_helper', '_extmethods', '__switch',)

  _yang_name = 'sw_hostname'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__switch = YANGDynClass(base=yc_switch_sw_hostname__switch, is_container='container', yang_name="switch", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:sw-hostname', defining_module='sw_hostname', yang_type='container', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return []

  def _get_switch(self):
    """
    Getter method for switch, mapped from YANG variable /switch (container)
    """
    return self.__switch
      
  def _set_switch(self, v, load=False):
    """
    Setter method for switch, mapped from YANG variable /switch (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_switch is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_switch() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=yc_switch_sw_hostname__switch, is_container='container', yang_name="switch", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:sw-hostname', defining_module='sw_hostname', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """switch must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=yc_switch_sw_hostname__switch, is_container='container', yang_name="switch", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:sw-hostname', defining_module='sw_hostname', yang_type='container', is_config=True)""",
        })

    self.__switch = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_switch(self):
    self.__switch = YANGDynClass(base=yc_switch_sw_hostname__switch, is_container='container', yang_name="switch", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:sw-hostname', defining_module='sw_hostname', yang_type='container', is_config=True)

  switch = __builtin__.property(_get_switch, _set_switch)


  _pyangbind_elements = OrderedDict([('switch', switch), ])


