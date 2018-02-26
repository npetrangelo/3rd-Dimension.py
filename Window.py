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
		self.canvas.config(bg="black")
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
		self.vertex.place(relx=0.2, rely=0.5, anchor=CENTER)
		self.edge.place(relx=0.4, rely=0.5, anchor=CENTER)
		self.face.place(relx=0.6, rely=0.5, anchor=CENTER)
		self.zSlider.place(relx=0.8, rely=0.5, anchor=CENTER)

		self.camPanel.pack(fill=BOTH, expand=YES, side=RIGHT)
		self.top.place(relx=0.25, rely=0.5, anchor=CENTER)
		self.front.place(relx=0.5, rely=0.5, anchor=CENTER)
		self.camSlider.place(relx=0.75, rely=0.5, anchor=CENTER)

# 		placing the button on my window

root = Tk()

#size of the window
root.geometry("896x693")

app = Window(root)

while True:
	root.update_idletasks()
	root.update()