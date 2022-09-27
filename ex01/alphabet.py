import random
import datetime

num_alph = 26
num_all_chr = 10
num_abs_chr = 2
num_try = 2

def shutudai(alphabet):
    all_chr = random.sample(alphabet,num_all_chr)
    print("対象文字: ",end="")

    for c in (all_chr):
        print(c,end=" ")

    abs_chr = random.sample(all_chr,num_abs_chr)
    print()

if __name__ == "__main__":
    alphabet = [chr(i+65) for i in range(num_alph)]
    shutudai(alphabet)