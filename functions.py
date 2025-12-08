import csv
import uuid

class val:
    def not_empthy(_list):
        if not _list:
            return False
        else:
            return True
    
    def search_element(_list, key, value):
        for i in range(len(_list)):
            if _list[i][key] == value:
                return True, i
        return False, "We didn't find a value with that value\n"
    
class expences:
    def add_expence(_list, name, value):
        id = str(uuid.uuid4())[:3]
        _list.append({"id":id,"name":name,"value":value,"paid":False})
        print("Expence sucessfully added\n")

    def show_expences(_list):
        paid = ""
        print("-------------------------------------Expences-------------------------------------")
        for i in range(len(_list)):
            if _list[i]["paid"] == False:
                paid = "To pay"
            else:
                paid = "Already paid"
            print(f"Name: {_list[i]["name"]} | Value: {_list[i]["value"]} | Status: {paid}")
        print("")

    def change_status(_list, i):
        _list[i]["paid"] = True
        print("Status sucessfully changed\n")

    def remove_expence(_list, i):
        _list.pop(i)
        print("Expence sucessfully deleted")

class income:
    def add_income(_list, name, value, total_income):
        id = str(uuid.uuid4())[:3]
        total_income += value
        _list.append({"id":id,"name":name,"value":value})
        print("Income sucessfully added\n")

    def show_incomes(_list, total_income):
        print("-------------------------------------Incomes-------------------------------------")
        for i in range(len(_list)):
            print(f"Name: {_list[i]["name"]} | Value: {_list[i]["value"]}")
        print(f"total_income\n")

    def change_value(_list, i, new_value):
        _list[i]["value"] = new_value
        print("Income sucessfully changed\n")

    def remove_income(_list, i):
        _list.pop(i)
        print("Income sucessfully deleted\bn")

class csv_implementation:
    def read(_list,file):
        with open("r",file) as reader:
            csv_reader = csv.DictReader(reader)
            for i in csv_reader:
                _list.append(i)

    def writer(_list,file,headers):
        with open ("w",file) as writer:
            csv_writer = csv.DictWriter(writer,fieldnames=headers)
            csv_writer.writerows(_list)
            csv_writer.writeheader()    