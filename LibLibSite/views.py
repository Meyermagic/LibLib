from django.core.urlresolvers import reverse
from settings import MEDIA_ROOT, MEDIA_URL
from django.shortcuts import render
from django.template import RequestContext
from models import *

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

def home(request):
    return render(request, "../templates/home.html", {'nodes' : Category.objects.exclude(title='root')}, context_instance=RequestContext(request))

def category_browse(request, category_id):
    current_category = Category.objects.get(id=int(category_id))
    return render(request, "../templates/category_browse.html",
            {'category' : current_category,
             'algorithms' : current_category.algorithm_set.all(),
             'structures' : current_category.datastructure_set.all(),
             })

def algorithm_browse(request, algorithm_id):
    current_algorithm = Algorithm.objects.get(id=int(algorithm_id))
    return render(request, "../templates/algorithm_browse.html",
            {'algorithm' : current_algorithm,
             'implementations' : current_algorithm.algorithmimplementation_set.all().order_by('created')
             })

def alg_impl_view(request, algorithm_id, impl_id):
    current_algorithm = Algorithm.objects.get(id=int(algorithm_id))
    current_impl = AlgorithmImplementation.objects.get(id=int(impl_id))
    lexer = get_lexer_by_name(current_impl.language)
    formatter = HtmlFormatter()
    source = highlight(current_impl.code, lexer, formatter)
    return render(request, "algorithm_implementation_view.html",
            {'algorithm' : current_algorithm,
             'impl' : current_impl,
             'sourcecode' : source
            })

def structure_browse(request, structure_id):
    current_structure = DataStructure.objects.get(id=int(structure_id))
    return render(request, "../templates/structure_browse.html",
            {'structure' : current_structure,
             'implementations' : current_structure.datastructureimplementation_set.all().order_by('created')
        })

def struct_impl_view(request, structure_id, impl_id):
    current_structure = DataStructure.objects.get(id=int(structure_id))
    current_impl = DataStructureImplementation.objects.get(id=int(impl_id))
    lexer = get_lexer_by_name(current_impl.language)
    formatter = HtmlFormatter()
    source = highlight(current_impl.code, lexer, formatter)
    return render(request, "structure_implementation_view.html",
            {'structure' : current_structure,
             'impl' : current_impl,
             'sourcecode' : source
        })