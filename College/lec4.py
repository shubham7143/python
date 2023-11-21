class India:
    def capital(self):
        print("New-Delhi")
    
    def language(self):
        print("Hindi and English")
    

class USA:
    def capital(self):
        print("Washinton D.C.")

    def language(self):
        print("English")



obj_Ind = India()
obj_usa = USA()

for country in (obj_Ind, obj_usa):
    country.capital()
    country.language()