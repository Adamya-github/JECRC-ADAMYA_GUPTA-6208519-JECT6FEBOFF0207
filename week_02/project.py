import time
## time.time()
class TODO:
    # todos = [
    #     {
    #         'id': '', ## ms are in floating so make sure not use ./decimal so typecast it in int
    #         'desc': '',
    #         'is_completed': False
    #     }, {}, {}, {}
    # ] format needs as 
    todo = []
    
    def add_todo(self, desc):
        ## 1. Take the desc from the user
        ## 2. We have to create one dictionary in which we will add the todo desc.
        ## 3. We have to append that dictionary inside the todos.
        # self.desc = desc ## input()
        dict1 = {}
        dict1['id'] = int(time.time())
        dict1['desc'] = desc ##self.desc
        dict1['is_completed'] = False
        self.todo.append(dict1)
        return self.todo
    
    def remove_todo(self, id):
        for i in self.todo:
            if i['id'] == id:
                self.todo.remove(i)
                return 1
        else:
            return -1         
    
    def display_todos(self):
        if len(self.todo) == 0:
            return
        return print(self.todo)
    
    def update_todo(self, id, new_desc):
        for i in self.todo:
            if i['id'] == id:
                i['desc'] = new_desc
  
    
    def toggle_mark_as_completed(self, id):
        for i in self.todo:
            if i['id'] == id:
                i['is_completed'] = True
    
    def completed_todos(self):
        if len(self.todo) == 0:
            return
        for i in self.todo:
            if i['is_completed'] == True:
                print(i)

    def incompleted_todos(self):
        if len(self.todo) == 0:
            return
        for i in self.todo:
            if i['is_completed'] == False:
                print(i)
    
