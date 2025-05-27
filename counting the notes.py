Amount=int(input("please enter amount for withdraw"))
note_1=Amount//100
note_2=((Amount%100)//50)
note_3=((Amount%100)%50)//10
print(note_1 , note_2 , note_3)