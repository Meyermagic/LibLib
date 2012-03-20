from django.contrib import admin
from LibLibSite.models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'description')
    search_fields = ['title']
admin.site.register(Category, CategoryAdmin)

class AlgorithmAdmin(admin.ModelAdmin):
    list_display = ('title',)
admin.site.register(Algorithm, AlgorithmAdmin)

class AlgorithmImplementationAdmin(admin.ModelAdmin):
    list_display = ('implements', 'language', 'author', 'created')
admin.site.register(AlgorithmImplementation, AlgorithmImplementationAdmin)

class DataStructureAdmin(admin.ModelAdmin):
    list_display = ('title',)
admin.site.register(DataStructure, DataStructureAdmin)

class DataStructureImplementationAdmin(admin.ModelAdmin):
    list_display = ('implements', 'language', 'author', 'created')
admin.site.register(DataStructureImplementation, DataStructureImplementationAdmin)

#admin.site.register(Algorithm)
#admin.site.register(DataStructure)
#admin.site.register(Demonstration)
#admin.site.register(TestSuite)
#admin.site.register(AlgorithmImplementation)
#admin.site.register(DataStructureImplementation)
#admin.site.register(DemonstrationImplementation)
#admin.site.register(TestSuiteImplementation)