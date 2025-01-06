class ClassA:
    def greet(self):
        print("Hello from ClassA!")


class ClassB:
    def __init__(self, class_a_instance):
        self.class_a_instance = class_a_instance

    def call_class_a(self):
        self.class_a_instance.greet()


a = ClassA()
b = ClassB(a)
b.call_class_a()
