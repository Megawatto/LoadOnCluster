import threading
import enumerator
import random

class Runner(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self, name=name)
        
     
    def run(self):
        print ('Run Th= %s \n\r' % self.name)
        flag = True
        while flag:
            q=0
            numb = enumerator.test(self.name)
            self.decoder(numb)
            for w in enumerator.mass:
                q+=w
                if q ==20:
                    flag = False
                    print('END_WORK -> %s\n\r' %(self.name))
                    break
##            d=0
##            r = random.randint(0,1000000)
##            print(r)
##            while d < r:
##                d+=1
            #print("%s Some_Work\n\r" %(self.name))

    def decoder(self,number):
        decode = ['x','xy','xyz','x+yz']
        print('decode %s->%12s\n\r'%(self.name,number))
