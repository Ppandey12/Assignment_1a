from fastapi import FastAPI
from todo import TodoList
from pydantic import BaseModel

app = FastAPI()
todo_list = TodoList()
todo_list.load()

class TodoItemModel(BaseModel):
    note: str
    priority: int = 0
    due: str = None
    done: bool = False


@app.get("/")
def get():
    return {"Todo": "TO DO List API is running!"}

@app.get("/help")
def help():
    return {
        '''
            "/": "Check if the API is running",
            "/help": "Get information about available endpoints"
            "/items": "returns a list of todo items",
            "/search?term={string}": "search for todo items containing the specified term",
            "/item/{identifier}": "get a specific todo item by its identifier",
            "/add: POST": "add a new todo item",
            "/update/{identifier}" : "update an existing todo item by its identifier",
        '''
        }


@app.get("/items")
def items():
    itemlist = []
    for item in todo_list:
        itemlist.append(item.as_json())
    return itemlist
    
    # return [item.as_json() for item in todo_list]



@app.get("/search")
def search(term: str):
    return todo_list.search(term)



@app.get("/item/{identifier}")
def item(identifier: int):
    for item in todo_list:
        print(item.identifier, identifier)

    # for item in todo_list:
    #     if item.identifier == identifier:
    #         print(item.identifier.as_json())
    #         return item.identifier.as_json()
    return {"error": "Item not found"}
  


@app.get("/add")
def add(todo: TodoItemModel):
    item = todo_list.add(note=todo.note, priority=todo.priority, due=todo.due, done=todo.done)
    todo_list.save()
    return item.as_json()


@app.get("/update/{identifier}")
def update(identifier: int, todo: TodoItemModel):
    for items in todo_list:
        if items.identifier == identifier:
            items.note = todo.note
            items.priority = todo.priority
            items.due = todo.due
            items.done = todo.done
            todo_list.save()
            return items.as_json()
    return {"error": "Item not found"}
