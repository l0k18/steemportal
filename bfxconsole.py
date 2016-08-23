class bfxconsole(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self,
        application_id="org.ascension.bfxconsole",
        flags=Gio.ApplicationFlags.FLAGS_NONE)
        self.connect("activate", self.on_activate)

    def on_keyentry_change(self, entry, *data):
        """
        data contains a list with two entry widgets and the confirm button widget
        If both the entry widgets contain the right amount of characters, then
        the confirm button is set as sensitive and can be clicked.
        If both are confirmed, the keys are entered into the dconf settings database.
        """
        length1 = data[0].get_buffer().get_length()
        length2 = data[1].get_buffer().get_length()
        confirmbutton = data[2]
        login = data[3]
        if (length1 == 43) and (length2 == 43):
            apikey = data[0].get_buffer().get_text()
            apisecret = data[1].get_buffer().get_text()
            login.set_string ("apikey", apikey)
            login.set_string ("apisecret", apisecret)
            confirmbutton.set_sensitive (True)
        else:
            confirmbutton.set_sensitive (False)

    def on_keyentry_confirm (self, button, *data):
        """
        When the user has entered two API credentials of the correct length
        check that the login is valid according to Bitfinex
        """
        window = data[0]
        entrygrid = data[1]
        login = data[2]
        apikey = data[2].get_string ("apikey")
        apisecret = data[2].get_string ("apisecret")
        window.remove (entrygrid)
        window.add (Gtk.Label (label="Checking Login Details..."))
        window.show_all ()
        self.test_login (window, login, apikey, apisecret)

    def test_login (self, window, login, apikey, apisecret):
        """
        Test whether the API key/secret are valid for Bitfinex.
        If they are invalid, change the window title to indicate this,
        and prompt the user to enter them again.
        This app saves all settings in the dconf database and any configuration
        changes are automatically saved so there is never a moment the user cannot
        simply close down the app. The rest of the data is saved on the Bitfinex
        servers and is reloaded when needed to display in this app.
        """
        success = False
        bfx_account = Trading (key=apikey, secret=apisecret)
        try:
            result = bfx_account.balances()
        except requests.exceptions.HTTPError:
            success = False
            window.set_title ("Invalid Login Credentials")
            login.set_string ("apikey", "")
            login.set_string ("apisecret", "")
            self.enter_keys (window, login, "", "")
            print ("bitfinex rejected credentials")
        else:
            window.set_title ("bfxconsole")
            child = window.get_child()
            if (child):
                window.remove (child)
            window.add (Gtk.Label(label="starting console"))
            window.show_all ()

    def enter_keys (self, window, login, apikey, apisecret):
        """
        Change window content to prompt the user for API Key and Secret
        """
        apikeygrid = Gtk.Grid()
        child = window.get_child()
        if (child):
            window.remove (child)
        apikeyinput = Gtk.Entry()
        apisecretinput = Gtk.Entry ()
        apiconfirmbutton = Gtk.Button (label="OK")
        apiconfirmbutton.set_sensitive (False)
        apikeygrid.attach (Gtk.Label (label="Please enter your Bitfinex API key and secret:"), 1, 1, 2, 1)
        apikeygrid.attach (Gtk.Label (label="API Key:"), 1, 2, 1, 1)
        apikeygrid.attach (Gtk.Label (label="API Secret:"), 1, 3, 1, 1)
        apikeygrid.attach (apikeyinput, 2, 2, 1, 1)
        apikeygrid.attach (apisecretinput, 2, 3, 1, 1)
        apikeygrid.attach (apiconfirmbutton, 1, 4, 2, 1)
        apikeyinput.connect ("changed", self.on_keyentry_change,
        apikeyinput, apisecretinput, apiconfirmbutton, login)
        apisecretinput.connect ("changed", self.on_keyentry_change,
        apikeyinput, apisecretinput, apiconfirmbutton, login)
        apiconfirmbutton.connect ("clicked", self.on_keyentry_confirm, window, apikeygrid, login)
        window.add (apikeygrid)
        window.show_all ()

    def on_activate(self, data=None):
        """
        Open application window, check for credentials, test login, then if successful,
        launch console interface.
        """
        window = Gtk.Window(type=Gtk.WindowType.TOPLEVEL)
        self.add_window(window)

        window.set_title("bfxconsole")
        window.set_border_width(24)
        window.set_position(Gtk.WindowPosition.CENTER)

        login = Gio.Settings("org.ascension.bfxconsole")
        apikey = login.get_string("apikey")
        apisecret = login.get_string("apisecret")
        if (apikey == "") or (apisecret == ""):
            self.enter_keys (window, login, apikey, apisecret)
        else:
            self.test_login (window, login, apikey, apisecret)
        #window.show_all ()
        #print ("logged in")

        #public=Public()
        #print(public.ticker())
        #bfx_account = Trading (key='GBiBGM3b4ncW6HRbp5SYkrElWkUNj1PYyuVnHLnZwgk',
        #    secret='HUaB2c0MkPlvtMUUYRIsThfPeC0qDaW5umLvACIdMVx')
        #print (bfx_account.positions ())
