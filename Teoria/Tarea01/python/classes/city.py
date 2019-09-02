from .petition import create

class city:
    """
    A class used to represent a City

    ...
    
    Atributes
    ---------
    __name : str
       the name of the city
    __latitude : str
       the latitude of the city
    __longitude : str 
       the longitude of the city
    __weather : str
       the weather of the city
       
    Methods
    -------
    get_weather(self)
       returns thw weather of the city
    _create_petition_(self)
       Private method, creates a petition using the class petition
       saves the result in @param weather
    """
    
    def __init__ (self , name , latitude , longitude):
        """
        Parameters
        ----------
        name : str
          The name of the city
        latitude : str
          The latitude of the city
        longitude : str
          The longitude of the city
        It calls the method create petition
        """
        self.__name = name
        self.__latitude = latitude
        self.__longitude = longitude
        self.__weather = ""
        self._create_petition_()

    def get_weather(self):
        """ Returns the city's weather """
        return self.__weather
    
    def _create_petition_(self):
        """ Creates a petition using the class petition.create() """
        self.__weather = create(self.__latitude, self.__longitude)


