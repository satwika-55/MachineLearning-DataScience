## multi processing 

## there is some error in the code... not running properly but pushing into github
git 

import multiprocessing
import time 

def square_number():
    for i in range(5):
        time.sleep(1)
        print(f"sqaure : {i*i}")

def cubes():
    for i in range(5):
        time.sleep(1)
        print(f"sqaure : {i*i*i}")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=square_number)
    p2 = multiprocessing.Process(target=cubes)
    
    t = time.time()
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    finished_time = time.time() - t 
    print(finished_time)

