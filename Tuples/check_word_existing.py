words = input("Въведи думите, които искаш да се съдържат в кортежа: ")
my_tuple = tuple(map(str, words.split()))
word_of_existing = input("Въведете думата, която искате да проверите дали е в кортежа: ")

if word_of_existing in my_tuple:
    print("Тази дума я има в кортежа!")
else:
    print("Избраната дума от вас я няма в кортежа!")