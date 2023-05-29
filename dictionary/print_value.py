# Exercise 3: Print the value of key ‘history’ from the below dict
d1 = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

ans=d1['class']['student']['marks']['history']
print(ans)