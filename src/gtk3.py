#!/usr/bin/python3
#
# gtk..py
#
# Gtk+-3.0 interface frontend
# Also requires GLib-2.0 and other related Gnome modules
#
# Here's your stinkin' licence: http://unlicense.org/
#
# - l0k1
#
# Contact details for l0k1
# steemit.com - https://steemit.com/@l0k1
# bitmessage - BM-2cXWxTVaXJbNyMxv5tAjNg87xS98hrAg8P
# torchat - xq6xcvqc2vy34qtx
# email - l0k1@null.net

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit', '3.0')
from gi.repository import Gtk, WebKit, GObject, Gio

debugflag = True

def debug (debugtext, header):
    if debugflag:
        if header: 
            debugtext = ">>> " + debugtext
        else:
            debugtext = "    " + debugtext
        print (debugtext)

def printmodulename ():
    print ("Importing Gtk+-3.0 frontend module")
    
class SPinterface (Gtk.Application):
    """
    Each distinct interface module will replicate the same class and core
    module's interfacing calls. Each module can contain other classes and
    functions, including imports, that are relevant to the module. This top
    level class abstracts the calls so the core can remain agnostic about
    which frontend is being used, and likewise, the frontend can call the 
    configuration backend without knowing about how it is implemented.
    
    The Gtk.Application has its own set of methods, but where the core interacts
    with it, will be with specific calls that are not from these methods, so
    that other GUI libraries can be abstracted also.
    """
    def __init__ (self):
        """
        Interface initialisation
        This function opens the window, calls back through the core, to 
        get the configuration, to load the initial interface. 
        
        The configuration tells the interface what to set up in the initial
        startup.
        """
        Gtk.Application.__init__(self,
            application_id="org.ascension.ascension",
            flags=Gio.ApplicationFlags.FLAGS_NONE)
        self.connect("activate", self.on_activate)

    def init (self, config):
        """
        Abstraction for command to open GUI. For Gtk+-3.0, this just maps to the
        built in Gtk.Application.run () command. For other GUI libraries, this
        will invoke the same. In this case, it triggers the activate hook.
        """
        # Import config object into this object's namespace
        self.config = config
        self.run ()
   
    def on_activate (self, data=None):
        """
        Activate Gtk.Application
        """
        debug ("Activating Gtk.Application", True)
        debug ("creating main window", False)
        self.window = window = Gtk.ApplicationWindow ()
        debug ("binding window to Application", False)
        self.add_window (window)
        winspec = self.config.get_interface ().split ()
        window.resize (int(winspec[2]), int(winspec[3]))
        window.move (int(winspec[0]), int(winspec [1]))
        window.connect('delete-event', self.save_state)
        window.show_all ()
            
    def get_window_state (self):
        winpos = self.window.get_position ()
        winsize = self.window.get_size ()
        return winpos[0], winpos[1], winsize[0], winsize[1]
        
    def save_state (self, *data):
        """
        This collects the current interface status for shutdown of the app
        """
        windowstate = self.get_window_state()
        interfacestring = (str(windowstate[0]) + " " + str(windowstate[1]) + 
            " " + str(windowstate[2]) + " "+ str(windowstate[3]))
        print (interfacestring)
        self.config.set_interface (interfacestring)
        
    def config_open ():
        """
        This opens up the user configuration dialog for user configuration
        of the interface and specifying the users' desired modes of 
        operation
        """
        pass
        
    def open_url (urlstring):
        """
        This takes the parameter of a URL and queries the core to gather
        the data required to display the new URL
        """
        pass
        
debug ("initialising Gtk.Application", True)        
app = SPinterface ()
