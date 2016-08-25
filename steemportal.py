#!/usr/bin/python3
# Fuck copyright. Here's your stinkin' licence: http://unlicense.org/
# I made this first and the burden of proof is on you.
#
# l0k1
#
# steemit.com - https://steemit.com/@l0k1
# bitmessage - BM-2cXWxTVaXJbNyMxv5tAjNg87xS98hrAg8P
# torchat - xq6xcvqc2vy34qtx
# email - l0k1@null.net

import os.path, sys, subprocess, os, re, gi, re, json, string, random
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio
from piston.steem import Steem
from piston import wallet as Wallet
import time

debugflag = True


class SPpiston:

    def test_login (self, settings):
        """
        Tests login by using the WIF login code stored in the dconf
        database. Returns true if successful, and stores the piston
        steem account object in the class namespace root.

        This is also deprecated code, uses a dconf key that has been
        removed, and will be used as a basis for working with the
        'write access' parts of the application
        """
        wif = settings.get_string("wif")
        try:
            steem_account = Steem(wif=wif)
        except Wallet.InvalidWifError:
            return False
        else:
            return steem_account


class SPinit:
    """
    This class manages the initial startup process when no configuration
    already exists.

    This will be modified later to account for the different types of
    keys used in the platform. Development of this section, although it
    works (with a dconf database key that is now out of the schema)
    it needs to go in the 'write access' parts of the interface so it
    will come later
    """
    def __init__(self, appwindow, appsettings):
        """
        A password input grid is created, and control is passed to
        the enter_keys to begin the process of the user configuring
        their Steem account
        """
        window = self.window = appwindow
        settings = self.settings = appsettings
        logingrid = self.logingrid = Gtk.Grid ()
        loginconfirmbutton = Gtk.Button (label="OK")
        loginconfirmbutton.set_sensitive (False)
        self.wifinput = wifinput = Gtk.Entry ()
        logingrid.attach (Gtk.Label
            (label="Please enter your Steemit Passwords:"), 1, 1, 2, 1)
        logingrid.attach (Gtk.Label (label="Password:"), 1, 2, 1, 1)
        logingrid.attach (wifinput, 2, 2, 1, 1)
        logingrid.attach (loginconfirmbutton, 1, 3, 2, 1)
        wifinput.connect ("changed",
            self.on_loginentry_change, loginconfirmbutton)
        loginconfirmbutton.connect ("clicked",
            self.on_loginentry_confirm)
        self.enter_keys ()

    def on_loginentry_change (self, wifentry, *data): #
        """
        data[0] is the confirm button which we deactivate if the
        field has insufficient characters in it
        If both the entry widgets contain the right amount of
        characters, then the confirm button is set as sensitive
        and can be clicked, and the data is placed into the dconf database
        """
        confirmbutton = data[0]
        wiflen = wifentry.get_buffer().get_length()
        if debugflag: print ("change detected")
        if (wiflen > 32):
            wif = wifentry.get_buffer().get_text()
            self.settings.set_string ("wif", wif)
            confirmbutton.set_sensitive (True)
            if debugflag: print ("key is long enough")
        else:
            confirmbutton.set_sensitive (False)

    def on_loginentry_confirm(self, entry):
        """

        When the OK button is pressed, next we query the Steem system to
        ensure the credentials are valid.
        """
        piston = SPpiston ()
        settings = self.settings
        wif = settings.get_string ("wif")
        window = self.window
        window.remove (self.logingrid)
        window.add (Gtk.Label (label="Checking Login Details..."))
        window.show_all ()
        if piston.test_login (settings):
            if debugflag: print ("key tested valid")
        else:
            if debugflag: print ("key invalid")
            window.set_title ("Invalid WIF, try again")
            settings.set_string ("wif", "")
            self.enter_keys ()

    def enter_keys (self):
        """
        Change window content to prompt the user for userid and wif
        """
        child = self.window.get_child()
        if (child):
            self.window.remove (child)
        self.window.add (self.logingrid)
        self.wifinput.set_text("")
        self.window.show_all ()


class steemportal(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self,
            application_id="org.ascension.steemportal",
            flags=Gio.ApplicationFlags.FLAGS_NONE)
        self.connect("activate", self.on_activate)

    def on_activate(self, data=None):
        """
        Open the window and check for a configured login
        """
        piston = SPpiston ()
        window = Gtk.Window(type=Gtk.WindowType.TOPLEVEL)
        window.set_title("steemportal")
        window.set_border_width(8)
        window.set_position(Gtk.WindowPosition.CENTER)
        label = Gtk.Label("steemportal - your steem, your feed")
        window.add(label)
        self.add_window(window)
        window.show_all()

        # The following code has been deactivated because write access
        # to account data must be implemented after read access
        #self.settings=settings = Gio.Settings("org.ascension.steemportal")
        #wif = settings.get_string("wif")
        #if debugflag: print ("testing wif")
        #if (wif == ""):
        #    if debugflag: print ("no key stored in configuration")
        #    SPinit(window, settings)
        #else:
        #    if piston.test_login (settings):
        #        if debugflag: print ("login successful")
        #    else:
        #        SPinit (window, settings)

if __name__ == "__main__":
    app = steemportal()
    app.run(None)
