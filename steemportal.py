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

class steemportal(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self,
            application_id="org.ascension.steemportal",
            flags=Gio.ApplicationFlags.FLAGS_NONE)
        self.connect("activate", self.on_activate)

    def test_login (self):
        """
        Tests login by using the WIF login code stored in the dconf
        database. Returns true if successful, and stores the piston
        steem account object in the class namespace root.
        """
        wif = self.settings.get_string("wif")
        try:
            self.steem_account = Steem(wif=wif)
        except Wallet.InvalidWifError:
            if debugflag: print ("invalid wif")
            return False
        else:
            if debugflag: print ("wif accepted")
            self.window.set_title("steemportal")
            return True

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
        parameters: window, logingrid, settings
        When the OK button is pressed, next we query the Steem system to
        ensure the credentials are valid.
        """
        wif = self.settings.get_string ("wif")
        self.window.remove (self.logingrid)
        self.window.add (Gtk.Label (label="Checking Login Details..."))
        self.window.show_all ()
        if self.test_login ():
            if debugflag: print ("key tested valid")
            self.start_interface()
        else:
            if debugflag: print ("key invalid")
            self.window.set_title ("Invalid WIF, try again")
            self.settings.set_string ("wif", "")
            self.enter_keys ()

    def enter_keys (self):
        """
        Change window content to prompt the user for userid and wif
        """
        self.logingrid = Gtk.Grid()
        child = self.window.get_child()
        if (child):
            self.window.remove (child)
        wifinput = Gtk.Entry ()
        loginconfirmbutton = Gtk.Button (label="OK")
        loginconfirmbutton.set_sensitive (False)
        self.logingrid.attach (Gtk.Label
            (label="Please enter your Steemit Password:"), 1, 1, 2, 1)
        self.logingrid.attach (Gtk.Label (label="password:"), 1, 2, 1, 1)
        self.logingrid.attach (wifinput, 2, 2, 1, 1)
        self.logingrid.attach (loginconfirmbutton, 1, 3, 2, 1)
        wifinput.connect ("changed",
            self.on_loginentry_change, loginconfirmbutton)
        loginconfirmbutton.connect ("clicked",
            self.on_loginentry_confirm)
        self.window.add (self.logingrid)
        self.window.show_all ()

    def start_interface (self):
        self.window.maximize ()

    def on_activate(self, data=None):
        """
        Open the window and check for a configured login
        """
        self.window = Gtk.Window(type=Gtk.WindowType.TOPLEVEL)
        self.window.set_title("steemportal")
        self.window.set_border_width(8)
        self.window.set_position(Gtk.WindowPosition.CENTER)
        label = Gtk.Label("steemportal - your steem, your feed")
        self.window.add(label)
        self.add_window(self.window)
        self.window.show_all()
        self.settings = Gio.Settings("org.ascension.steemportal")
        wif = self.settings.get_string("wif")
        if debugflag: print ("testing wif")
        if (wif == ""):
            if debugflag: print ("no key stored in configuration")
            self.enter_keys ()
        else:
            if self.test_login ():
                if debugflag: print ("login successful")
                self.start_interface ()
            else:
                self.enter_keys ()


if __name__ == "__main__":
    app = steemportal()
    app.run(None)
