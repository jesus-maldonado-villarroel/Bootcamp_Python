from .models import Tarea, SubTarea


def tareas_y_sub_tareas():
    tareas = Tarea.objects.all()
    result = []
    for tarea in tareas:
        subtareas = tarea.subtareas.all()
        result.append({
            'tarea': tarea,
            'subtareas': subtareas
        })

    return result


def crear_tarea(descripcion):
    tarea = Tarea.objects.create(descripcion=descripcion)
    return tareas_y_sub_tareas()


def crear_sub_tarea(tarea_id, descripcion):
    tarea = Tarea.objects.get(id=tarea_id)
    SubTarea.objects.create(tarea=tarea, descripcion=descripcion)
    return tareas_y_sub_tareas()


def elimina_tarea(tarea_id):
    Tarea.objects.get(id=tarea_id).delete()
    return tareas_y_sub_tareas()


def elimina_sub_tarea(subtarea_id):
    SubTarea.objects.get(id=subtarea_id).delete()
    return tareas_y_sub_tareas()


def imprimir(data):
    for item in data:
        tarea = item['tarea']
        print(f"[{tarea.id}] {tarea.descripcion}")
        for subtarea in item['subtareas']:
            print(f".... [{subtarea.id}] {subtarea.descripcion}")
