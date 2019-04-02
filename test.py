import os
import sys
import unittest
#from models import db, Book
from create_db import db, Book

class DBTestCases(unittest.TestCase):
    def test_source_insert_1(self):
        '''
        s = Book(id='20', title = 'C++')
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Book).filter_by(id = '20').one()
        self.assertEqual(str(r.id), '20')

        db.session.query(Book).filter_by(id = '20').delete()
        db.session.commit()
        '''
        return
        
    def test_source_insert_2(self):
        return

    def test_source_insert_3(self):
        return

if __name__ == '__main__':
    unittest.main()
