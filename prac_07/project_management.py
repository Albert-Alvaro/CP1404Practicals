import datetime
from prac_07.project import Project

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""
class_projects = []
project_dictionary = {}


def main():
    with open("projects.txt", "r", encoding="utf-8-sig") as in_file:
        data = in_file.readlines()
        extract_data(data)
    choice = get_choice()
    while choice != "Q":
        if choice == "L":
            filename = input("Filename: ")
            input_file = open(f"{filename}.txt", "r")
            in_file = input_file.readlines()
            extract_data(in_file)
            input_file.close()
        elif choice == "S":
            filename = input("Filename: ")
            output_file = open(f"{filename}.txt", "w")
            print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=output_file)
            for project in class_projects:
                print(
                    f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}",
                    file=output_file)
            output_file.close()
        elif choice == "D":
            class_projects.sort()
            print("Incomplete Project: ")
            for project in class_projects:
                if not project.is_completed():
                    print(project)
            print("Completed Projects: ")
            for project in class_projects:
                if project.is_completed():
                    print(project)
        elif choice == "F":
            date_string = input('Show projects that start after date (dd/mm/yy): ')
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            sorted_filtered_projects = []
            sort_by_date(date, sorted_filtered_projects)
            for project in sorted_filtered_projects:
                print(project)
        elif choice == "A":
            print("Let's add a new project")
            name = input("Name: ")
            start_date = input("Start date (dd/mm/yy): ")
            priority = int(input("Priority: "))
            cost_estimate = float(input("Cost estimate: $"))
            completion_percentage = int(input("Percent complete: "))
            class_projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
        elif choice == "U":
            for i, project in enumerate(class_projects, 0):
                print(
                    f"{i} {project.name}, start:{project.start_date}, priority {project.priority}, estimate: ${project.cost_estimate}, completion: {project.completion_percentage}% ")
                project_dictionary[i] = project
            project_choice = int(input("Project choice: "))
            print(project_dictionary[project_choice])
            new_percentage = int(input("New Percentage: "))
            new_priority = int(input("New Priority: "))
            class_projects[project_choice] = Project(class_projects[project_choice].name,
                                                     class_projects[project_choice].start_date, int(new_priority),
                                                     float(class_projects[project_choice].cost_estimate),
                                                     int(new_percentage))
        else:
            print("Invalid Choice")
        choice = get_choice()
    print("Thank you for using custom-built project management software.")


def sort_by_date(date, sorted_filtered_projects):
    filtered_projects = []
    filtered_dates = []
    for project in class_projects:
        if project.compare_date(date):
            filtered_projects.append(project)
    for project in filtered_projects:
        filtered_dates.append(project.start_date)
    for date in sorted(filtered_dates):
        for project in filtered_projects:
            if date == project.start_date:
                sorted_filtered_projects.append(project)


def get_choice():
    print(MENU, end="\n")
    choice = input(">>>").upper()
    return choice


def extract_data(data):
    projects = []
    for line in data[1:]:
        items = line.strip().split("\t")
        projects.append(items)
    for project in projects:
        class_projects.append(Project(project[0], project[1], int(project[2]), float(project[3]), int(project[4])))


main()
