import  cv2
import string
import os
d={}
c={}
for i in range(255):
  d[chr(i)]=i
  c[i]=chr(i)
x=cv2.imread(r"C:\Users\ASUS\Downloads\Duniya.jpg")

i=x.shape[0]
j=x.shape[1]
print(i,j)

key=input(" Enter the key to edit(Security key):")
text=input(" Enter the text to hide: ")

kl=0
tln=len(text)
z=0
n=0
m=0

l=len(text)

for i in range(1):8
x[n,m,z]=d[text[i]]^d[key[kl]]
n=n+1
m=m+1
m=(m+1)%3
kl=(kl+1)%len(key)
cv2.imwrite("flower.webp",x)
os.startfile("flower.webp")
print("Data Hidinng In Image Complete Successfully")

k1=0
tln=len(text)
z=0
n=0
m=0

ch=int(input("\nEnter 1 To extract data from Image : "))

if ch ==1:
  key1=input("\n\nRe-enter key to extract text : ")
  decrypt=""

  if key == key1 :
    for i in range(1):
      decrypt+=c[x[n,m,z]^d[key[k1]]]
      n=n+1
      m=m+1
      m=(m+1)%3
      k1=(k1+1)%len(key)
      print("Encrypted text was : ",decrypt)
  else:
    print("Key Dosen't Matched.")
else:
     print("Thank You. Exiting")