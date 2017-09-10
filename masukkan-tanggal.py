import sublime, sublime_plugin, time, locale
class InsertDatetimeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        locale.setlocale(locale.LC_ALL, "id_ID.UTF-8")
        sel = self.view.sel();
        for s in sel:
            self.view.replace(edit, s, time.strftime("%a, %d %b %Y %H:%M:%S"))