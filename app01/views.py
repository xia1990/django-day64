from django.shortcuts import render,redirect,HttpResponse,render_to_response
from app01 import models

def index(request):
    return render_to_response("index.html")

#查询出版社
def publisher_list(request):
    p_list=models.Publisher.objects.all()
    print(p_list)
    return render(request,"publisher_list.html",{"publisher_list":p_list})

#添加出版社
def add_publisher(request):
    error_msg=""
    if request.method=="POST":
        #得到要添加的出版社名称
        p_name=request.POST.get("pname")
        if p_name:
            #去数据库中创建出版社
            models.Publisher.objects.create(pname=p_name)
            #返回出版社列表界面
            return redirect("/publisher_list/")
        else:
            error_msg="出版社名称不能为空"
            return render(request,"add_publisher.html",{"error":error_msg})
    return render(request,"add_publisher.html")

#删除出版社
def delete_publisher(request):
    #从get请求中得到要删除的出版社ID
    d_id=request.GET.get("pid",None)
    print(d_id)
    if d_id:
        #通过ID得到出版社对象
        d_obj=models.Publisher.objects.get(pid=d_id)
        #执行删除操作
        d_obj.delete()
        #返回删除后的办面
        return redirect("/publisher_list/")
    else:
        return HttpResponse("id不存在！")

#删除出版社
def delete_publisher2(request,d_id):
    if d_id:
        #通过ID得到出版社对象
        d_obj=models.Publisher.objects.get(pid=d_id)
        #执行删除操作
        d_obj.delete()
        #返回删除后的办面
        return redirect("/publisher_list/")
    else:
        return HttpResponse("id不存在！")

#编辑出版社
def edit_publisher(request):
    if request.method=="POST":
        #得到要修改出版社ID
        edit_id=request.POST.get("pid")
        print("=========="*50)
        print(edit_id)
        #得到要修改出版社名称
        edit_name=request.POST.get("pname")
        #根据ID得到要修改的出版社对象
        edit_publisher=models.Publisher.objects.get(pid=edit_id)
        print("-"*100)
        print(edit_name)
        #将修改的出版社名称进行更新
        edit_publisher.pname=edit_name
        edit_publisher.save()
        #返回修改后的出版社列表页面
        return redirect("/publisher_list/")
    else:
        #1:得到要修改出版社ID
        #2:根据ID得到要修改出版社对象
        #3:然后将对象返回到编辑页面
        edit_id=request.GET.get("pid")
        if edit_id:
            edit_publisher=models.Publisher.objects.get(pid=edit_id)
            return render(request,"edit_publisher.html",{"publisher":edit_publisher})

#图书列表
def book_list(request):
    #从数据库中查询所有图书信息
    book_list=models.Book.objects.all()
    #将图书信息返回到html页面上
    return render(request,"book_list.html",{"book_list":book_list})


#添加图书
def add_book(request):
    #get请求得到所有出版社名称
    if request.method=="GET":
        publisher_list=models.Publisher.objects.all()
        return render(request,"add_book.html",{'publisher_list':publisher_list})
    else:
        #post请求得到新添加的图书名称和选择的出版社的ID
        new_bname=request.POST.get("bname")
        new_publisher_id=request.POST.get("publisher")
        #去数据库中创建新添加的图书
        models.Book.objects.create(bname=new_bname,publisher_id=new_publisher_id)
        #返回到图书列表页面
        return redirect("/book_list/")


#删除图书
def delete_book(request):
    #得到要删除书籍的id
    del_id=request.GET.get("bid")
    print(del_id)
    print("="*100)
    #得到要删除书籍对象，并执行删除操作
    models.Book.objects.get(bid=del_id).delete()
    return redirect("/book_list/")


#编辑图书
def edit_book(request):
    if request.method=="GET":
        #得到所有的出版社
        publisher_list=models.Publisher.objects.all()
        #要编辑图书id
        edit_id=request.GET.get("bid")
        #得到要编辑图书对象(这里的bid是数据库中图书编号的属性)
        edit_book=models.Book.objects.get(bid=edit_id)
        return render(
            request,
            "edit_book.html",
            {"publisher_list":publisher_list,"book":edit_book}
        )
    else:
        #得到要编辑书的编号
        new_edit_id=request.POST.get("id")
        # 得到要编辑的图书对象
        edit_book = models.Book.objects.get(bid=new_edit_id)
        #得到要编辑书的名称（即修改后的书名）
        new_edit_name=request.POST.get("name")
        #得到要编辑出版社id
        new_edit_pid=request.POST.get("publisher")
        #更新图书名称和出版社编号
        edit_book.bname=new_edit_name
        edit_book.publisher_id=new_edit_pid
        #保存
        edit_book.save()
        #返回修改后的图书页面
        return redirect("/book_list/")

#作者列表
def author_list(request):
    #得到数据库中所有作者
    author_all=models.Author.objects.all()
    return render(request,"author_list.html",{"author_list":author_all})

#添加作者
def add_author(request):
    if request.method=="POST":
        #要添加的作者名称
        new_aname=request.POST.get("aname")
        #要添加的书籍对象
        books=request.POST.getlist("books")
        print("---"*20)
        print(books)
        #创建新作者
        new_author=models.Author.objects.create(aname=new_aname)
        #设置书籍和作者的对应关系
        new_author.book.set(books)
        return redirect("/author_list/")
    else:
        #从数据库中查出所有书籍
        b_list=models.Book.objects.all()
        #得到要添加作者名称
        return render(request,"add_author.html",{"book_list":b_list})

#删除作者
def delete_author(request):
    #要删除作者的ID
    del_aid=request.GET.get("aid")
    models.Author.objects.get(aid=del_aid).delete()
    return redirect("/author_list/")

#编辑作者
def edit_author(request):
    if request.method=="POST":
        #修改的作者新名称
        new_aname=request.POST.get("aname")
        #修改的作者编号
        e_aid=request.POST.get("aid")
        #得到当前修改作者的作品
        new_books=request.POST.getlist("book_list")
        #得到要修改作者对象
        new_author=models.Author.objects.get(aid=e_aid)
        #更新作者名称
        new_author.aname=new_aname
        #更新作者作品
        new_author.book.set(new_books)
        #更新数据库
        new_author.save()
        return redirect("/author_list/")

    else:
        #查询数据库中的所有书籍
        b_list=models.Book.objects.all()
        #得到编辑的作者ID
        edit_aid=request.GET.get("aid")
        #要编辑作者对象
        edit_author=models.Author.objects.get(aid=edit_aid)
        return render(request,"edit_author.html",{"book_list":b_list,'author':edit_author})
