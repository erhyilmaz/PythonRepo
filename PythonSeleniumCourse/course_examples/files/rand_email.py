# Create a file with Randomly generated emails

import random
import string

list_of_domains = ['gmail.com', 'hotmail.com', 'yahoo.com', 'outlook.com', 'msn.com', 'mynet.com']
length_of_email = 10
letters = string.ascii_lowercase

# generate random emails and store ina list
all_email = []
for domain in list_of_domains:
    for i in range(20):
        random_string = ''.join(random.choice(letters) for i in range(length_of_email))  
        # email = random_string + '@' + domain
        email = f"{random_string}@{domain}"
        # email = "{}@{}".format(random_string, domain)
        all_email.append(email)

# print(all_email)

# take the list and write to a file
file_name = './sample_files/random_emails.txt'
with open(file_name, 'w') as f:
    # option 1
    # for email in all_email:
    #    f.write(email + ';' + '\n')

    # option 2
    all_email_str = ';\n'.join(all_email)
    f.write(all_email_str)

