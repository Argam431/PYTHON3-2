class Employees:
    def __init__(self,fs_name:str,ls_name:str,ph_num = None,salary = 200000,gender = 'M'):
        self.first_name = fs_name
        self.last_name = ls_name
        self.phone_number = ph_num
        self.salary = salary
        self.gender = gender.upper
        self.full_name = self.first_name + ' ' + self.last_name


    def __str__(self):
        return f' Employees -{self.first_name}'
    
    def __repr__(self):
        return f'The object Employees -{self.first_name}'  

    def __add__(self,other):
        if isinstance(other,Employees):
            self.salary += other
            return self.salary
        if isinstance(other,(int,float)):
            self.salary += other
            return self.salary
        raise NotImplemented

    def __radd__(self,other):
        salary = self + other
        return self.salary 
    
    def __lt__(self,other):
        if isinstance(other,Employees):
            return self.salary < other.salary
        if isinstance(other,int):
            return self.salary < other               
    

p = Employees('Argam','Manukyan','098066650')
