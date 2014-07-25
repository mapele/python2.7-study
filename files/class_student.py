########################################################################
# -*- coding UTF-8 -*-

class Student(object):
    """"""
    __slots__ = ('__name', '__score')
    
    #----------------------------------------------------------------------
    def __init__(self, name, score):
        """Constructor"""
        #pass
        self.__name = name
        self.__score = score
        
    #----------------------------------------------------------------------
    @property
    def score(self):
        """"""
        return self.__score
    
    #----------------------------------------------------------------------
    @score.setter
    def score(self, value):
        """"""
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100')
        self.__score = value
        
    #----------------------------------------------------------------------    
    def print_student(self):
        print '%s: %s' % (self.__name, self.__score)
    
    #----------------------------------------------------------------------
    def __getattr__(self, attr):
        """"""
        if attr == 'new_attr':
            return 99
        raise AttributeError('\'Student\' object has no attribute \'%s\'' %attr)
    
    #----------------------------------------------------------------------
    def __call__ (self):
            """"""
            print ('this is chain class by authon:%s!' %self.__name )    