
"""
Get an action by name (name is not a supported selector for action)
"""
# Path to lib directory which contains pytan package
PYTAN_LIB_PATH = '../lib'

# connection info for Tanium Server
USERNAME = "Tanium User"
PASSWORD = "T@n!um"
HOST = "172.16.31.128"
PORT = "444"

# Logging conrols
LOGLEVEL = 2
DEBUGFORMAT = False

import sys, tempfile
sys.path.append(PYTAN_LIB_PATH)

import pytan
handler = pytan.Handler(
    username=USERNAME,
    password=PASSWORD,
    host=HOST,
    port=PORT,
    loglevel=LOGLEVEL,
    debugformat=DEBUGFORMAT,
)

print handler

# setup the arguments for the handler method
kwargs = {}
kwargs["objtype"] = u'action'
kwargs["name"] = u'Distribute Tanium Standard Utilities'


# call the handler with the get method, passing in kwargs for arguments
# this should throw an exception: pytan.utils.HandlerError
import traceback
try:
    handler.get(**kwargs)
except Exception as e:
    traceback.print_exc(file=sys.stdout)



'''Output from running this:
Handler for Session to 172.16.31.128:444, Authenticated: True, Version: 6.2.314.3258
Traceback (most recent call last):
  File "<string>", line 39, in <module>
  File "/Users/jolsen/gh/pytan/lib/pytan/handler.py", line 1562, in get
    raise HandlerError(err(objtype, api_attrs))
HandlerError: Getting a action requires at least one filter: ['id']

'''
