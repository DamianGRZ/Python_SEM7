import threading
import time

class Fork(threading.Semaphore):
    def take_semaphor(self):
        locked = self.acquire(False)#get non-blocking lock (argument = false, timeout = default)
        #If a call with blocking set to True would block, return False immediately; otherwise, set the lock to locked and return True.
        if locked:
            return
        else:
            raise ResourceWarning

#inheriting threading class in Thread module
class Philosopher(threading.Thread):
    running = True  #used to check if everyone is finished eating

 #Since the subclass overrides the constructor, it must make sure to invoke the base class constructor (Thread.__init__()) before doing anything else to the thread.
    def __init__(self, index, forkOnLeft, forkOnRight):
        threading.Thread.__init__(self)
        self.index = index
        self.forkOnLeft = forkOnLeft
        self.forkOnRight = forkOnRight

    def run(self):
        while(self.running):
            print ('Philosopher %s is hungry.' % self.index)
            self.dine()

    def fight_for_forks(self):
        fork1, fork2 = self.leftfork, self.rightfork
        while self.running:
            try:
                fork1.take_semaphor()#try to take the first fork
            except ResourceWarning:#If resource warning, continue the loop, if not try to take the second fork
                continue
            else:
                try:
                    fork2.take_semaphor()#try to take the second fork
                except ResourceWarning:
                    fork1.release()#If resource warning, release the first taken fork
                else:
                    break#If taken both forks, stop waiting and go to eat

        self.dine()
        #release both of the forks after dining
        fork2.release()
        fork1.release()
 
    def dine(self):			
        print ('Philosopher %s starts eating. '% self.index)
        time.sleep(30)
        print ('Philosopher %s finishes eating and leaves to think.' % self.index)

def main():
    forks = [Fork() for _ in range(5)] #initialising array of semaphore i.e forks

    #here (i+1)%5 is used to get right and left forks circularly between 1-5
    philosophers= [Philosopher(i, forks[i%5], forks[(i+1)%5])
            for i in range(5)]

    for p in philosophers: p.start()
    time.sleep(80)#If sleep is smaller all philosophers finish eating, program finishes
    Philosopher.running = False
    print ("Now we're finishing.")

if __name__ == "__main__":
    main()
