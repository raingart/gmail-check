# gmail-check
A small python script to check and open new mail in gmail from RSS

Opportunities and script logic:
- Checking for new email/s
- The conclusion of the system message
- And the opening new mail/s in a browser

### Requirements 
> - python => 2.0
  - configparser
  - urllib
  - feedparser
 
### Installation Instructions
1. Copy file [gmail.py](/gmail.py) OR repo `$ git clone https://github.com/Artlant/gmail-check.git`
2. Make sure the script is executable by running `chmod +x ./gmail.py`
3. Run `$ ./gmail.py`

__//period call script should be implemented you__. For example in linux:
```
watch -n 300./gmail.py
```
where `-n sec` - every sec-seconds

### License 
[![MIT License](https://img.shields.io/badge/license-MIT-007EC7.svg?style=flat-square)](/LICENSE)
