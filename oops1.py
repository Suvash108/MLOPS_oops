class employee:
    def __init__(self) :
        print("started executing attributes/data")
        self.id = 1245
        self.salary= 1000000000000000000
        self.designation="CEO"
        print("attributes/data are being initalize")

#creating an object
    def travel(self, destination):
        print("this travel funciton is called manually")
        print(f"employee is travelling to {destination}")

sam=employee()
sam.travel("kerala")

# print(sam.salary)


# class student:
#     def __init__(self) :
#        self.department="cse"
#        self.roll=1

# suvash=student()

# print(suvash.department)