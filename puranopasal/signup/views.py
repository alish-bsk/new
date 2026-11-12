from django.shortcuts import render, redirect
from django.contrib import messages
from electronic.models import Account  # Adjust according to your app name
import re
from django.contrib.auth.hashers import make_password, check_password  # Import for password hashing
from django.views import View


class SignUpView(View):
    def __init__(self,first_name=None, middle_name=None, last_name=None, password=None, confirm_password=None, phone_number=None):
        self._first_name = first_name
        self._middle_name = middle_name
        self._last_name = last_name
        self._password = password
        self._confirm_password = confirm_password
        self._phone_number = phone_number
        
    def rotl(self,x, n):
        # Shift x left by n bits
        # Shift x right by (32 - n) bits
        # 0xffffffff it put exact same 32 bit fix size data
        return ((x << n) | (x >> (32 - n))) & 0xffffffff

    def sha1(self,msg):
        ## msg  change into byte
        msg = bytearray(msg.encode())

        ## Padding msg  change into bit
        length = len(msg) * 8

        ## msg change into hexadecimal
        msg.append(0x80)

        ## it works in modulus if input data % 512 or not equal 448 then it append zero 
        while len(msg) % 64 != 56:
            msg.append(0)

        ## it add remaning bit to make value 512 bit in 448 bit
        msg += length.to_bytes(8, 'big')

        ## Initial values
        h0 = 0x67452301
        h1 = 0xEFCDAB89
        h2 = 0x98BADCFE
        h3 = 0x10325476
        h4 = 0xC3D2E1F0

        # Process blocks. Now hasing process work
        for block in range(0, len(msg), 64):
            w = []

            ## it works w[0] to w[15].it combine data to 32 bit.
            for i in range(16):
                start = block + i * 4
                w.append(int.from_bytes(msg[start:start+4], 'big'))

            ## it works w[16] to w[80].According to formula w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16]

            for i in range(16, 80):
                w.append(self.rotl(w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16], 1))

            a, b, c, d, e = h0, h1, h2, h3, h4

            ## it works according k[] method

            for i in range(80):
                ## it works round 20
                if i < 20:
                    f = (b & c) | (~b & d)
                    k = 0x5A827999

                ## it works round 40
                elif i < 40:
                    f = b ^ c ^ d
                    k = 0x6ED9EBA1

                ## it works round 60

                elif i < 60:
                    f = (b & c) | (b & d) | (c & d)
                    k = 0x8F1BBCDC
                else:
                    f = b ^ c ^ d
                    k = 0xCA62C1D6

                ## add all
                temp = (self.rotl(a, 5) + f + e + k + w[i]) & 0xffffffff

                e = d
                d = c
                c = self.rotl(b, 30)
                b = a
                a = temp

            h0 = (h0 + a) & 0xffffffff
            h1 = (h1 + b) & 0xffffffff
            h2 = (h2 + c) & 0xffffffff
            h3 = (h3 + d) & 0xffffffff
            h4 = (h4 + e) & 0xffffffff

        return f"{h0:08x}{h1:08x}{h2:08x}{h3:08x}{h4:08x}"

       
       
        
    def signup(self,request):
        if request.method == 'POST':
            patternpsw = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

                # Minimum 8 characters
            if len(self._password) < 8:
                return render(request, 'signup01.html',{'err':'Password must be at least 8 characters long!'})  # Make sure to adjust the template name

                errors.append("Password must be at least 8 characters long.")

            # At least one lowercase letter
            if not re.search(r"[a-z]", self._password):
                return render(request, 'signup01.html',{'err':'Password must contain at least one lowercase letter!'})  # Make sure to adjust the template name


            # At least one uppercase letter
            if not re.search(r"[A-Z]", self._password):
                return render(request, 'signup01.html',{'err':'Password must contain at least one uppercase letter!'})  # Make sure to adjust the template name


            # At least one number
            if not re.search(r"\d", self._password):
                return render(request, 'signup01.html',{'err':'Password must contain at least one number!'})  # Make sure to adjust the template name


            # At least one special character
            if not re.search(r"[@$!%*?&]", self._password):
                return render(request, 'signup01.html',{'err':'Password must contain at least one special character!'})  # Make sure to adjust the template name



            if re.match(patternpsw,self._password):
                hashed_password = self.sha1(self._password)

            pattern=r"^[a-zA-Z']"
            pattnnum = r'^[0-9]+$'
            act = Account.objects.filter(phonenumber=self._phone_number).first()

    

            if re.match(pattern,self._first_name):
                if re.match(pattern,self._middle_name) or not self._middle_name:
                    if re.match(pattern,self._last_name):
                        if re.match(pattnnum,self._phone_number):
                            if len(self._phone_number)==10:
                                if self._password == self._confirm_password:
                                    if act:
                                        return render(request, 'signup01.html',{'err':'phonenumber is already exist'}) 
    
                                    else:
                                        account = Account(
                                            first_name=self._first_name,
                                            middle_name=self._middle_name,
                                            last_name=self._last_name,
                                            phonenumber=self._phone_number,
                                            password=hashed_password,  # Consider hashing this password
                                        )
                                        account.save()
                                        return render(request, 'signup01.html',{'err':'Account created successfully!'})  # Make sure to adjust the template name
                                    
                                else:
                                    messages.error(request, "Passwords do not match.")
                                    return render(request, 'signup01.html',{'err':'password is not correct'})  # Make sure to adjust the template name
                        
                            else:
                                return render(request, 'signup01.html',{'err':'please enter 10 digit phonenumber'}) 
                
                        else:
                            return render(request, 'signup01.html',{'err':'please enter number'}) 

                    else:
                        return render(request, 'signup01.html',{'err':'please enter lastname in word'}) 
        
                    
                else:
                    return render(request, 'signup01.html',{'err':'please enter middlename in word'}) 

            
            else:
                return render(request, 'signup01.html',{'err':'please enter firstname in word'}) 

        return render(request, "signup01.html")
        

class SignUpExct(View):
    def get(self,request):
        if 'phonenumber' not in request.session:
            return render(request, "signup01.html")
        
        account = Account.objects.get(phonenumber=request.session['phonenumber'])

        return render(request, "signup01.html", {'name': account})
    def post(self,request):
        first_name = request.POST['firstname']
        middle_name = request.POST['middlename']
        last_name = request.POST['lastname']
        password = request.POST['password']
        confirm_password = request.POST['confirmpassword']
        phone_number = request.POST['phonenumber']

        signup_view = SignUpView(first_name, middle_name, last_name, password, confirm_password, phone_number)
        valuebtn = request.POST.get('signup')
        print(f"Value of signup button: {valuebtn}")
        if valuebtn == "signup":
            return signup_view.signup(request)

    