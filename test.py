import os
import sys
import unittest
#from models import db, Book
from models import db, Book, Author, Publisher

class DBTestCases(unittest.TestCase):
    def test_pub_db(self):

        # assuming the database is built before the tests are ran
        s = Publisher(
            bookNum="96",
            title="In My Own Words",
            authorNum="32",
            publisherNum="28",
            publisher="ReadHowYouWant.com",
            parent_company="None",
            owner="None",
            location="None",
            founded="None",
            #google_id="Z8nL1it1eVQC" ,
            author="14th Dalai Lama",
            wikipedia_url="None",
            description="None",
            website="None",
            image_url="None"
        )

        #check if the attributes of s match with p
        for p in db.session.query(Publisher).all():
            if p.bookNum == '96':
                self.assertEqual(
                    [a for a in dir(s) if not a.startswith('__')],
                    [a for a in dir(p) if not p.startswith('__')]
                )
                break

    def test_pub_db_2(self):
        s = Publisher(
            bookNum="137",
            title="A Short History of Nearly Everything",
            authorNum="67",
            publisherNum="45",
            publisher="Lulu (company)",
            parent_company="None",
            owner="None",
            location="None",
            founded="2002",
            #google_id= "yRuICgAAQBAJ" ,
            author="Bill Bryson",
            wikipedia_url="https://en.wikipedia.org/wiki/Lulu_(company)",
            description="Lulu Press, Inc. is an online print-on-demand, self-publishing and distribution platform. Since its founding in 2002, Lulu has published nearly two million titles by authors in over 225 countries and territories.",
            website="http://Official website",
            image_url="http://upload.wikimedia.org/wikipedia/en/thumb/5/52/Lulu_logo.svg/220px-Lulu_logo.svg.png"
        )

        #check if the attributes of s match with p
        for p in db.session.query(Publisher).all():
            if p.bookNum == '96':
                self.assertEqual(
                    [a for a in dir(s) if not a.startswith('__')],
                    [a for a in dir(p) if not p.startswith('__')]
                )
                break

    def test_pub_db_3(self):
        s = Publisher(
            bookNum="109",
            title="1984",
            authorNum="46",
            publisherNum="35",
            publisher="Arcturus Publishing",
            parent_company="None",
            owner="None",
            location="None",
            founded="None",
            #google_id= "uyr8BAAAQBAJ" ,
            author="George Orwell",
            wikipedia_url="None",
            description="None",
            website="None",
            image_url="https://arcturuspublishing.com/wp-content/uploads/2015/07/Arcturus-Web-logo-cropped.jpg"
        )

        #check if the attributes of s match with p
        for p in db.session.query(Publisher).all():
            if p.bookNum == '96':
                self.assertEqual(
                    [a for a in dir(s) if not a.startswith('__')],
                    [a for a in dir(p) if not p.startswith('__')]
                )
                break

    def test_author_db(self):
        s = Author(
            bookNum="140",
            title="Gardens of the Moon",
            authorNum="70",
            publisherNum="4",
            author="Steven Erikson",
            #google_id= "Jgth_BYe7V8C" ,
            publisher="Palgrave Macmillan",
            born="1959-10-07",
            died="None",
            nationality="Canadian",
            education="None",
            alma_mater="None",
            wikipedia_url="https://en.wikipedia.org/wiki/Steven_Erikson",
            image_url="http://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Steven_Erikson_2016.jpg/179px-Steven_Erikson_2016.jpg",
            description="Steven Erikson is the pseudonym of Steve Rune Lundin, a Canadian novelist, who was educated and trained as both an archaeologist and anthropologist."
        )

        #check if the attributes of s match with p
        for p in db.session.query(Publisher).all():
            if p.bookNum == '96':
                self.assertEqual(
                    [a for a in dir(s) if not a.startswith('__')],
                    [a for a in dir(p) if not p.startswith('__')]
                )
                break

    def test_author_db_2(self):
        s = Author(
            bookNum="114",
            title="The Fellowship of the Ring",
            authorNum="51",
            publisherNum="39",
            author="J. R. R. Tolkien",
            #google_id= "aWZzLPhY4o0C" ,
            publisher="Houghton Mifflin Harcourt",
            born="1892-01-03",
            died="1973-09-02",
            nationality="British",
            education="None",
            alma_mater="Exeter College, Oxford",
            wikipedia_url="https://en.wikipedia.org/wiki/J._R._R._Tolkien",
            image_url="http://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Tolkien_1916.jpg/220px-Tolkien_1916.jpg",
            description="John Ronald Reuel Tolkien CBE FRSL, known by his pen name J. R. R. Tolkien, was an English writer, poet, philologist, and university professor who is best known as the author of the classic high-fantasy works The Hobbit, The Lord of the Rings, and The Silmarillion."
        )

        #check if the attributes of s match with p
        for p in db.session.query(Publisher).all():
            if p.bookNum == '96':
                self.assertEqual(
                    [a for a in dir(s) if not a.startswith('__')],
                    [a for a in dir(p) if not p.startswith('__')]
                )
                break

    def test_author_db_3(self):
        s = Author(
            bookNum="1",
            title="Harry Potter and the Sorcerer's Stone",
            authorNum="1",
            publisherNum="1",
            author="J. K. Rowling",
            #google_id= "wrOQLV6xB-wC" ,
            publisher="Pottermore",
            born="1965-07-31",
            died="None",
            nationality="British",
            education="Bachelor of Arts",
            alma_mater="University of Exeter",
            wikipedia_url="https://en.wikipedia.org/wiki/J._K._Rowling",
            image_url="http://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/J._K._Rowling_2010.jpg/220px-J._K._Rowling_2010.jpg",
            description='Joanne "Jo" Rowling, OBE, FRSL, pen names J. K. Rowling and Robert Galbraith, is a British novelist, screenwriter and film producer best known as the author of the Harry Potter fantasy series.'
        )

        #check if the attributes of s match with p
        for p in db.session.query(Publisher).all():
            if p.bookNum == '96':
                self.assertEqual(
                    [a for a in dir(s) if not a.startswith('__')],
                    [a for a in dir(p) if not p.startswith('__')]
                )
                break

    def test_book_db(self):
        s = Book(
            bookNum="149",
            authorNum="70",
            publisherNum="4",
            title="The Crippled God",
            subtitle="None",
            author="Steven Erikson",
            publisher="Palgrave Macmillan",
            publication_date="2011-03-01",
            isbn="9780765310101",
            google_id="kPpeTrfXpKsC",
            image_url="https://books.google.com/books/content/images/frontcover/kPpeTrfXpKsC?fife=w500",
            description="Tavore Paran struggles to hold her army together in order to combat a fearsome alien force, while the gods threaten to once again unleash dragons to destroy the world."
        )

        #check if the attributes of s match with p
        for p in db.session.query(Publisher).all():
            if p.bookNum == '96':
                self.assertEqual(
                    [a for a in dir(s) if not a.startswith('__')],
                    [a for a in dir(p) if not p.startswith('__')]
                )
                break

    def test_book_db_2(self):
        s = Book(
            bookNum="134",
            authorNum="65",
            publisherNum="44",
            title="The Origin of Species",
            subtitle="None",
            author="Charles Darwin",
            publisher="Everyman's Library",
            publication_date="1909",
            isbn="None",
            google_id="YY4EAAAAYAAJ",
            image_url="https://books.google.com/books/content/images/frontcover/YY4EAAAAYAAJ?fife=w500",
            description="First published in 1859, this landmark book on evolutionary biology was not the first to deal with the subject, but it went on to become a sensation—and a controversial one for many religious people who could not reconcile Darwin’s science with their faith. Darwin worked on the book for over 20 years before its publication. The radical crux of his scientific theory was the idea of natural selection, which meant that chance, not a divine Creator, played a great role in humanity's advancement and that individuals who weren't physically able to adapt with the greater populace died off."
        )

        #check if the attributes of s match with p
        for p in db.session.query(Publisher).all():
            if p.bookNum == '96':
                self.assertEqual(
                    [a for a in dir(s) if not a.startswith('__')],
                    [a for a in dir(p) if not p.startswith('__')]
                )
                break

    def test_book_db_3(self):
        s = Book(
            bookNum="1",
            authorNum="1",
            publisherNum="1",
            title="Harry Potter and the Sorcerer's Stone",
            subtitle="None",
            author="J. K. Rowling",
            publisher="Pottermore",
            publication_date="2015-12-08",
            isbn="9781781100486",
            google_id="wrOQLV6xB-wC",
            image_url="https://books.google.com/books/content/images/frontcover/wrOQLV6xB-wC?fife=w500",
            description="Turning the envelope over, his hand trembling, Harry saw a purple wax seal bearing a coat of arms; a lion, an eagle, a badger and a snake surrounding a large letter 'H'." +
            " Harry Potter has never even heard of Hogwarts when the letters start dropping on the doormat at number four, Privet Drive. Addressed in green ink on yellowish parchment with a purple seal, they are swiftly confiscated by his grisly aunt and uncle. Then, on Harry's eleventh birthday, a great beetle-eyed giant of a man called Rubeus Hagrid bursts in with some astonishing news: Harry Potter is a wizard, and he has a place at Hogwarts School of Witchcraft and Wizardry. An incredible adventure is about to begin!"
        )

        #check if the attributes of s match with p
        for p in db.session.query(Publisher).all():
            if p.bookNum == '96':
                self.assertEqual(
                    [a for a in dir(s) if not a.startswith('__')],
                    [a for a in dir(p) if not p.startswith('__')]
                )
                break

if __name__ == '__main__':
    unittest.main()
