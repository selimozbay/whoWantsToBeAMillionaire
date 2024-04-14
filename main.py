# Who Wants to Be a Millionaire

"""
("**** ****** **** *** ** **** **** ****?", --> question
         "*****", --> correct answer
         "****", --> incorrect answer
         "****", --> incorrect answer
         "****") --> incorrect answer
"""

import os
import time
import random
import questions as qs

# all questions

lifelines = ["Fifty-Fifty", "Phone a Friend", "Ask the Audience"]
questions_n_and_v = {
    1: 100,
    2: 200,
    3: 300,
    4: 500,
    5: 1000,
    6: 2000,
    7: 4000,
    8: 8000,
    9: 16000,
    10: 32000,
    11: 64000,
    12: 125000,
    13: 250000,
    14: 500000,
    15: 1000000,
}

question_times = {
    1: 15,
    2: 15,
    3: 15,
    4: 15,
    5: 15,
    6: 30,
    7: 30,
    8: 30,
    9: 45,
    10: 45,
    11: -1,
    12: -1,
    13: -1,
    14: -1,
    15: -1,
}

episode = 0
go_on = False
prize_money = 0


# print question numbers and values
def print_q_and_v(e):
    z = ""
    j = ""
    for x, y in questions_n_and_v.items():
        if len(str(x)) == 1:
            z = " " + str(x)
        else:
            z = x

        if e > x:
            j = str(y) + " ✓"
        elif e == x:
            j = str(y) + " ←--"
        else:
            j = str(y)

        if x in {2, 5, 10, 15}:
            j += "  Guaranteed"
        print(str(z), "- £" + str(j))


def beginning():
    # print game title
    print("Who Wants to Be a Millionaire")

    # print question numbers and values
    print_q_and_v(episode)

    # print jokers
    print("\nLifelines")
    for i in lifelines:
        print(i, end=" / ")


while True:

    beginning()

    shall_go_on = input("\n\nDo you wanna start? e/h")
    if shall_go_on in {"e", "h\n"}:
        if shall_go_on == "e":
            episode = 1
            go_on = True
        else:
            os.system('cls||clear')
            print("Bye")
            episode = 0
            go_on = False
        break
    else:
        print("Incorrect input!")
        continue


def print_question(q, o, o2, ):
    print(q)
    for m, n in enumerate(o):
        print(n, o2[m])


def ask_question(x):
    answer = ""
    options = set()
    opt_k = ["A) ", "B) ", "C) ", "D) "]
    opt_v = list()

    print("\nQuestion", str(episode), "- £" + str(questions_n_and_v[x]))

    # get random question number from pool
    rdn_question = random.randint(0, len(qs.questions[x - 1]) - 1)

    # define the question
    question = qs.questions[x - 1][rdn_question][0]

    for j in range(1, 5):
        options.add(qs.questions[x - 1][rdn_question][j])

    for k in options:
        opt_v.append(k)

    # define true choice
    answer = qs.questions[x - 1][rdn_question][1]

    question_time = question_times[x]

    if question_time != -1:
        while True:
            os.system('cls||clear')

            print("Left Time: ", question_time)
            print_question(question, opt_k, opt_v)

            time.sleep(1)
            question_time -= 1
            if question_time == 0:
                os.system('cls||clear')
                print("Game over. You win £", prize_money)
    else:
        print_question(question, opt_k, opt_v)


while go_on:
    os.system('cls||clear')
    print_q_and_v(episode)

    ask_question(episode)
    break
