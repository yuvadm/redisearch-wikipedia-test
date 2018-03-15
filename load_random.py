import wikipedia

from redisearch import Client, TextField


class RandomWikipediaImport(object):

    def __init__(self):
        self.rs = Client('wikipedia')
        self.rs.create_index((TextField('title', weight=5.0), TextField('body')))
        print(f'>>> Created index')

    def insert_random_loop(self):
        i = 1
        while True:
            ra = wikipedia.random()
            article = wikipedia.page(ra)
            self.rs.add_document(f'doc{i}', title=article.title, body=article.content)
            print(f'>>> Inserted {article.title}')
            i += 1


if __name__ == '__main__':
    rwi = RandomWikipediaImport()
    rwi.insert_random_loop()
