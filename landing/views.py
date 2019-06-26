from django.shortcuts import render

# Create your views here.

def mostrar_index(request):
    return render(request, 'index.html')

def mostrar_layout(request):
    return render(request, 'layout.html')

def mostrar_pombos(request):
    return render(request, 'pombos.html')

def monstrar_rolezinho(request):
    roles = ['bailão', 'shopping União', 'Quermesse Da Paróquia de São João', 'Caçadão de Osasco', 'SESC', 'Risca faca']
    bairro = 'Rochdale'
    return render(request, 'rolezinho.html', {'roles':roles, 'bairro': bairro})
    
def mostrar_cachorro_quente(request):
    return render(request, 'cachorro.html')

def mostrar_assaltos(request):
    return render(request, 'assaltos.html')

