class Base:
    def show_message(self):
        print(":Message from Base Class")

class SubClass(Base):
    def show_message(self):
        super().show_message()
        print("Extended message")


obj = SubClass()
obj.show_message()