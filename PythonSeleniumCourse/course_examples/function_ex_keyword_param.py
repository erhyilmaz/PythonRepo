# Example of using keyword parameters
# Example 1: write a function that will return number of words that have X length, given a string

def get_count_of_small_words(input_string, max_size=3):
    small_words = []
    for word in input_string.split():
        if len(word) <= max_size:
            small_words.append(word)

    return len(small_words)


my_string = "A spike caused by the skew of switches or logic Glitches are a troublesome " \
            "source of error in high-speed D/A convertors and they are most prevalent at " \
            "the mid scale switching location"

num_small_words = get_count_of_small_words(my_string)
print(num_small_words)

num_small_words = get_count_of_small_words(my_string, 2)
print(num_small_words)

num_small_words = get_count_of_small_words(my_string, 5)
print(num_small_words)


# Example 2: write a function that will
def connect_to_database(host='test.db.com', username='test_user', password='pwd'):
    print(f"Connection to host: {host}")
    print(f"Username: {username}")
    print(f"Password: {password}")


connect_to_database(host='aaa.db.com', username='erhan', password='1234')
print("----------")
connect_to_database()   # use default parameters!
print("----------")
connect_to_database('bbb.db.com', 'erhan2', '5678')
print("----------")
