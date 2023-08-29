from direct.actor import Actor

class Character(Actor):
 def __init__(self):
  super().__init__()
  
  self.playable = False
  self.c_pos = (0,0,0)
  self.c_scale = (1,1,1)
  self.c_model = None
  self.render = None
  
  self.c_model.reparentTo(self.render)
  self.c_model.setPos(self.c_pos)
  self.c_model.setScale(self.c_scale)

  self.accept("wheel_up",self.zoomInAction())
  self.accept("wheel_dowm",self.zoomOutAction())
  
  if self.playable:
   self.accept("mouse1",self.mouse1Action())
   self.accept("mouse2",self.mouse2Action())
   self.accept("mouse3",self.mouse3Action())
 
 def zoomInAction(self):
  self.c_scale = (self.c_scale[0]+0.5,self.c_scale[1]+0.5,self.c_scale[2]+0.5)
  self.c_model.setScale(self.c_scale)
 
 def zoomOutAction(self):
  self.c_scale = (self.c_scale[0]-0.5,self.c_scale[1]-0.5,self.c_scale[2]-0.5)
  self.c_model.setScale(self.c_scale)
  
 def mouse1Action(self):
  pass
 
 def mouse2Action(self):
  pass
 
 def mouse3Action(self):
  pass