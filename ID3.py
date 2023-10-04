from node import Node
import math

def entropy(examples):
  return examples

def find_best_attribute(examples):
  #dict = {all attributes : {all attribute outcomes : {all class outcomes : count}}}
  entropy_dict = {}
  all_attributes = set(examples[0].keys())
  all_attributes.remove("Class")

  #first, build a dict, keys are all attributes, set equal to {} initially
  for attribute in all_attributes:
    entropy_dict[attribute] = {}
    #second, go through all examples for all attributes, create map of attribute outcome and set to {} intially
    for ex in examples:
      possible_attribute_outcome = ex[attribute]
      if possible_attribute_outcome != "?" and possible_attribute_outcome not in entropy_dict[attribute]:
        entropy_dict[attribute][possible_attribute_outcome] = {}
      #at this point, we should have a dict in which the keys are all the attributes
      #the values should be a dict with the keys as all the attribute outcomes and values a dict
      #i.e. entropy_dict[cuisine] = {thai:{}, mexican:{}, italian:{}}

  #third, for each attribute outcome for every attribute, make dict all possible classes to their count
  total_valid_examples = 0
  for ex in examples:
    for attribute in all_attributes:
      possible_attribute_outcome = ex[attribute]
      if possible_attribute_outcome != "?":
        class_outcome = ex["Class"]
        if class_outcome not in entropy_dict[attribute][possible_attribute_outcome]:
          entropy_dict[attribute][possible_attribute_outcome][class_outcome] = 1
        else:
          entropy_dict[attribute][possible_attribute_outcome][class_outcome] += 1
        total_valid_examples += 1

  #entropy_dict should be filled now
  res = None
  minimum = float('inf')  
  for attribute in entropy_dict:
    single_attribute_values_ratio_dict = {}
    current_attribute_entropy = 0
    attribute_values = entropy_dict[attribute]
    for single_attribute_value in attribute_values:
      #single attribute values is equivalent to something like Thai or burger
      class_outcome = attribute_values[single_attribute_value]
      # class_outcome is yes: 3, no: 5, maybe: 7
      total_valid_examples_per_attribute = 0
      for outcome in class_outcome:
        total_valid_examples_per_attribute += class_outcome[outcome]
      single_attribute_values_ratio_dict[single_attribute_value] = total_valid_examples_per_attribute/total_valid_examples
      single_attribute_entropy = 0
      for outcome in class_outcome:
        single_attribute_entropy += -1*((class_outcome[outcome]/total_valid_examples_per_attribute)*math.log(class_outcome[outcome]/total_valid_examples_per_attribute,2))
      current_attribute_entropy += single_attribute_values_ratio_dict[single_attribute_value]*single_attribute_entropy
    if current_attribute_entropy < minimum:
      minimum = current_attribute_entropy
      res = attribute
  
  return [res, minimum]


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
  best_attribute, child_entropy = find_best_attribute(examples)

  currNode.entropy = parent_entropy - child_entropy
  currNode.splitting_attribute = best_attribute

  #do this for all children, remove from examples the rows with splitting attribute = best attribute
  #will need to loop for this, and recursive call each time
  

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
  # leaf node
  if not node.children: 
      return node.label
  # missing attribute
  if example[node.splitting_attribute] == "?":
      return node.label
  if example[node.splitting_attribute] in node.children:
      return evaluate(node.children[example[node.splitting_attribute]], example)

  return node.label

#this assumes that node.children is gonna be a dict of attribute values (thai, mexican, etc) to further nodes