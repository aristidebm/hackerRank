# Time in World
# 1. Je recupere l'heure et la minute dans deux variables.
# 2. Je definie une variable devant contenir resultats.
# 3. Je definie une transition suivant
#   + At minutes = 0 , use o' clock.
#   + For 0 < minutes <= 30, use past
#   + For minutes > 30  use to.
# 4. si la minutes > 30, j'incremente l'heure, je recupere la minute en utilisant 60 - minutes du dictonnaire mappant les date


def timeInWords(h, m):
    words = {
        0: "o' clock",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "quarter",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        # normal we can skip 21 - 29 but we don't have to manage the stuff of deducing
        21: "twenty one",
        22: "twenty two",
        23: "twenty three",
        24: "twenty four",
        25: "twenty five",
        26: "twenty six",
        27: "twenty seven",
        28: "twenty height",
        29: "twenty nine",
        30: "half",
    }

    hour = None
    minute = None
    transition = None

    if m > 30:
        hour = words[h + 1]
        minute = words[60 - m]
        min_ = "minutes" if 60 - m > 1 else "minute"
        transition = f"{min_} to" if 60 - m not in (15, 30) else "to"
    elif 0 <= m <= 30:
        hour = words[h]
        minute = words[m]
        min_ = "minutes" if m > 1 else "minute"
        transition = f"{min_} past" if m not in (15, 30) else "past"

    return f"{hour} {minute}" if m == 0 else f"{minute} {transition} {hour}"
