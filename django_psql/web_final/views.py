from django.template import RequestContext
from django.shortcuts import render, render_to_response
from web_final.forms import UserForm, UserProfileForm, ProductoForm, CategoriaForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
from web_final.models import Producto, Categoria


def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    category_list = Categoria.objects.order_by('id')
    producto_list = Producto.objects.order_by('id')[:9]
    productol1 = producto_list[0:3]
    productol2 = producto_list[3:6]
    productol3 = producto_list[6:9]
    context_dict = {'productos': producto_list,
                    'categorias': category_list,
                    'productos1': productol1,
                    'productos2': productol2,
                    'productos3': productol3}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request,'web_final/index.html', context_dict)

def register(request):
    registered = False
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True
            return HttpResponseRedirect('/web_final/')
        else:
            print(user_form.errors, profile_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'web_final/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/web_final/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Tu cuenta esta desabilitada.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print ("Datos invalidos o erroneos: {0}, {1}".format(username, password))
            return HttpResponse("datos de Inicio de sesion invalidos.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request,'web_final/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/web_final/')


@login_required
def product_register(request):
    if request.method == 'POST':
        prod = Producto(user = request.user)
        form = ProductoForm(request.POST, request.FILES, instance = prod)
        if form.is_valid():
            form.save()
            message = "Registro completado"
            return HttpResponseRedirect('/web_final/')
    else:
        form = ProductoForm()

    return render(request,'web_final/registrop.html', locals())

def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(nombre__icontains=query) |
            Q(descripcion__icontains=query)
        )
        results = Producto.objects.filter(qset).distinct()[:9]
        results1 = results[0:3]
        results2 = results[3:6]
        results3 = results[6:9]
    else:
        results = []
        results1 = []
        results2 = []
        results3 = []
    return render_to_response("web_final/search.html", {
        "results": results,
        "results1": results1,
        "results2": results2,
        "results3": results3,
        "query": query
    })
def about(request):
    return render(request, 'web_final/about.html', {})

@login_required
def categoria_register(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Registro completado"
            return HttpResponseRedirect('/web_final/')
    else:
        form = CategoriaForm()

    return render(request,'web_final/registroc.html', locals())

def searchc(request):
    category_list = Categoria.objects.order_by('id')
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(category_id = query)
        )
        qset1 = (
            Q(id = query)
        )
        results = Producto.objects.filter(qset).distinct()[:9]
        categ = Categoria.objects.filter(qset1)
        results1 = results[0:3]
        results2 = results[3:6]
        results3 = results[6:9]
    else:
        results = []
        results1 = []
        results2 = []
        results3 = []
    return render_to_response("web_final/searchc.html", {
        "results": results,
        "categorias":category_list,
        "results1": results1,
        "results2": results2,
        "results3": results3,
        "categ":categ,
        "query": query
    })


def producto(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(id = query)
        )
        results = Producto.objects.filter(qset).distinct()
    else:
        results = {}
    return render_to_response("web_final/producto.html",{"results":results,"query":query})