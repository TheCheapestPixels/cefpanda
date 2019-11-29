import sys

from direct.showbase.ShowBase import ShowBase

import cefpanda


class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.accept('escape', sys.exit)

        # Setup ui
        self.ui = cefpanda.CEFPanda()
        self.ui.set_js_function('call_py', self.handler_js_to_py)
        self.ui.load_file('ui/main.html')

    def handler_js_to_py(self):
        print('Python called')
        self.ui.exec_js_func('color_text_red')    


if __name__ == '__main__':
    app = App()
    app.run()
