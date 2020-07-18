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
#email is the email you want to censor and new_word is the word you want to replace it with
def censor_multiple_words(email, new_word):
   censored_email2 = email.replace(pterms[0], new_word).replace(pterms[1], new_word).replace(pterms[2], new_word).replace(pterms[3], new_word).replace(pterms[4], new_word).replace(pterms[5], new_word).replace(pterms[6], new_word).replace(pterms[7], new_word).replace(pterms[8], new_word).replace(pterms[9], new_word).replace(pterms[10], new_word).replace(pterms[11], new_word).replace(pterms[12], new_word).replace(pterms[13], new_word)
   censored_email2_new = censored_email2.replace(censored_email2[censored_email2.find("banana") + 1], 'XXXXX').replace(censored_email2[censored_email2.find("banana") - 1], 'XXXXX')
   return censored_email2_new
#print(censor_multiple_words(email_two, 'banana'))

# Third part, censoring negotive words from the negotive word list if 2 negative words occur one after another

negative_words = ["concerned", "behind", "danger",
                  "dangerous", "alarming", "alarmed",
                  "out of control", "help", "unhappy",
                  "bad", "upset", "awful", "broken", "damage",
                  "damaging", "dismal", "distressed", "distressing",
                  "concerning", "horrible", "horribly", "questionable"]

nws = [nw.capitalize() for nw in negative_words]
tot_neg_words = negative_words + nws
new_listed_email_three = []
#email is the email you want to get rid of negative words and happy_words is the word you want to replace the negative ones
def negative_word_censor(email, happy_word):
    smw_email3 = censor_multiple_words(email, 'banana')
    listed_email_three = smw_email3.split()
    for n, i in enumerate(listed_email_three):
        for j in negative_words:
            if i == j:
                listed_email_three[n] = happy_word
                listed_email_three[n - 1] = "XXXXX"
                listed_email_three[n + 1] = "XXXXX"
    new_email_three = ' '.join(listed_email_three)
    return new_email_three
    
print(negative_word_censor(email_four, "amazing"))



