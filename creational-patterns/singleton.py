class DatabaseConnection:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(DatabaseConnection, cls).__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == "__main__":
    s1 = DatabaseConnection()
    s2 = DatabaseConnection()

    if s1 is s2:
        print("s1 is s2")
    else:
        print("s1 is not s2")
