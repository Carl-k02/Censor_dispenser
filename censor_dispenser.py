# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()


def censor_email(censored_word, replaced_with):
    censored_email = email_one.replace(censored_word, replaced_with)
    return censored_email
print(censor_email('learning algorithms', 'banana'))
