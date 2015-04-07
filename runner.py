import threading
import enumerator

class Runner(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self, name=name)
        
     
    def run(self):
        print ('Hello from %s' % self.name)
        flag = True
        while flag:
            q=0
            enumerator.test(self.name)
            for w in enumerator.mass:
                q+=w
                if q ==20:
                    flag = False
                    break
            d=0
            while d < 10000000:
                d+=1
            print(self.name + " Some_Work")
