import os

def delete_old_file_on_update(instance,model,feld_name):
    if not instance.pk:
        return
    try:
        old_instace =model.objects.get(pk=instance.pk)
    except model.DoesNotExist:
        return
    old_file = getattr(old_instace, feld_name)
    new_file = getattr(instance, feld_name)
    if old_file and old_file != new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
    
    
def delete_old_file_on_delete(instance, feld_name):
    old_file = getattr(instance, feld_name)
    if old_file and os.path.isfile(old_file.path):
        os.remove(old_file.path)
        
        