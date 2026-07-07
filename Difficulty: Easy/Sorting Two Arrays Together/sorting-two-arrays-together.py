class Solution:
    def sortRecords(self, employee, salary):
        # code here
        paired = list(zip(salary, employee))
        paired.sort()
        sorted_employee = [name for salary, name in paired]
        return sorted_employee