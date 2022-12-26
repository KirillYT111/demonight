print("Импортирование обектов...")
from tkinter import *  
import os


print("Запуск лаунчера...")
window = Tk()  
window.title("DemoNight лаунчер")  
window.geometry('350x200')  
lbl = Label(window, text="DemoNight", font=("Arial Bold", 50))  
lbl.grid(column=0, row=0) 

lbl = Label(window, text="Введите никнейм")  
lbl.grid(column=0, row=1)  
txt = Entry(window,width=30)  
txt.grid(column=0, row=2)  
def startgame():
	lennick = len(format(txt.get()))
	if lennick < 3 or lennick > 16:
		window1 = Tk()  
		window1.title("DemoNight warning")  
		window1.geometry('415x65')	
		lbl = Label(window1, text="Никнейм дожен состоять из 3 - 16 символов!", font=("Arial Bold", 15)) 
		lbl.grid(column=0, row=0)
		def warnclose():
			window1.destroy()
		btn = Button(window1, text="ОК", command=warnclose)  
		btn.grid(column=0, row=1)
	else:
		os.system("start game\demonight.py")
		f = open('config.yml','w')
		f.write(f'nickname : "{format(txt.get())}"\n')
		exit()
btn = Button(window, text="Запустить", command=startgame)  
btn.grid(column=0, row=3)
window.mainloop()

