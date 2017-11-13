import hug
from app import handle

@hug.post('/')
def receive(body):
    """ Simple Hug Server """
    output = handle(body)
    return output
