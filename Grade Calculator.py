marks=[]
for i in range(5):
    mark=float(input("Enter marks:"))
    marks.append(mark)
    
percentage=sum(marks)/500*100   
print("Percentage =", percentage) 

if percentage >= 90:
    print("Grade A")
elif percentage >= 75:
    print("Grade B")
elif percentage >= 60:
    print("Grade C") 
elif percentage >= 50: 
    print("Grade D")      
else:
    print("Fail")