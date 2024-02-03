from pathlib import Path

def total_salary(path):
    """Arg. -> path to file.txt, return -> total_amount, number_of_emploees, average_salary"""
    try:                                                                        #check path errors
        path = Path(path).absolute()
        if path.is_file:                                                        #check if path is file
            if path.suffix == ".txt":                                           #check if file is .txt
                try:                                                            #check file opening errors
                    with open(path, "r", encoding="utf-8") as fh:
                        total_amount = 0
                        number_of_emploees = 0
                        for el in fh.readlines():
                            total_amount += float(el.split(",")[1])
                            number_of_emploees += 1
                        average_salary = total_amount / number_of_emploees
                        return total_amount, number_of_emploees, average_salary
                except Exception as e:
                    return print(e)
            else:
                return print(f"The '{path}' is not a '.txt' file")
        else:
            return print(f"The '{path}' is not a file")
    except Exception as e:
        return print(e)

total_salary("salary_calculation.py")
total_salary("salary.txt")
total_amount, number_of_emploees, average_salary = total_salary("salary_info.txt")
print(f"Salary total amount: {total_amount}, Number of emploees: {number_of_emploees}, Avg. salary: {average_salary}")
