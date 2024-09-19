# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".

def LCG(input_string: list[str]):
    """ Longest Common String takes only list as in put and outputs a non formatted string"""

    empty_list= []

    # for _ in input_string:


    check_holder =[]
    string_counter =0
    for n in range(len(input_string)):
        for s in input_string:
            for p in s:

                if p in input_string:
                    string_counter +=1
    print(string_counter)
    # falling asslep just trung to slpit up the input list in to a list of every charactor
    # please finish tomorow
    # find the greatest common string

print(LCG(["hello", "leetCode"]))
