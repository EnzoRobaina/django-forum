# from django.core.files.storage import FileSystemStorage
# from django.conf import settings
# import os



# class OverwriteStorage(get_storage_class()):

#     def _save(self, name, content):
#         self.delete(name)
#         return super(OverwriteStorage, self)._save(name, content)

#     def get_available_name(self, name):
#         return name
