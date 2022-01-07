from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.core.paginator import Paginator
from filter.models import Pd
from .filters import *
# Create your views here.
def show_all_persons_page(request):
    context = {}
    all_reccords = Pd.objects.all().count()
    filtered_persons =  PdFilter(
        request.GET,
        queryset = Pd.objects.all().order_by('fam', 'name', 'fname')
    )
    context['allrec'] = all_reccords
    context['filtered_persons'] = filtered_persons

    paginated_filtered_persons = Paginator(filtered_persons.qs, 15)
    page_number = request.GET.get('page')
    person_page_obj = paginated_filtered_persons.get_page(page_number)

    context['person_page_obj'] = person_page_obj
    return render(request,'filter/index2.html',context=context)

'''
class PdList(ListView):
    model = Pd
    template_name = 'filter/index.html'
    context_object_name = 'pds'

'''


class FilteredListView(ListView):
    filterset_class = None

    def get_queryset(self):
        # Get the queryset however you usually would.  For example:
        queryset = super().get_queryset()
        # Then use the query parameters and the queryset to
        # instantiate a filterset and save it as an attribute
        # on the view instance for later.
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        # Return the filtered queryset
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the filterset to the template - it provides the form.
        context['filterset'] = self.filterset
        return context

class BookListView(FilteredListView):
    #filterset_class = PdFilter
    pagination_by = 30