import unittest

class TestStringMethods(unittest.TestCase):

    def namelist(self, names):
        if len(names) == 0:
            return ""
        elif len(names) == 1:
            return names[0]['name']
        else:
            n = [item['name'] for item in names]
            return ', '.join(n[:-1]) + " & " + n[-1]

    def test_upper(self):
        names = [{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]
        self.assertEqual(self.namelist(names), 'Bart, Lisa, Maggie, Homer & Marge')
        self.assertEqual(self.namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]), 'Bart, Lisa & Maggie')
        self.assertEqual(self.namelist([{'name': 'Bart'},{'name': 'Lisa'}]), 'Bart & Lisa')
        self.assertEqual(self.namelist([{'name': 'Bart'}]), 'Bart')
        self.assertEqual(self.namelist([]), '')

if __name__ == '__main__':
    unittest.main()
