
# Copyright (c) 2014 Tanium Inc
#
# Generated from console.wsdl version 0.0.1     
#
#

from .base import BaseType


class WhiteListedUrl(BaseType):

    _OBJECT_LIST_TAG = 'white_listed_url'

    def __init__(self):
        BaseType.__init__(
            self,
            soap_tag='white_listed_url',
            simple_properties={'id': int,
                        'chunk_id': str,
                        'download_seconds': int,
                        'url_regex': str},
            complex_properties={'metadata': MetadataList},
            list_properties={},
        )
        self.id = None
        self.chunk_id = None
        self.download_seconds = None
        self.url_regex = None
        self.metadata = None
        

from metadata_list import MetadataList

