import random
from ID3 import *
from parse import *
from statistics import mode
## This will be a script that answers how a random forest compares to the single forest
forests = []

# lets randomly choose 20 forests

examples = parse('candy.data')

num_examples = len(examples)
train = int(.7*num_examples)
validate, testing = int(.15*num_examples), int(.15*num_examples)

# lets test this 50 times
single_accuracy = 0
forest_accuracy = 0
for _ in range(50):
    for i in range(20):
        # build 20 trees
        training_set = [random.choice(examples) for _ in range(train)]
        validation_set = [random.choice(examples) for _ in range(testing)]
        tree = ID3(training_set, 0)
        forests.append(tree)
        
    training_set = [random.choice(examples) for _ in range(train)]
    single_tree = ID3(training_set, 0)
    test_set = [random.choice(examples) for _ in range(testing)]

    single_accuracy += test(single_tree, test_set)
    correct, total = 0,0
    for ex in test_set:
        total += 1
        results = []
        for tree in forests:
            # for each example ask every tree
            results.append(evaluate(tree, ex))
        curr_res = mode(results)
        if curr_res == ex["Class"]:
            correct += 1
    forest_accuracy += (correct/total)

print("Random forest accuracy: " + str(forest_accuracy/50))
print("Single tree accuracy: " + str(single_accuracy/50))
    
    
    

