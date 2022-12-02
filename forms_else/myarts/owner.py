import q as q
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


class OwnerListView(ListView):
    """
        Sub-class the ListView to pass the request to the form.
    """


class OwnerDetailView(DetailView):
    """
    Sub-class the DetailView to pass the request to the form.
    """


class OwnerCreateView(CreateView):
    """
        Sub-class of the CreateView to automatically pass the Request to the Form
        and add the owner to the saved object.
        """

    def form_valid(self, form):  # storing data
        print('form_valid called')
        object = form.save(commit=False)  # create model object, but not save it to database
        object.owner = self.request.user  # pk of user
        object.save()
        return super(OwnerCreateView, self).form_valid(form)
        # calling the OG form_validation and making sure the form is valid


class OwnerUpdateView(UpdateView):
    """
        Sub-class the UpdateView to pass the request to the form and limit the
        queryset to the requesting user.
        """

    def get_queryset(self):  # querry to a database
        print('update get_queryset called')
        """ Limit a User to only modifying their own data. """
        qs = super(OwnerUpdateView, self).get_queryset()  # get querryset where px = x
        return qs.filter(
            owner=self.request.user)  # filter qs so that it'll return the qs if the logged in user is the owner (and pk = x)


class OwnerDeleteView(DeleteView):
    """
        Sub-class the DeleteView to restrict a User from deleting other
        user's data.
        """

    def get_queryset(self):
        print('delete get_queryset called')
        qs = super(OwnerDeleteView, self).get_queryset()
        return qs.filter(owner=self.request.user)
