dict1 = {"fname":"wijdan","lname":"ariff"}

dict2 = {
    "fname":"mohamad", "lname":"salah"
}

detail = {
    "person1":{
        "fname":"ali",
        "lname":"bakar"
    },

    "person2":{
            "fname":"aiman",
            "lname":"baki"
    }

}

print(dict1)
print(dict1["fname"])
print(dict2["lname"])
print(detail["person1"])

detail["person1"]["fname"] = "abu"
print(detail["person1"]["fname"])

del dict2["fname"]      #delete
print(dict2)

dict2["firstName"] = "ahmad"
dict2.update({"midlleName":"nabil"})
print(dict2)

