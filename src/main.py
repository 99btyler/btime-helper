

def get_int(question):
    answer = 0
    while True:
        try:
            answer = int(input(question))
            break
        except ValueError:
            continue # ask again
    return answer


column = input("column: ")

row_start = int(input("row_start: "))
row_end = int(input("row_end: "))
string = ""
for i in range(row_start, row_end+1):
    string += f"{column}{i}+"
print(string[:-1])

rows_good = [row.strip() for row in input("rows_good (separated by comma): ").split(",")]
string = ""
for row in rows_good:
    string += f"{column}{row}+"
print(string[:-1])