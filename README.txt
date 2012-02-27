freshy-server
=============

Keeping your web content fresh!

Work in progress....

You'll need to use [freshy-chrome-extension](https://github.com/lchi/freshy-chrome-extension) in conjunction with this server.

What does this do?
------------------
This tool watches for filesystem changes and broadcasts a message to connected clients any time a directory being 'watched' registers an event (creation, modification, deletion).  The intended client for this tool is the [freshy-chrome-extension](https://github.com/lchi/freshy-chrome-extension), but you're free to write your if you wish (API coming soon, though the code is fairly short).  Currently, the client refreshes the page you're viewing whenever a filesystem event is registered.  This is useful when you're working on a web app and don't want to keep pressing ctrl-r.

TLDR; Point this at a directory and open a page using the extension and the page will be refreshed everytime you change something in the directory.

Installation
------------
If you have ```pip``` you can simply use 

       $ pip install freshy-server

Otherwise, first clone this repository:

      $ git clone git@github.com:/lchi/freshy-server

Then, you'll need the watchdog, twisted and autobahn python libraries, which if you have ```pip``` installed is as easy as:

       $ pip install watchdog	  
       $ pip install autobahn
       $ pip install twisted

I'm using Linux Mint 12, and pip didn't work for twisted on my machine.  You can also try:

    $ sudo apt-get install python-twisted

Usage
-----
For now, the server always binds to port 4444.  This will be changed in the future so you can specify where you want to listen.  To run, use:

    $python freshy-server.py <directories>

Where <directories> specify one or more directories to be watched for filesystem changes.  Separate these with spaces.

Ctrl-C to quit.

**NOTE - The server has only been tested on Linux (Mint 12) at the moment, though it should theoretically work across OSX, Windows and Linux.  Because the underlying FS event library uses inotify, it is *very* possible that the tool will not work for Linux Kernels pre 2.6.  


Credit
------
Idea for this project was taken from Slushbox, a project by John J. Workman.  See the project at [slushbox](https://github.com/workmajj/slushbox).

License (MIT)
-------------
Copyright (c) 2012 Lucas Chi

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
