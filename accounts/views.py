from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User


def user_login(request):

    if request.method == 'POST':
        user = request.POST.get('username')
        password = request.POST.get('password')

        userVerify = auth.authenticate(
            request, username=user, password=password)

        if userVerify == None:
            messages.info(request, 'Usuário ou senha incorretos')
            return redirect('login')
        else:
            auth.login(request, userVerify)
            return redirect('home')
    
    else:  
        return render(request,'pages/login.html')
    

def tela_cadastro(request):
    if request.method == 'POST':
        # os nomes dentro dos parenteses, precisam ser os do .html
        user = request.POST.get('usuario')
        email = request.POST.get('email')
        password = request.POST.get('password')
        passrordConfim = request.POST.get('repeat_password')

        User.objects.create_user(username=user, email=email, password=password)

        return redirect('login')


    else:
        return render(request, 'pages/tela_cadastro.html')



        # # Verifique se as senhas coincidem
        # if password == repeat_password:
        #     # Crie um novo usuário no banco de dados
        #     novo_usuario = Usuario(usuario=usuario, email=email, password=password)
        #     novo_usuario.save()

        #     # Redirecione o usuário para alguma outra página, por exemplo, a página de login
        #     return redirect('login')
        # else:
        #     # Senhas não coincidem, você pode adicionar uma mensagem de erro
        #     mensagem_erro = "As senhas não coincidem"
        #     return render(request, 'tela_cadastro.html', {'mensagem_erro': mensagem_erro})