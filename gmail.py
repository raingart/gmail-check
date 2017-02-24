#!/usr/bin/env python3

# import local module
# import pkgutil
# import importlib
# packages = pkgutil.walk_packages(path='./lib/')
# packages = pkgutil.walk_packages(path='.')
# for importer, name, is_package in packages:
#     mod = importlib.import_module(name)

# DEBUG_MODE = True
DEBUG_MODE = False
config_file_path = ('/home/art/.local/gmail_config.cfg')


import sys
import os
import time
import configparser
import feedparser
import webbrowser
from furl import furl
from urllib.request import FancyURLopener

# module_list_dependence=''
module_list_dependence = [
    "pip",
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


def module_exists_local(module_name):
    # import sys
    if not module_name in sys.modules.keys():
        print("local ImportError: " + module_name)
        # print("ImportError: " + module_name)
        # import pip
        # pip.main(['install', module_name])
    else:
        debug_echo('%s -> %s' % ("import", module_name))


# check in system
def module_exists_sys(module_name):
    try:
        __import__(module_name)
        # import module_name
    except ImportError:
        print("pip install: " + module_name)
        # import pip
        # pip.main(['install', '--user', module_name])
        # import module_name
        # return False


def module_import(module_list=False):
    if not module_list:
        print("module_list_dependence not exist")
        return False

    for item in module_list:
        # debug_echo("%s -> %s" % ("import", item))
        module_exists_sys(item)
        module_exists_local(item)
        # print ( "%s -> %s" % (item, module_list[item]) )
        # module_exists( module_list[item] )


def debug_echo(msg="test msg"):
    if DEBUG_MODE:
        print(">> " + msg)
        # log.debug('>>', exc_info=True)
    else:
        return False


def get_config(config_file_path="./gmail_config.cfg"):
    # import configparser

    debug_echo("reading config file:" + config_file_path)

    # if not config_file_path:
    # if config_file_path in locals():
    # print('config file not found')
    try:
        config = configparser.ConfigParser()
        config.read(config_file_path)

        USER = config.get('profile', 'user')  # @gmail.com can be left out
        PASSWD = config.get('profile', 'passwd')

        url = get_mail_url(USER, PASSWD)
        return url

    except Exception as e:
        raise print(str(e), " could not read config file")
        # import sys
        # sys.exit()


def get_mail_url(user, pwd):
    return 'https://%s:%s@mail.google.com/mail/feed/atom' % (user, pwd)


def send_noti(head="mail notify", msg="test"):
    # import os
    return os.system('notify-send "' + head + '" "' + msg + '" --urgency=low')
    # os.system('notify-send "Gmail" "new '+fullcount+' '+ed+'" --urgency=low --icon=mail-forward')


def open_rss_link(url):
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
            'https://mail.google.com/mail/u/0/h/?&v=c&th=' + message_id)

        count += 1
        if int(count) > 10:
            # webbrowser.open_new_tab('https://mail.google.com/')
            # print("to many open new mail!")
            break
    else:
        webbrowser.open_new_tab('https://mail.google.com/')
        print("to many open new mail!")

    # return entry.link


def mail_rss(url):
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

        debug_echo(" " + fullcount)

        send_noti("Gmail", fullcount + " " + ed)
        # send_noti("Gmail", "new "+fullcount +" "+ ed)

        open_rss_link(contents)

    elif int(fullcount) != 0:
        print("gmail format xml is changed")
    else:
        debug_echo("not found new mail")


def check_Inet_Connect(ip_="8.8.8.8"):
    # import os
    # import time
    ## import threading

    hostname = "network"
    reconnect_sec = 10
    response = os.system('ping -c 3 ' + ip_ + ' -c1 >/dev/null 2>&1')

    if int(response) == 0:
        debug_echo(hostname + " is up!")
        return True
    else:
        debug_echo(hostname + " is down!")
        debug_echo("Trying to reconnect in %s seconds" % reconnect_sec)
        time.sleep(reconnect_sec)
        return check_Inet_Connect()
        # return threading.Timer(2, check_inet).start()


def main():
    try:
        module_import(module_list_dependence)

        print('')
        debug_echo("Working...")

        inet_connect = check_Inet_Connect()
        if inet_connect == True:
            mailurl = get_config(config_file_path)
            mail_rss(mailurl)

    except IOError as e:
        # print("I/O error: {0}".format(e))
        raise print("IOError error")
    except KeyboardInterrupt:
        return print("Keyboard: interruption")
    # except:
    #     print("Fatal error:", sys.exc_info()[0])
        # raise
    # else:
        # print('else!')
    finally:
        debug_echo("done!")
        # sys.exit()

if __name__ == '__main__':
    main()
