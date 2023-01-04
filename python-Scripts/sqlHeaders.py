import csv
import readline
import sys

readline.set_completer_delims(" \t\n=")
readline.parse_and_bind("tab: complete")

def csvOpen(file):

    with open(file, 'r', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        i = next(reader)
        dRows = sum(1 for line in reader)
        print(f"\nYou have {dRows} rows in the CSV file.\n" f"Your headers are:\n{', '.join(map(str.capitalize, i))}")


if len(sys.argv) > 1:
    file = sys.argv[1]
else:
    file = input("Please enter the filename to show the CSV headers: ")
csvOpen(file)
