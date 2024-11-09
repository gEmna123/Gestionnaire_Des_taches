import redis # type: ignore
import json
import os


import redis

r = redis.Redis(
  host='redis-19859.c16.us-east-1-2.ec2.redns.redis-cloud.com',
  port=19859,
  password='UyXwl2tvDFcsNcKaQJ42yd1lLGKPRAq0'
)

try:
    r.ping()
    print("Connexion à Redis réussie")
except redis.ConnectionError:
    print("Impossible de se connecter à Redis")



# Chemin du fichier de sauvegarde des tâches
FILE_PATH = "tasks.json"

# Charger les tâches depuis le fichier
def load_tasks():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    return []

# Sauvegarder les tâches dans le fichier
def save_tasks(tasks):
    with open(FILE_PATH, "w") as f:
        json.dump(tasks, f, indent=4)

# Ajouter une tâche
def add_task(tasks, task):
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print(f"Tâche '{task}' ajoutée avec succès !")

# Afficher les tâches
def list_tasks(tasks):
    if not tasks:
        print("Aucune tâche à afficher.")
        return
    for i, task in enumerate(tasks):
        status = "OK" if task["completed"] else "NOT OK"
        print(f"{i + 1}. {task['task']} - {status}")

# Marquer une tâche comme terminée
def complete_task(tasks, task_num):
    if 0 <= task_num < len(tasks):
        tasks[task_num]["completed"] = True
        save_tasks(tasks)
        print(f"Tâche {task_num + 1} marquée comme terminée.")
    else:
        print("Numéro de tâche invalide.")

# Supprimer une tâche
def delete_task(tasks, task_num):
    if 0 <= task_num < len(tasks):
        deleted_task = tasks.pop(task_num)
        save_tasks(tasks)
        print(f"Tâche '{deleted_task['task']}' supprimée.")
    else:
        print("Numéro de tâche invalide.")

# Menu principal
def main():
    tasks = load_tasks()
    while True:
        print("\nGestionnaire de Tâches")
        print("1. Ajouter une tâche")
        print("2. Afficher les tâches")
        print("3. Marquer une tâche comme terminée")
        print("4. Supprimer une tâche")
        print("5. Quitter")

        choice = input("Choisissez une option : ")

        if choice == "1":
            task = input("Entrez la nouvelle tâche : ")
            add_task(tasks, task)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            task_num = int(input("Entrez le numéro de la tâche à marquer comme terminée : ")) - 1
            complete_task(tasks, task_num)
        elif choice == "4":
            task_num = int(input("Entrez le numéro de la tâche à supprimer : ")) - 1
            delete_task(tasks, task_num)
        elif choice == "5":
            print("Au revoir !")
            break
        else:
            print("Choix invalide, veuillez réessayer.")
main()

