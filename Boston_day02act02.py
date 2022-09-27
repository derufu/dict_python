#Delf Carl Boston
print("======INPUT PAYSLIP=======")
print('Employee Name:')
name = input()
print('Enter Number of hour:')
number_of_hours = input()
print('SSS Contribution:')
sss_contribution = input()
print('PhilHealth:')
phil_health = input()
print('Housing Loan:')
housing_loan = input()

rate = 500
tax = 500

gross_salary = int(number_of_hours) * int(rate)
print("======PAY PAYSLIP==========")
print("======EMPLOYEE INFO========")
print("Employee name : " + name.upper())
print("Rendered Hour : " + number_of_hours)
print("Rate per hour : " + str(rate))
print("Gross Salary : " + str(gross_salary))
print("=====SALARY DEDUCTIONS=====")
print("SSS : " + sss_contribution)
print("PhilHealth : " + phil_health)
print("Housing : " + housing_loan)
total_deduction = int(sss_contribution) + int(phil_health) + int(housing_loan) + int(tax)
print("Total Deductions : " + str(total_deduction))
net_salary = gross_salary - total_deduction
print("Net Salary : " + str(net_salary))