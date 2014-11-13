
# Copyright (c) 2014 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class SensorList(BaseType):

    _OBJECT_LIST_TAG = 'sensors'

    def __init__(self):
        BaseType.__init__(
            self,
            soap_tag='sensors',
            simple_properties={},
            complex_properties={'cache_info': CacheInfo},
            list_properties={'sensor': Sensor},
        )
        
        self.cache_info = None
        self.sensor = []

from sensor import Sensor
from cache_info import CacheInfo

