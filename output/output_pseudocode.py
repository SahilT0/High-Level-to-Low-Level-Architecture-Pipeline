
def create_task(title, description, assigned_to):
    task = {
        "title": title,
        "description": description,
        "assigned_to": assigned_to,
        "status": "To-Do"
    }
    save_to_database(task)
