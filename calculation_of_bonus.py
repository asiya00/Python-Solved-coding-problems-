class Employee:
    def __init__(self, employee_name, designation, salary, overTimeContribution):
        self.employee_name = employee_name
        self.designation = designation
        self.salary = salary
        self.overTimeContribution = overTimeContribution
        self.overTimeStatus = False


class Organization:
    def __init__(self, employee_list):
        self.employee_list = employee_list

    def check_eligibility(self, overtime_threshold):
        for i in self.employee_list:
            totalhrs = sum(i.overTimeContribution.values())
            if totalhrs > overtime_threshold:
                i.overTimeStatus = True

    def bonus_amount_paid(self, rate_per_hour):
        total_bonus = 0
        for i in self.employee_list:
            if i.overTimeStatus:
                totalhrs = sum(i.overTimeContribution.values())
                total_bonus += (totalhrs*rate_per_hour)
        return total_bonus


if __name__ == "__main__":
    t = int(input())
    employees = []
    for i in range(t):
        employee_name = input()
        designation = input()
        salary = int(input())
        count_months = int(input())
        overTimeContribution = {}
        for i in range(count_months):
            month = input().lower()
            hours = int(input())
            overTimeContribution[month] = hours
        e = Employee(employee_name, designation, salary, overTimeContribution)
        employees.append(e)
    o = Organization(employees)
    overtime_threshold = int(input())
    o.check_eligibility(overtime_threshold)
    rate_per_hour = int(input())

    for obj in employees:
        print(obj.employee_name, obj.overTimeStatus)

    print(o.bonus_amount_paid(rate_per_hour))


# 5
# Sunita
# Faculty
# 23000
# 4
# jan
# 4
# March
# 6
# apr
# 6
# June
# 3
# Arun
# Admin
# 30000
# 3
# jan
# 4
# March
# 6
# apr
# 6
# Dipak
# Admin
# 25000
# 3
# jan
# 4
# March
# 6
# apr
# 6
# Balen
# HR
# 12000
# 3
# jan
# 4
# March
# 6
# apr
# 6
# Tarun
# HR
# 78000
# 3
# jan
# 4
# March
# 6
# apr
# 6
# 30
# 100

# 5
# Sunita
# Faculty
# 23000
# 2
# jan
# 4
# March
# 6
# Arun
# Admin
# 30000
# 3
# Feb
# 4
# March
# 12
# June
# 10
# Dipak
# Admin
# 25000
# 3
# Jan
# 12
# July
# 5
# Aug
# 3
# Balen
# HR
# 12000
# 3
# Jan
# 12
# July
# 5
# Aug
# 3
# Tarun
# HR
# 78000
# 3
# Jan
# 12
# July
# 5
# Aug
# 3
# 18
# 100

