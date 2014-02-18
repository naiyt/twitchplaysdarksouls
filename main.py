from threading import Thread
from ircbot import Bot
from play_game import Game
from queue import MyQ
from locals import *
from gui import Gui


def main():
    """
    Creates a queue that keeps track of commands to be entered into the game.

    Creates three more objects and spins up a thread for each:
    1 - The IRC bot, which monitors the Twitch IRC channel for new actions to queue.
    2 - The game thread, which pops entries from the queue if they exist, and runs
        them in the game.
    3 - The gui thread, which runs a simple (read: ugly) gui that displays the possible
        actions and their votes, and the actions in the queue.

    TODO: There's no way of stopping all of these threads at once yet.
    I just have to close my shell, which is bad. Need to put some conditions
    that watch for Ctrl-c in all of the threads, or something like that.
    
    """

    queue = MyQ()
    bot = Bot(BOT_OWNER, NICK, CHANNEL, SERVER, PORT, AUTH, queue)
    bot_thread = Thread(target=bot.run)
    bot_thread.start()

    game = Game(queue)
    game_thread = Thread(target=game.run_game)
    game_thread.start()

    gui_thread = Thread(target=start_gui, args=(queue,))
    gui_thread.start()


def start_gui(queue):
    Gui(queue)


if __name__ == '__main__':
    main()