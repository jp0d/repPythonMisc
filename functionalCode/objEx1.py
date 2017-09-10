class SummableList(list):
    def sum( self ):
        s= 0
        for v in self.__iter__():
            s += v
        return s
