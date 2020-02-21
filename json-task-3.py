# This program gets a JSON file from a URL (Rest Server)
# The JSON is parsed and formatted to a readable list
# The output is to a GUI and a console log with a structured list of data


import requests
import tkinter
from tkinter import *

data = requests.get('https://live.documents.snapfix.io/sw_analyst/user_42232.json').json()

root = Tk()
root.geometry('500x500')
text = Text(root, height=1000, width=1000)

num = 1
for key in data.keys():
    if not isinstance(data[key], list):
        print("%s%s%s" % (key, ': ', data.get(key)))
        text.insert(tkinter.END, ("%s%s%s" % ( key, ': ', data.get(key))) + '\n')
    else:
        print("%s%s" % (key, ': '))
        text.insert(tkinter.END, ("%s%s" % (key, ': ')) + '\n')
        for devicedict in data[key]:
            print("%s%s" % (num, ': '))
            text.insert(tkinter.END, ("%s%s" % (num, ': ')) + '\n')
            num += 1
            for devicekey in devicedict.keys():
                print("%s%s%s%s" % (devicekey, ': ', devicedict[devicekey], ' '))
                text.insert(tkinter.END, ("%s%s%s%s%s" % ('  ', devicekey, ': ', devicedict[devicekey], ' ')) + '\n')

text.pack()
root.mainloop()
