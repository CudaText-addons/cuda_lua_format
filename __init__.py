from . import format_proc
from . import lua_format

format_proc.INI = 'cuda_lua_format.json'
format_proc.MSG = '[Lua Format] '

def do_format(text):
    text = lua_format.format(text)
    #text = text.replace('\\n', '\n') #formatter issue
    return text


class Command:
    def config_global(self):
        format_proc.config_global()

    def config_local(self):
        format_proc.config_local()

    def run(self):
        format_proc.run(do_format)
