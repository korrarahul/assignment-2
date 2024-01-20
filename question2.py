file_=open("input.txt","r")
count=dict()
data=file_.read()
word_count=data.split()
for i in word_count:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)
f=open("output.txt","w")
f.write(data)
f.write("\nWord_Count:\n")
for key,value in count.items():
    f.write(f"{key}:{value}\n")
f.close()