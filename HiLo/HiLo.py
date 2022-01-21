import random
total = 300

def main():
    s = score()
    again = "y"
    print(f"Your beginning score is {total}")

    while again == "y":
        print()
        f_num = card("The", "is")
        HL = input("Higher or Lower? [h/l] ")
        s_num = card("Next", "was")
        s.score_fun(f_num, s_num, HL)
        print()
        again = input("Play again? [y/n] ")

    print()
    print(f"Thank you for playing. Your final score is {total}")


def card(a,b):
    R_num = random.randint(1,13)
    print(f"{a} card {b}: {R_num}")

    return R_num


# def score(f_num, s_num, HL):
#     global total
#     if HL == "h":
#         if f_num < s_num:
#             total += 100
#         else:
#             total -= 75
#     elif HL == "l":
#         if f_num > s_num:
#             total += 100
#         else:
#             total -= 75
#     else:
#          print("You did not type the right letter")

#     print(f"Your score is {total}")

#     return total



class score:

    def __init__(self):
        pass

    def score_fun(self, f_num, s_num, HL):
        global total
        if HL == "h":
            if f_num < s_num:
                total += 100
            else:
                total -= 75
        elif HL == "l":
            if f_num > s_num:
                total += 100
            else:
                total -= 75
        else:
                print("You did not type the right letter")

        print(f"Your score is {total}")

        return total




if __name__ == "__main__":
    main()