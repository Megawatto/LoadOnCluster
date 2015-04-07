import threading
import enumerator
import runner

t = runner.Runner("1")
t2 = runner.Runner("2")
t3 = runner.Runner("3")
t4 = runner.Runner("4")
t5 = runner.Runner("5")
t6 = runner.Runner("6")
t.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()

t.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
