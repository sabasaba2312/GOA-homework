#მომხმარებელს შეაყვანინე ინდექსი და ახალი ფერი, შეცვალე ამ ინდექსზე არსებული ფერი სიაში `colors = ["თეთრი", "შავი", "ნარინჯისფერი", "ვარდისფერი"]` და დაბეჭდე განახლებული სია

colors = ["თეთრი", "შავი", "ნარინჯისფერი", "ვარდისფერი"]
color = int(input("enter index: "))
axali_feri = input("enter new color: ")

if color <= 3:
    colors[color] = axali_feri
    print(colors)
else:
    print("arasworia")
