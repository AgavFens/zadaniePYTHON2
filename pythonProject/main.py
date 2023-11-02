import time


class Blog:
    def __init__(self, name, author, posts=[]):
        self.name = name
        self.author = author
        self.posts = posts

    def make_post(self, text, title):
        post = {}
        post["title"] = title
        post["text"] = text
        t = time.localtime()
        post["time"] = time.strftime("%H:%M:%S:", t)
        self.posts.append(post)

    def delete_post(self, title):
        for i in self.posts:
            if i["title"] == title:
                self.posts.remove(i)
            else:
                print("Поста с таким названием нет")


blog = Blog("Питон", "Лукьянов")

while True:
    choice = input("Вы можете:"
                   "\n1) Создать пост"
                   "\n2) Удалить пост"
                   "\nВаш выбор: ")
    match choice:
        case "1":
            title = input("Введите заголовок: ")
            text = input("Введите текст: ")
            blog.make_post(text, title)
            print(blog.posts)
        case "2":
            title = input("Введите заголовок: ")
            blog.delete_post(title)
            print(blog.posts)
        case _:
            print("Такой функции нет")