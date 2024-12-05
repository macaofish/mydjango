from django.shortcuts import render,HttpResponse
from .models import Book

# Create your views here.
def add_book(request):
    book = Book(name='三国演义', author='罗贯中', price=102)
    book.save()
    return HttpResponse("图书插入成功！")

def query_book(request):
    # books = Book.objects.all()
    # books = Book.objects.filter(name='三国演义')
    # for book in books:
    #     print(book.id, book.name, book.author, book.price)
    book = Book.objects.get(name='三国') # 使用get不存在会出错
    return HttpResponse("查找成功！")