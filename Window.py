from Tkinter import *

class Window(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)                 
		self.master = master
		self.init_window()
        
    #Creation of init_window
	def init_window(self):
		# changing the title of our master widget      
		self.master.title("3D Transformation")

		# Define all the widgets
		self.canvas = Canvas(self, width=768, height=561)
		self.rect = self.canvas.create_rectangle(50, 25, 150, 75, fill="blue")

		self.UIPanel = LabelFrame(self)

		self.cubePanel = LabelFrame(self.UIPanel, text="Cube Controls")
		self.vertex = Button(self.cubePanel, text="Vertex")
		self.edge = Button(self.cubePanel, text="Edge")
		self.face = Button(self.cubePanel, text="Face")
		self.zSlider = Scale(self.cubePanel, from_=-50, to=50, orient=HORIZONTAL, showvalue=False)

		self.camPanel = LabelFrame(self.UIPanel, text="Camera Controls")

		self.top = Button(self.camPanel, text="Top")
		self.front = Button(self.camPanel, text="Front")
		self.camSlider = Scale(self.camPanel, from_=0, to=100, orient=HORIZONTAL, showvalue=False)
		
		# Pack the panels, place the widgets
		self.pack(fill=BOTH, expand=YES)
		self.canvas.pack(fill=BOTH, expand=YES)

		self.UIPanel.pack(fill=BOTH, expand=YES)

		self.cubePanel.pack(fill=BOTH, expand=YES, side=LEFT)
		self.vertex.place(relx=0.0, rely=0.5, anchor=W)
		self.edge.place(relx=0.3, rely=0.5, anchor=CENTER)
		self.face.place(relx=0.5, rely=0.5, anchor=CENTER)
		self.camSlider.place(relx=1.0, rely=0.5, anchor=E)

		self.camPanel.pack(fill=BOTH, expand=YES, side=RIGHT)
		self.top.place(relx=0.0, rely=0.5, anchor=W)
		self.front.place(relx=0.5, rely=0.5, anchor=CENTER)
		self.camSlider.place(relx=1.0, rely=0.5, anchor=E)

# 		placing the button on my window

root = Tk()

#size of the window
root.geometry("896x693")

app = Window(root)

root.mainloop()