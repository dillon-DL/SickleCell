#Defining a function to translate a string of characters/nucleotides (inputted) into the appropriate protein/amino acid
#Defining lists that shall store data in it, in the format we want
#Then iterate through the loop in intervals of 3 to group 3 nucleotides at a time
#We then iterate through the new list namely n_list to obtain each element in the loop
#It is then checked with an if, elif, else statements if it matches the appropriate codons/proteins defined
#Lastly a new list is displayed that shows one what each DNA codon represents(its actual name)
def translate(DNA):
    dnaList = []
    n_list = []
    tn_List = []
    for letter in DNA.replace("\n", ""):
        dnaList.append(letter)
    for nuc in range(0, len(dnaList),3):
        ntide = ''
        nsle = ntide.join(dnaList[nuc: (nuc + 3)])
        n_list.append(nsle)
    for num,nucleo in enumerate(n_list):
        if n_list[num] == "ATT" or n_list[num] =='ATC' or n_list[num] =='ATA':
            word = "Isoleucine"
            tn_List.append( n_list[num] + " - represent: " + word)
        elif n_list[num] == 'CTT' or n_list[num] =='CTC' or n_list[num] =='CTA' or n_list[num] =='CTG' or n_list[num] =='TTA' or n_list[num] =='TTG':
            word = "Leucine"
            tn_List.append( n_list[num] + " -represent: " + word)
        elif n_list[num] == 'GTT' or n_list[num] == 'GTC' or n_list[num] =='GTA' or n_list[num] =='GTG':
            word = "Valine"
            tn_List.append( n_list[num] + " -represent: " + word)
        elif n_list[num] == 'TTT' or n_list[num] == 'TTC':
            word = "Phenylalanine"
            tn_List.append( n_list[num] + " -represent: " + word)
        elif n_list[num] == 'ATG':
            word = "Methionine"
            tn_List.append( n_list[num] + " -represent: " + word)
        else:
            word = "X"
            tn_List.append( n_list[num] + " -represent: " + word)

    return tn_List
# c= translate("ATTCTTGTTTTTATGATAGTGCTCCTTCAAAAGTGATAA")
# print(c)

########################################################################################################################

#In this function we will be reading the txt file DNA
#Then we shall be using the count method to count the occurence of 'a'
#Used the bold print funtion to emphasize the number of occurences in the DNA.txt file
#Lastly replace 'a' with 'A' in the first case/scenario, and 'T' in the second case/scenario for thr respective normal and mutated DNA txt files that it shall be written too
def Mutate(f):
    f = open("DNA.txt", "r", encoding= "UTF-8-sig")
    ofile = open("normalDNA.txt", 'w')
    ofile2 = open("mutatedDNA.txt", 'w')
    dna = str(f.read().replace("\n", ""))
    print("\n")
    print('\033[1m{:10s}\033[0m'.format("Occurances of 'a' is: {} ".format(dna.count("a"))))
    print("\n")

    for na in dna:
        if "a" in dna:
            nDNA = dna.replace("a", '\033[1m{:2s}\033[0m'.format(' A '))
    ofile.write(nDNA)
    print(nDNA)
    print("\n")

    for ma in dna:
        if "a" in dna:
            mDNA = dna.replace("a", '\033[1m{:1s}\033[0m'.format(' T '))
    ofile2.write(mDNA)
    print(mDNA)
    print("\n")
    return ofile, ofile2
#Mutate("DNA.txt")

########################################################################################################################

#Here we will be defining a function that allows the translate function to be capable of reading a text file
#As well as peform the Mutated function to display the results of this function from the txt file that is read
#Lastly displays all the this data for the chosen txt file of the user
def txtTranslate(fileO):
    fileO = open("DNA.txt", "r", encoding="UTF-8-sig")
    dnat = ''.join(fileO.read().replace("\n", ""))
    o = translate(dnat)
    p = Mutate(str(o))
    print(o)
    print("\n", "\n", "\n")
    fileO.close()
    return o, p

txtTranslate("DNA.txt")


