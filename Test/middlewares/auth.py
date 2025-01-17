from django.shortcuts import render,redirect

def login_auth_middleware(get_response):

    def middleware(request):
        if not request.session.get('student'):
            return redirect('login')        
        response = get_response(request)

        
        return response

    return middleware