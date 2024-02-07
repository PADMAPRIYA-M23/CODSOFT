l=[]
k=1
while k==True:
    print()
    print("-------------TO DO LIST-------------")
    print("1.add a task")
    print("2.delete a task")
    print("3.display task")
    print("4.exit")
    n=(int(input("enter your option :")))
    if n==1:
        a=input("enter your task :")
        l.append(a)
        print()
        print("task added successfully")
    if n==2:
        p=int(input("enter the task number"))
        try:
            if len(l)==0 :
                print()
                print("-----------NO TASK ASSIGNED---------")
            else:
                l.pop(p-1)
                print()
                print("TASK REMOVED SUCCESSFULLY")
        except:
            print()
            print("-----------NO TASK ASSIGNED---------")
    if n==3:
        if len(l)==0:
            print()
            print("NO TASK ASSIGNED")
        else:
            print()
            print("-------------TO DO LIST-------------")
            for i in range(len(l)):
                print(i+1,":",l[i])
            
    if n==4:
        k=False