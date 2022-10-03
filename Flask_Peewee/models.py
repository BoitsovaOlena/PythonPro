import peewee


db = peewee.SqliteDatabase('music_library.sqlite3')


class Author(peewee.Model):
    first_name = peewee.CharField()
    last_name = peewee.CharField()

    class Meta:
        database = db


class Song(peewee.Model):
    name = peewee.CharField()
    year = peewee.IntegerField()
    duration = peewee.TimeField()
    author = peewee.ForeignKeyField(Author)

    class Meta:
        database = db


if __name__ == '__main__':
    db.create_tables([Author, Song])
