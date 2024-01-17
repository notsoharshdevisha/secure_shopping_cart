import random
import string


def generate_customer_id() -> str:
    return (get_random_letters(3)
            + str(random.randrange(10000, 100000))
            + get_random_letters(2)
            + "-"
            + random.choice(["A", "Q"]))


def get_random_letters(length: int) -> str:
    return ''.join(random.choices(string.ascii_letters, k=length))
