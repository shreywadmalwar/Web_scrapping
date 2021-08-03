from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from django.views import View
from store.models.customer import Customer


class Login(View):
    returnUrl = None

    def get(self, request):
        Login.returnUrl = request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self, request):

        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                request.session['email'] = customer.email
                if Login.returnUrl:
                    return HttpResponseRedirect(Login.returnUrl)
                else:
                    Login.returnUrl = None
                    return redirect('homepage')
            else:
                error_message = "Invalid Email or Password"
        else:
            error_message = "Invalid Email or Password"
        print(email, password)
        return render(request, 'login.html', {'error': error_message})


def logout(request):
    request.session.clear()
    return redirect('login')
