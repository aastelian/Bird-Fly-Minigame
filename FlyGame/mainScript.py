from config.definitions import ROOT_DIR

class Func:
    
    def fly(self,id,speed):
        
        self.canv.move(id,speed,0)
        
        self.root.after(50,lambda:self.fly(id,speed))
        
    def fall(self,id):
        self.canv.move(id,0,3)
        self.root.after(50,lambda:self.fall(id))
        
    def ascend(self,id):
        self.canv.move(id,0,-20)
        