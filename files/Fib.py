########################################################################
class Fib(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        
        self.a, self.b = 0, 1
        
    #----------------------------------------------------------------------
    def __iter__(self):
        """"""
        
        return self
    
    #----------------------------------------------------------------------
    def next(self):
        """"""
        
        self.a, self.b = self.b, self.a + self.b
        if self.a > 20:
            raise StopIteration();
        return self.a
    
    #----------------------------------------------------------------------
    def __getitem__ (self, n):
        """"""
        if isinstance (n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        
        if isinstance(n, slice):
            start,stop, a, b,forint = n.start, n.stop, n.start, n.start + 1, n.stop - n.start
            L = []
            
            print start, stop
            
            if start == stop:
                L.append(a)
                return L
            
            if stop - start == 1:
                forint = 2
                
            for x in range (forint+1):
                if a > 0:
                    L.append(a)
                a, b = b, a + b
                
            return L
    #----------------------------------------------------------------------
    