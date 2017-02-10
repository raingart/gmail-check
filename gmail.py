#!/usr/bin/env python

def getConfig(configFilePath):
    import configparser

    config = configparser.ConfigParser()
    # configFilePath = ''
    config.read(configFilePath)
    try:
        USER = config.get('config', 'user') # @gmail.com can be left out
        PASSWD = config.get('config', 'passwd')

        url = getMailUrl(USER, PASSWD)
        return url

    except Exception as e:
        print(str(e), ' could not read configuration file')
        import sys
        sys.exit()


def getMailUrl(user, pwd):
    return 'https://%s:%s@mail.google.com/mail/feed/atom' % (user, pwd)


def sendNoti(head, msg):
    import os
    return os.system('notify-send "' + head + '" "' + msg + '"')
    # os.system('notify-send "Gmail" "new '+fullcount+' '+ed+'" --urgency=low --icon=mail-forward')


def openRssLink(url):
    import feedparser
    import webbrowser

    rss = feedparser.parse(url)
    # print ( "Feed Title %s" % rss.feed.title )

    for entry in rss.entries:
        # print ( "Title: %s" % entry.title )
        # print ( "link: %s" % entry.link )
        webbrowser.open_new_tab(entry.link)

    # return entry.link


def mailRss(url):

    from urllib.request import FancyURLopener

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

        # print(' '+fullcount)
        sendNoti("Gmail", fullcount + ' ' + ed)

        openRssLink(contents)

    # elif int(fullcount) != 0:
        # print('error')
    # else: print('ok')


def checkInetConnect():
    import os
    import time
    # import threading

    # hostname = "inet"
    response = os.system("ping -c 3 8.8.8.8 -c1 >/dev/null 2>&1")

    if int(response) == 0:
        # print (hostname, 'is up!')
        return True
    else:
        # print (hostname, 'is down!')
        time.sleep(10)
        return check_inet()
        # return threading.Timer(2, check_inet).start()


def main():
    try:
        # print ('Working...')
        print('')

        inet_connect = checkInetConnect()

        if inet_connect == True:
            mailurl = getConfig("/home/art/.local/gmail_settings.cfg")
            mailRss( mailurl )

    except IOError as err:
        # print("I/O error: {0}".format(err))
        print("mail error")
    except:
        print("Fatal error:", sys.exc_info()[0])
        # raise
    # else:
        # print('else!')
    # finally:
        # print('done!')

if __name__ == '__main__':
    main()
