from django.http import HttpResponse
from django.shortcuts import render, redirect
from bookapp.forms import BooksForm,PublisherForm
from bookapp.models import Books,Publisher

# Create your views here.

def home(request):
    return render(request,'home.html')
def master(request):
    print('master')
    return render(request,'master.html')


def addbooks(request):
    if request.method == "GET":
        b=BooksForm()
        # print(b)
        return render(request,'add_book.html',{'form':b})
    else:
        b=BooksForm(request.POST)
        if b.is_valid():
            b.save()
            b = BooksForm()
            return render(request,'add_book.html',{'form':b,'message':'added successfully'})
        else:
            return render(request, 'add_book.html',
                          {'form': b, 'message': "Sorry! Could not add due to error!"})

def show_books(request):
    b=Books.objects.all()
    return render(request,'show_books.html',{'showbooks':b})

def editbook(request,id):
    if request.method == 'GET':
        try:
            b=Books.objects.get(id=id)
            form=BooksForm(instance=b)
            return render(request,'edit_book.html',{'form':form})
        except Exception as ex:
            print(ex)
            return render(request,'edit_book.html',{'message':'some thing went wrong'})
    else:
        b=Books.objects.get(id=id)
        form=BooksForm(instance=b,data=request.POST)
        if form.is_valid():
            form.save()
            return  redirect('booklist')
        else:
            return render(request, 'edit_book.html', {'form': form})

def delete_book(request,id):
    try:
        b=Books.objects.get(id=id)
        print(b)
        b.delete()
        return redirect('booklist')
    except Exception as e:
        print(e)
        return  render(request,'deletebook.html',{})

