from django.shortcuts import redirect
from django.contrib import messages

def estabelecimento_required(view_func):
    """Garante que apenas estabelecimentos acessem a view"""
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated or getattr(request.user, 'tipo_usuario', None) != 'estabelecimento':
            messages.error(request, "Você precisa ser um estabelecimento para acessar esta página.")
            return redirect('estabelecimentos:login_estabelecimento')
        return view_func(request, *args, **kwargs)
    return wrapper

def instituicao_required(view_func):
    """Garante que apenas instituições acessem a view"""
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated or getattr(request.user, 'tipo_usuario', None) != 'instituicao':
            messages.error(request, "Você precisa ser uma instituição para acessar esta página.")
            return redirect('instituicoes:login_instituicao')
        return view_func(request, *args, **kwargs)
    return wrapper
