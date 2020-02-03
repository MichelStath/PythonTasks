#ΕΡΓΑΣΙΑ: 12
#Γράψτε ένα πρόγραμμα σε Python το οποίο παίρνει μια ημερομηνία σε μορφή ΗΗ/ΜΜ/ΕΕΕΕ και εμφανίζει πόσες μέρες/ώρες/δευτερόλεπτα απέχει αυτή από σήμερα καθώς και πόσες ημέρες έχει ο μήνας εκείνης της ημερομηνίας.
import datetime
from calendar import monthrange

#ΟΡΙΣΜΟΣ ΣΗΜΕΡΙΝΗΣ ΗΜΕΡΟΜΗΝΙΑΣ
today = datetime.date.today()  

# ΕΙΣΑΓΩΓΗ ΗΜΕΡΟΜΗΝΙΑΣ ΑΠΟ ΤΟΝ ΧΡΗΣΤΗ ΣΤΗΝ ΜΟΡΦΗ: "dd/mm/yyyy"
userdate = str(input('give date as: dd/mm/yyyy : ')) 

#ΜΕΤΑΤΡΟΠΗ ΗΜΕΡΟΜΗΝΙΑΣ ΣΕ ΛΙΣΤΑ ΚΑΙ ΑΦΑΙΡΕΣΗ "/"
userdate = list(userdate)
userdate.remove("/")
userdate.remove("/")

#ΕΠΙΛΟΓΗ ΚΑΤΑΛΛΗΛΩΝ ΣΤΟΙΧΙΩΝ ΑΠΟ ΤΗΝ ΛΙΣΤΑ ΓΙΑ ΤΟΝ ΟΡΙΣΜΟ ΤΗΣ ΗΜΕΡΟΜΗΝΙΑΣ ΤΟΥ ΧΡΗΣΤΗ
day = int(userdate[0] + userdate[1])
month = int(userdate[2]+userdate[3])
year = int(userdate[4] + userdate[5] + userdate[6] + userdate[7])
someday = datetime.date(year,month,day )

#ΥΠΟΛΟΓΙΣΜΟΣ ΔΙΑΦΟΡΑΣ ΜΕΡΩΝ ΑΝΑΜΕΣΑ ΣΤΙΣ ΗΜΕΡΟΜΗΝΙΕΣ ΚΑΙ ΜΕΤΑΤΡΟΠΗ ΣΕ ΩΡΕΣ ΚΑΙ ΔΕΥΤΕΡΟΛΕΠΤΑ
diff = someday - today
hours = diff.days * 24
seconds = hours * 3600

#ΕΥΡΕΣΗ ΗΜΕΡΩΝ ΤΟΥ ΜΗΝΑ ΤΗΣ ΗΜΕΡΟΜΗΝΙΑΣ ΤΟΥ ΧΡΗΣΤΗ
monthdays = monthrange(year, month)

#ΕΜΦΑΝΙΣΗ ΣΤΟΙΧΕΙΩΝ
print ('This date is: ',diff.days,'days,', hours, 'hours,', seconds,'seconds off')
print('The given  month has:',monthdays[1] ,'days')
