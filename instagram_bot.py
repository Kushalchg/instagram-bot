from instapy import InstaPy

session = InstaPy(username="sername", password="password")
#in password and username field you have to enter your instagram username and password
session.login()

session.set_relationship_bounds(enabled=True,max_followers=20000)

session.set_do_follow(True,percentage=100)


session.like_by_tags(["random","bot","education","tyr","first","now"],amount=15)
#in tag you need to specified tag you want
session.end()