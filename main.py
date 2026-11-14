import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gdk

def on_activate(app):
    win = Gtk.ApplicationWindow(application=app)
    win.fullscreen()
    css = Gtk.CssProvider()
    css.load_from_data(b"""
        window, box {
            background: black;
        }
        label {
            color: white;
            font-size: 48px;
        }
        button.green {
            background: green;
            color: white;
            border-radius: 0;
        }
        button.red {
            background: red;
            color: white;
            border-radius: 0;
        }
    """)
    Gtk.StyleContext.add_provider_for_display(
        Gdk.Display.get_default(),
        css,
        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
    )
    main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
    top = Gtk.Label(label="Hello, world!")
    top.set_vexpand(True)
    main.append(top)
    bottom = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    bottom.set_vexpand(True)
    green = Gtk.Button(label="GREEN")
    green.add_css_class("green")
    green.set_hexpand(True)
    green.connect("clicked", lambda x: print("Green pressed"))
    red = Gtk.Button(label="RED")
    red.add_css_class("red")
    red.set_hexpand(True)
    red.connect("clicked", lambda x: win.close())
    bottom.append(green)
    bottom.append(red)
    main.append(bottom)
    win.set_child(main)
    win.present()

app = Gtk.Application(application_id="org.gtk.Example")
app.connect("activate", on_activate)
app.run()