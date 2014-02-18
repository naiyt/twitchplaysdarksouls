from threading import Lock
from play_game import Action
from locals import *

class MyQ:

    def __init__(self):
        all_actions = ACTIONS + MOVEMENTS
        self.queue_count = {k: 0 for k in all_actions}
        self.q = []

    def add_command(self, command):
        type = MOVEMENT
        length = MOVEMENT_TIME
        if command in ACTIONS:
            type = ACTION
            length = ACTION_TIME
        do = ALL_TYPES[command]

        self.queue_count[command] += 1

        if self.queue_count[command] >= MAX_VOTES:
            self.queue_count[command] = 0
            if self.can_add(command):
                new_action = Action(type=type, do=do, length=length, name=command)
                self.q.append(new_action)
                self.display()

    def can_add(self, command):
        if len(self.q) >= 10:
            return False
        for curr_action in self.q:
            if curr_action.name == command:
                return False
        return True

    def get_action(self):
        if self.q:
            return self.q.pop(0)

    def display(self):
        for action in self.q:
            print action.name

    def get_votes(self):
        return self.queue_count

    def get_queue(self):
        return [x.name for x in self.q]