from django.core.urlresolvers import reverse
from django.http import Http404
from settings import MEDIA_ROOT, MEDIA_URL
from django.shortcuts import render, HttpResponseRedirect
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

def profile(request):
    context = RequestContext(request)
    user = context['user']
    algorithms = AlgorithmImplementation.objects.filter(author=user.pk)
    structures = DataStructureImplementation.objects.filter(author=user.pk)
    return render(request, "profile.html", {
        'algorithms' : algorithms,
        'structures' : structures
    })

def profile_other(request, uname):
    user = User.objects.get(username=uname)
    algorithms = AlgorithmImplementation.objects.filter(author=user.pk)
    structures = DataStructureImplementation.objects.filter(author=user.pk)
    return render(request, "profile_other.html", {
        'other_user' : user,
        'algorithms' : algorithms,
        'structures' : structures
    })

def new_algorithm(categories, title, description):
    algorithm = Algorithm.objects.create(categories=categories, title=title, description=description)
    algorithm.save()
    return HttpResponseRedirect(reverse("LibLibSite.views.algorithm_browse", args=[algorithm.id]))

def new_algorithm_impl(algorithm, author, language, code):
    pass

def new_structure(categories, title, description):
    structure = DataStructure.objects.create(categories=categories, title=title, description=description)
    structure.save()
    return HttpResponseRedirect(reverse("LibLibSite.views.structure_browse", args=[structure.id]))

def new_structure_impl(structure, author, language, code):
    pass

def handle_create(request):
    pass

def create_page(request):
    return render(request, "create.html")