
"""
Export a ResultSet from asking a question as CSV with false for expand_grouped_columns
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

# setup the export_obj kwargs for later
export_kwargs = {}
export_kwargs["export_format"] = u'csv'
export_kwargs["expand_grouped_columns"] = False

# ask the question that will provide the resultset that we want to use
ask_kwargs = {
    'qtype': 'manual_human',
    'sensors': [
        "Computer Name", "IP Route Details", "IP Address",
        'Folder Name Search with RegEx Match{dirname=Program Files,regex=.*Shared.*}',
    ],
}
response = handler.ask(**ask_kwargs)

# export the object to a string
# (we could just as easily export to a file using export_to_report_file)
export_kwargs['obj'] = response['question_results']
export_str = handler.export_obj(**export_kwargs)


print ""
print "print the export_str returned from export_obj():"
if len(out.splitlines()) > 15:
    out = out.splitlines()[0:15]
    out.append('..trimmed for brevity..')
    out = '\n'.join(out)

print out


'''Output from running this:
Handler for Session to 172.16.31.128:444, Authenticated: True, Version: 6.2.314.3258
2014-12-08 16:29:25,976 INFO     question_progress: Results 0% (Get Computer Name and IP Route Details and IP Address and Folder Name Search with RegEx Match[No, Program Files, No, ] from all machines)
2014-12-08 16:29:31,003 INFO     question_progress: Results 0% (Get Computer Name and IP Route Details and IP Address and Folder Name Search with RegEx Match[No, Program Files, No, ] from all machines)
2014-12-08 16:29:36,035 INFO     question_progress: Results 0% (Get Computer Name and IP Route Details and IP Address and Folder Name Search with RegEx Match[No, Program Files, No, ] from all machines)
2014-12-08 16:29:41,062 INFO     question_progress: Results 0% (Get Computer Name and IP Route Details and IP Address and Folder Name Search with RegEx Match[No, Program Files, No, ] from all machines)
2014-12-08 16:29:46,088 INFO     question_progress: Results 0% (Get Computer Name and IP Route Details and IP Address and Folder Name Search with RegEx Match[No, Program Files, No, ] from all machines)
2014-12-08 16:29:51,126 INFO     question_progress: Results 0% (Get Computer Name and IP Route Details and IP Address and Folder Name Search with RegEx Match[No, Program Files, No, ] from all machines)
2014-12-08 16:29:56,153 INFO     question_progress: Results 0% (Get Computer Name and IP Route Details and IP Address and Folder Name Search with RegEx Match[No, Program Files, No, ] from all machines)
2014-12-08 16:30:01,183 INFO     question_progress: Results 0% (Get Computer Name and IP Route Details and IP Address and Folder Name Search with RegEx Match[No, Program Files, No, ] from all machines)
2014-12-08 16:30:06,213 INFO     question_progress: Results 0% (Get Computer Name and IP Route Details and IP Address and Folder Name Search with RegEx Match[No, Program Files, No, ] from all machines)
2014-12-08 16:30:11,240 INFO     question_progress: Results 0% (Get Computer Name and IP Route Details and IP Address and Folder Name Search with RegEx Match[No, Program Files, No, ] from all machines)
2014-12-08 16:30:16,269 INFO     question_progress: Results 0% (Get Computer Name and IP Route Details and IP Address and Folder Name Search with RegEx Match[No, Program Files, No, ] from all machines)
2014-12-08 16:30:21,306 INFO     question_progress: Results 0% (Get Computer Name and IP Route Details and IP Address and Folder Name Search with RegEx Match[No, Program Files, No, ] from all machines)
2014-12-08 16:30:26,331 INFO     question_progress: Results 33% (Get Computer Name and IP Route Details and IP Address and Folder Name Search with RegEx Match[No, Program Files, No, ] from all machines)
2014-12-08 16:30:31,362 INFO     question_progress: Results 100% (Get Computer Name and IP Route Details and IP Address and Folder Name Search with RegEx Match[No, Program Files, No, ] from all machines)

print the export_str returned from export_obj():
Handler for Session to 172.16.31.128:444, Authenticated: True, Version: 6.2.314.3258
2014-12-08 16:28:45,552 INFO     question_progress: Results 0% (Get Computer Name and IP Route Details and IP Address and Folder Name Search with RegEx Match[No, Program Files, No, ] from all machines)
2014-12-08 16:28:50,583 INFO     question_progress: Results 0% (Get Computer Name and IP Route Details and IP Address and Folder Name Search with RegEx Match[No, Program Files, No, ] from all machines)
2014-12-08 16:28:55,610 INFO     question_progress: Results 0% (Get Computer Name and IP Route Details and IP Address and Folder Name Search with RegEx Match[No, Program Files, No, ] from all machines)
2014-12-08 16:29:00,640 INFO     question_progress: Results 17% (Get Computer Name and IP Route Details and IP Address and Folder Name Search with RegEx Match[No, Program Files, No, ] from all machines)
2014-12-08 16:29:05,668 INFO     question_progress: Results 17% (Get Computer Name and IP Route Details and IP Address and Folder Name Search with RegEx Match[No, Program Files, No, ] from all machines)
2014-12-08 16:29:10,699 INFO     question_progress: Results 50% (Get Computer Name and IP Route Details and IP Address and Folder Name Search with RegEx Match[No, Program Files, No, ] from all machines)
2014-12-08 16:29:15,728 INFO     question_progress: Results 67% (Get Computer Name and IP Route Details and IP Address and Folder Name Search with RegEx Match[No, Program Files, No, ] from all machines)
2014-12-08 16:29:20,762 INFO     question_progress: Results 83% (Get Computer Name and IP Route Details and IP Address and Folder Name Search with RegEx Match[No, Program Files, No, ] from all machines)
2014-12-08 16:29:25,794 INFO     question_progress: Results 100% (Get Computer Name and IP Route Details and IP Address and Folder Name Search with RegEx Match[No, Program Files, No, ] from all machines)

print the export_str returned from export_obj():
Handler for Session to 172.16.31.128:444, Authenticated: True, Version: 6.2.314.3258
2014-12-08 16:28:45,385 INFO     handler: Report file '/var/folders/dk/vjr1r_c53yx6k6gzp2bbt_c40000gn/T/SystemSettingsList_2014_12_08-16_28_45-EST.json' written with 327 bytes
Traceback (most recent call last):
..trimmed for brevity..

'''
