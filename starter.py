import threading
import enumerator
import runner
import time

e =[x for x in range(0,10)]
i=0
tv = time.time()
while i < 10:
    e[i] = runner.Runner(i)
    i+=1

for i in e:
    i.start()

##t = runner.Runner("1")
##t2 = runner.Runner("2")
##t3 = runner.Runner("3")
##t4 = runner.Runner("4")
##t5 = runner.Runner("5")
##t6 = runner.Runner("6")
##t.start()
##t2.start()
##t3.start()
##t4.start()
##t5.start()
##t6.start()
##
##t.join()
##t2.join()
##t3.join()
##t4.join()
##t5.join()
##t6.join()
print('wait')
for i in e:
    i.join()
tl = time.time()
print('finish')
print('time %d' %((tl-tv)))
