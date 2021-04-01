# 实体类
class Book:
    def __init__(self, book_id, name, cover, summary, url, author, tags):
        self.book_id = book_id
        self.name = name
        self.cover = cover
        self.summary = summary
        self.url = url
        self.author = author
        self.tags = tags

    def __str__(self):
        return '%s->%s' % (self.book_id, self.name)

    def __repr__(self):
        return self.__str__()