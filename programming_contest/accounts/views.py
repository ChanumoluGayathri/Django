from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
# from accounts.forms import UserAdminCreationForm
from accounts.forms import UserAdminCreationForm
from .models import EvenOdd,ReverseNum,PrimeNum,Userdata,QuestionKey,HomeTime,LoginTime,TestTime,FinishTime,UserHiddenData,HiddenEvenOdd,HiddenPrimeNum,HiddenReverseNum,PostiveNum,HiddenPositiveNum,HiddenMagicNum,MagicNum,CapitalizeVowels,HiddenCapitalizeVowels,UnitNum,HiddenUnitNum,Tensdigit,HiddenTensdigit,Palindrome,HiddenPalindrome,Armstrong,HiddenArmstrong
from django.core.files import File
from django.http import HttpResponse
import time
import datetime
from datetime import date,timedelta
from datetime import datetime
from datetime import timedelta
from django_globals import globals
from django.conf import settings

global result1
result1 = {}
global result2
result2 = {}
global result3
result3 = {}
global result4
result4 = {}

@login_required()
def register(req):
    form = UserAdminCreationForm()
    if req.method == 'POST':
        form = UserAdminCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('login')


    return render(req, 'register.html', {'form': form})

def login(request):
    LoginTime.objects.all().delete()
    login=datetime.now().strftime('%H:%M:%S')
    print("login: ",login)
    var3=LoginTime(login=login)
    var3.save()

    return render(request,'accounts/registration/login.html')

def home(request):
    HomeTime.objects.all().delete()
    home=datetime.now().strftime('%H:%M:%S')
    print(home)
    var2=HomeTime(home=home)
    var2.save()

    Userdata.objects.all().delete()
    UserHiddenData.objects.all().delete()

    return render(request,'home.html')

def main(request):
    TestTime.objects.all().delete()
    test=datetime.now().strftime('%H:%M:%S')
    print(test)
    var3=TestTime(test=test)
    var3.save()
    events = QuestionKey.objects.all()
    for i in events:
        print(i.key)
    return render(request,'main.html',{'events':events})

def invalid(request):
    return render(request,'Invalid.html')

def key(request):
    QuestionKey.objects.all().delete()

    keys=['Talent01','Talent02','Talent03','Talent04','Talent05','Talent06','Talent07','Talent08','Talent09','Talent10']
    if request.method=='POST':
        key = request.POST.get('key')
        if key in keys:
            var1 = QuestionKey(key=key)
            print(key)
            var1.save()
            global result2
            result2 = {}
            global result4
            result4 = {}
            print("successfully saved")
            return redirect('main')
        else:
            return redirect('invalid')
    return render(request,'key.html')

                     # compiling part
from django.shortcuts import render
from django.http import HttpResponse
import sys
# Create your views here.
def greetings(request):
    res = render(request,'main.html')
    return res

def runcode(request):
    def EvalTest(list1,list2):
        for i in list1:
            if request.method == 'POST':
                code_part = request.POST['code_area']
                input_part = i

                y = input_part
                #input_part = input_part.replace("\n"," ").split(" ")
                def input():
                    a = input_part
                    return a
                try:
                    orig_stdout = sys.stdout
                    sys.stdout = open('file.txt', 'w')
                    exec(code_part)
                    sys.stdout.close()
                    sys.stdout=orig_stdout
                    output = open('file.txt', 'r').read()
                except Exception as e:
                    sys.stdout.close()
                    sys.stdout=orig_stdout
                    output = e
                #print(output)
            if request.method=='POST':
                code = request.POST['code_area']
                input = input_part
                out = output
                print(code,input,out)
                var1 = Userdata(code=code,input_part=input,output_part=out)
                var1.save()
                print("successfully saved")

            else:
                print("Not successful")
        for i in list2:
            if request.method == 'POST':
                code_part = request.POST['code_area']
                input_part = i

                y = input_part
                #input_part = input_part.replace("\n"," ").split(" ")
                def input():
                    a = input_part
                    return a
                try:
                    orig_stdout = sys.stdout
                    sys.stdout = open('file.txt', 'w')
                    exec(code_part)
                    sys.stdout.close()
                    sys.stdout=orig_stdout
                    output = open('file.txt', 'r').read()
                except Exception as e:
                    sys.stdout.close()
                    sys.stdout=orig_stdout
                    output = e
                #print(output)
            if request.method=='POST':
                code = request.POST['code_area']
                input = input_part
                out = output
                print(code,input,out)
                var1 =UserHiddenData(input=input,output=out)
                var1.save()
                print("successfully saved")

            else:
                print("Not successful")

    events = QuestionKey.objects.all()
    for i in events:
        print(i.key)
    if i.key=='Talent01':
        list1=[2,3,12,7,6]
        list2=[-1,-2,-100]
        EvalTest(list1,list2)
        tol=list(EvenOdd.objects.values_list('output', flat=True))
        til=list(EvenOdd.objects.values_list('input', flat=True))
        uil=list(Userdata.objects.values_list('input_part', flat=True))
        uol=list(Userdata.objects.values_list('output_part', flat=True))
        #Hidden
        tol1=list(HiddenEvenOdd.objects.values_list('output', flat=True))
        til1=list(HiddenEvenOdd.objects.values_list('input', flat=True))
        uil1=list(UserHiddenData.objects.values_list('input', flat=True))
        uol1=list(UserHiddenData.objects.values_list('output', flat=True))

    elif i.key=='Talent02':
        list1=[289,123456,24,12,101]
        list2=[777,475,81]
        EvalTest(list1,list2)
        tol=list(ReverseNum.objects.values_list('output', flat=True))
        til=list(ReverseNum.objects.values_list('input', flat=True))
        uil=list(Userdata.objects.values_list('input_part', flat=True))
        uol=list(Userdata.objects.values_list('output_part', flat=True))
        #Hidden
        tol1=list(HiddenReverseNum.objects.values_list('output', flat=True))
        til1=list(HiddenReverseNum.objects.values_list('input', flat=True))
        uil1=list(UserHiddenData.objects.values_list('input', flat=True))
        uol1=list(UserHiddenData.objects.values_list('output', flat=True))
    elif i.key=='Talent03':
        list1=[3,2,9,11,121]
        list2=[211,401,555]
        EvalTest(list1,list2)
        tol=list(PrimeNum.objects.values_list('output', flat=True))
        til=list(PrimeNum.objects.values_list('input', flat=True))
        uil=list(Userdata.objects.values_list('input_part', flat=True))
        uol=list(Userdata.objects.values_list('output_part', flat=True))
        #Hidden
        tol1=list(HiddenPrimeNum.objects.values_list('output', flat=True))
        til1=list(HiddenPrimeNum.objects.values_list('input', flat=True))
        uil1=list(UserHiddenData.objects.values_list('input', flat=True))
        uol1=list(UserHiddenData.objects.values_list('output', flat=True))
    elif i.key=='Talent04':
        list1=[8,-7,-77,5,65]
        list2=[673,-674,675]
        EvalTest(list1,list2)
        tol=list(PostiveNum.objects.values_list('output', flat=True))
        til=list(PostiveNum.objects.values_list('input', flat=True))
        uil=list(Userdata.objects.values_list('input_part', flat=True))
        uol=list(Userdata.objects.values_list('output_part', flat=True))
        #Hidden
        tol1=list(HiddenPositiveNum.objects.values_list('output', flat=True))
        til1=list(HiddenPositiveNum.objects.values_list('input', flat=True))
        uil1=list(UserHiddenData.objects.values_list('input', flat=True))
        uol1=list(UserHiddenData.objects.values_list('output', flat=True))

    elif i.key=='Talent05':
        list1=[226,110,325,23,199]
        list2=[65,29,28]
        EvalTest(list1,list2)
        tol=list(MagicNum.objects.values_list('output', flat=True))
        til=list(MagicNum.objects.values_list('input', flat=True))
        uil=list(Userdata.objects.values_list('input_part', flat=True))
        uol=list(Userdata.objects.values_list('output_part', flat=True))
        #Hidden
        tol1=list(HiddenMagicNum.objects.values_list('output', flat=True))
        til1=list(HiddenMagicNum.objects.values_list('input', flat=True))
        uil1=list(UserHiddenData.objects.values_list('input', flat=True))
        uol1=list(UserHiddenData.objects.values_list('output', flat=True))

    elif i.key=='Talent06':
        list1=['erosenninJirayaSama','dialecticalmaterialism','religionisthesighoftheopressedcreature','information','technology']
        list2=['utopia','question','world']
        EvalTest(list1,list2)
        tol=list(CapitalizeVowels.objects.values_list('output', flat=True))
        til=list(CapitalizeVowels.objects.values_list('input', flat=True))
        uil=list(Userdata.objects.values_list('input_part', flat=True))
        uol=list(Userdata.objects.values_list('output_part', flat=True))
        #Hidden
        tol1=list(HiddenCapitalizeVowels.objects.values_list('output', flat=True))
        til1=list(HiddenCapitalizeVowels.objects.values_list('input', flat=True))
        uil1=list(UserHiddenData.objects.values_list('input', flat=True))
        uol1=list(UserHiddenData.objects.values_list('output', flat=True))

    elif i.key=='Talent07':
        list1=[543,231,325,110,26]
        list2=[473,654,75]
        EvalTest(list1,list2)
        tol=list(UnitNum.objects.values_list('output', flat=True))
        til=list(UnitNum.objects.values_list('input', flat=True))
        uil=list(Userdata.objects.values_list('input_part', flat=True))
        uol=list(Userdata.objects.values_list('output_part', flat=True))
        #Hidden
        tol1=list(HiddenUnitNum.objects.values_list('output', flat=True))
        til1=list(HiddenUnitNum.objects.values_list('input', flat=True))
        uil1=list(UserHiddenData.objects.values_list('input', flat=True))
        uol1=list(UserHiddenData.objects.values_list('output', flat=True))

    elif i.key=='Talent08':
        list1=[543,231,325,110,26]
        list2=[473,654,75]
        EvalTest(list1,list2)
        tol=list(Tensdigit.objects.values_list('output', flat=True))
        til=list(Tensdigit.objects.values_list('input', flat=True))
        uil=list(Userdata.objects.values_list('input_part', flat=True))
        uol=list(Userdata.objects.values_list('output_part', flat=True))
        #Hidden
        tol1=list(HiddenTensdigit.objects.values_list('output', flat=True))
        til1=list(HiddenTensdigit.objects.values_list('input', flat=True))
        uil1=list(UserHiddenData.objects.values_list('input', flat=True))
        uol1=list(UserHiddenData.objects.values_list('output', flat=True))

    elif i.key=='Talent09':
        list1=['malayalam','madam','teacher','gagan','radar']
        list2=['madam','gayathri','kayak']
        EvalTest(list1,list2)
        tol=list(Palindrome.objects.values_list('output', flat=True))
        til=list(Palindrome.objects.values_list('input', flat=True))
        uil=list(Userdata.objects.values_list('input_part', flat=True))
        uol=list(Userdata.objects.values_list('output_part', flat=True))
        #Hidden
        tol1=list(HiddenPalindrome.objects.values_list('output', flat=True))
        til1=list(HiddenPalindrome.objects.values_list('input', flat=True))
        uil1=list(UserHiddenData.objects.values_list('input', flat=True))
        uol1=list(UserHiddenData.objects.values_list('output', flat=True))

    elif i.key =='Talent10':
        list1=[407,663,1634,153,53]
        list2=[370,545,345]
        EvalTest(list1,list2)
        tol=list(Armstrong.objects.values_list('output', flat=True))
        til=list(Armstrong.objects.values_list('input', flat=True))
        uil=list(Userdata.objects.values_list('input_part', flat=True))
        uol=list(Userdata.objects.values_list('output_part', flat=True))
        #Hidden
        tol1=list(HiddenArmstrong.objects.values_list('output', flat=True))
        til1=list(HiddenArmstrong.objects.values_list('input', flat=True))
        uil1=list(UserHiddenData.objects.values_list('input', flat=True))
        uol1=list(UserHiddenData.objects.values_list('output', flat=True))
    else:
        return redirect('invalid')

    global result1
    result1 = {}
    global result2
    result2 = {}
    global result3
    result3 = {}
    global result4
    result4 = {}
    for key in til:
        for value in tol:
            result1[key] = value
            tol.remove(value)
            break
    for key in uil:
        for value in uol:
            result2[key] = value
            uol.remove(value)
            break

    for key in til1:
        for value in tol1:
            result3[key] = value
            tol1.remove(value)
            break
    for key in uil1:
        for value in uol1:
            result4[key] = value
            uol1.remove(value)
            break

    if request.method == 'POST':
        code_part = request.POST['code_area']
        input_part =  request.POST['input_area']

        if input_part not in list1:
            y = input_part
            input_part = input_part.replace("\n"," ").split(" ")
            def input():
                a = input_part[0]
                del input_part[0]
                return a
            try:
                orig_stdout = sys.stdout
                sys.stdout = open('file.txt', 'w')
                exec(code_part)
                sys.stdout.close()
                sys.stdout=orig_stdout
                output = open('file.txt', 'r').read()
            except Exception as e:
                sys.stdout.close()
                sys.stdout=orig_stdout
                output = e
            #print(output)
        if request.method=='POST':
            code = request.POST['code_area']
            input = request.POST['input_area']
            out = output
            print(code,input,out)
            var1 = Userdata(code=code,input_part=input,output_part=out)
            var1.save()
            print("successfully saved")
        else:
            print("Not successfully saved")
    res = render(request,'main.html',{"code":code_part,"input":y,"output":output,"events":events,"result1":result1,"result2":result2,"result3":result3,"result4":result4})
    return res

def result(request):
    FinishTime.objects.all().delete()
    t1=datetime.now().strftime('%H:%M:%S')
    print(t1)
    var4=FinishTime(finish=t1)
    var4.save()
    score=0
    wrong=0
    correct=0
    total=0
    if result2.items() != {}:
        for (uk,uv) in result2.items():
            for (tk,tv) in result1.items():
                if tk == uk:
                    print("Hiiiii",uk,uv);
                    total=total+1
                    if tv == uv.strip():
                        score=score+10
                        correct=correct+1
                        print(tk,uk,tv,uv,"Success",score,correct)
                        break;
                    else:
                        wrong=wrong+1
                        print(tk,uk,tv,uv,"Failed",wrong)
        for (uk,uv) in result4.items():
            for (tk,tv) in result3.items():
                if tk == uk:
                    print("Hiiiii",uk,uv);
                    total=total+1
                    if tv == uv.strip():
                        score=score+10
                        correct=correct+1
                        print(tk,uk,tv,uv,"Success",score,correct)
                        break;
                    else:
                        wrong=wrong+1
                        print(tk,uk,tv,uv,"Failed",wrong)

    percent=(score/80)*100
    print(percent)
    context ={
    'score':score,
    'correct':correct,
    'wrong':wrong,
    'percent':percent,
    'total':total
    }
    list1=HomeTime.objects.all()
    list2=TestTime.objects.all()
    list3=FinishTime.objects.all()
    my_list = zip(list2,list3)
    for i,j in my_list :
        hour=(j.finish.hour-i.test.hour )* 60;
        minute=j.finish.minute-i.test.minute;
        tot=hour+minute
        context1={
        "tot":tot
        }
    return render(request,'Result.html',{'list1':list1,'list2':list2,'list3':list3,'my_list':my_list,'context':context,'context1':context1})
