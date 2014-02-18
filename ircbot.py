import socket
import sys
from locals import *

class Bot:
    def __init__(self, owner, nick, channel, server, port, auth, queue):
        self.irc = socket.socket()
        self.irc.connect((server, port))
        self.irc.send('PASS ' + auth + '\r\n')
        self.irc.send('USER ' + nick + ' 0 * :' + owner + '\r\n')
        self.irc.send('NICK ' + nick + '\r\n')
        self.irc.send('JOIN ' + channel + '\r\n')
        self.running = True
        self.queue = queue

    def run(self):
        readbuffer = ''
        while self.running:
            readbuffer=readbuffer+self.irc.recv(1024)
            print readbuffer
            if readbuffer.find('PING') != -1:
                self.irc.send(readbuffer.replace('PING', 'PONG'))
            data = readbuffer.split()
            try:
                command = data[3][1:].upper().strip()
                if command in ACTIONS or command in MOVEMENTS:
                    self.queue.add_command(command)
            except:
                pass
            readbuffer = ''