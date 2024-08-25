import os

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.widget import Widget

import compiler

Window.size=(1200,600)
Builder.load_file("yo.kv")
class Root(Widget):
    def run(self):
        self.ids.output.text="Output :\n"
        text=self.ids.code.text
        with open('temp.txt','w') as f:
            f.write(text)
        os.system('python3 compiler.py')

        os.system('python3 code.py >output.txt')
        with open("output.txt") as file:
            lines=file.readlines()
            for i in lines:
                self.ids.output.text+=str(i)



class MainApp(App):
    title ="YO"
    def build(self):
        return Root()
if __name__=="__main__":
    MainApp().run()