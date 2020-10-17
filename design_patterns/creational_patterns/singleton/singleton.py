class Borg:
    """The Borg design pattern"""
    _shared_data = {}

    def __init__(self):
        self.__dict__ = self._shared_data

class Singleton(Borg): # Inherits from the Borg class
    """The singleton class""" # Makes singleton objects global object-oriented variables.
    
    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_data.update(kwargs)

    def __str__(self):
        return str(self._shared_data)

ex = Singleton(HTTP = "Hyper Text Transfer Protocol")
print(ex)

ex2 = Singleton(SNMP = "Simple Network Management Protocol")
print(ex2)
