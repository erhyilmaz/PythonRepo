def my_sum(a=0, b=0):
    summation = a + b
    return summation


def my_division(a=20, b=10):
    div = None
    try:
        div = a / b
    except ZeroDivisionError:
        print(f"Zero Division Issue!: {a} / {b}")
    finally:
        return div


in1 = 12
in2 = 24
out = my_sum(in1, in2)
print(f"Sum of {in1} and {in2} is {out}")

in2 = 0
out = my_division(in1, in2)
print(f"Division of {in1} and {in2} is {out}")

# use of default values 1
out = my_division()
print(f"Division of default values is {out}")


# use of default values 2
out = my_division(a=30)
print(f"Division of default values is {out}")

# use of default values 2
out = my_division(b=5)
print(f"Division of default values is {out}")


############################
# Use of Function Default arguments
def send_email(email_to, email_from='abc@xyz.com.tr', subject="No subject"):

    return True


send_email(email_to="aa@bb.com.tr")
send_email(email_to="aa@bb.com", email_from='cc@dd.com')
send_email(email_to="aa@bb.com", email_from='cc@dd.com', subject="Test Results")
send_email(email_to="aa@bb.com", subject="Test Results")
send_email("aa@bb.com", "cc@dd.com", "Test Results")


############################
# Use of Function Default arguments
def is_capital(city_name):
    capitals = ['ANKARA', 'TOKYO', 'PARIS', 'MOSCOW', 'ROME']

    if city_name.upper() in capitals:
        print(f"{city_name.upper()} is capital!")
        return True
    else:
        print(f"{city_name} is Not capital!")
        return False


cap = is_capital("ankara")

############################
# Example

