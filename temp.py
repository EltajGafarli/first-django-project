database = {
    "blogs":{
        "python":{
        "id":123,
        "img":"python.jpg",
        "description":"The best Programming language and using for ML, AI, Web Development, Data Science etc.",
        "name" : "Python"
    },
    "c#":{
        "id":124,
        "img":"C#.jpg",
        "description":"The best Programming language and using for Web Development, App development, Game Development etc.",
        "name" : "C#"
    },
    "java":{
        "id":125,
        "img":"java.jpg",
        "description":"The best Programming language and using for App development Web Development, Game Development, Big Data etc.",
        "name" : "Java"
    },
    "django":{
        "id":126,
        "img":"django.jpg",
        "description":"The best Python FrameWork using for Web App development and Easy to learn",
        "name" : "Django"
    }
    }
}


print(database.get("blogs").get("python").get("name"))