#import libraries
import pandas as pd 
import numpy as np
#text file to dataframe 'data'
data = pd.read_csv('words.txt', sep=",", header=None)
#modify column name to 'a'
data.columns = ['a']
#add blank columns 'b','c', 'd'
data['b'] = ""
data['c'] = ""
data['d'] = ""
#text file to dataframe 'dictionary'
dictionary = pd.read_csv('dictionary.txt', header = None)
dictionary.columns = ['x']

#apply for loop to seprate text less then 6 and grater then 6 and append in blank columns 'b' ,'c' of dataframe 'data'
for i in range(0,len(data)):
    if len(str(data['a'][i])) <= 6:
        data['b'][i]= data['a'][i]
    else:
        data['c'][i]= data['a'][i]
#dictonary dataframe converting into 'y' list
y = dictionary['x'].values.tolist()

#create a blank list 'end' to store all decompounding values
end = []
#apply for loop for selecting string values from column 'c' of dataframe 'data' and apply decompounding on each value
for x in data['c'].iloc[:len(data)]:
    #create a blank list 'final' to store decompounding values of each word
    final = []
    
    #print(x)
    #apply if condition and append blank string to list 'end' if condition satisfies 
    if len(x) == 0:
        end.append("")
    #if Condition not satisfies then
    else:
        #apply for loop on string 'x'
        for k in range(1,len(x)):
            #creat two blank lists 'last', 'first'
            last = []
            first = []
            #value i stores string first part if string is decompoundable
            i = x[0:k]
            #value j stores string last part if string is decompoundable
            j = x[k:len(x)]
            #apply for loop on dictonary list 'y' for comparison with string 'x' and decopound it  
            for item in y:
                #apply if condation on j to check that it is present in dictonary or not
                if item == j :
                    last.append(item)
                #apply if condation on i to check that it is present in dictonary or not    
                elif item == i:   
                    first.append(item)
            #apply if condation on list 'last' and list 'first'  to check weather they are 0 or not if not then append in list 'final'       
            if len(last)!= 0 and len(first)!=0:
                final.append(first[0])
                final.append(last[0])
        #apply if condition on list 'final' to check weather it is empty or not if it is then append string 'x' into list 'final'        
        if len(final) == 0:
            final.append(x)
        #every final list in loop append in list 'end'
        end.append(final)
#list 'end' append in dataframe 'data' in column 'd'
data['d'] = np.array(end)
#initialized a new list 'strlist' to store dataframe column's data from list to string formate
strlist = []
#apply for loop on dataframe's column 'd'
for i in data['d'].iloc[:len(data)]:
    #variable 'listToStr' contain value converted from list to string formate
    listToStr = ' '.join([str(elem) for elem in i]) 
    #append each converted value from list to string in 'strlist'
    strlist.append(listToStr)
#add list 'strlist' into dataframe 'data' in column 'e'
data['e'] = np.array(strlist)
#add both columns 'b' and 'e' into column 'f' of dataframe
data['f'] = data['b']+data['e']
#save dataframes data into csv file 'Comprased_word.csv'
data.to_csv('path/to/save/file/file_name.csv', index=False)
