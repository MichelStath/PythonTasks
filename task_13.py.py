#ΕΡΓΑΣΙΑ 13
#Γράψτε ένα πρόγραμμα σε Python το οποίο παίρνει σαν είσοδο από το χρήστη έναν αριθμό πιστοτικής κάρτας (16 ψηφία) και χρησιμοποιεί τον αλγόριθμο του Luhn για να επιβεβαιώσει τον τύπο της.

#ΣΥΝΑΡΤΗΣΗ ΠΟΥ ΒΡΙΣΚΕΙ ΑΝ Ο ΑΡΙΘΜΟΣ ΤΗΣ ΚΑΡΤΑΣ ΕΙΝΑΙ ΕΓΚΥΡΟΣ 
def luhn_check(number):
    if number.isdigit():
        last_digit = int(str(number)[-1])
        reverse_sequence = list(int(d) for d in str(int(number[-2::-1])))

        for i in range(0, len(reverse_sequence), 2):
            reverse_sequence[i] *= 2

        for i in range(len(reverse_sequence)):
            if reverse_sequence[i] > 9:
                reverse_sequence[i] -= 9

        sum_of_digits = 0
        for i in range(len(reverse_sequence)):
            sum_of_digits += reverse_sequence[i]

        result = divmod(sum_of_digits, 10)

        if result == last_digit:
            print("[VALID]: %s CARD NUMBER IS VALID. " % number)
        else:
            print("%s CARD NUMBER IS INVALID." % number)
        quit()

    print("[ERROR]: \"%s\" IS NOT A VALID SEQUENCE. TRY AGAIN! " % number)


#ΕΙΣΑΓΩΓΗ ΑΡΙΘΜΟΥ ΚΑΡΤΑΣ
number = input ("give your card 16digit number : ")
luhn_check(number)

#τσεκ για νουμερο
#if not (len(result) == 16) or not type(int(result) == int) :
