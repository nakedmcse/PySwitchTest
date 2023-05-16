# Python Switch Test (modified)

# Dan Sloans version with larger test cases and better timing

# Note: some of the changes I've made are my own idiosyncracies, that I changed before
# I thought about sharing this. Where a change is actually something of interest, I've
# written comments...
# The notes on code style/conventions...take it or leave it. Just informational. :-)

# idiosyncracy: i prefer to import specific functions, not whole modules. ;-) totally a personal pref.

# timeit is suuper useful for this sort of testing. https://docs.python.org/3/library/timeit.html
from timeit import timeit
# choice is a useful shorthand for what you did with randint. No idea if faster or slower but it avoids hardcoded
# list sizes, as it uses the testlist itself. Its possibly/probably slower than randint or randrange, but since it
# isn't part of the test itself and it's the same for all test cases, it doesn't really matter.
from random import choice as random_choice
# note: the as random_choice is just because I wanted to avoid name collision, but I'm too lazy to rename stuff

# Note; this is effectively a constant; in python convention is to make global constant names all upper case.
# define dictionary globally
SMALL_CASES = {
    "winter": "growing",
    "growing": "harvest",
    "harvest": "winter",
}

# Larger list of cases for testing how things change with more values
BIG_CASES = {
    "winter": "growing",
    "growing": "harvest",
    "harvest": "winter",
    "hello": "meep",
    "hello1": "meep21",
    "hello2": "meep20",
    "hello3": "meep19",
    "hello4": "meep18",
    "hello5": "meep17",
    "hello6": "meep16",
    "hello7": "meep15",
    "hello8": "meep14",
    "hello9": "meep13",
    "helloa": "meep12",
    "hellob": "meep11",
    "helloc": "meep10",
    "hellod": "meep9",
    "helloe": "meep8",
    "hellof": "meep7",
    "hellog": "meep6",
    "helloh": "meep5",
    "helloi": "meep4",
    "helloj": "meep3",
    "hellok": "meep2",
    "hellol": "meep1"
}


# Note I used snake case instead of camel case, as that's the convention in python
# ELIF Tree
def small_elif_tree(choice):
    if choice == "winter":
        return "growing"
    elif choice == "growing":
        return "harvest"
    elif choice == "harvest":
        return "winter"
    else:
        return "unknown"


def big_elif_tree(choice):
    if choice == "winter":
        return "growing"
    elif choice == "growing":
        return "harvest"
    elif choice == "harvest":
        return "winter"
    elif choice == "hello":
        return "meep"
    elif choice == "hello1":
        return "meep21"
    elif choice == "hello2":
        return "meep20"
    elif choice == "hello3":
        return "meep19"
    elif choice == "hello4":
        return "meep18"
    elif choice == "hello5":
        return "meep17"
    elif choice == "hello6":
        return "meep16"
    elif choice == "hello7":
        return "meep15"
    elif choice == "hello8":
        return "meep14"
    elif choice == "hello9":
        return "meep13"
    elif choice == "helloa":
        return "meep12"
    elif choice == "hellob":
        return "meep11"
    elif choice == "helloc":
        return "meep10"
    elif choice == "hellod":
        return "meep9"
    elif choice == "helloe":
        return "meep8"
    elif choice == "hellof":
        return "meep7"
    elif choice == "hellog":
        return "meep6"
    elif choice == "helloh":
        return "meep5"
    elif choice == "helloi":
        return "meep4"
    elif choice == "helloj":
        return "meep3"
    elif choice == "hellok":
        return "meep2"
    elif choice == "hellol":
        return "meep1"
    else:
        return "unknown"


# Dictionary
def small_dict_lookup(choice):
    global SMALL_CASES
    return SMALL_CASES.get(choice, "unknown")


def big_dict_lookup(choice):
    global BIG_CASES
    return BIG_CASES.get(choice, "unknown")


# Match
def small_match_test(choice):
    match choice:
        case "winter":
            return "growing"
        case "growing":
            return "harvest"
        case "harvest":
            return "winter"
        case _:
            return "unknown"


def big_match_test(choice):
    match choice:
        case "winter":
            return "growing"
        case "growing":
            return "harvest"
        case "harvest":
            return "winter"
        case "hello":
            return "meep"
        case "hello1":
            return "meep21"
        case "hello2":
            return "meep20"
        case "hello3":
            return "meep19"
        case "hello4":
            return "meep18"
        case "hello5":
            return "meep17"
        case "hello6":
            return "meep16"
        case "hello7":
            return "meep15"
        case "hello8":
            return "meep14"
        case "hello9":
            return "meep13"
        case "helloa":
            return "meep12"
        case "hellob":
            return "meep11"
        case "helloc":
            return "meep10"
        case "hellod":
            return "meep9"
        case "helloe":
            return "meep8"
        case "hellof":
            return "meep7"
        case "hellog":
            return "meep6"
        case "helloh":
            return "meep5"
        case "helloi":
            return "meep4"
        case "helloj":
            return "meep3"
        case "hellok":
            return "meep2"
        case "hellol":
            return "meep1"
        case _:
            return "unknown"


# extracting this out makes it easier to run the same set of tests with the variations.
# Possible expansion of the test:
#  - We could probably inline the whole function into the "timeit" statement and generate the testlist, CASES, and the
#    actual elif_tree/match_test functions completely dynamically, to test a variety of testlist sizes. But that's
#    a bit more work than I can be bothered with right now...although I'm very curious how things scale up into the
#    ridiculous number of lookup cases haha
def run_tests(cases, elif_tree, dict_lookup, match_test):
    testlist = [*cases.keys(), "notacase"]

    # extract this out so that it is consistent across all tests
    def pick_random_value():
        return random_choice(testlist)

    print("Testing ELIF tree...")
    elapsed = timeit(
        "elif_tree(pick_random_value())",
        number=10000000,
        globals={
            "elif_tree": elif_tree,
            "pick_random_value": pick_random_value
        }
    )
    print(f"Elapsed Time: {elapsed:.4f} seconds\n")

    print("Testing Dictionary Lookup using function...")
    elapsed = timeit(
        "dict_lookup(pick_random_value())",
        number=10000000,
        globals={
            "dict_lookup": dict_lookup,
            "pick_random_value": pick_random_value
        }
    )
    print(f"Elapsed Time: {elapsed:.4f} seconds\n")

    # this one showcases two things worth knowing in python:
    # 1. you can assign any callable (functions, class methods, builtins, anything) to another variable and then
    #    call it. In this case we assign the dict object's class method "get" to our dict_lookup variable, bypassing
    #    a function call and bypassing the 'dot' reference lookup. This is not very readable so normally a bad idea,
    #    but it demonstrates the idea.
    # 2. function calls can be expensive - by removing the dict_lookup() function and calling dict.get() directly, we
    #    get a decent speed up. You shouldn't sacrifice readability of course, but in some cases where the function is
    #    just a wrapper and doesn't do anything (like this case) it can make sense to "inline" things in this way.
    print("Testing Dictionary Lookup using dict get() directly...")
    elapsed = timeit(
        "dict_lookup(pick_random_value(), 'unknown')",
        number=10000000,
        globals={
            "dict_lookup": cases.get,
            "pick_random_value": pick_random_value
        }
    )
    print(f"Elapsed Time: {elapsed:.4f} seconds\n")

    print("Testing Match...")
    elapsed = timeit(
        "match_test(pick_random_value())",
        number=10000000,
        globals={
            "match_test": match_test,
            "pick_random_value": pick_random_value
        }
    )
    print(f"Elapsed Time: {elapsed:.4f} seconds\n")


print("\nStarting Switch Test\n")
print("\nSmall tests...\n")
run_tests(
    cases=SMALL_CASES,
    elif_tree=small_elif_tree,
    dict_lookup=small_dict_lookup,
    match_test=small_match_test,
)
print("\nBig tests...\n")
run_tests(
    cases=BIG_CASES,
    elif_tree=big_elif_tree,
    dict_lookup=big_dict_lookup,
    match_test=big_match_test,
)

# For reference, results I got on my M2 macbook:
#
# Starting Switch Test
#
#
# Small tests...
#
# Testing ELIF tree...
# Elapsed Time: 2.0478 seconds
#
# Testing Dictionary Lookup using function...
# Elapsed Time: 2.1180 seconds
#
# Testing Dictionary Lookup using dict get() directly...
# Elapsed Time: 1.9280 seconds
#
# Testing Match...
# Elapsed Time: 2.0914 seconds
#
#
# Big tests...
#
# Testing ELIF tree...
# Elapsed Time: 2.6609 seconds
#
# Testing Dictionary Lookup using function...
# Elapsed Time: 1.8051 seconds
#
# Testing Dictionary Lookup using dict get() directly...
# Elapsed Time: 1.6085 seconds
#
# Testing Match...
# Elapsed Time: 2.7672 seconds


# -------------
# The ELIF tree is pretty obvious; it has to work its way through the list of cases top-down, so the more cases there is
# the slower it will be.
#
# The dictionary lookup using a function is faster when there is more lookup cases; that's not surprising, as python's
# dict lookup is pretty fast and uses hashing to scale really well to larger sizes. Would be curious how big it needs
# to be before that starts to drop off and it gets slower again...assuming it does...
#
# I put the "using dict get() directly" in deliberately because I knew it would be faster. More of a difference than I
# expected though. I did some checks and almost all of the speedup comes from not calling dict_lookup(), but instead
# calling the get() directly. I had thought the speedup was going to be to do with skipping the "dot" reference, but
# further testing suggests its entirely to do with avoiding the extra function call. Not sure if that's related to the
# "global" statement or just the function call itself.
#
# The match surprised me. I thought I'd heard that it scaled up to larger numbers of cases really well, but it doesn't
# seem to. Since it behaves much like the if/elif block, it probably also has to sequentially execute the statement
# block until it finds a match.