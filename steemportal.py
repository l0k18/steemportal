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

class steemportal(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self,
            application_id="org.ascension.steemportal",
            flags=Gio.ApplicationFlags.FLAGS_NONE)
        self.connect("activate", self.on_activate)

    def test_login (self, window, settings):
        wif = settings.get_string("wif")
        try:
            steem_account = Steem(wif=wif)
        except Wallet.InvalidWifError:
            self.enter_keys (window, settings)
        else:
            print ("wif accepted")
            print (steem_account)

    def on_loginentry_change (self, button, *data): # 
        """
        parameters: wifentry, confirmbutton, settings
        If both the entry widgets contain the right amount of
        characters, then the confirm button is set as sensitive
        and can be clicked, and the data is placed into the dconf database
        """
        wifentry = data[0]
        confirmbutton = data[1]
        settings = data[2]
        
        wiflen = wifentry.get_buffer().get_length()
       
        print ("change detected")
        if (wiflen > 32):
            wif = wifentry.get_buffer().get_text()
            settings.set_string ("wif", wif)
            confirmbutton.set_sensitive (True)
            print ("new text is long enough")
        else:
            confirmbutton.set_sensitive (False)

    def on_loginentry_confirm(self, entry, *data): 
        """
        parameters: window, logingrid, settings
        When the OK button is pressed, next we query the Steem system to
        ensure the credentials are valid.
        """
        window = data[0]
        logingrid = data[1]
        settings = data[2]
        
        wif = settings.get_string ("wif")
        window.remove (logingrid)
        window.add (Gtk.Label (label="Checking Login Details..."))
        window.show_all ()
        self.test_login (window, settings)
        print ("key confirmed")

    def enter_keys (self, window, settings):
        """
        Change window content to prompt the user for userid and wif
        """
        logingrid = Gtk.Grid()
        child = window.get_child()
        if (child):
            window.remove (child)
        wifinput = Gtk.Entry ()
        loginconfirmbutton = Gtk.Button (label="OK")
        loginconfirmbutton.set_sensitive (False)
        logingrid.attach (Gtk.Label
            (label="Please enter your Steemit Password:"), 1, 1, 2, 1)
        logingrid.attach (Gtk.Label (label="password:"), 1, 2, 1, 1)
        logingrid.attach (wifinput, 2, 2, 1, 1)
        logingrid.attach (loginconfirmbutton, 1, 3, 2, 1)
        wifinput.connect ("changed", 
			self.on_loginentry_change,
			wifinput, loginconfirmbutton, settings)
        loginconfirmbutton.connect ("clicked",
            self.on_loginentry_confirm, window, logingrid, settings)
        window.add (logingrid)
        window.show_all ()

    def on_activate(self, data=None):
        """
        Open the window and check for a configured login
        """
        window = Gtk.Window(type=Gtk.WindowType.TOPLEVEL)
        window.set_title("steemportal")
        window.set_border_width(8)
        window.set_position(Gtk.WindowPosition.CENTER)
        label = Gtk.Label("steemportal - your steem, your feed")
        window.add(label)
        self.add_window(window)
        window.show_all()
        settings = Gio.Settings("org.ascension.steemportal")
        wif = settings.get_string("wif")
        if (wif == ""):
            self.enter_keys (window, settings)
        else:
            self.test_login (window, settings)


if __name__ == "__main__":
    app = steemportal()
    app.run(None)
    
