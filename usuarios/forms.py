from django.contrib.auth.forms import AuthenticationForm

class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs ):
        super(FormularioLogin,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control' 
        self.fields['username'].widget.attrs['placeholder'] = 'nombre de usuario    '   
        self.fields['username'].widget.attrs['class'] = 'form-control'   
        self.fields['username'].widget.attrs['placeholder'] = 'contraseña'     