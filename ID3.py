from node import Node
import math

def entropy(examples):
  return examples

def find_best_attribute(examples):
  all_attributes = set(examples[0].keys())
  all_attributes.remove("Class")
  res = None
  minimum = float('inf')
  for single_att in all_attributes:
    count = {}
    tc = 0
    for ex in examples:
      tc += 1
      # track the count for each value per attribute
      if ex[single_att] not in count:
        count[ex[single_att]] = 0
      count[ex[single_att]] += 1
      
    entropy = 0
    for val in count:
      entropy += -1*((count[val]/tc) * log2((count[val]/tc)))
      
    if entropy < minimum:
      res = single_att
      minimum = entropy
      
  return res

def ID3(examples, default):
  '''
  Takes in an array of examples, and returns a tree (an instance of Node) 
  trained on the examples.  Each example is a dictionary of attribute:value pairs,
  and the target class variable is a special attribute with the name "Class".
  Any missing attributes are denoted with a value of "?"
  '''
  
  currNode = Node()
  currNode.label = default
  
  # shouldnt hit this case
  if not examples:
    return currNode
  
  # check if every class in examples is the SAME
  occurencePerClass = {}
  for ex in examples:
    if ex["Class"] not in occurencePerClass:
      occurencePerClass[ex["Class"]] = 0
    occurencePerClass[ex["Class"]] += 1
  
  currNode.label = list(occurencePerClass.keys())[0]

  if len(occurencePerClass) == 1 and len(examples[0].keys() < 2):
    return currNode
  
  parent_entropy = entropy(examples)
  best_attribute = find_best_attribute(examples)
  

def prune(node, examples):
  '''
  Takes in a trained tree and a validation set of examples.  Prunes nodes in order
  to improve accuracy on the validation data; the precise pruning strategy is up to you.
  '''
  print(node)

def test(node, examples):
  '''
  Takes in a trained tree and a test set of examples.  Returns the accuracy (fraction
  of examples the tree classifies correctly).
  '''
  print(node)

def evaluate(node, example):
  '''
  Takes in a tree and one example.  Returns the Class value that the tree
  assigns to the example.
  '''
  print(node)