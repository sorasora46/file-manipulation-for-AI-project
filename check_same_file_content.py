
def compare_files(file1_path, file2_path):
    try:
        number_diff = 0
        with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
            lines1 = file1.readlines()
            lines2 = file2.readlines()

            for i, (line1, line2) in enumerate(zip(lines1, lines2), start=1):
                if line1 != line2:
                    print(f"Difference found at line {i}:")
                    print(f"{file1_path}: {line1.strip()}")
                    print(f"{file2_path}: {line2.strip()}\n")
                    number_diff += 1

            if len(lines1) != len(lines2):
                print("The number of lines in the files is different.")

            return lines1 == lines2, number_diff

    except FileNotFoundError:
        print("One or both files not found.")
        return False


# Example usage
file1_path = 'classified_target_species.txt'
file2_path = 'verify.txt'

is_file_same, no_diff = compare_files(file1_path, file2_path)

if is_file_same:
    print("The contents of the files are the same.")
else:
    print("The contents of the files are different.")
    print("number of different:", no_diff)

#132 non_venomous
#39 venomous