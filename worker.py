import time

def task_in_background(t):  
 
    delay = 1  
 
    print("Running Task")  
    print("Simulates the {delay} seconds")  
 
    time.sleep(delay)  
 
    print(len(t))  
    print("Completed Task")  
 
    return len(t)