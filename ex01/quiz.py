import random

quiz=[("問題：サザエさんの旦那の名前は？"),
      ("問題：カツオの妹の名前は？"),
      ("問題：タラオはカツオから見てどんな関係？")]

ans=[("ますお","マスオ"),
     ("わかめ","ワカメ"),
     ("おい","甥","おいっこ","甥っ子")]

print(random.choice(quiz))

user_ans=input("回答は？：")
if user_ans in ans:
    print("正解！！！")
else:
    print("残念...")

