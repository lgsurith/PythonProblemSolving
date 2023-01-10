''' 
regex:

+  one or more occurances
*  zero or more occurances
?  one or more occurances
^  starts with
$ ends with
[] range / set of charcters or numbers
{} specific number of times
{m,n} this represents that the character must be atleast m or atmost n to be found in the given raw string.
\ for any special character
\d represents digit
\s whitespaces

note: findall returns list of intergers
'''

#given code is to find if the given email id matches or not

import re
email_id=input()
correct_email_id=re.match('[0-9a-zA-Z]+@[0-9a-zA-Z]+\.[a-zA-Z]{3}',email_id)
if correct_email_id:
  print("The email id entered is correct")
else:
  print("Enter an valid email-id")
