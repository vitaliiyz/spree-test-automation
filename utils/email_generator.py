from uuid import uuid4


def generate_email():
    return uuid4().hex[:9] + "@spree-test.com"
