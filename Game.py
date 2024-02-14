import random
import game_database
import os
score=0
def display_account_info(account):
    name=account['name']
    description=account['description']
    country=account['country']
    return f" {name} , a {description} ,from {country} "
def check_answer(guess,followers_count1,followers_count2):
    if followers_count1<followers_count2:
        if guess==1:
            #return guess==2 it also works
            return False
        else :
            return True
    else:
        if guess==1:
            return True
        else:
            return False
account2=random.choice(game_database.dataset)
continue_flag=True
while continue_flag:
    account1=account2
    account2=random.choice(game_database.dataset)
    while account1==account2:
        account2=random.choice(game_database.dataset)
    print(f"compare 1:{display_account_info(account1)}")
    print("***********VS************")
    print(f"compare2: {display_account_info(account2)}")
    guess=int(input("who has more followers....type 1 or 2:"))
    followers_count1=account1['follower_count']
    followers_count2=account2['follower_count']
    is_correct=check_answer(guess,followers_count1,followers_count2)
    os.system('cls')
    if is_correct==True:
        score+=1
        print(f" you are right... your score is {score}")
    else:
        print(f"you are wrong...your score is {score}")
        continue_flag=False
