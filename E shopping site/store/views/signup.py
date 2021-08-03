from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.views import View
from store.models.customer import Customer


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        error_message = None
        postDATA = request.POST
        first_name = postDATA.get('Firstname')
        last_name = postDATA.get('lastname')
        phone = postDATA.get('phone')
        email = postDATA.get('email')
        password = postDATA.get('password')
        # VALIDATION
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email,
        }

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)

        # saving
        error_message = self.validateCustomer(customer)
        if not error_message:
            print(first_name, last_name, phone, email, password)
            customer.password = make_password(customer.password)

            customer.register()

            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None
        if len(customer.phone) < 10:
            error_message = "Enter valid phone number"

        elif len(customer.password) < 6:
            error_message = "Password must atleast 6 characters"

        elif customer.isExists():
            error_message = "Email Already Registered Please Login"

        return error_message
