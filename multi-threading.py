import threading


avg = 0  #initialization of avg
maxm = 0 # initialization of maxm
minm = 0  # initialization of minm
list = [90, 81, 78, 95, 79, 72, 85]  #array

def print_avg():
  total = sum(list)  #built in function sum() gives sum of values in list
  avg = total//len(list)  #// for integer division
  print("The average value is ", avg)  

def print_max():
  maxm = max(list)  #built in function max() gives maximum value from the list
  print("The maximum value is ", maxm)

def print_min():
  minm = min(list) #built in function min() gives minimum value from the list
  print("The minimum value is", minm) 
	
	 
if __name__ == "__main__":
# creating thread
  t1 = threading.Thread(target=print_avg)
  t2 = threading.Thread(target=print_max)
  t3 = threading.Thread(target=print_min)

  #starting thread 1
  t1.start()
  #starting thread 2
  t2.start()
  #starting thread 3
  t3.start()

  #wait until thread 1 is completely executed
  t1.join()
  #wait until thread 2 is completely executed
  t2.join()
  #wait until thread 3 is completely executed
  t3.join()

  #both threads completely executed 
  print("Done!") 

