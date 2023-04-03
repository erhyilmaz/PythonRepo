
import json

input_file_name  = './sample_files/randdomain_emails.csv'
output_file_name = './sample_files/emaildomaincounts.json'


def get_emails_from_file(file_path):
    print(f"Getting emails from file:{file_path}\n")
    with open(file_path, "r") as f:
        emails_raw = f.readlines()
        # print(emails_raw)
    emails_clean = [i.strip(',\n') for i in emails_raw]
    return emails_clean


# Solution 1:
def count_domains_option1(list_of_emails):
    print("Option 1 function call:\n")
    email_counts = dict()
    for email in list_of_emails:
        domain = email.split('@')[-1]
        if domain not in email_counts.keys():
            email_counts[domain] = 1
        else:
            email_counts[domain] = email_counts[domain] + 1
    return email_counts


# Solution 2:
def count_domains_option2(list_of_emails):
    print("Option 2 function call:\n")
    domain_list = []
    for email in list_of_emails:
        domain = email.split('@')[-1]
        domain_list.append(domain)

    unique_domains = set(domain_list)
    # print(unique_domains)
    email_count = dict()
    for domain in unique_domains:
        email_count[domain] = domain_list.count(domain)

    return email_count


# write output to a json file
def save_output_in_json_file(counts_dict, json_file_path):
    print(f"Printing file: {json_file_path}")
    with open(json_file_path, 'w') as f:
        json_obj = json.dumps(counts_dict)
        print(json_obj)
        f.write(json_obj)


# get email list from a file
emails_list = get_emails_from_file(input_file_name)

# --------------------
# Solution 1:
counts1 = count_domains_option1(emails_list)
# write to a json file
save_output_in_json_file(counts1, output_file_name)

# --------------------
# Solution 2:
counts2 = count_domains_option2(emails_list)
# write to a json file
save_output_in_json_file(counts2, output_file_name)
