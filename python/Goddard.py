import Tkinter as tk
import serial


# Translates keypress to robot
commands = { 'W' : 'FG', 'A' : 'RG', 'S' : 'RT', 'D' : 'FT' }

def onKeyPress(event):
    key = event.char.upper()
    print key
    if key in ('W', 'A', 'S', 'D' ):
        com = commands.get( key )
        ser.write( com )
        print key, com

#ser = serial.Serial('/dev/ttyUSB0',9600)
ser = serial.Serial('COM4',9600) # Uncomment for Windows

root = tk.Tk()
root.geometry('300x200')
text = tk.Text(root, background='black', foreground='green', font=('Console', 12))
text.pack()
root.bind('<KeyPress>', onKeyPress)
root.mainloop()
