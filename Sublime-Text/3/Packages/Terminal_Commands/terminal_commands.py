import sublime_plugin
import subprocess

class open_conemu(sublime_plugin.TextCommand):
    def run(self, edit):
        # Note that ConEmu64.exe must be on your PATH!
        terminal_command = "ConEmu64 /Single /cmd"
        
        file_name = self.view.file_name()
        path = file_name.split("\\")
        path.pop()
        current_directory = "\\".join(path)
        command = "cd " + current_directory + " & start " + terminal_command
        subprocess.Popen(command, shell=True)

class open_cmd(sublime_plugin.TextCommand):
    def run(self, edit):
        file_name = self.view.file_name()
        path = file_name.split("\\")
        path.pop()
        current_directory = "\\".join(path)
        command = "cd " + current_directory + " & start cmd"
        subprocess.Popen(command, shell=True)
