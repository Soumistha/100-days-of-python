class User:
    #pass # or print("i am a user")
    #create a constructor
    def __init__(self,u_id,u_name):#in addition to self which means the object itself we can add many more attributes 
        print("new user created")
        self.id = u_id
        self.name = u_name 
        self.follower = 0 #default value
        self.following = 0
    
    def follow(self,user):
        user.follower+=1
        self.following+=1

#creating a attribute - a variable accociated with the object
#user_1 = User()

#when there are no constructors
#user_1.id = "001"
#print(user_1.id)

#using constructors
user_1 = User(101,"muku")
user_2 = User(102,"soumi")

user_1.follow(user_2)

print(user_1.id)
print(user_1.name)
print(user_1.follower)
print(user_1.following)