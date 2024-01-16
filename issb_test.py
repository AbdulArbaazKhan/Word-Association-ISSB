from tkinter import *
import time
import random
import threading

root = Tk()
root.geometry("800x700")
root.title("Psychology Test")


def word_coming():
    strt_btn.pack_forget()

    def changing_word():
        t_initial = int(time.time())
        print(t_initial)
        while(True):
            if int(time.time()) == t_initial + 10:
                random_word = random.choice(words_list)
                word_label.config(text=f"{random_word}")
                words_list.remove(f"{random_word}")
                root.update()
                if len(words_list) == 0:
                    break

    frame = Frame(bg="black")
    Label(frame, text="Write the sentece of this word: ",
          bg="black", fg="#2D6E67", font="timesnewroman 20 bold").pack(pady=20, fill=X)
    frame.pack(anchor="nw", fill=X, pady=10)
    with open("word.txt", "r") as f:
        content = f.read().split(" ")
    # print(content)
    words_list = ["lick", "try", "mood"]

    word_label = Label(root, text="GAME", font="timesnewroan 20", fg="black")
    word_label.pack(pady=20)

    threading.Thread(target=changing_word).start()


root.config()
main_frame = LabelFrame(bd=2, relief=SUNKEN, text="Let's take the test", fg="#7FDDFF", bg="black")
main_label = Label(main_frame, bd=2, relief=GROOVE, text="Welcome TO Psychology Test Which you want to choose",
                   bg="black", fg="#7FDDFF", font="timesnewroman 20 bold")
main_label.pack(pady=20, fill=X)
main_frame.pack(fill=X)
strt_btn = Button(root, text="Start", fg="white", bg="black", relief=GROOVE, width=12,
                  height=2, command=word_coming, font='timesnewroman 12')
strt_btn.pack(pady=80)
root.mainloop()
