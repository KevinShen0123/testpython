'''实现的功能：

（1）多位数的四则运算

（2）DEL功能：退除

（3）清零再计算

（4）复合（括号）运算

（5）三角函数的运算、exp函数的运算

'''



from tkinter import *    #引入各个模块

import math



a=[]

b=[]

def clic(x):   #点击按钮并且显示

    b.append(x)

    a.append(x)

    if Var1.get()=='' and len(a)!=len(b):

        b.clear()

        a.clear()

        b.append(x)

        Var1.set(x)

        a.append(x)

    else:

        m=''

        for i in b:

            m+=i

        Var1.set(m)



def Undo():    #退除功能

    del a[-1]

    del b[-1]

    m=''

    for i in b:

        m+=i

        Var1.set(m)



def equl():    #按下=键

    #对字符进行整合

    f = 0

    g = 0

    for i in a:

        if i == 'X' or i == '/' or i == '+' or i == '-':

            f += 1

        s=['sin','cos','tan','arcsin','arcos','arctan','e^']

        if i == '(' or i == ')'or i in s:

            g += 1

    while f*2+1!= len(a)-g:

        for i in range(len(a)):

            if i + 1 != len(a):

                if a[i].isdigit() and a[i + 1].isdigit():

                    m = a[i] + a[i + 1]

                    del a[i:i + 2]

                    a.insert(i, m)

                    break

    #有括号的计算

    while '(' in a:

        if '(' in a:

            q=a.index('(')

            p=a.index(')')

            newa=a[q+1:p]

            while len(newa) > 1:  #括号内的计算

                h = len(newa)

                b = []

                for i in newa:

                    if i == 'X' or i == '/' or i == '+' or i == '-':

                        b.append(i)

                #print(b)

                for i in range(1, h, 2):

                    if newa[i] == 'X' or newa[i] == '/':

                        if newa[i] == 'X':

                            answer = float(newa[i - 1]) * float(newa[i + 1])

                            del newa[i - 1:i + 2]

                            newa.insert(i - 1, answer)

                            break

                        else:

                            answer = float(newa[i - 1]) / float(newa[i + 1])

                            del newa[i - 1:i + 2]

                            newa.insert(i - 1, answer)

                            break

                    elif (newa[i] == '+' or newa[i] == '-') and ('X' not in b and '/' not in b):

                        if newa[i] == '+':

                            answer = float(newa[i - 1]) + float(newa[i + 1])

                            del newa[i - 1:i + 2]

                            newa.insert(i - 1, answer)

                            break

                        else:

                            answer = float(newa[i - 1]) - float(newa[i + 1])

                            del newa[i - 1:i + 2]

                            newa.insert(i - 1, answer)

                            break

            del a[q:p+1]

            a.insert(q,str(newa[0]))

    #EXP的计算

    while 'e^' in a:

        flag=a.index('e^')

        result=str(math.exp(float(a[flag+1])))

        del a[flag:flag+2]

        a.insert(flag,result)

    #三角的计算

    while 'sin' in a:   #sin的计算

        flag=a.index('sin')

        flag2=float(a[flag+1])

        reslut=str(math.sin(flag2))

        del a[flag:flag+2]

        a.insert(flag,reslut)

    while 'cos' in a:   #cos的计算

        flag=a.index('cos')

        flag2=float(a[flag+1])

        reslut=str(math.cos(flag2))

        del a[flag:flag+2]

        a.insert(flag,reslut)

    while 'tan' in a:   #tan的计算

        flag=a.index('tan')

        flag2=float(a[flag+1])

        reslut=str(math.tan(flag2))

        del a[flag:flag+2]

        a.insert(flag,reslut)

    while 'arcsin' in a:   #arcsin的计算

        flag=a.index('arcsin')

        flag2=float(a[flag+1])

        reslut=str(math.asin(flag2))

        del a[flag:flag+2]

        a.insert(flag,reslut)

    while 'arcos' in a:   #arcos的计算

        flag=a.index('arcos')

        flag2=float(a[flag+1])

        reslut=str(math.acos(flag2))

        del a[flag:flag+2]

        a.insert(flag,reslut)

    while 'arctan' in a:   #arctan的计算

        flag=a.index('arctan')

        flag2=float(a[flag+1])

        reslut=str(math.atan(flag2))

        del a[flag:flag+2]

        a.insert(flag,reslut)



    #开始计算

    while len(a)>1:

        h=len(a)

        b=[]

        for i in a:

            if i =='X' or i=='/' or i=='+' or i=='-':

                b.append(i)

        print(b)

        for i in range(1,h,2):

            if a[i]=='X' or a[i]=='/':

                if a[i]=='X':

                    answer=float(a[i-1]) * float(a[i+1])

                    del a[i-1:i+2]

                    a.insert(i-1,answer)

                    break

                else:

                    answer=float(a[i-1]) / float(a[i+1])

                    del a[i - 1:i + 2]

                    a.insert(i - 1,answer )

                    break

            elif (a[i]=='+' or a[i]=='-') and ('X' not in b and '/' not in b):

                if a[i]=='+':

                    answer=float(a[i-1]) + float(a[i+1])

                    del a[i - 1:i + 2]

                    a.insert(i - 1, answer)

                    break

                else:

                    answer=float(a[i-1]) - float(a[i+1])

                    del a[i - 1:i + 2]

                    a.insert(i - 1, answer)

                    break

    Var1.set(a[0])



def ZERO():    #清零的操作

    Var1.set('')



#计算器的初始化

root=Tk()

root.geometry('400x450')

root.configure(bg='powderblue')

root.resizable(0,0)   #不允许更改界面的大小

root.title('计算器')



#计算机的页面

#第一行

button7=Button(root,text='7',bd=0.5,font=('黑体',20),bg='dodgerblue',fg='white',relief='ridge',command=lambda x='7':clic(x))

button7.place(x=20,y=150,width=64,height=40)

button8=Button(root,text='8',bd=0.5,font=('黑体',20),bg='dodgerblue',fg='white',relief='ridge',command=lambda x='8':clic(x))

button8.place(x=94,y=150,width=64,height=40)

button9=Button(root,text='9',bd=0.5,font=('黑体',20),bg='dodgerblue',fg='white',relief='ridge',command=lambda x='9':clic(x))

button9.place(x=168,y=150,width=64,height=40)

DEL=Button(root,text='DEL',bd=0.5,font=('黑体',20),bg='khaki',fg='dimgray',relief='ridge',command=Undo)

DEL.place(x=242,y=150,width=64,height=40)

AC=Button(root,text='AC',bd=0.5,font=('黑体',20),bg='khaki',fg='dimgray',relief='ridge',command=ZERO)

AC.place(x=316,y=150,width=64,height=40)

#第二行

button4=Button(root,text='4',bd=0.5,font=('黑体',20),bg='dodgerblue',fg='white',relief='ridge',command=lambda x='4':clic(x))

button4.place(x=20,y=210,width=64,height=40)

button5=Button(root,text='5',bd=0.5,font=('黑体',20),bg='dodgerblue',fg='white',relief='ridge',command=lambda x='5':clic(x))

button5.place(x=94,y=210,width=64,height=40)

button6=Button(root,text='6',bd=0.5,font=('黑体',20),bg='dodgerblue',fg='white',relief='ridge',command=lambda x='6':clic(x))

button6.place(x=168,y=210,width=64,height=40)

buttonmul=Button(root,text='X',bd=0.5,font=('黑体',20),bg='dodgerblue',fg='white',relief='ridge',command=lambda x='X':clic(x))

buttonmul.place(x=242,y=210,width=64,height=40)

buttondiv=Button(root,text='/',bd=0.5,font=('黑体',20),bg='dodgerblue',fg='white',relief='ridge',command=lambda x='/':clic(x))

buttondiv.place(x=316,y=210,width=64,height=40)

#第三行

button1=Button(root,text='1',bd=0.5,font=('黑体',20),bg='dodgerblue',fg='white',relief='ridge',command=lambda x='1':clic(x))

button1.place(x=20,y=270,width=64,height=40)

button2=Button(root,text='2',bd=0.5,font=('黑体',20),bg='dodgerblue',fg='white',relief='ridge',command=lambda x='2':clic(x))

button2.place(x=94,y=270,width=64,height=40)

button3=Button(root,text='3',bd=0.5,font=('黑体',20),bg='dodgerblue',fg='white',relief='ridge',command=lambda x='3':clic(x))

button3.place(x=168,y=270,width=64,height=40)

buttonplus=Button(root,text='+',bd=0.5,font=('黑体',20),bg='dodgerblue',fg='white',relief='ridge',command=lambda x='+':clic(x))

buttonplus.place(x=242,y=270,width=64,height=40)

buttonsub=Button(root,text='-',bd=0.5,font=('黑体',20),bg='dodgerblue',fg='white',relief='ridge',command=lambda x='-':clic(x))

buttonsub.place(x=316,y=270,width=64,height=40)

#第四行

button0=Button(root,text='0',bd=0.5,font=('黑体',20),bg='dodgerblue',fg='white',relief='ridge',command=lambda x='0':clic(x))

button0.place(x=20,y=330,width=64,height=40)

buttonl=Button(root,text='(',bd=0.5,font=('黑体',20),bg='dodgerblue',fg='white',relief='ridge',command=lambda x='(':clic(x))

buttonl.place(x=94,y=330,width=64,height=40)

buttonr=Button(root,text=')',bd=0.5,font=('黑体',20),bg='dodgerblue',fg='white',relief='ridge',command=lambda x=')':clic(x))

buttonr.place(x=168,y=330,width=64,height=40)

Exp=Button(root,text='EXP',bd=0.5,font=('黑体',20),bg='dodgerblue',fg='white',relief='ridge',command=lambda x='e^':clic(x))

Exp.place(x=242,y=330,width=64,height=40)

buttonamu=Button(root,text='=',bd=0.5,font=('黑体',20),bg='dodgerblue',fg='white',relief='ridge',command=equl)

buttonamu.place(x=316,y=330,width=64,height=40)

#第五行（三角）

Sin=Button(root,text='sin',bd=0.5,font=('黑体',15),bg='deepskyblue',fg='white',relief='ridge',command=lambda x='sin':clic(x))

Sin.place(x=20,y=390,width=50,height=30)

Cos=Button(root,text='cos',bd=0.5,font=('黑体',15),bg='deepskyblue',fg='white',relief='ridge',command=lambda x='cos':clic(x))

Cos.place(x=82,y=390,width=50,height=30)

Tan=Button(root,text='tan',bd=0.5,font=('黑体',15),bg='deepskyblue',fg='white',relief='ridge',command=lambda x='tan':clic(x))

Tan.place(x=144,y=390,width=50,height=30)

ASin=Button(root,text='asin',bd=0.5,font=('黑体',15),bg='deepskyblue',fg='white',relief='ridge',command=lambda x='arcsin':clic(x))

ASin.place(x=206,y=390,width=50,height=30)

ACos=Button(root,text='acos',bd=0.5,font=('黑体',15),bg='deepskyblue',fg='white',relief='ridge',command=lambda x='arcos':clic(x))

ACos.place(x=268,y=390,width=50,height=30)

ATan=Button(root,text='atan',bd=0.5,font=('黑体',15),bg='deepskyblue',fg='white',relief='ridge',command=lambda x='arctan':clic(x))

ATan.place(x=330,y=390,width=50,height=30)



#输出框

Var1=StringVar(root,'')

entry1=Entry(root,textvariable=Var1,state='readonly',font=('Arial',12))

entry1.place(x=20,y=20,width=360,height=80)



root.mainloop()

