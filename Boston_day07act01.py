import random
fname = ("Iram", "Logan", "Margaret", "Mark", "Sami", "Ibraheem", "Mahamed", "Can", "Leighton", "Findlay")
mname = ("A","B","C","D","E","F","G","H","I")
lname = ("Mcmanus", "Felix", "Calhoun", "Quinn", "Moore", "Webber", "Goddard", "Neill", "Snow", "Dolan")
def run():
    q = input(f"Do you want to generate a name? : ")
    yes = "yY"
    no = "nN"
    if q in yes:
        _random = random.randrange(0,10)
        print("Congratulations! Your new name: " + fname[_random]+" - where newname is the new full name "+ lname[_random]+", "+fname[_random]+" "+mname[_random])
        run()
    if q in no:
        print("Thank you!" , fname, mname, lname)
run()

