#!/usr/bin/env python3

# import local module
# import pkgutil
# import importlib
# packages = pkgutil.walk_packages(path='./lib/')
# packages = pkgutil.walk_packages(path='.')
# for importer, name, is_package in packages:
#     mod = importlib.import_module(name)

# _Settings____________________________________________________________________
# DEBUG_MODE = True
DEBUG_MODE = False
CONFIG_PATH = ('~/.local/gmail_config.cfg')  # only HOME directory
# _____________________________________________________________________________


import sys
import os
import time
import configparser
import argparse
import feedparser
import webbrowser
from furl import furl
from urllib.request import FancyURLopener

# module_list_dependence=''
MODULE_LIST_DEPENDENCE = [
    "pip",
    "sys",
    "os",
    "time",
    "configparser",
    "argparse",
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


def module_exists_local(MODULE_NAME):
    # import sys
    if not MODULE_NAME in sys.modules.keys():
        print("local ImportError: " + MODULE_NAME)
        # print("ImportError: " + MODULE_NAME)
        # import pip
        # pip.main(['install', MODULE_NAME])
    else:
        debug_echo('%s -> %s' % ("import", MODULE_NAME))


# check in system
def module_exists_sys(MODULE_NAME):
    try:
        __import__(MODULE_NAME)
        # import MODULE_NAME
    except ImportError:
        print("pip install: " + MODULE_NAME)
        # import pip
        # pip.main(['install', '--user', MODULE_NAME])
        # import MODULE_NAME
        # return False


def module_import(MODULE_LIST=False):
    if not MODULE_LIST:
        print("module_list_dependence not exist")
        return False

    for item in MODULE_LIST:
        # debug_echo("%s -> %s" % ("import", item))
        module_exists_sys(item)
        module_exists_local(item)
        # print ( "%s -> %s" % (item, MODULE_LIST[item]) )
        # module_exists( MODULE_LIST[item] )


def get_argsOFF():
    if "--debug" in sys.argv or \
       "-d" in sys.argv:
        global DEBUG_MODE
        DEBUG_MODE = True
        # print ("debug agrv")
        for param in sys.argv:
            # print ("param:"+param)
            if param.startswith("--config") or "-c":
                # print ("find argv --config")
                if "=" in param:
                    # print ("filepath1:"+filepath)
                    global CONFIG_PATH
                    CONFIG_PATH = param[param.index("=") + 1:]


def get_args():
    # import argparse
    parser = argparse.ArgumentParser(
        description='In interactive mode you able to manage your keys.'
    )
    parser.add_argument(
        '-d', '--debug', action='store_true', help='show log info'
    )
    parser.add_argument(
        # '-c', '--config', nargs='?', default=CONFIG_PATH, help='patch to a config file'
        '-c', '--config', help='patch to a config file'
    )
    args = parser.parse_args()

    if args.config:
        global CONFIG_PATH
        CONFIG_PATH = args.config

    if args.debug:
        global DEBUG_MODE
        DEBUG_MODE = args.log

    # if args.log:
    #     return(True)
    # return(False)


def debug_echo(MSG="test msg"):
    # if (not get_args()):
    # if DEBUG_MODE or (get_args()):
    if DEBUG_MODE:
        print(">> " + MSG)
        # log.debug('>>', exc_info=True)
    # else:
    #     return False


def parse_config(CONFIG_PATH="./gmail_config.cfg", CONFIG_SECTION='profile'):
    # import configparser
    if CONFIG_PATH.startswith('~'):
        CONFIG_PATH = os.path.expanduser("~") + CONFIG_PATH[1:]
	# HOME = os.environ['HOME']
	# CONFIG_PATH = HOME + '/' + CONFIG_PATH

    debug_echo("reading config file:" + CONFIG_PATH)

    # if not CONFIG_PATH:
    # if CONFIG_PATH in locals():
    # print('config file not found')
    try:
        config_file = configparser.ConfigParser()
        config_file.read(CONFIG_PATH)

        # config_file.sections()                # Get list ALL sections
        # config_file.options(CONFIG_SECTION)   # Get ALL options in section
        # @gmail.com can be left out
        USER = config_file.get(CONFIG_SECTION, 'user')
        PASSWD = config_file.get(CONFIG_SECTION, 'passwd')

    except Exception as e:
        raise print(str(e), " could not read config file")
        # import sys
        # sys.exit()

    url = get_mail_url(USER, PASSWD)
    return url


def get_mail_url(USER, PWD):
    return 'https://%s:%s@mail.google.com/mail/feed/atom' % (USER, PWD)


def send_noti(HEAD="mail notify", MSG="test"):
    # import os
    return os.system('notify-send "' + HEAD + '" "' + MSG + '" -u low')
    # os.system('notify-send "Gmail" "new '+fullcount+' '+ed+'" --urgency=low --icon=mail-forward')


def open_rss_link(URL):
    # import feedparser
    # import webbrowser
    # from furl import furl

    rss = feedparser.parse(URL)
    COUNT = 0
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

        COUNT += 1
        if int(COUNT) > 8:
            webbrowser.open_new_tab('https://mail.google.com/')
            print("to many open new mail!")
            break

    # return entry.link


def get_count_gmail(URL):
    # from urllib.request import FancyURLopener

    opener = FancyURLopener()
    page = opener.open(URL)
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


def check_inet_connect(IP="8.8.8.8"):
    # import os
    # import time
    ## import threading

    HOSTNAME = "network"
    RECONNECT_SEC = 10
    response = os.system('ping -c 3 ' + IP + ' -c1 >/dev/null 2>&1')

    if int(response) == 0:
        debug_echo(HOSTNAME + " is up!")
        return True
    else:
        debug_echo(HOSTNAME + " is down!")
        debug_echo("Trying to reconnect in %s seconds" % RECONNECT_SEC)
        time.sleep(RECONNECT_SEC)
        # return check_inet_connect()
        check_inet_connect()
        # return threading.Timer(2, check_inet).start()


def main():
    try:
        get_args()
        module_import(MODULE_LIST_DEPENDENCE)
        debug_echo("Working...")

        inet_connect = check_inet_connect()
        if check_inet_connect():
            # if inet_connect:
            mail_url = parse_config(CONFIG_PATH)
            get_count_gmail(mail_url)

    except IOError as e:
        # print("I/O error: {0}".format(e))
        raise print("IOError error")
    except KeyboardInterrupt:
        return print("Keyboard: interruption")
    except:
    	print("Fatal error:", sys.exc_info()[0])
    	sys.exit(33)
    	raise
    # else:
        # print('else!')
    finally:
        debug_echo("done!")
        # sys.exit()


# def process_pid(process):
    # return os.system('pidof %s' % process)
    # return os.system('pidof %s |wc -l' % process)
    # import psutil
    # for proc in psutil.process_iter():
    #     name = proc.name()
    #     print(name)
    #     if name == "program.exe":
    #     if name == process:
    #         pass


if __name__ == '__main__':
	print("")
	# get_args()
	# process_num = process_pid("python3 " + __file__)
	# debug_echo("run (" + str(process_num) + "):" + __file__)
	# if process_num in (0, 256):
	#     debug_echo('duplicate (' + str(process_num) + ') running: exit')
	#     # pass
	#     sys.exit()
	main()
