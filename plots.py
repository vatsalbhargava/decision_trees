import ID3
import parse
import random
import matplotlib.pyplot as plt

def getPlottedResults(infile):
    withPruning = {}
    withoutPruning = {}
    data = parse.parse(infile)

    for i in range(10, 301, 29):
        total_nonPruneAcc = 0
        total_pruneAcc = 0

        for j in range(100):
            # Create a copy of the data and shuffle the copy
            shuffled_data = data.copy()
            random.shuffle(shuffled_data)
            train = shuffled_data[:i]
            test = shuffled_data[i:]

            tree = ID3.ID3(train, 'democrat')
            nonPruneAcc = ID3.test(tree, test)
            
            ID3.prune(tree, test)
            pruneAcc = ID3.test(tree, test)

            total_nonPruneAcc += nonPruneAcc
            total_pruneAcc += pruneAcc

        withoutPruning[i] = total_nonPruneAcc / 100
        withPruning[i] = total_pruneAcc / 100

    # Plotting the learning curves
    plt.figure(figsize=(10, 6))
    
    plt.plot(list(withoutPruning.keys()), list(withoutPruning.values()), label='Without Pruning', marker='o')
    plt.plot(list(withPruning.keys()), list(withPruning.values()), label='With Pruning', marker='o')
    
    plt.xlabel('Number of Training Examples')
    plt.ylabel('Accuracy')
    plt.title('Learning Curves')
    plt.legend()
    plt.grid(True)
    plt.show()

# Assuming your file name is 'house_votes_84.data'
getPlottedResults('house_votes_84.data')
