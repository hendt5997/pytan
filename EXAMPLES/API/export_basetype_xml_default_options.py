
"""
Export a BaseType from getting objects as XML with the default options
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
export_kwargs["export_format"] = u'xml'

# get the objects that will provide the basetype that we want to use
get_kwargs = {
    'name': [
        "Computer Name", "IP Route Details", "IP Address",
        'Folder Name Search with RegEx Match',
    ],
    'objtype': 'sensor',
}
response = handler.get(**get_kwargs)

# export the object to a string
# (we could just as easily export to a file using export_to_report_file)
export_kwargs['obj'] = response
export_str = handler.export_obj(**export_kwargs)


print ""
print "print the export_str returned from export_obj():"

out = export_str
if len(out.splitlines()) > 15:
    out = out.splitlines()[0:15]
    out.append('..trimmed for brevity..')
    out = '\n'.join(out)

print out


'''Output from running this:
Handler for Session to 172.16.31.128:444, Authenticated: True, Version: 6.2.314.3258

print the export_str returned from export_obj():
<sensors><cache_info /><sensor><category>Reserved</category><preview_sensor_flag /><hash>3409330187</hash><name>Computer Name</name><hidden_flag>0</hidden_flag><delimiter /><creation_time /><exclude_from_parse_flag>0</exclude_from_parse_flag><last_modified_by /><string_count>7</string_count><source_hash /><modification_time /><ignore_case_flag>1</ignore_case_flag><max_age_seconds>86400</max_age_seconds><value_type>String</value_type><cache_row_id /><source_id>0</source_id><deleted_flag /><parameter_definition /><id>3</id><description>The assigned name of the client machine.
Example: workstation-1.company.com</description><string_hints /><subcolumns /><metadata /><parameters /><queries><query><platform>Windows</platform><script_type>WMIQuery</script_type><signature /><script>select CSName from win32_operatingsystem</script></query></queries></sensor><sensor><category>Network</category><preview_sensor_flag /><hash>435227963</hash><name>IP Route Details</name><hidden_flag>0</hidden_flag><delimiter>|</delimiter><creation_time>2014-12-08T19:20:42</creation_time><exclude_from_parse_flag>1</exclude_from_parse_flag><last_modified_by>Jim Olsen</last_modified_by><string_count>49</string_count><source_hash /><modification_time>2014-12-08T19:20:42</modification_time><ignore_case_flag>1</ignore_case_flag><max_age_seconds>60</max_age_seconds><value_type>String</value_type><cache_row_id /><source_id>0</source_id><deleted_flag /><parameter_definition /><id>737</id><description>Returns IPv4 network routes, filtered to exclude noise. With Flags, Metric, Interface columns.
Example:  172.16.0.0|192.168.1.1|255.255.0.0|UG|100|eth0</description><string_hints /><subcolumns><subcolumn><index>0</index><name>Destination</name><ignore_case_flag>1</ignore_case_flag><exclude_from_parse_flag /><hidden_flag>0</hidden_flag><value_type>IPAddress</value_type></subcolumn><subcolumn><index>1</index><name>Gateway</name><ignore_case_flag>1</ignore_case_flag><exclude_from_parse_flag /><hidden_flag>0</hidden_flag><value_type>IPAddress</value_type></subcolumn><subcolumn><index>2</index><name>Mask</name><ignore_case_flag>1</ignore_case_flag><exclude_from_parse_flag /><hidden_flag>0</hidden_flag><value_type>String</value_type></subcolumn><subcolumn><index>3</index><name>Flags</name><ignore_case_flag>1</ignore_case_flag><exclude_from_parse_flag /><hidden_flag>0</hidden_flag><value_type>String</value_type></subcolumn><subcolumn><index>4</index><name>Metric</name><ignore_case_flag>1</ignore_case_flag><exclude_from_parse_flag /><hidden_flag>0</hidden_flag><value_type>NumericInteger</value_type></subcolumn><subcolumn><index>5</index><name>Interface</name><ignore_case_flag>1</ignore_case_flag><exclude_from_parse_flag /><hidden_flag>0</hidden_flag><value_type>String</value_type></subcolumn></subcolumns><metadata><item><admin_flag>0</admin_flag><name>defined</name><value>Tanium</value></item></metadata><parameters /><queries><query><platform>Windows</platform><script_type>VBScript</script_type><signature /><script>strComputer = &amp;quot;.&amp;quot;
Set objWMIService = GetObject(&amp;quot;winmgmts:&amp;quot; _
    &amp;amp; &amp;quot;{impersonationLevel=impersonate}!\\&amp;quot; &amp;amp; strComputer &amp;amp; &amp;quot;\root\cimv2&amp;quot;)

Set collip = objWMIService.ExecQuery(&amp;quot;select * from win32_networkadapterconfiguration where IPEnabled=&amp;#039;True&amp;#039;&amp;quot;)
dim ipaddrs()
ipcount = 0
for each ipItem in collip
    for each ipaddr in ipItem.IPAddress
        ipcount = ipcount + 1
    next
next
redim ipaddrs(ipcount)
..trimmed for brevity..

'''
