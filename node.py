class Node:
  def __init__(self):
    self.ignore_attributes = []
    self.label = None
    self.children = {}
    self.entropy = None
    self.splitting_attribute = None
    
    