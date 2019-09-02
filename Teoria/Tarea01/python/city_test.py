import unittest

from .classes.city import city
from .classes.reader import reader

class test(unittest.TestCase):
    """
      Unique test class, used to test the basic functionality of the project
      Methods
      -------
      test_invalid_city(self)
         Checks what happens when the program recieves an invalid city
      test_valid_city(self)
         Checks the normal functionality of the program
      test_petitions_vs_cities(self)
         Verifies if the cache (dictionary) is working right, there should be
         more cities than petitions
      test_dictionary_len_vs_petitions(self)
         Verifies if the length of the dictionary is the same as the petitions made
         This test checks if the cities have been saved right
    """
    
    def test_invalid_city(self):
        city_1 = city("not valid","random","random")
        self.assertEqual(city_1.get_weather(),"Invalid city")

    def test_valid_city(self):
        city_1 = city("MX","19.43","-99.07")
        self.assertNotEqual(city_1.get_weather(),"Invalid city")
    
    def test_petitions_vs_cities(self):
        reader_ = reader("../files/testdataset.csv")
        cities = reader_.get_cities()
        petitions = reader_.get_petitions()
        self.assertTrue(petitions <= cities)
        
    def test_dictionary_len_vs_petitions(self):
        reader_ = reader("../files/testdataset.csv")
        petitions = reader_.get_petitions()
        dictionary = reader_.city_dict()
        self.assertTrue(petitions == len(dictionary))
    
if __name__ == '__main__':
    unittest.main()
