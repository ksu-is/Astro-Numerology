import tkinter as tk
    
def firewaterair():
    import fireair.py

def guessthenumber():
    from nachomines.scripts.main import run
    if __name__ == "__main__":
        run()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="fire water air",
                   command= firewaterair)
slogan.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="guesstheumber",
                   command= guessthenumber)
slogan.pack(side=tk.RIGHT)
root.mainloop()
