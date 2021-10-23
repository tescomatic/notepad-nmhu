from tkinter import *
#To get the space above the message
from tkinter.messagebox import *
#To get the dialog box to open when required
from tkinter.filedialog import *
import tkinter.ttk as ttk
import os
import sys
from PIL import Image, ImageTk
# import PIL
class Notepad():
	def __init__(self):
		self.root=Tk()
		self.root.title("Untitled-Notepad")
		self.displayText='this is a textexample python program'
		self.var=BooleanVar()
		self.vars=BooleanVar()
		self.bold=BooleanVar()
		self.thisWidth = 500
		self.thisHeight = 600
		self.yscrollbar=Scrollbar(self.root,orient='vertical')
		self.TextArea = Text(self.root,yscrollcommand=self.yscrollbar.set,font=('arial',12))
		self.TextArea.grid(sticky = N + E + S + W)
		 # To add scrollbar
		self.yscrollbar.grid(row=0, column=1,sticky='ns')
		self.yscrollbar.config(command=self.TextArea.yview)
		# self.TextArea=" "
		# thisScrollBar = Scrollbar(TextArea)

  # Center the window
		self.screenWidth = self.root.winfo_screenwidth()
		self.screenHeight =self.root.winfo_screenheight()
 # For left-alling
		self.left = (self.screenWidth / 2) - (self.thisWidth / 2)
      # For right-allign
		self.top = (self.screenHeight / 2) - (self.thisHeight /2)
      # For top and bottom
		self.root.geometry('%dx%d+%d+%d' % (self.thisWidth, self.thisHeight, self.left, self.top))
		 # To make the textarea auto resizable
		self.root.grid_rowconfigure(0, weight=1)
		self.root.grid_columnconfigure(0, weight=1)
		
		self.menuBar()
		
		self.showsStatus()
		self.root.mainloop()
	def setStatus_keyboard(self,event):
		self.list1 = self.TextArea.index(INSERT).split('.')
		# print(self.list1)
		self.statusbar = "Line= "+str(self.TextArea.count('1.0', END, 'lines'))+ ", Cursor Position = row: "+self.list1[0]+", col: "+self.list1[1]+", word Count= "+str(len(self.TextArea.get('1.0', 'end-1c').split()))
		# print(str(self.TextArea.count('1.0', END, 'lines')))
		# print(self.statusbar)
		self.showstatus.set(self.statusbar)
	def setStatus_button(self,event):
		pass
	def showsStatus(self):
		self.showstatus=StringVar()
		self.StatusFrame = Frame(self.root)
		self.StatusFrame.grid(row=5)
		# self.list1 = self.TextArea.index(INSERT).split('.')
		# # print(self.list1)
		# self.statusbar = "Line= "+str(self.TextArea.count('1.0', END, 'lines'))+ ", Cursor Position = row: "+self.list1[0]+", col: "+self.list1[1]+", word Count= "+str(len(self.TextArea.get('1.0', 'end-1c').split()))
		# # print(str(self.TextArea.count('1.0', END, 'lines')))
		# print(self.statusbar)
		self.textlabl = Label(self.StatusFrame, textvariable=self.showstatus, font=('arial', 10), bd=10)
		self.textlabl.grid(row=5)
		self.list1 = self.TextArea.index(INSERT).split('.')
		# print(self.list1)
		self.statusbar = "Line= "+str(self.TextArea.count('1.0', END, 'lines'))+ ", Cursor Position = row: "+self.list1[0]+", col: "+self.list1[1]+", word Count= "+str(len(self.TextArea.get('1.0', 'end-1c').split()))
		# print(str(self.TextArea.count('1.0', END, 'lines')))
		# print(self.statusbar)
		self.showstatus.set(self.statusbar)
		
	def menuBar(self):
		# loadn=Image.open('image/1.png')
		# rendern=ImageTk.PhotoImage(loadn,master=self.root)
		self.menubar=Menu(self.root)
		self.fileMenu=Menu(self.menubar,tearoff=0)
		self.fileMenu.add_command(label='New',command=self.newPage, accelerator="ctrl + N")
		self.fileMenu.add_command(label='Open',command=self.openfile, accelerator="ctrl + O")
		self.fileMenu.add_command(label="Save", command=self.saveFile, accelerator="ctrl + S")
		self.fileMenu.add_command(label="Save as...", command=self.saveasFile)
		self.fileMenu.add_separator()
		self.fileMenu.add_command(label="Close", command=self.donothing)

		self.fileMenu.add_checkbutton(label='Bold',variable=self.bold,command=self.onClick)

		self.option=Menu(self.fileMenu,tearoff=0)
		self.option.add_command(label='option',command=self.openfile)
		self.option.add_command(label='option1',command=self.openfile)
		self.option.add_command(label='option2',command=self.openfile)
		self.fileMenu.add_cascade(label='option',menu=self.option,underline=0)
		# self.text.bind("<Control-Key-n>",self.newPage)
		# self.text.bind("<Control-Key-N>",self.newPage)
		self.menubar.add_cascade(label='File',menu=self.fileMenu,underline=0)

		self.editmenu = Menu(self.menubar, tearoff=0)
		self.editmenu.add_command(label="Undo", command=self.undo,accelerator="ctrl + Z")
		self.editmenu.add_separator()
		self.editmenu.add_command(label="GoTo", command=self.GoTo,accelerator="ctrl + G")

		self.editmenu.add_command(label="Cut", command=self.cut,accelerator="ctrl + X")
		self.editmenu.add_command(label="Copy", command=self.copy,accelerator="ctrl + C")
		self.editmenu.add_command(label="Paste", command=self.paste, accelerator="ctrl + P")
		self.editmenu.add_command(label="Delete", command=self.delete,accelerator="delete")
		self.editmenu.add_separator()
		self.editmenu.add_command(label="Find", command=self.find,accelerator="ctrl + F")
		self.editmenu.add_command(label="Select All", command=self.selectall,accelerator="ctrl + A")
		self.editmenu.add_separator()
		self.menubar.add_cascade(label="Edit", menu=self.editmenu, command=self.quitApplication)

		self.helpmenu = Menu(self.menubar, tearoff=0)
		self.helpmenu.add_command(label="Help Index", command=self.donothing)
		self.helpmenu.add_command(label="About Notepad...", command=self.showAbout)
		self.menubar.add_cascade(label="Help", menu=self.helpmenu, command=self.donothing)

		self.formatmenu = Menu(self.menubar, tearoff=0)
		self.formatmenu.add_command(label="Font...",command=self.showfont)
		self.formatmenu.add_separator()

		self.formatmenu.add_command(label="Word Wrap...",command=self.showfont)
	# helpmenu.add_command(label="About...", command=showAbout)
		self.menubar.add_cascade(label="Format", menu=self.formatmenu)

		self.viewmenu = Menu(self.menubar, tearoff=0)
		self.viewmenu.add_checkbutton(label="Statu Bar",variable=self.vars, command=self.showStatus)
# helpmenu.add_command(label="About...", command=showAbout)
		self.menubar.add_cascade(label="View", menu=self.viewmenu)
		self.TextArea.bind("<Control-Key-s>", self.saveShort)
		self.TextArea.bind("<Control-Key-S>", self.saveShort)
		self.TextArea.bind("<Control-Key-o>", self.sopen)
		self.TextArea.bind("<Control-Key-O>", self.sopen)
		self.TextArea.bind("<Control-Key-g>", self.sgoto)
		self.TextArea.bind("<Control-Key-G>", self.sgoto)


		self.TextArea.bind("<Control-Key-a>", self.shortSelect)
		self.TextArea.bind("<Control-Key-A>", self.shortSelect)
		# self.TextArea.bind("<Control-Key-s>", self.saveShort)
		# self.TextArea.bind("<Control-Key-S>", self.saveShort)
		self.TextArea.bind("<Control-Key-x>", self.sCut)
		self.TextArea.bind("<Control-Key-X>", self.sCut)
		self.TextArea.bind("<Control-Key-c>", self.sCopy)
		self.TextArea.bind("<Control-Key-C>", self.sCopy)
		self.TextArea.bind("<Control-Key-v>", self.sPaste)
		self.TextArea.bind("<Control-Key-V>", self.sPaste)
		self.TextArea.bind("<Control-Key-z>", self.sUndo)
		self.TextArea.bind("<Control-Key-Z>", self.sUndo)
		# self.TextArea.bind("<Control-Key-y>", self.sRedo)
		# self.TextArea.bind("<Control-Key-Y>", self.sRedo)
		self.TextArea.bind("<Key-Delete>", self.sdelete)
		# self.TextArea.bind("<Key-F5>", self.sDT)
		# self.TextArea.bind("<Control-Key-b>", self.sBold)
		# self.TextArea.bind("<Control-Key-B>", self.sBold)
		# self.TextArea.bind("<Control-Key-i>", self.sItalic)
		# self.TextArea.bind("<Control-Key-I>", self.sItalic)
		self.TextArea.bind("<Control-Key-f>", self.sfind)
		self.TextArea.bind("<Control-Key-F>", self.sfind)
		# self.TextArea.bind("<Control-Key-h>", self.sReplace)
		# self.TextArea.bind("<Control-Key-H>", self.sReplace)

		self.TextArea.bind("<KeyPress>", self.setStatus_keyboard)
		self.TextArea.bind("<ButtonPress-1>", self.setStatus_button)
		self.root.config(menu=self.menubar)

	def showStatus(self):
		if self.vars.get()== True:
			# print('here')
			self.StatusFrame.destroy() 
		else: 
   			self.showsStatus()     
   	
	def showAbout(self):
		showinfo("About Notepad","Simple text editor like notepad using Python")
	def cut(self):
		self.TextArea.event_generate("<<Cut>>")
	def copy(self):
		self.t=self.TextArea.event_generate("<<Copy>>")
		# print(int(self.t))
	def paste(self):
		self.TextArea.event_generate("<<Paste>>")
	def delete(self):
		self.TextArea.event_generate("<<remove>>")

	# def showAbout(self,event):
	# 	showinfo("About Notepad","Simple text editor like notepad using Python")
	def sCut(self,event):
		self.TextArea.event_generate("<<Cut>>")
	def sCopy(self,event):
		self.t=self.TextArea.event_generate("<<Copy>>")
		# print(int(self.t))
	def sPaste(self,event):
		self.TextArea.event_generate("<<Paste>>")
	def sdelete(self,event):
		self.TextArea.event_generate("<<remove>>")

	def quitApplication(self):
		self.root.destroy()				
	def donothing(self):
		pass
	def saveasFile(self):
		pass
		self.files=None
		# if self.files == None:
		# Save as new file
		self.files = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")])
		if self.files == "":
			self.files = None
		else:
         # Try to save the file
			self.file = open(self.files,"w")
			self.file.write(self.TextArea.get(1.0,END))
			self.file.close()
         # Change the window title
			self.root.title(os.path.basename(self.files) + " - Notepad")
		# else:
		# 	self.file = open(self.files,"w")
		# 	self.file.write(self.TextArea.get(1.0,END))
		# 	self.file.close()
	def saveFile(self):
		self.files=None
		if self.files == None:
		# Save as new file
			self.files = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")])
			if self.files == "":
				self.files = None
			else:
         # Try to save the file
				self.file = open(self.files,"w")
				self.file.write(self.TextArea.get(1.0,END))
				self.file.close()
         # Change the window title
				self.root.title(os.path.basename(self.files) + " - Notepad")
		else:
			self.file = open(self.files,"w")
			self.file.write(self.TextArea.get(1.0,END))
			self.file.close()
		# add_checkButton()
	def saveShort(self,event):
		pass
		self.files=None
		if self.files == None:
		# Save as new file
			self.files = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")])
			if self.files == "":
				self.files = None
			else:
         # Try to save the file
				self.file = open(self.files,"w")
				self.file.write(self.TextArea.get(1.0,END))
				self.file.close()
         # Change the window title
				self.root.title(os.path.basename(self.files) + " - Notepad")
		else:
			self.file = open(self.files,"w")
			self.file.write(self.TextArea.get(1.0,END))
			self.file.close()	
	def newPage(self):
		pass
		self.root.title("Untitled Notepad")
		self.file=None
		self.asked=askyesnocancel("warning","Do you want to save this page?")
		if self.asked==True:
			if self.file==None:
				self.files = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")])
				self.TextArea.delete(1.0,END)
			elif self.asked==False:
				self.TextArea.delete(1.0,END)
	def openfile(self):
		pass
		self.file = askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
		if self.file == "":
         # no file to open
			self.file = None
		else:
         # Try to open the file
         # set the window title
			self.root.title(os.path.basename(self.file) + " - Notepad")
			self.TextArea.delete(1.0,END)
			self.file = open(self.file,"r")
			self.TextArea.insert(1.0,self.file.read())
			self.file.close()
	def sopen(self,event):
		pass
		self.file = askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
		if self.file == "":
         # no file to open
			self.file = None
		else:
         # Try to open the file
         # set the window title
			self.root.title(os.path.basename(self.file) + " - Notepad")
			self.TextArea.delete(1.0,END)
			self.file = open(self.file,"r")
			self.TextArea.insert(1.0,self.file.read())
			self.file.close()	
	def onClick(self):
		# pass
		if self.var.get()==True:
			# mytext=self.text.get(1.0,END)
			self.text.tag_add('bold1',1.0,END)
			self.text.tag_config('bold1',font=('bold'))
			# root.title("Checkbutton")
		else:
			self.text.tag_remove('bold1',1.0,END)
			# root.title('')

	def sfind(self,event):
		self.find =Toplevel()
		self.find.title('Find')
		self.find.resizable(0,0)
		self.find.grid_propagate(0)
		self.frm=Frame(self.find)
		self.frm.pack(side=TOP, pady=6)
		self.frm.grid_propagate(0)
		Label(self.frm, text="Find what? ").pack(side=LEFT,expand=YES, fill=BOTH)
		self.findw=Entry(self.frm, width=50)
		self.findw.focus_set()
		self.findw.pack(side=LEFT, expand=YES, fill=BOTH, padx=3)
		self.frm2=Frame(self.find)
		self.frm2.pack(side=TOP, pady=6)
		self.frm2.grid_propagate(0)
		Label(self.frm2, text="Replace with").pack(side=LEFT,expand=YES,fill=BOTH)
		self.replace=Entry(self.frm2,width=50)
		self.replace.pack(side=LEFT,expand=YES,fill=BOTH,padx=3)
		self.frm3=Frame(self.find)
		self.frm3.pack(side=TOP, padx=6)
		self.frm3.grid_propagate(0)
		self.findbtn= Button(self.frm3, text="Find", width=10 ,command=self.findit)
		self.findbtn.pack(side=LEFT,expand=YES,fill=BOTH, padx=3)
		self.replacebtn= Button(self.frm3, text="Replace",width=10, command=self.replaceit)
		self.replacebtn.pack(side=LEFT,expand=YES, fill=BOTH, padx=3)
		self.TextArea.tag_remove(SEL, '1.0', END)

	def find(self):
		self.find =Toplevel()
		self.find.title('Find')
		self.find.resizable(0,0)
		self.find.grid_propagate(0)
		self.frm=Frame(self.find)
		self.frm.pack(side=TOP, pady=6)
		self.frm.grid_propagate(0)
		Label(self.frm, text="Find what? ").pack(side=LEFT,expand=YES, fill=BOTH)
		self.findw=Entry(self.frm, width=50)
		self.findw.focus_set()
		self.findw.pack(side=LEFT, expand=YES, fill=BOTH, padx=3)
		self.frm2=Frame(self.find)
		self.frm2.pack(side=TOP, pady=6)
		self.frm2.grid_propagate(0)
		Label(self.frm2, text="Replace with").pack(side=LEFT,expand=YES,fill=BOTH)
		self.replace=Entry(self.frm2,width=50)
		self.replace.pack(side=LEFT,expand=YES,fill=BOTH,padx=3)
		self.frm3=Frame(self.find)
		self.frm3.pack(side=TOP, padx=6)
		self.frm3.grid_propagate(0)
		self.findbtn= Button(self.frm3, text="Find", width=10 ,command=self.findit)
		self.findbtn.pack(side=LEFT,expand=YES,fill=BOTH, padx=3)
		self.replacebtn= Button(self.frm3, text="Replace",width=10, command=self.replaceit)
		self.replacebtn.pack(side=LEFT,expand=YES, fill=BOTH, padx=3)
		self.TextArea.tag_remove(SEL, '1.0', END)
	def findit(self):
		pass
		self.start="1.0"
		self.end="end"
		self.start=self.TextArea.index(self.start)
		self.end=self.TextArea.index(self.end)
		self.count=IntVar()
		self.count=self.count
		self.TextArea.mark_set("matchStart",self.start)
		self.TextArea.mark_set("matchEnd",self.start)
		self.TextArea.mark_set("searchLimit",self.end)
		self.targetfind=self.findw.get()
		if self.targetfind:
			while True:
				self.where=self.TextArea.search(self.targetfind, "matchEnd","searchLimit", count=self.count)
				if self.where=="":
					break
				elif self.where:
					self.pastit=self.where + ('+%dc' % len(self.targetfind))
					self.TextArea.mark_set("matchStart",self.where)
					self.TextArea.mark_set("matchEnd","%s+%sc" % (self.where, self.count.get())) 
					self.TextArea.tag_add(SEL, self.where, self.pastit)
					self.TextArea.see(INSERT)
					self.TextArea.focus()
		

	def replaceit(self):
		# pass
		self.bodytxt=self.TextArea.get(1.0,END)
		self.finded=self.findw.get()
		self.replacew=self.replace.get()
		self.TextArea.replace(1.0, 'end',self.TextArea.get(1.0, 'end').replace(self.finded,self.replacew))  
			

				
	def GoTo(self):
		# global TextArea
			
		self.go=Toplevel()
		self.go.grid_propagate(0)
		self.go.resizable(0,0)
		self.go.title('Go To')
		Label(self.go,text='Enter Line Number?').pack(side=TOP,expand=YES,fill=BOTH)
		self.gotow=Entry(self.go,width=30,text='goto')
		self.gotow.pack(side=TOP,padx=5,pady=3)
		Button(self.go,text='Go To',width=10,command=self.findline).pack(side=TOP,expand=YES, fill=BOTH, padx=3)
	def sgoto(self,event):
		# global TextArea
			
		self.go=Toplevel()
		self.go.grid_propagate(0)
		self.go.resizable(0,0)
		self.go.title('Go To')
		Label(self.go,text='Enter Line Number?').pack(side=TOP,expand=YES,fill=BOTH)
		self.gotow=Entry(self.go,width=30,text='goto')
		self.gotow.pack(side=TOP,padx=5,pady=3)
		Button(self.go,text='Go To',width=10,command=self.findline).pack(side=TOP,expand=YES, fill=BOTH, padx=3)
	def findline(self):
				self.goline=self.gotow.get()
				self.TextArea.mark_set(INSERT,self.goline +'.0')
				self.TextArea.see(INSERT)
				self.TextArea.focus()	
	def selectall(self):
		pass
		try:
			self.TextArea.tag_add(SEL,'1.0',END)
			self.TextArea.mark_set(INSERT,'1.0')
			self.TextArea.see(INSERT)
			return 'break'
		except:
			showinfo("message","Nothing to Select")	
	def shortSelect(self,event):
		pass
		try:
			self.TextArea.tag_add(SEL,'1.0',END)
			self.TextArea.mark_set(INSERT,'1.0')
			self.TextArea.see(INSERT)
			return 'break'
		except:
			showinfo("message","Nothing to Select")	
	def showfont(self):
		pass
		
# https://www.tutorialbrain.com/css_tutorial/css_font_family_list/
		self.stylelist=['AcadEref','Agency FB','AIGDT','Algerian','AmdSymbols','AMGDT','Arial','Arial Rounded MT Bold','Arial narrow','Arial Black','Helvetica','Verdana', 
'Calibri','Century Gothic','Candara','Noto','Lucida Sans','']
		self.numlist=[8,9,10,11,12,13,14,15,16,17,18,19,20,72]
		self.fontlist=['normal','italic','bold','bold italic']

		self.font=Toplevel()
		self.font.geometry('450x350') 
		self.font.title("Font")
		self.font.resizable(0,0)
		Label(self.font,text="Font:").grid(row=0,column=0,columnspan=2)

		self.stent=StringVar()
		self.stentry=Entry(self.font,width=23,textvariable=self.stent)
		self.stentry.grid(row=1,column=0,columnspan=2)
		self.stent.set('arial')
		self.yscrollbar=Scrollbar(self.font,orient='vertical')
		self.stylebox=Listbox(self.font,yscrollcommand=self.yscrollbar.set,exportselection=0)
		self.yscrollbar.grid(row=2, column=2,sticky='ns')
		self.yscrollbar.config(command=self.stylebox.yview)
		for i in self.stylelist:
			self.stylebox.insert(END,str(i))
		self.stylebox.grid(row=2,column=0,columnspan=2)	
		# self.stylecomb=ttk.Combobox(self.font, value=self.stylelist)
		# self.stylecomb.set('AcadEref')
		# self.stylecomb.grid(row=1,column=0,columnspan=3,padx=10)
		self.stylebox.bind("<<ListboxSelect>>", self.style_select)

		Label(self.font,text="Font style:").grid(row=0,column=3,columnspan=2)
		self.stent1=StringVar()
		self.stentry1=Entry(self.font,width=20,textvariable=self.stent1)
		self.stentry1.grid(row=1,column=3,columnspan=2)
		self.stent1.set('normal')
		self.yscrollbar1=Scrollbar(self.font,orient='vertical')
		self.stylebox1=Listbox(self.font,yscrollcommand=self.yscrollbar1.set)
		self.yscrollbar1.grid(row=2, column=6,sticky='ns')
		self.yscrollbar1.config(command=self.stylebox1.yview)
		for i in self.fontlist:
			self.stylebox1.insert(END,str(i))
		self.stylebox1.grid(row=2,column=3,columnspan=2,)	
		# self.fontcomb=ttk.Combobox(self.font, value=self.fontlist)
		# self.fontcomb.set('Regular')
		# self.fontcomb.grid(row=1,column=3,columnspan=3,padx=10)
		self.stylebox1.bind("<<ListboxSelect>>", self.size_select)

		Label(self.font,text="Size:").grid(row=0,column=8,columnspan=2)
		self.stent2=StringVar()
		self.stentry2=Entry(self.font,width=20,textvariable=self.stent2)
		self.stentry2.grid(row=1,column=8,columnspan=2)
		self.stent2.set('12')
		self.yscrollbar2=Scrollbar(self.font,orient='vertical')
		self.stylebox2=Listbox(self.font,yscrollcommand=self.yscrollbar2.set)
		self.yscrollbar2.grid(row=2, column=10,sticky='ns')
		self.yscrollbar2.config(command=self.stylebox2.yview)
		for i in self.numlist:
			self.stylebox2.insert(END,str(i))
		self.stylebox2.grid(row=2,column=8,columnspan=2,)
		self.stylebox2.bind("<<ListboxSelect>>", self.num_select)
		self.varl=BooleanVar()
		self.underline =Checkbutton(self.font,text='Underline',variable=self.varl,command=self.under_line)
		self.underline.grid(row=3,column=0,padx=10,pady=20)

		self.labelframe = LabelFrame(self.font, text="Sample",width=220, height=80)
		self.labelframe.grid(row=3,column=4,columnspan=6, padx=5, pady=0, ipadx=0, ipady=0)
		# Entry(self.labelframe,).place(x=10, y=10, anchor="w")
		self.lb = Label(self.labelframe, text="PreviewText",font=('arial', 12,'normal'),)
		self.lb.place(x=110, y=30, anchor="center")

		self.btnok= Button(self.font, text="Ok",width=10, command=self.clickok )
		self.btnok.grid(row=4,column=0,columnspan=9,padx=10,pady=20)
		# Label(self.font,text="Preview Text").grid(row=2,column=3,padx=10,pady=20)
		self.btncancel= Button(self.font, text="Cancel",width=10,command=self.cancel_effect )
		self.btncancel.grid(row=4,column=1,columnspan=10,padx=10,pady=20 )
		
	def style_select(self,event):

		# self.val=
		# self.val2=0
		# self.val3=""
		# # pass
		self.stent.set(self.stylebox.get(self.stylebox.curselection()))
		self.val=self.stylebox.get(self.stylebox.curselection())
		self.val2=self.stentry2.get()
		self.val3=self.stentry1.get()
		# print(self.val,self.val2,self.val3)
		# self.value=self.val
		self.lb.config(font=(self.val,self.val2,self.val3))
		self.label=self.val,self.val2,self.val3
		# print(self.label)
	def size_select(self,event):
		self.stent1.set(self.stylebox1.get(self.stylebox1.curselection()))  
		self.val=self.stylebox1.get(self.stylebox1.curselection())
		self.val2=self.stentry2.get()
		self.val3=self.stentry.get()
		
		self.lb.config(font=(self.val3,self.val2,self.val))
		self.label=self.val3,self.val2,self.val
		# print(self.label)
	def under_line(self):
		if self.varl.get()==True:
			self.lb.config(font='Verdana 10 underline')  
		else:
			self.labelframe.destroy()
			self.labelframe = LabelFrame(self.font, text="Sample",width=220, height=80)
			self.labelframe.grid(row=3,column=4,columnspan=6, padx=5, pady=0, ipadx=0, ipady=0)
			self.lb = Label(self.labelframe, text="PreviewText")
			self.lb.place(x=110, y=30, anchor="center")
		
	def num_select(self,event):
		self.stent2.set(self.stylebox2.get(self.stylebox2.curselection()))
		self.val=self.stylebox2.get(self.stylebox2.curselection())
		self.val2=self.stentry.get()
		self.val3=self.stentry1.get()
		self.lb.config(font=(self.val2,self.val,self.val3))
		self.label=self.val2,self.val,self.val3

	def cancel_effect(self):
		self.font.destroy()	
	def clickok(self):
		self.font.destroy()	
		self.TextArea.config(font=(self.label))
	def undo(self):
		try:
			self.TextArea.edit_undo()

		except:
			showinfo(title='Error', message='There is nothing to Undo')

	def sUndo(self,event):
		try:
			self.TextArea.edit_undo()

		except:
			showinfo(title='Error', message='There is nothing to Undo')
		
				
Notepad()


#npm i nodemom
# ternary opera