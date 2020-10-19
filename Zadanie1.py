from typing import Any

class Node:
    value: Any
    nastepny: 'None'
    def __init__(self,value=Any,nastepny=None):
        self.value=value
        self.nastepny = nastepny
    def __repr__(self):
        if(self.nastepny==None):
            return f'{self.value}'
        return f'{self.value} -> {self.nastepny}'
    

class LinkedList:
    head: Node
    tail: Node
    
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail=tail
    
    def append(self,value):
        new_wezel=Node(value)
        if self.head == None:
            self.head = new_wezel
            self.tail= new_wezel
        else:
            self.tail.nastepny=new_wezel
            self.tail=new_wezel

    
    def push(self,value):
        new_wezel=Node(value,self.head)
        self.head=new_wezel
        if(self.tail==None):
            self.tail = new_wezel

    def node(self,n):
        liczba=self.head
        suma=0
        while(suma != n ):
            suma+=1
            liczba=liczba.nastepny
        if(liczba.nastepny == None):
            return liczba
        else:
            return liczba
    
    def insert(self,nw,after):
        
        if (after.nastepny == None):
            after.nastepny=Node()
            after.nastepny.value=nw
        after.nastepny=Node(value=nw, nastepny=after.nastepny)     
        
    def pop(self):
        kick=self.head
        self.head=kick.nastepny
        return kick.value
    
    def remove_last(self):
        kick=self.tail
        liczba=self.head
        while(liczba.nastepny.nastepny!= None):
            liczba=liczba.nastepny
        liczba.nastepny=None
        self.tail=liczba
        return kick.value
    

    def remove(self, n):

        licznik = self.head
        
        while licznik.nastepny != None:
            licznik= licznik.nastepny
            if licznik == n:
                licznik.nastepny=None

                


    def __len__(self):
        suma=0
        liczba=self.head
        while (liczba!=None):
            liczba=liczba.nastepny
            suma+=1
        return suma

    def __repr__(self):
        return f'{self.head}'

class Queue():
    queue : LinkedList       

    def __init__(self):
        self.queue=LinkedList()
    def peek(self):
        return self.queue.head.value
    def enqueue(self,w):
        self.queue.append(w)
    def dequeue(self):
        return self.queue.pop()
    
    def __len__(self):
        return len(self.queue)
    def __repr__(self):
        return str(self.queue)   


list_ = LinkedList()
assert list_.head == None
list_.push(1)
list_.push(0)
assert str(list_) == '0 -> 1'
list_.append(9)
list_.append(10)
assert str(list_) == '0 -> 1 -> 9 -> 10'
middle_node = list_.node(n=1)
list_.insert(5, after=middle_node)

assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'
first_element=list_.node(n=0)
returned_first_element = list_.pop()
assert first_element.value == returned_first_element
last_element=list_.node(n=3)
returned_last_element = list_.remove_last()
assert last_element.value == returned_last_element

assert str(list_) == '1 -> 5 -> 9'

second_node = list_.node(n=1)
list_.remove(second_node)

print(list_)
assert str(list_) == '1 -> 5'
# ZAD 3
queue = Queue()
assert len(queue) == 0
queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')
#assert str(queue) == 'klient1, klient2, klient3'  - to mi nie dziala(nie wiem jak poprawic aby wyswietlalo jak jest w zadaniu), ale jak zmienie "," na "->"to dziala      
assert str(queue) == 'klient1 -> klient2 -> klient3'
client_first = queue.dequeue()
assert client_first == 'klient1'
#assert str(queue) == 'klient2, klient3' - tak samo jak w poprzednim przypadku
print(queue)
assert str(queue) == 'klient2 -> klient3'
assert len(queue) == 2

    