#ΕΡΓΑΣΙΑ: 11
#Γράψτε ένα πρόγραμμα σε Python το οποίο έχει μια λίστα από 4άδες αριθμών σε ένα αρχείο και παίρνει σαν είσοδο μια 6άδα αριθμών με σειρά προτεραιότητα και εμφανίζει το αν υπάρχει διαθέσιμη 4άδα από αυτούς τους 6 αριθμούς.

#ΕΙΣΟΔΟΣ ΑΡΧΕΙΟΥ
file = input('give a file as testfile.txt : ')

#ΜΕΤΑΦΟΡΑ ΤΕΤΡΑΔΩΝ ΑΠΟΤ ΤΟ ΑΡΧΕΙΟ ΣΕ ΜΙΑ ΛΙΣΤΑ ΜΕ ΟΝΟΜΑ "lines"
with open(file) as file_in:
    lines = []
    for line in file_in:
        lines.append(line)

#ΑΦΑΙΡΕΣΗ ΤΩΝ ΣΤΟΙΧΕΙΩΝ "\n"       
lines = [line.rstrip('\n') for line in open("testfile.txt")]

#ΕΙΣΑΓΩΓΗ ΕΞΑΨΗΦΙΟΥ ΑΠΟ ΤΟΝ ΧΡΗΣΤΗ ΚΑΙ ΜΕΤΑΤΡΟΠΗ ΣΕ ΛΙΣΤΑ
number = str(input ('give your  6-digit number in priority order like "123456" :'))
#number = list(number)

# ΔΗΜΙΟΥΡΓΙΑ ΠΡΟΣΩΡΙΝΗΣ ΛΙΣΤΑΣ ΜΕ ΜΟΝΑΔΙΚΟ ΣΤΟΙΧΕΙΟ ΓΙΑ ΚΑΘΕ ΕΠΑΝΑΛΗΨΗ ΤΟΝ ΚΑΘΕ ΤΕΤΡΑΨΗΦΙΟ ΑΠΟ ΤΗΝ ΛΙΣΤΑ "lines"
templist = []
for i in lines : 
    templist = i
    templist = list(templist)   
    for j in list(number):    #ΕΛΕΓΧΟΣ ΥΠΑΡΞΗΣ ΤΟΥ ΚΑΘΕ ΨΗΦΙΟΥ ΤΗΣ 6ΑΔΑΣ ΣΤΙΣ 4ΑΔΕΣ       
        if j in templist :  #ΑΝ ΥΠΑΡΧΕΙ ΚΑΠΟΙΟ ΨΗΦΙΟ ΑΦΑΙΡΕΙΤΑΙ ΜΕ ΣΤΟΧΟ ΝΑ ΜΕΙΝΕΙ Η ΠΡΟΣΩΡΙΝΗ ΛΙΣΤΑ ΚΕΝΗ
            templist.remove(j)
    if templist == []:  #ΑΝ Η ΛΙΣΤΑ ΕΙΝΑΙ ΚΕΝΗ , ΤΟΤΕ ΥΠΑΡΧΕΙ ΔΙΑΘΕΣΙΜΗ ΤΕΤΡΑΔΑ
        print("there is an available 4-digit number")
        print("you gave the nymber :" , number , " and your available 4-digit number is :" , i)
        break
    else :
        print("there is no available 4-digit number in :" , i ,"for :" , number)


