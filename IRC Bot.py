# -*- coding: utf-8 -*-
__author__ = 'Brad'
import socket
import string
import urllib
import bs4





HOST="irc.snoonet.org"
PORT=6667
NICK="IloveBrad"
IDENT="BradBot"
REALNAME="BradBot"
readbuffer=""

s=socket.socket( )
s.connect((HOST, PORT))
s.send("NICK %s\r\n" % NICK)
s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
s.send("JOIN #lizp, \r\n")
s.send("JOIN #asianladyboners, \r\n")
s.send("JOIN #korean, \r\n")
s.send("JOIN ##yolo, \r\n")









while 1:
    readbuffer=readbuffer+s.recv(1024)
    temp=string.split(readbuffer, "\n")
    readbuffer=temp.pop( )


    for line in temp:
        line=string.rstrip(line)
        line=string.split(line)
        print line
        if line[0] == "PING":
            s.send("PONG %s\r\n" % line[1])
        if(line[1]=='PRIVMSG' and line[3] == ':.lookup'):
            if len(line) > 4:
                html = urllib.urlopen("http://dic.naver.com/search.nhn?query=%s" % ' ' .join(line[4:])).read()
                soup = bs4.BeautifulSoup(html)
                try:
                    s.send("PRIVMSG %s :%s\r\n" %(line[2], unicode(soup.find_all("dd")[1].get_text()).encode('utf8').strip()))

                except IndexError:
                    s.send("PRIVMSG %s :Page not found\r\n" % (line[2]))

            else:
                s.send("PRIVMSG %s :.lookup <word>\r\n" % (line[2]))









