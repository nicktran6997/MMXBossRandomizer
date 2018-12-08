from Tkinter import *
import mmx_boss_randomizer as mmx
import time


def main():
    def callback():
        #start_time = time.time()
        text.delete(1.0, END)
        text.insert(END,mmx.main(entry.get()))
        #print "--- %s seconds ---" % (time.time() - start_time)

    #Gather Mega Man Game Information

    def callback():
        text.delete(1.0, END)
        for i in range(8):
            if games[i].get():
                text.insert(END, mmx.main('x'+str(i+1), other_constraints))
                text.insert(END, '\n')
    def getAll():
        text.delete(1.0, END)
        for i in range(8):
            text.insert(END, mmx.main('x'+str(i+1), other_constraints))
            text.insert(END, '\n')
    def copy_to_clipboard():
        root.clipboard_clear()
        root.clipboard_append(text.get("1.0",END))

    def to_text():
        with open("Output.txt", "w") as text_file:
            text_file.write(text.get("1.0", END))


    #Create Frames
    root = Tk()
    root.title("Mega Man X Series Boss Randomizer")
    root.iconbitmap('sigma_KRi_2.ico')
    #root.minsize(622, 466)

    #basic goal: take in Entry() input, send it to mmx_boss_randomizer
    label = Label(root, text="MMX game(s)")
    games = [IntVar() for i in range(8)]
    for i in range(1, 5):
        Checkbutton(root, text='X'+str(i), variable=games[i-1]).grid(row=0, column=i, sticky=W+N)
    for i in range(5,9):
        Checkbutton(root, text='X'+str(i), variable=games[i-1]).grid(row=1, column=i-4, sticky=W+N)
    b = Button(root, text="Randomize!", command=callback)

    other_constraints = [IntVar() for i in range(4)]
    constraints_text = ['Randomize Backtracking Constraints?', 'Randomize Characters? (Only for X4-X8)', 'Randomize Armor Constraints if playing as X?', 'Randomize Special Weapon Usage if playing as X?']
    for i in range(4):
        Checkbutton(root, text=constraints_text[i], variable=other_constraints[i]).grid(row=i+2, column=0, columnspan=4, sticky=N+W)


    label.grid(row=0, column=0, sticky=W+N)
    b.grid(row=6, column=0, columnspan=2,sticky=W)


    all = Button(root, text="Randomize All Games", command=getAll)
    all.grid(row=6, column=2, columnspan=3,sticky=E)


    copy_to_clipboard_button = Button(root, text="Copy to clipboard", command=copy_to_clipboard)
    copy_to_clipboard_button.grid(row=99, column=0, columnspan=2, sticky=W)

    to_text_button = Button(root, text="Output to output.txt", command=to_text)
    to_text_button.grid(row=98, column=0, columnspan=2, sticky=W)

    #text box on frame
    text = Text(root, width=25, height=14)
    text.configure(font=("Times New Roman", 12, ""))
    textVerticalScroll = Scrollbar(root, width=20)
    text.configure(yscrollcommand=textVerticalScroll.set)
    textVerticalScroll.configure(command=text.yview)
    text.grid(column=5, row=0, rowspan=100)
    textVerticalScroll.grid(column=6, row=0, rowspan=100, sticky=N+S)


    root.mainloop()

if __name__ == "__main__":
    main()
