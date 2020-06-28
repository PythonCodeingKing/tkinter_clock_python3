import datetime
from tkinter import Tk, Button, Canvas
from sys import exit

root = Tk()
c = Canvas(root, width = 800, height = 700, bg = "green")
root.resizable(height = False, width = False)
time_string = None
time_string2 = None
quit=lambda event: exit()
def get_time():
	global time_string
	global time_string2
	date = datetime.date.today()
	now = datetime.datetime.now()
	time = now.strftime("%H:%M:%S")
	fontB = "TkFixedFont 20"
	fontA = "Ariel 20 bold underline"
	string = str(date) + "\t\t" + str(time)
	if time_string != None and time_string2 != None:
		c.delete(time_string)
		c.delete(time_string2)
		time_string2 = c.create_text(400, 300, fill = 'yellow', font = fontB, text = "Time:")
		time_string = c.create_text(400, 400, fill = "red", font = fontA, text = string)
	else:
		time_string2 = c.create_text(400, 300, fill = 'yellow', font = fontB, text = "Time:")
		time_string = c.create_text(400, 400, fill = "red", font = fontA, text = string)

def main():
	root.title("My Clock!")	
	b = Button(root, anchor = "se", text = "get the time", command = get_time)
	b2 = Button(root, text = "quit", command = quit)	
	b.pack()
	c.pack()
	root.bind("<q>",quit)
	root.bind("<g>", get_time)
	root.mainloop()
main()