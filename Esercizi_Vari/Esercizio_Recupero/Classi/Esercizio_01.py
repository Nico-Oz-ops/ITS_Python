# Esercizio 1

class TaskManager:
    def __init__(self):
        self.tasks = {}
    
    def create_task(self, task_id: str, descrizione: str) -> dict|str:
        if task_id in self.tasks:
            return "Errore: task esiste già"
        self.tasks[task_id] = {"Descrizione": descrizione, "Completato": False}

        return {task_id: self.tasks[task_id]}
    
    def complete_task(self, task_id: str) -> dict|str:
        if task_id not in self.tasks:
            return "Errore: task non trovato"
        self.tasks[task_id]["Completato"] = True

        return {task_id: self.tasks[task_id]}
    
    def update_description(self, task_id: str, nuova_descrizione: str) -> dict|str:
        if task_id not in self.tasks:
            return "Errore: task non trovato"
        self.tasks[task_id]["Descrizione"] = nuova_descrizione

        return {task_id: self.tasks[task_id]}

    def remove_task(self, task_id: str) -> dict|str:
        if task_id not in self.tasks:
            return "Errore: task non trovato"
        task_rimosso = self.tasks.pop(task_id)

        return {task_id: task_rimosso}
    
    def list_task(self) -> list[str]:
        return [task_id for task_id in self.tasks.keys()] # --> forma più compatta: return list(self.tasks.keys()) o list(self.tasks)
    
    def get_task(self, task_id: str) -> dict|str:
        if task_id not in self.tasks:
            return "Errore: task non trovato"
        return {task_id: self.tasks[task_id]}


# tasks = {
#     "task_01": {"Descrizione": "blablabla", "Completato": True},
#     "task_02": {"Descrizione": "blablabla", "Completato": False},
# }

tm = TaskManager()
create = tm.create_task("task_03", "blablahjsfdfnk")
print(create)


        