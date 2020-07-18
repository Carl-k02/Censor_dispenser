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
ptcap = [ptcaps.capitalize() for ptcaps in proprietary_terms]
pterms = proprietary_terms + ptcap 

def censor_multiple_words(email, new_word):
   censored_email2 = email.replace(pterms[0], new_word).replace(pterms[1], new_word).replace(pterms[2], new_word).replace(pterms[3], new_word).replace(pterms[4], new_word).replace(pterms[5], new_word).replace(pterms[6], new_word).replace(pterms[7], new_word).replace(pterms[8], new_word).replace(pterms[9], new_word).replace(pterms[10], new_word).replace(pterms[11], new_word).replace(pterms[12], new_word).replace(pterms[13], new_word)
   return censored_email2


print(censor_multiple_words(email_two, 'banana'))
print(pterms)
