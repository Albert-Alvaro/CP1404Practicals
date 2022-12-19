from prac_07.project import Project

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""
projects = []
class_projects = []


def main():
    with open("projects.txt", "r", encoding="utf-8-sig") as in_file:
        data = in_file.readlines()
        extract_data(data)
        add_to_class()
        # choice = get_choice()
        # while choice != "Q":
        #     if choice == "L":
        #         pass
        #     elif choice == "S":
        #         pass
        #     elif choice == "D":
        #         pass
        #     elif choice == "F":
        #         pass
        #     elif choice == "A":
        #         pass
        #     elif choice == "U":
        #         pass
        #     else:
        #         print("Invalid Choice")
        #     choice = get_choice()


def add_to_class():
    for project in projects:
        class_projects.append(Project(project[0], project[1], int(project[2]), float(project[3]), int(project[4])))


def get_choice():
    print(MENU, end="\n")
    choice = input(">>>").upper()
    return choice


def extract_data(data):
    for line in data[1:]:
        items = line.strip().split("\t")
        projects.append(items)


main()

