import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib, Pango

class KeystrokeGUI:
    def __init__(self, device_file):
        self.device_file = device_file
        self.window = Gtk.Window(title="Keystroke GUI")
        self.label = Gtk.Label(label="Keystrokes:")
        self.label.modify_font(Pango.FontDescription("Sans 24"))
        self.window.add(self.label)
        self.window.connect("delete-event", Gtk.main_quit)
        GLib.timeout_add_seconds(3, self.clear_keystrokes)
        GLib.timeout_add(100, self.update_keystrokes)
        
    def update_keystrokes(self):
        with open(self.device_file, 'r') as f:
            keystrokes = f.read()
        self.label.set_label("Keystrokes: " + keystrokes)
        return True

    def clear_keystrokes(self):
        self.label.set_label("Keystrokes:")
        return False
        
    def run(self):
        self.window.show_all()
        Gtk.main()

if __name__ == "__main__":
    gui = KeystrokeGUI("../keylogger2/keylog0")
    gui.run()
