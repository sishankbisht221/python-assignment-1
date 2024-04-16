class BMI:
    def init(self):
        self.bmi = 0
        
    def bmi_calc(self, height, weight):
        self.height = height
        self.weight = weight
        self.bmi = self.weight / (self.height * self.height)
        
        if self.bmi < 18.5:
            print("Offo! You are underweight \n Eat some fruits")
        
        elif 18.5 <= self.bmi < 25.0:
            print("Congratulations! You are under Healthy Weight")
            
        elif 25.0 <= self.bmi < 30.0:
            print("Overweight!!!\n Eat a little less and do some exercise")
            
        elif self.bmi >= 30.0:
            print("Obesity!!!\n Hey you Fatty Guy \n Eat some healthy foods, not Pizza Burger all the time \n Go to the gym otherwise you will become a Watermelon-Man")
        
        else:
            print("Error")

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))
person_bmi = BMI()
person_bmi.bmi_calc(height, weight)
print(f"Your Body Mass Index is: {person_bmi.bmi}")
