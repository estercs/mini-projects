import random
num = random.randint(1, 6)
text = input("Você deseja rodar o dado? 1(sim)/0(não) ")
while text == "1":
    print(num)
    text = input("Deseja continuar? 1(sim)/0(não) ")
    num = random.randint(1, 6)
