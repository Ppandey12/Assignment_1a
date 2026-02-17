source venv/bin/activate

install 
- pip install fastapi uvicorn

# Run the server
uvicorn fastAPI_todolist:app --reload


For this assignment, I downloaded modules such as 
- fastapi
- uvicorn
- pydantic

To start the server, I used the command
- uvicorn fastAPI_todolist:app --reload

The API has the following endpoints:
1. "/": A simple GET request to check if the API is running.
2. '/help': Provides information about the available endpoints and their usage.
3. '/items': Returns a list of all todo items.
4. 'search?term={string}': Searches for todo items containing the specified term in their notes.
5. '/item/{identifier}': Returns a specific todo item by its identifier.
6. '/add': Adds a new todo item with specified attributes.
7. '/update/{identifier}': Updates an existing todo item identified by its identifier.


------------------------------------------------------------------------------------------------------------------------

# Assignment 1b - Flask



for this assignment, I downloaded modules such as 
- flask, render_template, request, redirect, url_for
- datetime
- virtualenv

- To start the server, I used the command
- python app.py
The API has the following endpoints:
1. "/": A simple GET request to check if the API is running.
2. '/add': A POST request to add a new todo item with specified attributes.
3. '/edit/<int:item_id>': A POST request to edit an existing todo item

I did not want to make this more complited than it already is, so I did not have multiple pages. all of this is done in the Home page. 
