class player:
    def __init__(self,jn,name,r,w,team_name):
        self.jersy_name=jn
        self.name=name
        self.r=r
        self.w=w
        self.team_name=team_name
    def get_jn(self):
        return self.jn
    def set_jn(self,value):
        self.jn=value
    def get_name(self):
        return self.name
    def set_name(self,value):
        self.name=value
    def get_r(self):
        return self.r
    def set_r(self,value):
        self.r=value
    def get_w(self):
        return self.w
    def set_w(self,value):
        self.w=value
    def get_team_name(self):
        return self.team_name
    def set_team_name(self,value):
        self.team_name=value
team_rcb=[
        player(18,"Virat",7000,4,"rcb"),player(45,"Maxwell",2500,25,"rcb"),player(33,"Karthik",4200,2,"rcb"),player(10,"Siraj",500,75,"rcb"),player(77,"Rajat",1500,5,"rcb")
    ]
print("\n1. Batsman with more than 1000 runs:")
for i in team_rcb:
    if i.get_r()>1000:
        print("name:",i.get_name(),"-",i.get_r(),"runs")
print("\n2. Bowlers with more than 20 wickets:")
for i in team_rcb:
    if i.get_w()>20:
        print("name:",i.get_name(),"-",i.get_w(),"wickets")
print("\n3. players whose name contains 'r':")
for i in team_rcb:
    if "r" in i.get_name():
        print("name:",i.get_name())

