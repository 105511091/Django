from django.shortcuts import render

# Create your views here.
import hashlib
from .models import Member

from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
def login(request):
    msg = ""
    if "email" in request.POST:
        email = request.POST['email']
        password = request.POST['password']
        password = hashlib.sha3_256(password.encode('utf-8')).hexdigest()
        
        obj=Member.objects.filter(email=email,password=password).count()
        
        if obj > 0 :#表示資料表中有這個使用者，且帳密都正確
            #建立SESSION 物件
            # 可以將值 暫時存在 伺服器端，當瀏覽器關閉時，SESSION 內的值
            # 就會不見，重開瀏覽器，就會抓不到值。
            # 打開瀏覽器時，它會主動跟伺服器端抓取一個id ，id會不同
            # 儲存在本地端電腦的，稱為 COOKIES
            
            request.session['myMail'] = email#儲存session資料
            request.session['isAlive'] = True
            
            #加上Cookie功能，若使用者禁用時，就會失效
            
            #宣告Cookie物件
            
            response = HttpResponseRedirect('/')
            #max_age = 秒，在這個範例是存活1200秒
            response.set_cookie("UMail",email,max_age=1200)
                                #自訂變數
            
            return response#指向根目錄(首頁)
        else:
            msg = "帳密錯誤，請重新輸入"
            return render(request,'login.html',locals())
    else:
        if "myMail" in request.session and "isAlive" in request.session:
            return HttpResponseRedirect('/member')
        else:
            myemail = request.COOKIES.get("UMail","")#抓取Cookie的值。若沒有澤空白
            return render(request,'login.html',locals())
        
def logout(request):
    del request.session["isAlive"] #刪除SESSION內容
    del request.session["myMail"]
    
    response = HttpResponseRedirect('/login')
    
    response.delete_cookie("UMail")
    
    
    return response
    
    #另一種寫法，記得上面要import HttpResponse
    #response = HttpResponse("Delete Cookie")
    #response.delete_cookie("UMail")
    #return HttpResponseRedirect('/login')

def register(request):
    msg = ""
    if 'userName' in request.POST:
        username = request.POST['userName']
        email = request.POST['email']
        password = request.POST['pwd']
        sex = request.POST['sex']
        birthday = request.POST['birthday']
        address = request.POST['address']
        
        #加密SHA256
        #password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        password = hashlib.sha3_256(password.encode('utf-8')).hexdigest()
        
        #此行是要查詢email是否已存在的
        obj = Member.objects.filter(email=email).count() #回傳筆數
        
        if obj == 0:#表示這個 email沒有註冊過
            #新增會員資料
            Member.objects.create(name=username,sex=sex,birthday=birthday,email=email,password=password,address=address)
            msg="恭喜你，已完成註冊!"
        else:
            msg = "此Email已存在，請換一個 mail 註冊"
        
    return render(request,'register.html',locals())

def manage(request):
    
    #要判斷是否已經登入了。
    if "myMail" in request.session and "isAlive" in request.session:
        
        msg = ''
        if "oldpwd" in request.POST:
            oldpwd = request.POST['oldpwd']
            newpwd = request.POST['newpwd']
            
            #確認使用者輸入的舊密碼是否正確，先將兩個密碼加密
            oldpwd = hashlib.sha3_256(oldpwd.encode('utf-8')).hexdigest()
            newpwd = hashlib.sha3_256(newpwd.encode('utf-8')).hexdigest()
            
            email = request.session['myMail']
            
            #確認使用者輸入的舊密碼是否正確
            obj = Member.objects.filter(email=email,password=oldpwd).count()
            if obj > 0:
                #更新密碼，
                user = Member.objects.get(email=email)
                user.password = newpwd
                user.save()
                msg = "密碼變更完成"
            else:
                msg = "舊密碼不正確，請重新輸入"
            
            
        return render(request,'manage.html',locals())
    else:
        return HttpResponseRedirect('/login')