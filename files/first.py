#!/usr/bin/python  
#-*-coding:utf-8-*- 

#print('this is my fisrt python file!')
#print('乘法表:')
#for i in range(1,10):
    #for j in range(1,i+1):
	#print(str(j)+'*'+str(i)+'='+str(i*j),end=' ')
	#if i==j:
	    #print()

#def power(x):		
    #return x * x

#import Image 
#im = Image.open('E:\logo1.png')
#print im.format, im.size, im.mode
#Image.open('E:\logo1.png')

#from __future__ import  unicode_literals
#print '\'xxx\' is unicode?', isinstance('xxx', unicode)
#print 'u\'xxx\' is unicode?', isinstance(u'xxx', unicode)
#print '\'xxx\' is str?', isinstance('xxx', str)
#print 'b\'xxx\' is str?', isinstance(b'xxx', str)


#with open('E:\initorclsb.ora', mode='r') as f:
    #for line in f.readlines():
	#print(line.strip())

#with open('E:\gbkfile.txt', mode='r') as g:
    #u = g.read().decode('gbk')
    #print (u)
    
#try:
    #f = open('E:\logo1.png', mode='rb')
    #print(f.read())
#finally:
    #if f:
	#f.close()

#import codecs
#with codecs.open('E:\gbkfile.txt', 'rb', 'gbk') as f:
    #print(f.read())

#import codecs   
#with open('E:\python_write_test.txt', 'w') as f:
    #f.write('sdjk!你好')
    #f.write('sdjk!你好')
#with codecs.open('E:\python_write_test.txt', 'r', 'utf8') as f:
    #print(f.read())
    
#序列化（pickling）
#try:
    #import cPickle as pickle
#except ImportError:
    #import pickle

#d = dict(name='xwy', age=28, score=100)
#with open('E:\python_write_test.txt', 'w') as f:
    #pickle.dump(d, f)

#with open('E:\python_write_test.txt', 'r') as f:
    #d = pickle.load(f)
    #print(d)
    
#import json
#try:
    #import cPickle as pickle
#except ImportError :
    #import pickle
    
#d = dict(name='xwy', age=28, score=100)
#j = json.dumps(d)
#print 'j:', j

#with open('E:\python_write_test.txt', 'w') as f:
    #j = json.dump(d, f)
    #pickle.dump(j, f)
    
#j = '{"age": 28, "score": 100, "name": "xwy"}'
#p = json.loads(j)
#print 'p:', p

#with open('E:\python_write_test.txt', 'r') as f:
    #p = json.load(f)
    #print 'p:', p
    
