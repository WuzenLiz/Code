from math import sin,cos, pi
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3
from direct.actor.Actor import Actor

class App(ShowBase):
 scaleX:float = 0.1 
 scaleY:float = 0.1
 scaleZ:float = 0.1
 speed:float = 1
 
 def __init__(self):
  ShowBase.__init__(self)
  self.scale = (self.scaleX,self.scaleY,self.scaleZ)
  # self.set_background_color(0,0,0,1)
  
  #sence
  self.scene = self.loader.loadModel('models/enviroment/CupOfWine')
  self.scene.reparentTo(self.render)
  self.scene.setScale(self.scale)
  self.scene.setPos(0,0,0)

  # #player
  # self.player = Actor('models/character/base')
  # self.player.reparentTo(self.render)
  # self.player.setScale(self.scale)
  # self.player.setPos(0,0,0)
  
  # #camera
  # self.camera.setPos(0,-50,0)
  # self.camera.lookAt(self.scene)
  # 
  #task
  # self.taskMgr.add(self.updateTask, "update")

  #action
  self.accept_once("wheel_up",self.zoomInAction)
  self.accept_once("wheel_down",self.zoomOutAction)
  # self.accept_once("mouse1",self.mouse1Action)
  # self.accept_once("mouse2",self.mouse2Action)
  # self.accept_once("mouse3",self.mouse3Action)
  
 # def updateTask(self, task):
 #  dt = globalClock.getDt()
 #  self.player.setPos(self.player.getPos() + Point3(0,0,dt*self.speed))
 #  return Task.cont
 
 def zoomInAction(self):
  self.scale = (self.scale[0]+0.5,self.scale[1]+0.5,self.scale[2]+0.5)
  self.scene.setScale(self.scale)
  
 def zoomOutAction(self):
  self.scale = (self.scale[0]-0.5,self.scale[1]-0.5,self.scale[2]-0.5)
  self.scene.setScale(self.scale)
 
 
app = App()
app.run()