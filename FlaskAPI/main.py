from apiflask import APIFlask

app = APIFlask(__name__)

@app.get('/')
def index():
    return {"message": "Hello World"}

"""
    get /task get_all_task
    post /tasks create_task
    get /task/<task_id> get_task_by_id
    put /task/<task_id> update_task
    delete /task/<task_id> delete_task
"""
