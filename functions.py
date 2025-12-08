import csv
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
    
class budget:
    def add_expence(_list, name, value):
        _list.append({"name":name,"value":value,"paid":False})
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
        print("Status changed\n")

    def remove_expence(_list, i):
        _list.pop(i)
        print("Sucessfully deleted")

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