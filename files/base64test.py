import base64

print (base64.b64encode('binary\x00string'))
print (base64.b64decode('YmluYXJ5AHN0cmluZw=='))
print (base64.b64encode('i\xb7\x1d\xfb\xef\xff'))
print (base64.urlsafe_b64encode('i\xb7\x1d\xfb\xef\xff'))
print (base64.urlsafe_b64decode('abcd--__'))

#----------------------------------------------------------------------
def mybase64decode(b):
    """"""
    if len(b) % 4 == 0:
        return base64.b64decode(b)
    else:
        return base64.b64decode(b+'='*(4-len(b) % 4))
    
if __name__ == '__main__':
    print ('YWJjZA==:%s' % mybase64decode('YWJjZA=='))
    print ('YWJjZA:%s' % mybase64decode('YWJjZA'))