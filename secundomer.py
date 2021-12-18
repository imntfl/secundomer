from tkinter import *
from datetime import *

temp = 0
after_id = ''

def tick():
    global temp, after_id
    after_id = root.after(1000, tick)
    f_temp = str(timedelta(seconds=temp))
    dig.configure(text=str(f_temp))
    temp += 1

def start_tick():
    btnStart.grid()
    btnStop.grid()
    tick()

def stop_tick():
    btnStop.grid()
    btnStart.grid()
    btnReset.grid()
    root.after_cancel(after_id)
            
def reset_tick():
    global temp
    temp = 0
    dig.configure(text='0:00:00')
    btnReset.grid_forget()
    btnStop.grid_forget()
    btnStart.grid()
    root.after_cancel(after_id)

root = Tk()
root.title('Секундомер')
root.geometry('433x300')
root.resizable(width=False, height=False)

dig = Label(root, width=10, font=('Arial Bold', 40), text='0:00:00')
dig.grid(row=0, column=0, padx=10, pady=20)

btnStart = Button(root, text='Старт', bg='#013220', fg='#ccc', font=('Arial Bold', 15), command=start_tick)
btnStart.grid(row=1, column=0, sticky="ew")

btnStop = Button(root, text='Cтоп', bg='#013220', fg='#ccc', font=('Arial Bold', 15), command=stop_tick)
btnStop.grid(row=2, column=0, sticky="ew")

btnReset = Button(root, text='Сброс', bg='#8b0000', fg='#ccc', font=('Arial Bold', 15), command=reset_tick)
btnReset.grid(row=3, column=0, sticky="ew")

root.mainloop()

