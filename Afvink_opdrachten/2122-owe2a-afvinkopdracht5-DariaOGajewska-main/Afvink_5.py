#afvink 5 opdracht 1
#opgave 1
class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age


    def set_name(self, name):
        self.__name = name


    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type


    def set_age(self, age):
        self.__age = age


    def get_name(self, name):
        return self.__name


    def get_animal_type(self, animal_type):
        return self.__animal_type


    def get_age(self, age):
        return self.__age





#opgave 2
class Car:
    def __init__(self, year_model, make, speed):
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed


    def set_year_model(self, year_model):
        self.__year_model = year_model

    def set_make(self, make):
        self.__make = make

    def set_speed(self, speed):
        self.__speed = speed

    def get_year_model(self):
        return self.__year_model

    def get_make(self):
        return self.__make

    def get_speed(self):
        return self.__speed











#opgave 3
class Player:
    def __init__(self, player):
        self.player = player

    def getPlayer(self):
        return self.player

    def round(self):
        questions = [{'question': 'Red and yellow together make orange',
                      'answer': 'True'},
                     {'question': 'Black is the brightest color that excist',
                      'answer': 'False'},
                     {'question': '4 + 2 = 6', 'answer': 'True'},
                     {'question': '2 * 2 = 7', 'answer': 'False'},
                     {'question': 'It is year 2000', 'answer': 'False'}
                     ]
        points = 0
        for i in questions:
            print(keyword.questions)
            answer = str(input('True/False: '))
            print(answer)
            if answer == value.questions:
                points += 1
            else:
                continue








# opg. 3 hf. 11
class Person:
    def __init__(self, name, adress, phone):
        self.name = name
        self.adress = adress
        self.phone = phone


    # def setName(self, name):
    #     self.name = name


    # def setAdress(self, adress):
    #     self.adress = adress


    # def setPhone(self, phone):
    #     self.phone = phone


    def getName(self):
        return self.name


    def getAdress(self):
        return self.adress


    def getPhone(self):
        return self.phone


class Customer:
    def __init__(self, customer_number, mailing_list):
        self.customer_number = customer_number
        self.mailing_list = bool(mailing_list)


    def getCustNumb(self):
        return self.customer_number


    def getMail(self):
        return self.mailing_list


def main():
    p1 = Person('Hugo', 'Wolfskuil 1', '0687 XXX XXX')

    print('Name of a customer:', p1.getName())
    print('Adress of a customer:', p1.getAdress())
    print('Phone number of a customer:', p1.getPhone())

    p1 = Customer('87654', True)

    print('Customer number:', p1.customer_number)
    print('Mailing list:', p1.mailing_list)









        # p1 = Player('Amber')
        # p2 = Player('Jill')
        #
        # p1 = print(Player.round)
        #
        # questions = [{'question' : 'Red and yellow together make orange', 'answer' : 'True'},
        #              {'question' : 'Black is the brightest color that excist', 'answer' : 'False'},
        #              {'question' : '4 + 2 = 6', 'answer' : 'True'},
        #              {'question' : '2 * 2 = 7', 'answer' : 'False'},
        #              {'question' : 'It is year 2000', 'answer' : 'False'}
        #              ]


    # pet_name = input('What is de name of your pet?:')
    # pet_animal_type = input('What is the animal type of your pet?:')
    # pet_age = input('What is the age of your pet?:')
    # pet = Pet(pet_name, pet_animal_type, pet_age)
    #
    # print('-'*80)
    # print('Name of your pet:', pet.get_name(pet_name))
    # print('Animal type of your pet:', pet.get_animal_type(pet_animal_type))
    # print('Age of your pet:', pet.get_age(pet_age))
    # print('-' * 80)



    # car1 = Car(year_model, make, speed)
    # car1.set_year_model = (input('year_model:'))
    # car1.set_make = (input('make'))
    # car1.set_speed = (input('speed'))
    #
    # print('-' * 80)
    # print('Year model:', car1.get_year_model())
    # print('Make of your car:', car1.get_make())
    # print('Speed of your car:', car1.get_speed())
    # print('-' * 80)






main()