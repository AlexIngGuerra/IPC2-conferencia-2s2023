from views.Config import raiz
from views.Principal import ViewPrincipal

def main():
    viewPrincipal = ViewPrincipal(raiz)
    raiz.mainloop()

if __name__ == '__main__':
    main()