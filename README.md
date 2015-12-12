Twitch Plays Dark Souls
=======================

This was the code used for the Twitch Plays Dark Souls experiment (a knock off of the popular "Twitch Plays Pokemon" stream, but with a much more ridiculous game).

Please keep in mind that this code could very much be considered alpha for something like this, and I threw it together in an afternoon. There are bugs, and I can't guarantee it will work for you or your game. Feel free to fork it and use it to your heart's content, just be aware that it may break on you.

I'll try and add more documentation in the future. For now, here's a general overview of how it works:

It contains a `Bot` class that monitors the Twitch IRC chat for the channel you are connected to. (You'll need to place your Twitch credentials in the `locals.py` file). If it sees somebody enter something that's listed in the `ACTIONS` or `MOVEMENTS` lists in `locals.py`, it adds that action to the Queue object.

The `Queue` creates `Action` objects and stores them in a list. Actions have an `execute()` method. You could change that execute to be implemented however you want -- in the case of Dark Souls, I had it call a set of AutoHotKey scripts to send the actual commands to the game, because I was having no luck with Python emulating the keystrokes directly. Actions also have member variables that specify what they "do", what their "name" is, what "type" they are, and the length the action should take place.

Finally, there's a `Game` object that, every .5 seconds, looks for an action on the Queue. If there is one, it pops it off the queue and executes it.

`main.py` spins up threads for the bot, the game, and a small gui that displays actions that have been voted on, and actions in the queue.

Sorry for the lack of detailed documentation currently, but there were a few people asking for the source, so I wanted to get it up quickly. If you have specific questions, feel free to ask me.
