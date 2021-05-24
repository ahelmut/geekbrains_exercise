# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. # А также класс «Оргтехника»,
# который будет базовым для классов-наследников. # Эти классы — конкретные типы оргтехники
# (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
# и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц
# оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

from abc import ABC


class Message():
    def __init__(self, type, text):
        self._type = type
        self._text = text

    def __str__(self):
        return str(self._type) + ". " + str(self._text)


class MessageList():
    def __init__(self):
        self.__content = []

    def add_message(self, message):
        self.__content.append(message)

    def print_content(self):
        txt = ''
        for el in self.__content:
            txt = txt + str(el) + '\n'

        return txt[:-1]

    @property
    def content(self):
        return self.__content


class Storage():
    __inv_number_set = set()


    def __init__(self, address, name, capacity):
        self._address = address
        self._name = name
        self.__capacity = capacity
        self.__stored_volume = 0
        self.__items = dict()
        self.__current_item_id = 0

    def store_item(self, item, mlog):
        if self.capacity_check(item) == True:
            self.__stored_volume = self.__stored_volume + item._storage_volume
            self.__current_item_id += 1
            item_id = self.__current_item_id
            self.__items.update({item_id: item})
            mlog.add_message(Message('information',
                                     'Storage ' + self._name + '. Item ' + str(item) + ' added with ITEM_ID: ' + str(
                                         item_id)))
            return True

        else:
            mlog.add_message(Message('information', 'Storage ' + self._name + '. Cannot add item ' + str(
                item) + '. Storage capacity reached.'))
            return False

    def unstore_item(self, item_id, mlog):
        item = self.__items.get(item_id)
        if self.__items.pop(item_id, False):
            self.__stored_volume = self.__stored_volume - item._storage_volume
            mlog.add_message(Message('information',
                                     'Storage ' + self._name + '. Item ' + str(item) + ' have been removed.'))
            return True
        else:
            mlog.add_message(Message('information',
                                     'Storage ' + self._name + '. Cannot remove the item ' + str(
                                         item) + '. There is no item ID ' + str(item_id)))
            return False

    def check_item(self, item_id):
        return str(self.__items.get(item_id))

    def capacity_check(self, item):
        if (item._storage_volume + self.__stored_volume) < self.__capacity:
            return True
        else:
            return False

    def move_item(self, item_id, destination, mlog):
        item = self.__items.get(item_id)
        if destination.capacity_check(item):
            self.unstore_item(item_id, mlog)
            destination.store_item(item, mlog)
        else:
            mlog.add_message(Message('information', 'Storage ' + destination._name + '. Cannot move item ' + str(
                item) + '. Storage capacity reached.'))


    def list_items(self):
        txt = ''
        for key in self.__items:
            txt = txt + str(key) + ": " + str(self.__items[key]) + '\n'

        return txt[:-1]

    def storage_report(self):
        print('На складе ' + self._name + " находится на хранении:" + '\n' + self.list_items())


class OfficeEquipment(ABC):
    __inventory_number = 0

    def __init__(self, type, vendor, model, production_date, mass, storage_volume):
        self._type = type
        self._vendor = vendor
        self._model = model
        self._mass = mass
        self._storage_volume = storage_volume
        self._production_date = production_date
        self.__inventory_number = OfficeEquipment.give_inventory_number()

    def __str__(self):
        return str(self._type) + ": " + str(self._vendor) + " " + str(self._model)

    @classmethod
    def give_inventory_number(cls):
        cls.__inventory_number = cls.__inventory_number + 1
        return cls.__inventory_number

    @property
    def inv_number(self):
        return self.__inventory_number


class Printer(OfficeEquipment):
    def __init__(self, type, vendor, model, mass, storage_volume, production_date, color_printing, printing_type,
                 paper_size):
        super().__init__(type, vendor, model, production_date, mass, storage_volume)
        _color_printing = color_printing
        _printing_type = printing_type
        _paper_size = paper_size


class Scaner(OfficeEquipment):
    def __init__(self, type, vendor, model, mass, storage_volume, production_date, paper_size):
        super().__init__(type, vendor, model, production_date, mass, storage_volume)
        _paper_size = paper_size


class Monitor(OfficeEquipment):
    def __init__(self, type, vendor, model, mass, storage_volume, production_date, diagonal):
        super().__init__(type, vendor, model, production_date, mass, storage_volume)
        _diagonal = diagonal


class PComputer(OfficeEquipment):
    def __init__(self, type, vendor, model, mass, storage_volume, production_date, ram, processor):
        super().__init__(type, vendor, model, production_date, mass, storage_volume)
        _ram = ram
        _processor = processor


message_log = MessageList()

mystorage = Storage('Москва, ул. Нижняя Красносельская 40/12к2', 'Склад на Бауманской', 20)
mydepartment = Storage('Москва, ул. Нижняя Красносельская 40/12к2', 'Департамент учета и отчетности', 5)
myprinter1 = Printer('Принтер', 'HP', 'Laser 107wr', 4.16, 1, '16.01.2020', False, 'Laser', 'A4')
myprinter2 = Printer('Принтер', 'Canon', 'PIXMA G1411', 4.8, 0.5, '16.02.2020', True, 'InkJet', 'A4')
scaner1 = Scaner('Сканер', "Canon", "CanoScan LiDE400", 1.7, 10, "01.01.2020", "А4")
monitor1 = Monitor("Монитор", "LG", "32QN600-B", 7.2, 5, "01.01.2020", 32)
computer1 = PComputer('Компьютер', "IRU", "Home 225", 10, 5, '16.01.2020', "DIMM, DDR4 16384 Мб 2400 МГц",
                      "AMD Ryzen 5 2600")

mystorage.store_item(myprinter1, message_log)
print(message_log.content[-1])
mystorage.store_item(myprinter2, message_log)
print(message_log.content[-1])

print()

mystorage.storage_report()

print()

mystorage.unstore_item(1, message_log)
print(message_log.content[-1])
mystorage.store_item(scaner1, message_log)
print(message_log.content[-1])
mystorage.store_item(monitor1, message_log)
print(message_log.content[-1])
mystorage.store_item(computer1, message_log)
print(message_log.content[-1])

print()
mystorage.storage_report()
print()

mystorage.move_item(3, mydepartment, message_log)
print(message_log.content[-1])

print()
mystorage.storage_report()
print()
mydepartment.storage_report()
print()

mystorage.move_item(2, mydepartment, message_log)
print(message_log.content[-1])

print()
mystorage.storage_report()
print()
mydepartment.storage_report()
print()

print(message_log.print_content())



