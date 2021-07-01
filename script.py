class Patient:
  def __init__(self, name, age, sex, bmi, num_of_children, smoker):
    self.name = name
    self.age = age
    self.sex = sex
    self.bmi = bmi
    self.num_of_children = num_of_children
    self.smoker = smoker

# First method to estimate patient insurance cost.
  def estimated_insurance_cost(self):
    estimated_cost = 250*self.age - 128*self.sex + 370*self.bmi + 425*self.num_of_children + 24000*self.smoker - 12500
    print(self.name + "’s estimated insurance costs is " + str(estimated_cost) + " dollars.".format(self.name, estimated_cost))

# Second method for update age and recalculate insurance cost.
  def update_age(self, new_age):
    self.age = new_age
    print(self.name + " is now " + str(self.age) + " years old.".format(self.name, self.age))
    self.estimated_insurance_cost()

# Third method for update of number of children.
  def update_num_of_children(self, new_num_of_children):
    self.num_of_children = new_num_of_children
# Control flow for correct grammer child/children.
    if self.num_of_children > 1:
      print(self.name + " has " + str(self.num_of_children) + " children.")
    else:
      print(self.name + " has " + str(self.num_of_children) + " child.")
    self.estimated_insurance_cost()

# Method for updating patience bmi and recalculating insurance cost.
  def update_bmi(self, new_bmi):
    self.bmi = new_bmi
    print(self.name + " BMI is " + str(self.bmi))
    self.estimated_insurance_cost()
  
# Method for storing patience info in var using dict.
  def patient_profile(self):
    patient_information = {}
    patient_information["Name"] = self.name
    patient_information["Age"] = self.age
    patient_information["Sex"] = self.sex
    patient_information["BMI"] = self.bmi
    patient_information["Number of Children"] = self.num_of_children
    patient_information["Smoker"] = self.smoker
    return patient_information

# Patient 1 info 
patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)

# Testing that the __init__ is functioning.
print(patient1.name)
print(patient1.age)
print(patient1.sex)
print(patient1.bmi)
print(patient1.num_of_children)
print(patient1.smoker)

# Testing insurance cost method
print(patient1.estimated_insurance_cost())

# Testing update age method
print(patient1.update_age(26))

# Testing update of number of children method
print(patient1.update_num_of_children(1))

# Testing update BMI.
print(patient1.update_bmi(25))

# Testing patient profile.
print(patient1.patient_profile())