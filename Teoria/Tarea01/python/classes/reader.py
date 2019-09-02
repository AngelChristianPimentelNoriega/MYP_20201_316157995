import csv
from .city import city

class reader:
    """
     A class to read a cvs file
     
     ...
     
     Atributes
     ---------
     __number_petitions : int
       the amount of petitions made to Open Weather
     __number_cities : int
       the amount of cities contained in the csv file
     __city_dict : dictionary
       the dictionary used to avoid dupicate petitions
     __file_name : str
       the file we are going to read
     
     Methods
     -------
     get_petitions(self)
       returns the amount of petitions
     get_cities(self)
       returns the amount of cities
     get_dict(self)
       returns the cities dictionary
     read(self)
       reads the csv file and in each row it checks if the city is already in the
       dictionary, if it is, it just increments the number_cities atribute, if it is not,
       it creates a new city with its values
       It also prints the weather of each city and the relation between the number of
       cities and the number of petitions
    """
    def __init__(self , file_name):
        """
        Parameters
        ----------
        file_name : str
          the name of the csv file
        """
        self.__number_petitions = 0
        self.__number_cities = 0
        self.__city_dict = {}
        self.__file_name = file_name
        
    def get_petitions(self):
        """ Returns the amount of petitions """
        return self.__number_petitions
    
    def get_cities(self):
        """ Returns the amount of cities """
        return self.__number_cities

    def city_dict(self):
        """Returns the cities dictionary"""
        return self.__city_dict
    
    def read(self):
        """ Reads the csv file and creates the cities
            
        If the city is already in the dictionary a new petition is not made
        Else the petition is made
        
        Raises
        ------
        FileNotFoundException
           if the file is not a valid csv file
        """
        with open (self.__file_name, 'r') as csvFile:
            csv_reader = csv.reader(csvFile)
            row_line = 0
            for row in csv_reader:
                
                if row_line is 0: # discart the first row of the file
                    row_line += 1
                    continue
            
                if not(row[0] in self.__city_dict):
                    self.__city_dict[row[0]] = city(row[0],row[2], row[3])
                    self.__number_petitions += 1
                print(self.__city_dict[row[0]].get_weather())
                
                if not(row[1] in self.__city_dict):
                    self.__city_dict[row[1]] = city(row[1],row[4],row[5])
                    self.__number_petitions += 1
                print(self.__city_dict[row[1]].get_weather())
                self.__number_cities += 2
        print("Number of petitions {} vs number of cities {}".format(self.__number_petitions,self.__number_cities))
        


