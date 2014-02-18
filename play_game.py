import os
from subprocess import check_output
from locals import *
from time import sleep
from threading import Lock

script_path = "ahkscripts"
start_script = "start.ahk"
movement_script = "movement.ahk"
action_script = "action.ahk"
autohotkey_path = 'AutoHotkey.exe'


class Game:
    def __init__(self, queue):
        self.queue = queue
        self.mutex = Lock()
    
    def run_game(self):
        start = Action(type=ACTION, do=START, name='start')
        start.execute()

        while True:
            sleep(.5)
            action = self.queue.get_action()
            if action:
                action.execute()
                print "Executed: {}".format(action.name)


class Action:
    def __execute(self, command):
        return check_output(command)

    def __init__(self, do, name, type=None, length=None):
        self.do = do
        self.type = type
        if length is None:
            self.length = 0
        else:
            self.length = length
        self.name = name

    def execute(self):
        command = None
        if self.do == START:
            script = "{}/{}".format(script_path, start_script)
            command = [autohotkey_path, script]
        elif self.type == ACTION:
            script = os.path.join(script_path, action_script)
            command = '{} {} {}'.format(autohotkey_path, script, self.do)
        elif self.type == MOVEMENT:
            script = script = os.path.join(script_path, movement_script)
            command = '{} {} {} {}'.format(autohotkey_path, script, self.do, self.length*1000)
        self.__execute(command)