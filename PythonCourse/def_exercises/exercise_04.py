import time

def count (start, end):
   for idx in range(start, end):
        print(idx)
        time.sleep(1)
count(1, 10)
print("DONE!")