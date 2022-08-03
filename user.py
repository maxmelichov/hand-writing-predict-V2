
    
# class Admin(User):
#     pass

class Score():
    def __init__(self,score = 0,id=0) -> None:
        self.score= score
        self.id=id
    def get_score(self):
        return self.score
    def set_score(self,score):
        self.score=score 
    def get_id(self):
        return self.id
class User(Score):
    
    def __init__(self,name,id = 0) -> None:
        self.name=name
        self.id =id
    def get_name(self):
        return self.name
    def get_id(self):
        return self.id
    def set_name(self,name):
        self.name= name