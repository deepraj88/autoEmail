This script mails all the members mentioned in Excelsheet.

From excelsheet, it takes paper (content for body of the mail), email, and name of the person (which is also used in body of the mail).

In the test1.xlsx, the above information is stored at column 5(F), 15(P), and 17(R). test1.xslx -> test1.csv

Command:
python send_mail_solicitation.py test1.csv 5 15 17
