import dataset


# reference:
# https://dataset.readthedocs.io/en/latest/


class DBHandler:
    def __init__(self, dbname):
        self.dbname = dbname

        self.db = dataset.connect(f"sqlite:///{dbname}.db")
        self.DATA_TABLE = self.db["data"]


if __name__ == "__main__":
    db = DBHandler("test_db")
