Create Package From JSON Readme
===========================

---------------------------
<a name='toc'>Table of contents:</a>

  * [Help for Create Package From JSON](#user-content-help-for-create-package-from-json)
  * [Export package id 1 as JSON](#user-content-export-package-id-1-as-json)
  * [Change name or url_regex in the JSON](#user-content-change-name-or-url_regex-in-the-json)
  * [Create a new package from the modified JSON file](#user-content-create-a-new-package-from-the-modified-json-file)

---------------------------

# Help for Create Package From JSON

  * Print the help for create_package_from_json.py
  * All scripts in bin/ will supply help if -h is on the command line
  * If passing in a parameter with a space or a special character, you need to surround it with quotes properly. On Windows this means double quotes. On Linux/Mac, this means single or double quotes, depending on what kind of character escaping you need.
  * If running this script on Linux or Mac, use the python scripts directly as the bin/create_package_from_json.py
  * If running this script on Windows, use the batch script in the winbin/create_package_from_json.bat so that python is called correctly.

```bash
create_package_from_json.py -h
```

```
usage: create_package_from_json.py [-h] [-u USERNAME] [-p PASSWORD]
                                   [--session_id SESSION_ID] [--host HOST]
                                   [--port PORT] [-l LOGLEVEL] [--debugformat]
                                   [--record_all_requests]
                                   [--stats_loop_enabled] [--http_auth_retry]
                                   [--http_retry_count HTTP_RETRY_COUNT] -j
                                   JSON_FILE

Create an object of type: package from a JSON file

optional arguments:
  -h, --help            show this help message and exit

Handler Authentication:
  -u USERNAME, --username USERNAME
                        Name of user (default: None)
  -p PASSWORD, --password PASSWORD
                        Password of user (default: None)
  --session_id SESSION_ID
                        Session ID to authenticate with instead of
                        username/password (default: None)
  --host HOST           Hostname/ip of SOAP Server (default: None)
  --port PORT           Port to use when connecting to SOAP Server (default:
                        443)

Handler Options:
  -l LOGLEVEL, --loglevel LOGLEVEL
                        Logging level to use, increase for more verbosity
                        (default: 0)
  --debugformat         Enable debug format for logging (default: False)
  --record_all_requests
                        Record all requests in
                        handler.session.ALL_REQUESTS_RESPONSES (default:
                        False)
  --stats_loop_enabled  Enable the statistics loop (default: False)
  --http_auth_retry     Disable retry on HTTP authentication failures
                        (default: True)
  --http_retry_count HTTP_RETRY_COUNT
                        Retry count for HTTP failures/invalid responses
                        (default: 5)

Create Package from JSON Options:
  -j JSON_FILE, --json JSON_FILE
                        JSON file to use for creating the object (default: )
```

  * Validation Test: exitcode
    * Valid: **True**
    * Messages: Exit Code is 0

  * Validation Test: noerror
    * Valid: **True**
    * Messages: No error texts found in stderr/stdout



[TOC](#user-content-toc)


# Export package id 1 as JSON

  * Get the first package object
  * Save the results to a JSON file

```bash
bin/get_package.py -u Administrator -p 'Tanium2015!' --host 10.0.1.240 --loglevel 1 --id 1 --file "/tmp/out.json" --export_format json
```

```
PyTan v2.1.0 Handler for Session to 10.0.1.240:443, Authenticated: True, Platform Version: 6.5.314.4301
Found items:  PackageSpecList, len: 1
Report file '/tmp/out.json' written with 2688 bytes
```

  * Validation Test: exitcode
    * Valid: **True**
    * Messages: Exit Code is 0

  * Validation Test: file_exist_contents
    * Valid: **True**
    * Messages: File /tmp/out.json exists, content:

```
{
  "_type": "package_specs", 
  "package_spec": [
    {
      "_type": "package_spec", 
      "available_time": "2015-08-26T20:15:17", 
      "command": "cmd /c cscript //T:900 java-installer.vbs /KillAppsUsingJava:Yes /RebootIfNeeded:Yes /MaxWaitTimeInSeconds:300", 
      "command_timeout": 900, 
      "creation_time": "2015-08-26T20:14:33", 
      "deleted_flag": 0, 
...trimmed for brevity...
```

  * Validation Test: noerror
    * Valid: **True**
    * Messages: No error texts found in stderr/stdout



[TOC](#user-content-toc)


# Change name or url_regex in the JSON

  * Add CMDLINE TEST to name or url_regex in the JSON file

```bash
perl -p -i -e 's/^(      "(name|url_regex)": ".*)"/$1 CMDLINE TEST 3179"/gm' /tmp/out.json && cat /tmp/out.json
```

```
{
  "_type": "package_specs", 
  "package_spec": [
    {
      "_type": "package_spec", 
      "available_time": "2015-08-26T20:15:17", 
      "command": "cmd /c cscript //T:900 java-installer.vbs /KillAppsUsingJava:Yes /RebootIfNeeded:Yes /MaxWaitTimeInSeconds:300", 
      "command_timeout": 900, 
      "creation_time": "2015-08-26T20:14:33", 
      "deleted_flag": 0, 
      "display_name": "Update Java 64-bit - Kill / Reboot", 
      "expire_seconds": 1500, 
      "files": {
        "_type": "package_files", 
        "file": [
          {
            "_type": "file", 
            "bytes_downloaded": 22900, 
            "bytes_total": 22900, 
            "cache_status": "Cached", 
            "download_seconds": 0, 
            "download_start_time": "2015-08-26T20:14:56", 
            "file_status": {
              "_type": "file_status", 
              "status": [
                {
                  "_type": "status", 
                  "bytes_downloaded": 22900, 
                  "bytes_total": 22900, 
                  "cache_status": "Cached", 
                  "download_start_time": "2015-08-26T20:14:56", 
                  "last_download_progress_time": "2015-08-26T20:15:28", 
                  "server_id": 1, 
                  "server_name": "TPT1-0.localdomain:17472", 
                  "status": 52
                }
              ]
            }, 
            "hash": "19930421efb5b9ed3725aabcf1580eb04d1c3c355ac0e05123f5b162f29928f7", 
            "id": 1, 
            "last_download_progress_time": "2015-08-26T20:15:28", 
            "name": "java-installer.vbs", 
            "size": 22900, 
            "source": "https://content.tanium.com/files/published/InitialContent/2015-06-04_18-59-45_6.5.1.0011-ga516c3c/update_java_64-bit_-_kill_-_reboot/java-installer.vbs", 
            "status": 52
          }
        ]
      }, 
      "hidden_flag": 0, 
      "id": 1, 
      "last_modified_by": "Administrator", 
      "last_update": "2015-08-26T20:14:33", 
      "metadata": {
        "_type": "metadata", 
        "item": [
          {
            "_type": "item", 
            "admin_flag": 0, 
            "name": "defined", 
            "value": "Tanium"
          }, 
          {
            "_type": "item", 
            "admin_flag": 0, 
            "name": "category", 
            "value": "Tanium"
          }
        ]
      }, 
      "modification_time": "2015-08-26T20:14:33", 
      "name": "Update Java 64-bit - Kill / Reboot CMDLINE TEST 3179", 
      "skip_lock_flag": 0, 
      "source_id": 0, 
      "verify_expire_seconds": 600, 
      "verify_group": {
        "_type": "group", 
        "id": 0
      }, 
      "verify_group_id": 0
    }
  ]
}
```

  * Validation Test: exitcode
    * Valid: **True**
    * Messages: Exit Code is 0

  * Validation Test: file_exist
    * Valid: **True**
    * Messages: File /tmp/out.json exists

  * Validation Test: noerror
    * Valid: **True**
    * Messages: No error texts found in stderr/stdout



[TOC](#user-content-toc)


# Create a new package from the modified JSON file

```bash
bin/create_package_from_json.py -u Administrator -p 'Tanium2015!' --host 10.0.1.240 --loglevel 1 -j "/tmp/out.json"
```

```
PyTan v2.1.0 Handler for Session to 10.0.1.240:443, Authenticated: True, Platform Version: 6.5.314.4301
Created item: PackageSpec, name: 'Update Java 64-bit - Kill / Reboot CMDLINE TEST 3179', id: 404, ID: 404
```

  * Validation Test: exitcode
    * Valid: **True**
    * Messages: Exit Code is 0

  * Validation Test: noerror
    * Valid: **True**
    * Messages: No error texts found in stderr/stdout



[TOC](#user-content-toc)


###### generated by: `build_bin_doc v2.1.0`, date: Thu Sep  3 21:50:21 2015 EDT, Contact info: **Jim Olsen <jim.olsen@tanium.com>**