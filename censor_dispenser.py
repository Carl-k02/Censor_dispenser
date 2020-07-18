# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

# first part, censoring a word and replacing it wiih another word
def censor_email(censored_word, replaced_with):
    censored_email = email_one.replace(censored_word, replaced_with)
    return censored_email
#print(censor_email('learning algorithms', 'banana'))

#Second part, sensoring multiple words from an email
proprietary_terms = ["she", "personality matrix", "sense of self",
                     "self-preservation", "learning algorithm",
                     "her", "herself"]
range1 = range(len(proprietary_terms) - 1)
email2_lower = email_two.lower()

censored_email2 = email2_lower.replace(proprietary_terms[0], "banana").replace(proprietary_terms[1], "banana").replace(proprietary_terms[2], "banana").replace(proprietary_terms[3], "banana").replace(proprietary_terms[4], "banana").replace(proprietary_terms[5], "banana").replace(proprietary_terms[6], "banana")

    

print(censored_email2)
    
