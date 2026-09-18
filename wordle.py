def binary_search(array,target):
  high=len(array)-1
  low=0
  while low<=high:
    mid=(low+high)//2
    if array[mid]<target:
      low=mid+1
    elif array[mid]>target:
      high=mid-1
    else:
      return True
  return False

def correctplace(word,guess,result):
  a=0
  for i in range(len(guess)):
    if word[i]==guess[i]:
      result[i]=guess[i].upper()
      numR[i]=True
      numW[i]=True
      a=a+1
    else:
      result[i]="_"
  return a

def wrongplace(word,guess,result,numW,numR):
  for i in range(5):
    for j in range(5):
      if guess[i]==word[j] and numR[i]==False and numW[j]==False:
        result[i]=guess[i]
        numR[i]=True
        numW[j]=True

wordlist=[""]*5757
f=open("sortedwords.txt","r")
for i in range (5756):
  wordlist[i]=f.readline().strip("\n")
solution=str(input("Which word to guess? "))
valid=binary_search(wordlist,solution)
if valid == True:
  print("Word exists")
  for i in range(100):
    print()
else:
  print("Word does not exist")
numR=[False]*5
numW=[False]*5
lives=6
while lives>0:
  guess = input("Enter the guess of the word ")
  output_string = [""]*5
  lives=lives-1
  numbercorrect = correctplace(solution, guess, output_string)
  wrongplace(solution, guess, output_string,numW,numR)
  for i in range(5):
    print(f"{output_string[i]} ",end="")
  if numbercorrect == 5:
    print(" Winner")
    break
  print("       ",lives," lives")
  if lives==0:
    print("You Lose!")




    
