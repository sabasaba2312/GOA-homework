# მომხმარებელს შემოატანინეთ ქულა score და შეინახეთ ცვლადში, როგორც integer.
#შემდეგ, ქულის მიხედვით განსაზღვრეთ შეფასება (grade):
#A – თუ score მეტია 80-ზე
#B – თუ score მეტია 60-ზე
#C – თუ score მეტია 40-ზე
#D – თუ score მეტია 20-ზე
#F – თუ score 20-ზე ნაკლებია

#ბოლოს, დაბეჭდეთ შესაბამისი grade.
score = int(input("enter your score: "))
if score > 80:
    print("grade = A")
elif score > 60:
    print("grade = B")
elif score > 40:
    print("grade = C")
elif score > 20:
    print("grade = D")
else:
    print("grade = F")
