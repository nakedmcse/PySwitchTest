# Python Switch Test
import time
import random

# ELIF Tree
def elifTree(choice):
    if choice == "winter":
        return "growing"
    elif choice == "growing":
        return "harvest"
    elif choice == "harvest":
        return "winter"
    else:
        return "unknown"

# Dictionary
def dictLookup(choice):
    global cases
    return cases.get(choice,"unknown")

# Match
def matchTest(choice):
    match choice:
        case "winter":
            return "growing"
        case "growing":
            return "harvest"
        case "harvest":
            return "winter"
        case _:
            return "unknown"

# Main
testlist = ["winter","growing","harvest","notacase"]

# define dictionary globally
cases = {
        "winter": "growing",
        "growing": "harvest",
        "harvest": "winter"
}

print()
print("Starting Switch Test")
print()

start_time_elif = time.time()
print("Testing ELIF tree")
for i in range(1,10000000):
    choiceELIF = random.randint(0,3)
    retval = elifTree(testlist[choiceELIF])
end_time_elif = time.time()
elapsed_elif = end_time_elif - start_time_elif
print(f"Elapsed Time: {elapsed_elif:.4f} seconds")
print()

start_time_dict = time.time()
print("Testing Dictionary Lookup")
for i in range(1,10000000):
    choiceDICT = random.randint(0,3)
    retval = dictLookup(testlist[choiceDICT])
end_time_dict = time.time()
elapsed_dict = end_time_dict - start_time_dict
print(f"Elapsed Time: {elapsed_dict:.4f} seconds")
print()

start_time_match = time.time()
print("Testing Match")
for i in range(1,10000000):
    choiceMATCH = random.randint(0,3)
    retval = matchTest(testlist[choiceMATCH])
end_time_match = time.time()
elapsed_match = end_time_match - start_time_match
print(f"Elapsed Time: {elapsed_match:.4f} seconds")
print()