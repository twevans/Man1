#!/usr/bin/python3

from pylab import *
from Tkinter import *
fields = ('R1', 'R2', 'I1', 'I2')

def submit(entries):
	print "Generating..."
	l1 = float(entries['R1'].get())	# -0.7447108
   	l2 = float(entries['R2'].get())	# -0.742423
   	l3 = float(entries['I1'].get())	# 0.1302584
   	l4 = float(entries['I2'].get())	# 0.1325462
	inc = (l2-l1)/1000.0
	its = 1000.0
	S = 1.0
	z = 0
	c = 0
	X = []
	Y = []
	Z = []
	col = plt.cm.jet
	for x in range(0, int((l2-l1) / inc)):
		for y in range(0, int((l4-l3) / inc)):
			c = (l1 + x*inc) + (l3 + y*inc)*(1j)
			for i in range(1, int(its) + 1):
				z = z**2 + c
				if abs(z) > 2:
					break
			X.append(l1 + x*inc)
			Y.append(l3 + y*inc)
			Z.append(log10(i))
			z = 0
	fig, ax = plt.subplots()
	im = ax.scatter(X, Y, c = Z, s = S, cmap = col, linewidths = 0)
	fig.colorbar(im, ax=ax)
	im.set_clim(0.0, 3.0)
	show()

def makeform(root, fields):
   entries = {}
   #initvals = [1,2,4,5]
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=22, text=field+": ", anchor='w')
      ent = Entry(row)
      ent.insert(0,"0")
      #ent=initvals[field]      

      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries[field] = ent
   return entries

if __name__ == '__main__':
   root = Tk()
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
   b1 = Button(root, text='Submit',
          command=(lambda e=ents: submit(e)))
   b1.pack(side=LEFT, padx=5, pady=5)
   b2 = Button(root, text='Quit', command=root.quit)
   b2.pack(side=LEFT, padx=5, pady=5)
   root.mainloop()



	
