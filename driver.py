import logging
import os
import os.path
#import gensim
#model = gensim.models.KeyedVectors.load_word2vec_format('lexvec.commoncrawl.300d.W+C.pos.neg3.vectors',binary = False)
import numpy as np

# Reads and returns the list of files from a directory
def read_directory(mypath):
    current_list_of_files = []

    while True:
        for (_, _, filenames) in os.walk(mypath):
            current_list_of_files = filenames
        logging.info("Reading the directory for the list of file names")
        return current_list_of_files


# Function you will be working with
def creating_subclusters(list_of_terms, name_of_file):
    
# Your code that converts the cluster into subclusters and saves the output in the output folder with the same name as input file
# Note the writing to file has to be handled by you.
    mypath = "annotations"
    name =  os.path.join(mypath,name_of_file)
    file_object = open(name)
    count_word = 0
    class_name = []
    words = []
    line_count = 0
    pedestrian_count = 0
    for line in file_object:
        line_count = line_count + 1
        if line_count == 6:
            for word in line.split(' '):
                count_word = count_word + 1
                class_name.append(0)
                words.append(word)            
            #print(word)
            pedestrian_count = int(words[5])
            break
    print(name_of_file)
    print(pedestrian_count)
    print('-------------------------------------------')
    p = 0
    #print(words)
    '''class_count = 0
    for i in range(0,count_word):
        for j in range(i+1,count_word):
            try:
                xx = model[[words[i]]]
            except:
                continue
            try:
                yy = model[[words[j]]]
            except:
                continue
            if np.dot(model[words[i]],model[words[j]]) > 70:
                if class_name[i] == 0 and class_name[j] == 0:
                    class_name[i] = class_name[j] = class_count + 1
                    class_count = class_count + 1
                elif class_name[i] == 0 and class_name[j] != 0:
                        class_name[i] = class_name[j]
                elif class_name[j] == 0 and class_name[i] != 0:
                    class_name[j] = class_name[i]'''
    '''print('----------------------------------------------------')
    print('File is ')
    print(pqr)
    print(len(class_name))
    print(count_word)
    print(words)
    print(class_name)'''
    '''mypath = "output"
    name = os.path.join(mypath,name_of_file)
    e = open(name,"w")    
    for i in range(0,class_count + 1):
        #print('--------------Class is ')
        #print(i)
        for j in range(0,count_word):            
            if class_name[j] == i:
                #print(words[j])
                e.write(words[j]+' ')
        #print('\n')
        e.write('\n')
    e.close()'''
    file_object.close()

    pass


# Main function
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

    # Folder where the input files are present
    mypath = "annotations"
    list_of_input_files = read_directory(mypath)
    for each_file in list_of_input_files:
        with open(os.path.join(mypath, each_file), "r") as f:
            file_contents = f.read()
        list_of_term_in_cluster = file_contents.split()

        # Sending the terms to be converted to subclusters in your code
        creating_subclusters(list_of_term_in_cluster, each_file)


        # End of code