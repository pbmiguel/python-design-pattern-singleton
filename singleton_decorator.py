# PEP 318 -- Decorators for Functions and Methods
# https://www.python.org/dev/peps/pep-0318/
def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class Database:
    def __init__(self, url):
        self.url = url

    def connect(self):
        if 'https' not in self.url:
            raise ValueError("invalid url: it must be encrypted")
        return True
