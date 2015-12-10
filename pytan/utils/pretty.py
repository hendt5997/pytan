#!/usr/bin/env python
# -*- mode: Python; tab-width: 4; indent-tabs-mode: nil; -*-
# ex: set tabstop=4
# Please do not change the two lines above. See PEP 8, PEP 263.
"""Prettifying module for :mod:`pytan`"""

import logging
import json
from .external import xmltodict

mylog = logging.getLogger(__name__)


def jsonify(v, indent=2, sort_keys=True):
    """Turns python object `v` into a pretty printed JSON string

    Parameters
    ----------
    v : object
        * python object to convert to JSON

    indent : int, 2
        * number of spaces to indent JSON string when pretty printing

    sort_keys : bool, True
        * sort keys of JSON string when pretty printing

    Returns
    -------
    str :
        * JSON pretty printed string
    """
    return json.dumps(v, indent=indent, sort_keys=sort_keys)


def log_session(h):
    """Uses :func:`xml_pretty` to pretty print the last request and response bodies from the
    session object in h to the logging system

    Parameters
    ----------
    h : Handler object
        * Handler object with session object containing last request and response body
    """
    response_obj = h.session.LAST_REQUESTS_RESPONSE
    request_body = response_obj.request.body
    response_body = response_obj.text

    try:
        req = xml_pretty(request_body)
    except Exception as e:
        req = "Failed to prettify xml: {}, raw xml:\n{}".format(e, request_body)

    mylog.debug("Last HTTP request:\n{}".format(req))

    try:
        resp = xml_pretty(response_body)
    except Exception as e:
        resp = "Failed to prettify xml: {}, raw xml:\n{}".format(e, response_body)

    mylog.debug("Last HTTP response:\n{}".format(xml_pretty(resp)))


def xml_pretty(x, pretty=True, indent='  ', **kwargs):
    """Uses :mod:`xmltodict` to pretty print an XML str `x`

    Parameters
    ----------
    x : str
        * XML string to pretty print

    Returns
    -------
    str :
        * The pretty printed string of `x`
    """

    x_parsed = xmltodict.parse(x)
    x_unparsed = xmltodict.unparse(x_parsed, pretty=pretty, indent=indent)
    return x_unparsed


def xml_pretty_resultxml(x):
    """Uses :mod:`xmltodict` to pretty print an the ResultXML element in XML str `x`

    Parameters
    ----------
    x : str
        * XML string to pretty print

    Returns
    -------
    str :
        * The pretty printed string of ResultXML in `x`
    """

    x_parsed = xmltodict.parse(x)
    x_find = x_parsed["soap:Envelope"]["soap:Body"]["t:return"]["ResultXML"]
    x_unparsed = xml_pretty(x_find)
    return x_unparsed


def xml_pretty_resultobj(x):
    """Uses :mod:`xmltodict` to pretty print an the result-object element in XML str `x`

    Parameters
    ----------
    x : str
        * XML string to pretty print

    Returns
    -------
    str :
        * The pretty printed string of result-object in `x`
    """

    x_parsed = xmltodict.parse(x)
    x_find = x_parsed["soap:Envelope"]["soap:Body"]["t:return"]
    x_find = x_parsed["result-object"]
    x_unparsed = xmltodict.unparse(x_find, pretty=True, indent='  ')
    return x_unparsed
