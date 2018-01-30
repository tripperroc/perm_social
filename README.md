# Capstone

To run the program, run the shell script, task.sh using following command:
"chmod u+x task.sh"
"./task.sh"
This will run the file as a shell script.

main.py is the python code where the entire execution of the code begins. Uncomment all the lines from main.py and run the code.

readText.py is used to read the JSON file and extract user IDs from the data to create a set of IDs(users).

mentionsGraph.py creates a graphs.json file that has all the users mentioned by corresponding individual user as a key-value pair.

splitDataset.py is used to split the dataset into 3 parts: training, testing and validation.

createDictionaryOfScores.createDict() creates a dictionary of each user as the key with their LIWC scores as the values.

extractEmotion.emotion() is used to extract some of the categories and differentiate users based on whether they are below the average score for a particular category or above it.

egograph.py is used to extract networkx features from the different set of users.

The files mentioned above are expected to be run through main.py only. The order in which the files need to be executed is mentioned in this file.
