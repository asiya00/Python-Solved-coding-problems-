class Employee:
	def __init__(self, employee_name, designation_type, salary):
		self.employee_name = employee_name
		self.designation_type = designation_type
		self.salary = salary
		self.overTimeContribution = overTimeContribution
		self.overTimeStatus = overTimeStatus

	class Organization(Employee):
		def __init__(self, employee_list):
			self.employee_list = employee_list

		def overtimestatus(self, overtimethreshold):
			for i in self.employee_list:
				if int(sum(i.overTimeContribution.values())) >= overtimethreshold:
					i.overTimeStatus = True
			return self.employee_list

		def total_bonus(self, rate_per_hour):
			pass
			

