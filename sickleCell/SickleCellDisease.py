#Defining a function to translate a string of characters(nucleotides) into the appropriate protein/amino acid

def translate(DNA):
    dnaList = []
    n_list = []
    tn_List = []
    for letter in DNA:
        dnaList.append(letter)
    for nuc in range(0, len(dnaList),3):
        ntide = ''
        nsle = ntide.join(dnaList[nuc: (nuc + 3)])
        n_list.append(nsle)
    for num,nucleo in enumerate(n_list):
        if n_list[num] == "ATT" or n_list[num] =='ATC' or n_list[num] =='ATA':
            word = "Isoleucine"
            tn_List.append(n_list[num] + " - represent: " + word)
        elif n_list[num] == 'CTT' or n_list[num] =='CTC' or n_list[num] =='CTA' or n_list[num] =='CTG' or n_list[num] =='TTA' or n_list[num] =='TTG':
            word = "Leucine"
            tn_List.append(n_list[num] + " -represent: " + word)
        elif n_list[num] == 'GTT' or n_list[num] =='GTC' or n_list[num] =='GTA' or n_list[num] =='GTG':
            word = "Valine"
            tn_List.append(n_list[num] + " -represent: " + word)
        elif n_list[num] == 'TTT' or n_list[num] =='TTC':
            word = "Phenylalanine"
            tn_List.append(n_list[num] + " -represent: " + word)
        elif n_list[num] == 'ATG':
            word = "Methionine"
            tn_List.append(n_list[num] + " -represent: " + word)
    return tn_List

c= translate("ATTCTTGTTTTTATGATAGTGCTCCTT")
print(c)


