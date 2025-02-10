from difflib import SequenceMatcher

with open("test_file1.txt") as file1 , open("test_file2.txt") as file2 :

    f1data=file1.read()
    f2data=file2.read()

    percentage = SequenceMatcher(None,f1data,f2data).ratio()

    print(f"{percentage * 100}%")

