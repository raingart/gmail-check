# gmail-check
Python script to check for new unread GMAIL mail. And the subsequent opening of it in the browser

Opportunities and script logic:
- Checking for new email/s
- (Optional) The conclusion of the system message
- And the opening new mail/s in a browser

### Requirements (for run [gmail.py](/gmail.py))
> - python => 3.0

### Installation for Windows
1. open https://myaccount.google.com/lesssecureapps and set `Allow less secure apps: ON`
2. Copy file [gmail.exe](/gmail.exe) and [gmail.cfg](/gmail.cfg)
3. Change in `gmail.cfg` you `login` and `pass` from gmail account
4. Run [gmail.exe](/gmail.exe)
5. (Optional) Run `add task.bat` as __Administrator option__.

#### (Optional) Compile for Windows:
1. Install Python => 3.6
1. Copy repo `$ git clone https://github.com/Artlant/gmail-check.git`
2. Run `$ pip install -r requirements.txt` in `gmail-check` folder
3. Install [Auto PY to EXE](https://github.com/brentvollebregt/auto-py-to-exe)
4. Convert [gmail.py](/gmail.py) in "Auto PY to EXE and Convert"

### Installation for Linux
1. Copy repo `$ git clone https://github.com/Artlant/gmail-check.git`
2. Run `$ pip install -r requirements.txt`
3. open https://myaccount.google.com/lesssecureapps and set `Allow less secure apps: ON`
4. Make sure the script is executable by running `chmod +x ./gmail.py`
5. Change in `gmail.cfg` you `login` and `pass` from gmail account
6. Run `$ ./gmail.py`

__//period call script should be implemented you__. For example in linux:
```
watch -n 300./gmail.py
```
where `-n sec` - every sec-seconds


### Start arguments
```
./gmail.py -h
usage: gmail.py [-h] [-l] [-c CONFIG]

optional arguments:
  -h, --help              show this help message and exit
  -l, --log               show log info
  -c file, --config file  patch to a config file
```

### License
[![MIT License](https://img.shields.io/badge/license-MIT-007EC7.svg?style=flat-square)](/LICENSE)
