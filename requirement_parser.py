# requirement_parser.py

def parse_requirement(requirement):
    # This is a mocked version. You can later upgrade it to use OpenAI/HuggingFace.

    return {
        "modules": [
            "User Management",
            "Task Assignment",
            "Task Tracking",
            "Notifications"
        ],
        "schema": {
            "User": {
                "id": "int",
                "name": "string",
                "email": "string"
            },
            "Task": {
                "id": "int",
                "title": "string",
                "description": "text",
                "assigned_to": "User.id",
                "status": "enum [To-Do, In Progress, Done]",
                "due_date": "date"
            }
        },
        "pseudocode": """
def create_task(title, description, assigned_to):
    task = {
        "title": title,
        "description": description,
        "assigned_to": assigned_to,
        "status": "To-Do"
    }
    save_to_database(task)
"""
    }
