# Create a file with Randomly generated emails with random domains

import random
import string

file_name = './sample_files/randdomain_emails.csv'
list_of_domains = ['gmail.com', 'hotmail.com', 'yahoo.com', 'outlook.com', 'msn.com', 'mynet.com']
length_of_email = 10
total_num_of_emails = 100
letters = string.ascii_lowercase

if 0:
    # OPTION 1
    all_email = []
    for i in range(total_num_of_emails):
        random_domain = random.choice(list_of_domains)
        random_string = ''.join(random.choice(letters) for k in range(length_of_email))
        email = f"{random_string}@{random_domain}"
        all_email.append(email)
        # all_email.append(f"{''.join(random.choice(letters) for k in range(length_of_email))}@{random.choice(list_of_domains)}")

    with open(file_name, 'w') as f:
        all_email_str = ';\n'.join(all_email)
        f.write(all_email_str)


# OPTION 2
with open(file_name, 'w') as f:
    for i in range(total_num_of_emails):
        random_domain = random.choice(list_of_domains)
        random_string = ''.join(random.choice(letters) for k in range(length_of_email))
        email = f"{random_string}@{random_domain}"
        if i == (total_num_of_emails-1):
            f.write(email + ',')
        else:
            f.write(email + ',\n')

