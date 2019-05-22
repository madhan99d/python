class node:
    def __init__(self,d):
      self.addr=None
      self.data=d
      
class oper:
    def __init__(self):
        self.head=None
        
    def display(self):
        temp=self.head
        while (temp!=None):
          print(temp.data,"-->",end="")
          temp=temp.addr
        print("none")
        
    def count(self):
      temp=self.head
      c=0
      while(temp!=None):
        c=c+1
        temp=temp.addr
      print(c)

    def insert(self):
        print("enter the data of the new node to be inserted")
        dat=input()
        newnode=node(dat)
        print("enter the position to be inserted ")
        i=input()
        if(i=='0' or i=="first" or i=="First" or i== "FIRST"):
            newnode.addr=self.head
            self.head=newnode
            print("insertion successfull")
        elif(i=="last" or i=="Last" or i=="LAST"):
            temp=self.head
            while(temp!=None):
                if temp.addr==None:
                    break
                temp=temp.addr
            temp.addr=newnode
            print("insertion successfull")
        else:
            c=1
            temp=self.head
            while(c<int(i)):
                c=c+1
                temp=temp.addr
            prev=temp.addr
            temp.addr=newnode
            newnode.addr=prev
            print("insertion successfull")
    def delete(self):
          print("enter the node to be deleted")
          dat=int(input())
          if self.head.data==dat:
              self.head.next=head
              self.head.addr=None
              print("deletion successfull")
          else:
              temp=self.head
              while(temp!=None):
                  if temp.addr.data==dat:
                      break
                  temp=temp.addr
              ne=temp.addr
              temp.addr=ne.addr
              ne.addr=None
              print("deletion successfull")
        
obj=oper()
ch=0

while(ch!=5):
  ch=int(input("enter the value  1.display 2.count 3.insert 4.delete"))
  if ch==1:
    obj.display()
  elif ch==2:
    obj.count()
  elif ch==3:
     obj.insert()
  elif ch==4:
      obj.delete()
