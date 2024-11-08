#Part 1
class Patient:
    def __init__(self, name, age, diagnosis):
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_diagnosis(self):
        return self.diagnosis
    def set_name(self,name):
        self.name = name
    def set_age(self,age):
        self.age = age
    def set_diagnosis(self,diagnosis):
        self.diagnosis = diagnosis
def main():
    patient = Patient("John Doe", 35, "Hypertension")
    print(f"Patient's name: {patient.get_name()}, Age: {patient.get_age()}, Diagnosis: {patient.get_diagnosis()}")
    patient.set_name("Jane Doe")
    patient.set_age(42)
    patient.set_diagnosis("Diabetes")
    print(f"Updated patient information - Name: {patient.get_name()}, Age: {patient.get_age()}, Diagnosis: {patient.get_diagnosis()}")
main()