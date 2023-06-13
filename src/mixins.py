from fastapi.requests import Request


def contact_mixin(request: Request):
    return {
        'request': request,
        'phone': '+375259145208',
        'email': 'pratayeu.a@gmail.com'
    }
