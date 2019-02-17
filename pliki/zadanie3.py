import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', "--input", help='input file',
                    action="store")
parser.add_argument('-o', "--output", help='output file',
                    action="store")

args = parser.parse_args()

cleaned_emails = set()

with open(args.input) as f:
    for line in f:
        line = line.strip().lower()
        if line.count("@") == 1:
            cleaned_emails.add(line)

with open(args.output, 'w') as f:
    for emails in cleaned_emails:
        f.write(emails + "\n")


# print(args.input)
# print(args.output)
#
# try:
#     f_name = sys.argv[1]
# except IndexError:
#     print("Nie podałeś nazwy pliku")
#     exit()
#
# email_list=[]
#
# try:
#     with open(f_name) as f:
#         for line in f:
#             for znak in line:
#                 if znak == "@":
#                 email_list += line.lower()


# except FileNotFoundError:
# print("Nie ma takiego pliku")
