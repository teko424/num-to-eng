def two_digits(n):
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    nums_2 = ["twen", "thir", "for", "fif", "six", "seven", "eigh", "nine"]
    uniqteens = ["ten", "eleven", "twelve"]
    teens = ["thir", "four", "fif", "six", "seven", "eigh", "nine"]
    if str(n)[0] == "1":
        if str(n)[1] == "0" or str(n)[1] == "1" or str(n)[1] == "2":
            return uniqteens[int(str(n)[1])]
        else:
            return teens[int(str(n)[1]) - 3] + "teen"
    else:
        if str(n)[1] == "0":
            return f"{nums_2[int(str(n)[0]) - 2]}ty"
        else:
            return f"{nums_2[int(str(n)[0]) - 2]}ty {nums[int(str(n)[1])]}"


def num_to_eng(n):
    onedigit = 0
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    if len(str(n)) == 1:
        print(nums[n])
    elif len(str(n)) == 2:
        if len(str(n)) == 2:
            print(two_digits(n))
    elif len(str(n)) == 3:
        if str(n)[1] == "0":
            if str(n)[2] != "0":
                print(nums[int(str(n)[0])] + " hundred", nums[int(str(n)[2])])
            else:
                print(nums[int(str(n)[0])] + " hundred")
        else:
            print(nums[int(str(n)[0])] + " hundred", two_digits(int(str(n)[-2:])))


if __name__ == "__main__":
    while 1:
        try:
            q = int(input("type a number between 0 and 999: "))
            if 0 <= q <= 999:
                num_to_eng(q)
            else:
                print("the number must be between 0-999")
        except ValueError:
            print("please type only a number, nothing else")
