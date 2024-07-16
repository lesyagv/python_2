import time

def delay(seconds):
    "Indicates the number of seconds to delay execution of the decorated function"
    def decorator(func):
        "We accept the function that needs to be decorated"
        def wrapper(*args, **kwargs):
            "To delay execution"
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@delay(5)
def it_may_be(name=''):
    "Execution is delayed for 5 seconds before returning the result"
    return (name + " ask: It's nearly Luncheon Time? \n")

for t in range(12):
    print(it_may_be(name='Winnie-the-Pooh'))
