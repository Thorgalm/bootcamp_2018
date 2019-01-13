# dekoratory włącza sie przez malpa nazwa dekoratora przes fukncją dekorowaną
def bold(funkcja):
    def wrapper(*args, **kwargs):
        # print("<b>")
        # funkcja(*args, **kwargs)
        # print("</b>")
        return f'<b>{funkcja(*args, **kwargs)}</b>'
    return wrapper

def italic(funkcja):
    def wrapper(*args, **kwargs):
        return f'<i>{funkcja(*args, **kwargs)}</i>'
    return wrapper


@bold
@italic
def foo(arg):
    return f'To jest {arg}'


print(foo("x"))


def test_decorated_foo():
    assert foo("x") == '<b><i>To jest x</i></b>'
