#  Copyright (c) 2024.

# Who Wants to Be a Millionaire

"""
("**** ****** **** *** ** **** **** ****?", --> question
         "*****", --> correct answer
         "****", --> incorrect answer
         "****", --> incorrect answer
         "****") --> incorrect answer
"""

import os
import random

import questions as qs

# all questions

lifelines_org = ['1 Fifty-Fifty', '2 Phone a Friend', '3 Ask the Audience']
lifelines = list()

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

episode = 0
go_on = False
prize_money = 0
g_prize_money = 0


# print question numbers and values
def print_q_and_v(e):
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
    global lifelines
    # print game title
    print(
        "______Who Wants to Be a Millionaire______\nMake choice (a, b, c, d)\nGet lifelines (1, 2, 3)\nLeave with prize (q)\n")

    lifelines = lifelines_org
    # print question numbers and values
    print_q_and_v(episode)

    # print jokers
    print("\nLifelines")
    for i in lifelines_org:
        print(i)


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
            prize_money = 0
            lifelines = []
            go_on = False
        break
    else:
        print("Incorrect input!")
        continue


def print_question(q, o, o2):
    print(q)
    for m, n in enumerate(o):
        print(n, o2[m])


def ask_question(x):
    global go_on, episode, prize_money, g_prize_money
    answer = ""
    answer_key = ""
    options = set()
    options_k = ["A) ", "B) ", "C) ", "D) "]
    options_v = list()

    print("\nQuestion", str(episode), "- £" + str(questions_n_and_v[x]))

    # get random question number from pool
    rdn_question = random.randint(0, len(qs.questions[x - 1]) - 1)

    # define the question
    question = qs.questions[x - 1][rdn_question][0]

    for j in range(1, 5):
        options.add(qs.questions[x - 1][rdn_question][j])

    for k in options:
        options_v.append(k)

    # define true choice
    answer = qs.questions[x - 1][rdn_question][1]

    answer_key = options_k[options_v.index(answer)][0].lower()

    available_choices = [answer.lower(), "a", "b", "c", "d", "q", "1", "2", "3"]

    os.system('cls||clear')

    print_question(question, options_k, options_v)

    while True:
        user_answer = input("Make a choice: ").lower()

        if user_answer in available_choices:
            # 50-50
            if user_answer == "1":
                deleted_choices = 0

                while deleted_choices != 2:

                    rdn = random.randint(0, len(options_v) - 1)
                    if options_v[rdn] != answer:
                        options_v.pop(rdn)
                        options_k.pop(rdn)
                        deleted_choices += 1

                lifelines.remove('1 Fifty-Fifty')
                available_choices.remove("1")
                print_question(question, options_k, options_v)
            # phone a friend
            elif user_answer == "2":
                if random.randint(0, 100) > 75:
                    y = 0
                    while y < 1:
                        v = random.randint(0, len(options_v) - 1)
                        if options_v[v] != answer:
                            print("Your friend's answer is: ", options_v[v])
                            y += 1
                            break
                else:
                    print("Your friend's answer is: ", answer)

                lifelines.remove('2 Phone a Friend')
                available_choices.remove("2")
            # ask the audience
            elif user_answer == "3":
                r1 = random.randint(0, 100)
                r2 = random.randint(0, 100 - r1)
                r3 = random.randint(0, 100 - r1 - r2)
                r4 = 100 - r3 - r2 - r1

                a = "A) "
                for _ in range(r1):
                    a += "|"
                a += "   %" + str(r1)
                print(a)

                b = "B) "
                for _ in range(r2):
                    b += "|"
                b += "   %" + str(r2)
                print(b)

                c = "C) "
                for _ in range(r3):
                    c += "|"
                c += "   %" + str(r3)
                print(c)

                d = "D) "
                for _ in range(r4):
                    d += "|"
                d += "   %" + str(r4)
                print(d)

                lifelines.remove('3 Ask the Audience')
                available_choices.remove("3")
            # true answer
            if user_answer in {answer_key, answer}:
                os.system('cls||clear')
                print("Congratulations correct answer! You earned £", questions_n_and_v[x], "Let's keep going.")
                if episode in {2, 5, 10, 15}:
                    print("£", questions_n_and_v[x], "guaranteed.")
                    g_prize_money = questions_n_and_v[x]
                prize_money = questions_n_and_v[x]
                episode += 1
                ask_question(episode)
                if episode == 16:
                    os.system('cls||clear')
                    print("Congratulations, you won the big prize!")
                    break
            else:
                os.system('cls||clear')
                print("Unfortunately wrong answer!\nAnswer is", answer, "\nYou won £", g_prize_money)
                break

        else:
            print("Incorrect input")
            continue


while go_on:
    os.system('cls||clear')
    print_q_and_v(episode)

    ask_question(episode)
    break
