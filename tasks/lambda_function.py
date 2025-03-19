import json

def lambda_handler(event, context):
    task_title = event.get("task_title", "Unknown Task")
    assigned_to = event.get("assigned_to", "Unassigned")
    
    message = f"Task '{task_title}' assigned to {assigned_to} is now completed."
    
    print(f"Lambda Notification: {message}")

    return {"statusCode": 200, "body": json.dumps({"message": message})}