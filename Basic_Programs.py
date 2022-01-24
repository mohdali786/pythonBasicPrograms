#birth_year=int(input())
#urrent_year=int(input())
#your_age=current_year-birth_year
#print(your_age)

#2nd program
##first_name=str(input("enter firstname: "))
#middle_name=str(input("enter middlename: "))
##last_name=str(input("enter lastname: "))
#print(first_name+ middle_name+last_name)
#3rd program
#def location():
    #street=str(input())
   # city=str(input())
  #  country=str(input())
 #   print(street+
 #         " \n" +city +"\n"+country)
#location()
 #4 program
#string="Earth revolve around the sun"
#print(string[6:13])
#print(string[-4:])

#5 program
#fruits=int(input())
#vegetables=int(input())
#print("I eat ",vegetables,"veggies","and",fruits,"fruits daily")

#6 program
#s="200 banana eaten"
#s1=s.replace(s,"10 samosa")
#print(s1)

#7 program
def calculate_sugar_level():
    sugar_level=int(input())
    if sugar_level in range(80,100):
        print("normal")
    elif sugar_level<80:
        print("low")
    else:
        print("high")

calculate_sugar_level()
