import random
import datetime

num_alph= 26
num_all_chr = 10
num_abs_chr = 2
num_try = 2

def shutudai(alphabet):
    all_chr= random.sample(alphabet,num_all_chr)
    print("対象文字: ",end="")

    for c in all_chr:
        print(c,end=" ")
    print()

    abs_chr = random.sample(all_chr,num_abs_chr)
    print("表示文字: ",end="")

    for c in all_chr:
        if c not in abs_chr:
            print(c,end=" ")
    print()
    
    print("デバック用欠損文字: ",end="")
    print()
    return abs_chr

def kaito(ans):
    st=datetime.datetime.now()
    num = int(input("欠損文字はいくつあるでしょう？"))
    if num != num_abs_chr:
        print("残念... もう一度数えましょう")

    else:
        print("正解！！！　では、欠損している文字を1つずつ入力してください。")
        
        for i in range(num):
            chr=input(f"{i+1}文字を入力してください。")
            if chr not in abs_chr:
                print("残念、また挑戦してください。")
                return False

            else:
                ans.remove(chr)
        
        else:
            ed=datetime.datetime.now()
            print(str((ed-st).seconds)+str("秒"))
            print("欠損文字も含めて正解です！！！") 
            return True
    return False        

        


if __name__ == "__main__":
    alphabet = [chr(i+65) for i in range(num_alph)]
    abs_chr=shutudai(alphabet)
    for c in range(num_try):
        abs_chr = shutudai(alphabet)

        ret=kaito(abs_chr)
        
        if ret:
            break

        else:
            print("-"*20)