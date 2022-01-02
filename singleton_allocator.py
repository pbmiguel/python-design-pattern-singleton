class Database:
    initialized = False
    _instance = None

    def __init__(self, url):
        if not self.initialized:
            self.url = url
            self.initialized = True

    def __new__(cls, url, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def connect(self):
        if 'https' not in self.url:
            raise ValueError("invalid url: it must be encrypted")
        return True