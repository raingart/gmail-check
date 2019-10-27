# gmail-check
Python script to check for new unread GMAIL mail. And the subsequent opening of it in the browser

Opportunities and script logic:
- Checking for new email/s
- The conclusion of the system message
- And the opening new mail/s in a browser

### Requirements
> - python => 3.0
  - configparser
  - feedparser
  - urllib

### Installation Instructions
1. Copy files [gmail.py](/gmail.py), [conf](/gmail.cfg)
2. Make sure the script is executable by running `chmod +x ./gmail.py`
3. Change in `gmail.cfg` you `login` and `pass` from gmail account
4. (optional) Change in file `gmail.py` variable `configFilePath` from you path conf
5. Open https://myaccount.google.com/lesssecureapps and set `Allow less secure apps: ON`
6. Run `$ ./gmail.py`

### Start arguments
```
./gmail.py -h
usage: gmail.py [-h] [-d] [-c CONFIG]

optional arguments:
  -h, --help              show this help message and exit
  -d, --debug             show log info
  -c file, --config file  patch to a config file
```

__//period call script should be implemented you__. For example in linux:
```
watch -n 300./gmail.py
```
where `-n sec` - every sec-seconds

### License
[![MIT License](https://img.shields.io/badge/license-MIT-007EC7.svg?style=flat-square)](/LICENSE)
