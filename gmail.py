#!/usr/bin/env python3

# import local module
# import pkgutil
# import importlib
# packages = pkgutil.walk_packages(path='./lib/')
# packages = pkgutil.walk_packages(path='.')
# for importer, name, is_package in packages:
#     mod = importlib.import_module(name)

DEBUG_MODE = True
# DEBUG_MODE = False
configFilePath = ('/home/user/.local/gmail_settings.cfg')


import sys
import os
import time
import configparser
import feedparser
import webbrowser
from furl import furl
from urllib.request import FancyURLopener


module_list = [
    "sys",
    "os",
    "time",
    "configparser",
    "feedparser",
    "webbrowser",
    "furl",
    "urllib"
]

# module_list = {
#     'import': 'time',
#     'import': 'configparser',
#     'import': 'feedparser',
#     'import': 'webbrowser',
#     'import': 'furl'
# }

# check in file project
def module_exists(module_name):
    # import sys
    if not module_name in sys.modules.keys():
        print("ImportError: " + module_name)
        # import pip
        # pip.main(['install', module_name])
    else:
        debug_echo("%s -> %s" % ("import", module_name))


# check in system
# NOW OFF
def module_exists_OFF(module_name):
    try:
        __import__(module_name)
        # import module_name
    except ImportError:
        # print("ImportError: " + module_name)
        # raise ImportError("ImportError:", module_name)
        return False
        # import pip
        # pip.main(['install', module_name])
    else:
        debug_echo("%s -> %s" % ("import", module_name))
        return True


def module_import(module_list):
    for item in module_list:
        # debug_echo("%s -> %s" % ("import", item))
        module_exists( item )
        # print ( "%s -> %s" % (item, module_list[item]) )
        # module_exists( module_list[item] )




def debug_echo(msg):
    if DEBUG_MODE == True:
        print('>> ' + msg)
        # log.debug('>>', exc_info=True)
    else:
        return False


def getConfig(configFilePath):
    # import configparser

    debug_echo('reading config file:' + configFilePath)

    # # if not configFilePath:
    # if configFilePath in locals():
    #     print('config file not found')

    config = configparser.ConfigParser()
    config.read(configFilePath)
    try:
        USER = config.get('config', 'user')  # @gmail.com can be left out
        PASSWD = config.get('config', 'passwd')

        url = getMailUrl(USER, PASSWD)
        return url

    except Exception as e:
        print(str(e), ' could not read config file')
        # import sys
        # sys.exit()
        raise


def getMailUrl(user, pwd):
    return 'https://%s:%s@mail.google.com/mail/feed/atom' % (user, pwd)


def sendNoti(head, msg):
    # import os
    return os.system('notify-send "' + head + '" "' + msg + '"')
    # os.system('notify-send "Gmail" "new '+fullcount+' '+ed+'" --urgency=low --icon=mail-forward')


def openRssLink(url):
    # import feedparser
    # import webbrowser
    # from furl import furl

    rss = feedparser.parse(url)
    count = 0
    # debug_echo( "Feed Title %s" % rss.feed.title )

    for entry in rss.entries:
        debug_echo("Title: %s" % entry.title)
        debug_echo("link: %s" % entry.link)

        f = furl(entry.link)
        message_id = f.args['message_id']
        debug_echo("link: %s" % f.args['message_id'])
        # webbrowser.open_new_tab(entry.link)
        webbrowser.open_new_tab(
            "https://mail.google.com/mail/u/0/h/?&v=c&th=" + message_id)

        count += 1
        if int(count) > 10:
            webbrowser.open_new_tab("https://mail.google.com/")
            print('to many open new mail!')
            break
    # return entry.link
    return True


def mailRss(url):
    # from urllib.request import FancyURLopener

    opener = FancyURLopener()
    page = opener.open(url)
    contents = page.read().decode('utf-8')
    # print(contents)

    ifrom = contents.index('<fullcount>') + 11
    ito = contents.index('</fullcount>')

    fullcount = contents[ifrom:ito]

    if int(fullcount) > 0:
        ed = "mail"

        if int(fullcount) > 1:
            ed += "s"

        debug_echo(' ' + fullcount)
        sendNoti('Gmail', fullcount +' '+ ed)

        openRssLink(contents)

    elif int(fullcount) != 0:
        print('gmail format xml is changed')
    else:
        debug_echo('not found new mail')


def checkInetConnect():
    # import os
    # import time
    ## import threading

    hostname = "network"
    reconnect_sec = 10
    response = os.system('ping -c 3 8.8.8.8 -c1 >/dev/null 2>&1')

    if int(response) == 0:
        debug_echo(hostname + ' is up!')
        return True
    else:
        debug_echo(hostname + ' is down!')
        debug_echo("Trying to reconnect in %s seconds" % reconnect_sec )
        time.sleep( reconnect_sec )
        return checkInetConnect()
        # return threading.Timer(2, check_inet).start()


def main():
    try:
        module_import(module_list)

        print('')
        debug_echo('Working...')

        inet_connect = checkInetConnect()
        if inet_connect == True:
            mailurl = getConfig( configFilePath )
            mailRss( mailurl )

    except IOError as err:
        # print("I/O error: {0}".format(err))
        print('IOError error')
        raise
    # except:
    #     print("Fatal error:", sys.exc_info()[0])
        # raise
    # else:
        # print('else!')
    finally:
        debug_echo('done!')
        # sys.exit()

if __name__ == '__main__':
    main()
