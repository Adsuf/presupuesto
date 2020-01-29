from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Balance, Movimiento, Categoria
from .forms import MovimientoForm

# Mostrar Presupuesto.
def getBadget(request):
    balance = Balance.objects.all()
    movimiento = Movimiento.objects.all()
    context = {"balance" : balance, "movimiento" : movimiento}
    return render(request, 'home.html', context)

def mostarMovimiento(request):
    movimientos = Movimiento.objects.all()
    return render(request, 'home.html',{"mostrarMov" : movimientos})

def Movement(request):
    template_name = 'crear_movimiento.html'
    form = MovimientoForm()

    if request.method == 'POST':
        form = MovimientoForm(request.POST)
        if form.is_valid():
            form.save()
            #se afecta el Balance
            #balance = Balance.objects.get(pk=1)
            #if request.POST['tipo'] == "Gasto": #GASTO
            #    balance.saldo -= int(request.POST['monto'])
            #    balance.gastos += int(request.POST['monto'])
            #else:
            #    balance.saldo += int(request.POST['monto'])
            #    balance.ingresos += int(request.POST['monto'])
            #balance.save()
            updateBalance(request.POST['tipo'], int(request.POST['monto']))
            return HttpResponseRedirect('/')
    return render(request, template_name, {'form': form})

def updateBalance(tipo, monto):
    #se afecta el Balance
    balance = Balance.objects.get(pk=1)
    if tipo == "Gasto": #GASTO
        balance.saldo -= monto
        balance.gastos += monto
    else:
        balance.saldo += monto
        balance.ingresos += monto
    balance.save()
    return

def deleteMovement(request, pk):
    movimiento = Movimiento.objects.get(pk=pk)
    alterBalance(movimiento.tipo, movimiento.monto)
    movimiento.delete()
    return HttpResponseRedirect('/')

def alterBalance(tipo, monto):
    #se afecta el balance
    balance = Balance.objects.get(pk=1)
    if tipo == "Gasto": #GASTO
        balance.saldo += monto
        balance.gastos -= monto
    else:
        balance.saldo -= monto
        balance.ingresos -= monto
        balance.save()
        return
