from abc import ABC, abstractmethod
from colorama import *


class Audible(ABC):
    def __init__(self, title, publish_year, speaker, time, price):
        self.title = title
        self.publish_year = publish_year
        self.speaker = speaker
        self.time = int(time)
        self.price = float(price)
        self.listen_time = 0
        self.progress = 0

    def get_status(self):
        if self.listen_time == self.time:
            print("Finished")

        elif self.listen_time == 0:
            print("Unread")

        else:
            print("Reading")

    def listen(self, time):
        if self.listen_time + time > self.time:
            raise ValueError(f"you can not listen more than {self.__class.__name__}'s length.")
        else:
            self.listen_time += time
            self.progress = self.listen_time / self.time * 100
            if self.listen_time == self.time:
                print(f"you have listen {time} more minutes from {self.title}.")
                print(f"Congrats you have finished the {self.title}")

            else:
                print(
                    f"you have listen {time} more minutes from {self.title}. There are {self.time - self.listen_time} minutes left")


class Readable(ABC):
    def __init__(self, title, author, publish_year, pages, language, price):
        self.title = title
        self.publish_year = publish_year
        self.author = author
        self.pages = int(pages)
        self.language = language
        self.price = float(price)
        self.readen_pages = 0
        self.progress = 0

    def read(self, pages):
        if self.readen_pages + pages > self.pages:
            raise ValueError(f"you can not read more than {self.__class__.__name__}'s pages.")
        else:
            self.readen_pages += pages
            self.progress = self.readen_pages / self.pages * 100
            if self.readen_pages == self.pages:
                print(f"you have read {pages} more pages from {self.title}.")
                print(f"Congrats you have finished the {self.title}")

            else:
                print(
                    f"you have read {pages} more pages from {self.title}. There are {self.pages - self.readen_pages} pages left")

    def get_status(self):
        if self.readen_pages == self.pages:
            print("Finished")

        elif self.readen_pages == 0:
            print("Unread")

        else:
            print("Reading")


class Book(Readable):
    shelf = {}

    def __init__(self, title, author, publish_year, pages, language, price):
        super().__init__(title, author, publish_year, pages, language, price)
        Book.shelf[self.title] = self

    def __str__(self) -> str:
        text = f"""Book name: {self.title}\nBook author: {self.author}\nPublish year: {self.publish_year}\nBook pages: {self.pages}\nLanguage: {self.language}\nprice: {"%.2f" % self.price}$"""

        return text


class Magazine(Readable):
    shelf = {}

    def __init__(self, title, author, publish_year, pages, language, price, issue):
        super().__init__(title, author, publish_year, pages, language, price)
        self.issue = issue
        Magazine.shelf[self.title] = self

    def __str__(self) -> str:
        text = f"""Magazine name: {self.title}\nMagazine issue: {self.issue}\nMagazine author: {self.author}\nPublish year: {self.publish_year}\nMagazine pages: {self.pages}\nLanguage: {self.language}\nprice: {"%.2f" % self.price}$"""

        return text


class Podcast(Audible):
    shelf = {}

    def __init__(self, title, publish_year, speaker, time, price, language):
        super().__init__(title, publish_year, speaker, time, price)
        self.language = language
        Podcast.shelf[self.title] = self

    def __str__(self) -> str:
        text = f"Podcast name: {self.title}\nSpeaker: {self.speaker}\nPublish year: {self.publish_year}\nTime: {self.time}\nLanguage: {self.language}\nPrice: {'%.2f' % self.price}$"
        return text


class AudioBook(Audible):
    shelf = {}

    def __init__(self, title, publish_year, speaker, time, price, book_language, audio_language, author):
        super().__init__(title, publish_year, speaker, time, price)
        self.book_language = book_language
        self.audio_language = audio_language
        self.author = author
        AudioBook.shelf[self.title] = self

    def __str__(self) -> str:
        text = f"Podcast name: {self.title}\nSpeaker: {self.speaker}\nAuthor: {self.author}\nPublish year: {self.publish_year}\nTime: {self.time}\nBook Language: {self.book_language}\nAudio Language: {self.audio_language}\nPrice: {'%.2f' % self.price}$"
        return text


# a = Book("ahmad", "ahmad", "1", "100", "ahmad", "100")
# a.read(50)
# print(a)
# b = Magazine("asghar", "ahmad", "1", "100", "ahmad", "100", "ahmad")
# b.read(50)
# print(b)
# c = Magazine("Kolbe zendegi", "Ahmad", 1380, 86, "fa", 12, "something")
# print(c)
# c.read(50)
# c.read(36)

# def print_inspect(obj):
#     print(f"{type(obj)}\n")
#     var_names = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
#     for v in var_names:
#         print(f"\tself.{v} = {getattr(obj, v)}\n")

def choose_class():
    text = '''
Choose category:
1. Book
2. Magazine
3. Podcast
4. Audio Book
5. Back
>>> '''

    choice = input(text)
    match choice:
        case "1":
            return Book
        case "2":
            return Magazine
        case "3":
            return Podcast
        case "4":
            return AudioBook
        case "5":
            main_menu()
        case _:
            print(Fore.RED, "wrong input, enter a valid number!", Fore.RESET)
            choose_class()


def choose_item(class_, list1):
    print(f"\n{class_.__name__}s:\n")
    for i in range(1, len(list1) + 1):
        print(f"{i}. {list1[i - 1]}")
    print(f"{len(list1) + 1}. Back")
    choice = int(input(f"choose a {class_.__name__}\n>>> "))
    if choice == (len(list1) + 1):
        main_menu()
    elif choice > len(list1) + 1:
        return choose_item(class_, list1)

    return list1[choice - 1]


def progress():
    list1 = list()
    for cls in [Book, Magazine, Podcast, AudioBook]:
        for k, v in cls.shelf.items():
            list1.append([cls.__name__, k, round(v.progress, 2)])
    list1.sort(key=lambda x: x[-1], reverse=True)
    return list1


def main_menu():
    while True:
        text = """
1. Add new item
2. Read/Listen
3. Inspect shelf
4. Status
5. Progress
6. Quit
>>> """
        choice = input(text)

        match choice:
            case "1":
                class_ = choose_class()
                list1 = list(class_.__init__.__code__.co_varnames)[1:]
                list2 = list()
                for item in list1:
                    list2.append(input(f"\n{item}\n>>> "))

                class_(*list2)
                print(f"{class_.__name__} added to shelf.")

            case "2":
                while True:
                    class_ = choose_class()
                    list1 = list(class_.shelf.keys())
                    if list1:
                        break
                    print("Nothing found!")

                choice = choose_item(class_, list1)
                obj = class_.shelf[choice]
                method = [method for method in dir(obj) if method.startswith(('read', "listen")) is True][0]
                attr = int(input(f"how much do you want to {method}:\n>>> "))
                if method == "read":
                    obj.read(attr)
                elif method == "listen":
                    obj.listen(attr)

            case "3":
                class_ = choose_class()
                list1 = list(class_.shelf.keys())
                print(f"\n{class_.__name__}'s shelf:")
                for item in list1:
                    print(f"• {item}")

            case "4":
                while True:
                    class_ = choose_class()
                    list1 = list(class_.shelf.keys())
                    if list1:
                        break
                    print("Nothing found!")

                choice = choose_item(class_, list1)
                obj = class_.shelf[choice]
                obj.get_status()

            case "5":
                list1 = progress()
                for lst in list1:
                    print(f"Name: {lst[1]} ◘ Media type: {lst[0]} ◘ Progress: {lst[2]}%\n{'-' * 20}")

            case "6":
                input("press enter to close...")
                quit()
            case _:
                print(Fore.RED, "wrong input, enter a valid number!", Fore.RESET)
                main_menu()


main_menu()
