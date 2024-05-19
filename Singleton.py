class Singleton():
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
            return cls.instance


s = Singleton()
print("object created", s)

s1 = Singleton()
print("object created", s1)