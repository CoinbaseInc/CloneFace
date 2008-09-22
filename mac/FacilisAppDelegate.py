#
#  FacilisAppDelegate.py
#  Facilis
#
#  Created by Joao Moreno on 9/21/08.
#  Copyright 2008. All rights reserved.
#

import sys
from os.path import split

from Foundation import *
from AppKit import *
from objc import nil, NO

from facilis.core.app import FacilisApp
from facilis.core.misc import IsADir
from growl import Growl

FILEADDED = "FileAdded"
ISDIR = "IsDir"
ERROR = "Error"
STARTUP = "Startup"

class FacilisAppDelegate(NSObject):
    def applicationWillFinishLaunching_(self, sender):
        self.start()
    
    def applicationDidFinishLaunching_(self, sender):
        NSLog("Application loaded")
    
    def application_openFile_(self, sender, fname):
        name = split(fname)[1]
        try:
            url = self.app.addFile(fname)
        except IOError:
            self.notifier.notify(ERROR, "Error", "Something bad happened. Try again.")
        except IsADir:
            self.notifier.notify(ISDIR, "Error", name + " is a directory.")
        else:
            self.notifier.notify(FILEADDED, "File added to Facilis", "\"" + name + "\" was just added to Facilis, its URL was copied to the pasteboard. Use Cmd-V to paste it.")

    def start(self):
        self.app = FacilisApp()
        self.app.start()
        self.notifier = Growl.GrowlNotifier("Facilis", [FILEADDED, ISDIR, ERROR, STARTUP])
        self.notifier.register()
        self.notifier.notify(STARTUP, "Facilis", "Facilis just started on port " + str(self.app.config['port']))