import pyttsx3 #pip install pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
# to speak slowly
engine.setProperty('rate',140)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

num={1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten",\
     11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen",20:"Twenty",\
     10:"Ten",30:"Thirty",40:"Forty",50:"Fifty",60:"Sixty",70:"Seventy",80:"Eighty",90:"Ninety",\
     100:"Hundred",1000:"Thousand",100000:"Lakh",10000000:"Crore"}
'''converts two digits number into works'''
def two(a):
    if len(a)==2 and a[0]!="1" and a[0]!="0" and a[-1]!='0':
        s=num[int(a[0]+'0')]+" "+num[int(a[-1])]
        return s

    elif a=='00':
        return ""    
    elif (len(a)==2  or len(a)==1) or a[0]=='0':
        s=num[int(a)]

        return s
    
        

'''converts three digit number into words'''
def three(a):
    s=""
    if a[0]!='0':
        s=num[int(a[0])]+" "+num[100]+' '+two(a[1:])
    elif a[0]=='0':
        s=two(a[1:])
    elif a=="000":
        s=""
    return s               

while True:
    

    num1=input("enter a number:-")
    if num1=='exit':
        break
    else:
        length=len(num1)

        list1=[i for i in num1]
        list2=[]
        string=""
        string2=""
        count=0
        if num1[0]=='0':
            print("A Number Can not be start with zero ")
        elif len(num1)>=10:
            print("maximum limit of digit is 9 , and you have exceed the limit")
                
        
                
        else:
            #it convets even numbers of digits into words
            if length%2==0 and length>=4:
                list2.append(list1[0])
                list1.pop(0)
                if length>4:
                    for i in range((length-4)//2):
                        list2.append("".join(list1[0:2]))
                        del list1[0:2]
                list2.append("".join(list1))
                list1.clear()
            

            #it converts odd numbers of digits into words
            elif length%2!=0 and length>=4  :
                
                for i in range((length-3)//2):
                    list2.append(("".join(list1[0:2])))
                    del list1[0:2]
                list2.append(("".join(list1)))
                list1.clear()
            #its converts three digit number into words    
            elif length<=3:
                list2.append(("".join(list1)))
                list1.clear()
                
            print(list2)
            length2=len(list2)        
            for i in range(len(list2)):
                if list2[i]==list2[-1]:
                    if len(list2[i])==3:
                        string=string+" "+three(list2[i])
                        break
                    else:
                        string=two(list2[i])
                        break
                else:
                    if list2[i]=='00':
                        length2=length2-1
                    else:
                        string2= two(list2[i])+" "+num[(10**3)*(10**(2*(length2-2)))]
                        string=string+" "+string2
                        length2=length2-1
                        
                        
                
            print(string)
            speak(string)



   
    

    







    





