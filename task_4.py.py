#ΕΡΓΑΣΙΑ 4
#Γράψτε μια συνάρτηση η οποία μετατρέπει ένα string σε αριθμό σύμφωνα με την αναπαράσταση των αριθμών σε ASCII code και μετά ελέγχει αν ο αριθμός είναι πρώτος. Για τον έλεγχο αν ένας αριθμός είναι πρώτος ΔΕΝ μπορείτε να χρησιμοποιήσετε εξωτερική βιβλιοθήκη.

#ΕΙΣΑΓΩΓΗ STRING ΑΠΟ ΤΟΝ ΧΡΗΣΤΗ
word = input('Give a string : ')

# ΜΕΤΑΤΡΟΠΗ ΣΕ ΛΙΣΤΑ ΓΙΑΤΟΝ ΔΙΑΧΩΡΙΣΜΟ ΤΩΝ ΧΑΡΑΚΤΗΡΩΝ
word = list(word)
print (word)
finnum=str('')
i=0

#ΜΕΤΑΤΡΟΠΗ ΤΩΝ ΧΑΡΑΚΤΗΡΩΝ ΣΕ ASCII code
while i<len(word) :
    word[i] = str(ord(word[i])) 
    i=i+1
i=0

#ΕΝΩΣΗ ΟΛΩΝ ΤΩΝ ΑΡΙΘΜΩΝ ASCII
while i<len(word) :
    finnum = finnum + word[i]
    i=i+1
print (word,finnum)

# finnum: Ο ΕΝΙΑΙΟΣ ΑΡΙΘΜΟΣ ΣΕ ΜΟΡΦΗ "INT"
finnum =int(finnum) 

#ΕΛΕΓΧΟΣ ΑΝ ΕΙΝΑΙ ΠΕΡΙΤΤΟΣ Η ΟΧΙ
for i in range(2,finnum):          
    if (finnum % i) == 0: 
        prime = 0  
        break
    else: 
         prime = 1
         
#ΕΜΦΑΝΙΣΗ ΜΗΝΥΜΑΤΩΝ ΓΙΑ ΤΟ ΑΠΟΤΕΛΕΣΜΑ ΤΟΥ ΑΡΙΘΜΟΥ 
if prime:
    print("Your string in ASCII code is not a prime number")
else:
   print("Your string in ASCII code is a prime number") 
