class Cat:
    all=[]

    def init__(self,name,breed,age):
        self.name=name
        self.breed=breed
        self.age=age
        self.add_cat_to_all(self)

    @classmethod
    def add_cat_to_all(cls,cat):
        cls.all.append(cat)

    def save(self,cursor):
        cursor.execute(
            'INSERT INTO cats (name,breed,age) VALUES (?,?,?)',
            (self.name, self.breed, self.age)
        )

        # create new cats and save them to db

db_connection=sqlite3.connect('db/pets.db')
db_cursor=db_connection.cursor()

cat("Maru", "Scottish Fold", 3)
cat("Hana", "tortoiseshell",1)

for cat in Cat.all:
    cat.save(db_cursor)