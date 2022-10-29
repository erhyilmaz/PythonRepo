def my_sum(a, b):
    summation = a + b
    return summation


def my_division(a, b):
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
