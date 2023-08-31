from tkinter import *

i = -1
data = [
    {"auther": "Auther 1", "qoute": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."},
    {"auther": "Auther 2", "qoute": "Pulvinar etiam non quam lacus suspendisse faucibus interdum posuere. Ipsum faucibus vitae aliquet nec ullamcorper sit amet. Donec massa sapien faucibus et molestie ac feugiat sed. Dolor morbi non arcu risus quis varius quam. Consequat semper viverra nam libero justo laoreet sit amet cursus. Odio pellentesque diam volutpat commodo. Ut tellus elementum sagittis vitae et. Libero justo laoreet sit amet cursus sit amet. Justo donec enim diam vulputate ut pharetra sit amet. Varius quam quisque id diam vel."},
    {"auther": "Auther 3", "qoute": "Nullam vehicula ipsum a arcu cursus vitae. Volutpat diam ut venenatis tellus in metus. Tempor orci eu lobortis elementum. Egestas fringilla phasellus faucibus scelerisque eleifend donec pretium vulputate. Euismod in pellentesque massa placerat duis ultricies lacus sed turpis. Nunc consequat interdum varius sit amet mattis vulputate enim nulla. Aliquam sem et tortor consequat id porta. Ac auctor augue mauris augue."},
    {"auther": "Auther 4", "qoute": "Donec enim diam vulputate ut pharetra sit amet. Sed pulvinar proin gravida hendrerit lectus a. Pellentesque id nibh tortor id aliquet. Eu non diam phasellus vestibulum lorem sed risus. Augue lacus viverra vitae congue eu consequat. Sed arcu non odio euismod lacinia at. Ut faucibus pulvinar elementum integer enim neque volutpat. Pharetra massa massa ultricies mi. Sed sed risus pretium quam vulputate dignissim."}
]

def load():
    global i, popup
    if i == len(data)-1:
        i = 0
    else:
        i = i+1

    for widget in popup.pack_slaves():
        widget.destroy()

    auther = Label(popup, text=data[i]["auther"], font=(
        "verdana", 25, "bold"), pady=(15), bg="purple", width=500)
    auther.pack()

    auther = Label(popup, text=data[i]["qoute"], font=(
        "verdana", 15, "bold"), pady=(10), bg="purple", width=500, wraplength=500)
    auther.pack()

    btn = Button(popup, text="Next", font=(9), command=load)
    btn.pack(pady=(10))

popup = Tk()
popup.title("Qoutes slider")
popup.geometry("500x550")
popup.configure(bg="purple")
load()
popup.mainloop()
