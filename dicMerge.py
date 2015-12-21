#encoding:utf-8
import os, sys, time
start_time = time.time()

dicDirectory = sys.argv[1]
outPutFile = sys.argv[2]
outPutPath = dicDirectory + outPutFile

dicArray = []
dicName = []
merge = []

'''get all dictionary in specify directory'''
for file in os.listdir(dicDirectory):
    if file.endswith(".txt"):
        fileDir = dicDirectory + file
        dicArray.append(fileDir)
        dicName.append(file)

countDic = int(0)
print("\nProcessing:")
'''compare to entire dictionary'''
for eachDic in dicArray:
    if int(0) == countDic:
        print(eachDic)
        with open(eachDic, "r") as ins:
            for line in ins:
                merge.append(line.rstrip())
    else:
        print(eachDic)
        new_word_array = []
        duplicates = []
        new_list = []
        ''' put all new word into array for comparing duplicates '''
        with open(eachDic, "r") as ins:
            for line in ins:
                new_word_array.append(line.rstrip())

        ''' check if duplicated then put it into the duplicateList '''
        for new_word in new_word_array:
            ''' for filter anything '''
            if '..' in new_word:
                    duplicates.append(new_word)

            for old_word in merge:
                if new_word == old_word:
                    duplicates.append(new_word)

        ''' remove duplicates '''
        print("Number of duplicates: ",len(duplicates),"\n")
        new_list = list(set(new_word_array) - set(duplicates))
        
        ''' add to merge '''
        for new_words in new_list:
            merge.append(new_words)
    countDic += 1

''' write to result '''
result = open(outPutPath, 'w+')
result.write("\n".join(merge))
result.close()

''' information logging '''
print("\n-->",countDic," dictionary:\n ","	".join(dicName),"\n\n---> joined into: ",outPutFile,"\n---> Dictionary Size: ",len(merge)," words\n---> %s seconds" % (time.time() - start_time),"\n")
