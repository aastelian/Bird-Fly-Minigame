from config.definitions import ROOT_DIR
import tkinter as tk
from mainScript import Func
import keyboard as kb
from pil import Image, ImageTk

class App(Func):
    
    def __init__(self):
        self.mark = -40
        self.root = tk.Tk()
        self.root.geometry("800x400")
        self.canv = tk.Canvas(self.root, width=800, height=400)
        self.canv.config(highlightthickness=0)
        self.canv.pack()
        self.background = self.canv.create_rectangle(0,0,1200,400, fill="light blue")
        self.create_obstacles()
        
        self.img_non_resized = Image.open("bird.png")
        self.img = self.img_non_resized.resize((40,40))
        self.bird = ImageTk.PhotoImage(self.img)
        self.bird_image = self.canv.create_image(100,100,image=self.bird)
        
        #self.rect=self.canv.create_rectangle(100,100,120,120,fill="black")
        
        self.fly(self.background,0)
        self.fall(self.bird_image)
        kb.add_hotkey("w",lambda:self.ascend(self.bird_image))
        self.root.mainloop()
        
    def create_obstacles(self):
    
        if self.mark <= 0:
        
            for i in range(8):
            
                x0=850+i*100
                if i%2 == 0:
                    y0=80
                else:
                    y0=200
                self.obs = self.canv.create_rectangle(x0,y0,x0+100,y0+50,fill="red")
            
                self.fly(self.obs,-2)
            # x0=850
            # y0=200
            
            # self.obs = self.canv.create_rectangle(x0,y0,x0+100,y0+50,fill="red")
            
            # self.fly(self.obs,-2)
            
            # x0=950
            # y0=80
            
            # self.obs2 = self.canv.create_rectangle(x0,y0,x0+100,y0+50,fill="red")
            
            # self.fly(self.obs2,-2)
            
            # x0=1050
            # y0=200
            
            # self.obs3 = self.canv.create_rectangle(x0,y0,x0+100,y0+50,fill="red")
            
            # self.fly(self.obs3,-2)
            # self.mark = 850
            
            # x0=1150
            # y0=80
            
            # self.obs4 = self.canv.create_rectangle(x0,y0,x0+100,y0+50,fill="red")
            
            # self.fly(self.obs4,-2)
            self.mark = 850
            
        self.mark -= 2
        self.root.after(50, self.create_obstacles)
        
    
        
App()