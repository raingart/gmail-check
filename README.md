# gmail-check
A small python script to check and open new mail in gmail from RSS

Opportunities and script logic:
- Checking for new email/s
- The conclusion of the system message
- And the opening new mail/s in a browser

### Requirements
> - python => 2.0
  - configparser
  - feedparser
  - urllib
  - furl

```
sudo pip install configparser feedparser furl
```

### Installation Instructions
```
python setup.py install
```
OR
1. Copy file [gmail.py](/gmail.py) OR repo `$ git clone https://github.com/Artlant/gmail-check.git`
2. Make sure the script is executable by running `chmod +x ./gmail.py`
3. Run `$ ./gmail.py`
4. Change in `gmail_config.cfg` you `login` and `pass` from gmail account
5. Change in file `gmail.py` variable `configFilePath` from you path conf
6. (optional) Change variable `DEBUG_MODE` = `True`/`False`  in `gmail.py`

### Start arguments
```
./gmail.py -h
usage: gmail.py [-h] [-l] [-c CONFIG]

optional arguments:
  -h, --help              show this help message and exit
  -l, --log               show log info
  -c file, --config file  patch to a config file
```

__//period call script should be implemented you__. For example in linux:
```
watch -n 300./gmail.py
```
where `-n sec` - every sec-seconds

### License
[![MIT License](https://img.shields.io/badge/license-MIT-007EC7.svg?style=flat-square)](/LICENSE)
