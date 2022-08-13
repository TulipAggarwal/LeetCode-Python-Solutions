class MyCircularQueue:
  def __init__ (self, k:int): #k is the maximum size of the queue
    self.head = 0
    self.tail = 0
    self.size = 0
    self.k = k
    self.q = [None] * k
    
  def enQueue(self, value:int) -> bool:
    if self.isFull():
      return False
    self.q[self.tail] = value
    self.size += 1
#this will ensure if the queue is full then it will go back to the beginning again
    self.tail = (self.tail+1)%(self.k) 
    return True

  def deQueue(self) -> bool:
    if self.isEmpty():
      return False
    self.size = self.size - 1
    #self.q[self.head] = value   #this is not needed here because the size is going to keep check if the size is zero or what
    self.head = (self.head+1)%(self.k)
    return True

  def Front(self) -> int:
    if self.isEmpty():
      return -1
    return self.q[self.head]

  def Rear(self) -> int:
    if self.isEmpty():
      return -1
    return self.q[self.tail-1] #Because tail is going to get to the next index number so we minus one to get the previous value 
  def isEmpty(self) -> bool:
    if self.size == 0:
      return True
    return False
  def isFull(self) -> bool:
    if self.size == self.k:
      return True
    return False
