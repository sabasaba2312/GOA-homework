#შექმენით tuple სახელად animals, რომელშიც იქნება რამდენიმე ცხოველის სახელი. გამოიყენეთ .count და .index მეთოდები ამ tuple-ზე

animals = ["horse", "dog", "bear", "cat", "dog"]
animal_count = animals.count("dog")
animals_index = animals.index("horse")
print(f"'horse' მდებარეობს პოზიციაზე {animals_index}.")
print(f"'dog' არის {animal_count}ჯერ.")
