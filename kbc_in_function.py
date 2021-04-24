#KBC
def question_please(i):
    question=["how many continents are there","What is the capital of india","NG mai kon sa cource padhya jata hai"]
    print(question[i])
def options_please(i,j):
    options=options=[["four","nine","seven","eight"],["chatisgarh","bhopal","channi","delhi"],["software engineering","counselling","tourisem","Agriculure"]]
    print(j+1,options[i][j])
def solution_please(i):
    solution=[3,4,1]
    s=solution[i]
    return s
def a_please(i):
    a=a=[["1 four","3 seven"],["2 bhopal","4 delhi"],["1 software engineering","2 tourisem"]]
    print(a[i][0])
    print(a[i][1])
txt="####*🤩🤩🤩Kaun Banega Corodpati (KBC)🤩🤩🤩*####"
x=txt.center(90)
print(x)
count=0
for i in range(0,3):
    print("👇")
    print("👁 Your question is on your screen👁")
    question_please(i)
    for j in range(0,4):
        options_please(i,j)
    user=int(input("🤔Choose Correct Answer or Use 5050 life line🤔\n"))
    s=solution_please(i)
    if user==s:
        print("congratulations")
    elif user==5050:
        if count<1:
            count=count+1  
            a_please(i)
            user1=int(input("you have 2 answers to choose"))
            z=solution_please(i)
            if user1==z:
                print("congratulations")
            else:
                print("game over")
                break
        else:
            print("you have already used life line")
            r=solution_please(i)
            user2=int(input("enter your answer"))
            if user2==r:
                print("congratulations")
            else:
                print("game over")
                break
    else:
        print("game over")
        break
