#!/bin/python
# reference
# https://webkitgtk.org/reference/webkitgtk/stable/
from gi.repository import Gtk
from gi.repository import WebKit

class App():
    def __init__(self):
        self.window = Gtk.Window()
        self.window.connect("delete-event", Gtk.main_quit)
        self.webView = WebKit.WebView()
        self.window.add(self.webView)
        self.settings = self.webView.get_settings()
        self.settings.set_property('enable-caret-browsing',True)
        self.settings.set_property('enable-spatial-navigation',True) 
        self.webView.load_uri('http://www.google.com')
        self.window.show_all()
    def run(self):
        Gtk.main()

app = App()
app.run()
