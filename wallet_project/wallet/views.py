from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Wallet, Transaction

def dashboard(request):
    # Fetch all wallets and transactions
    wallets = Wallet.objects.all()
    transactions = Transaction.objects.all().order_by('-created_at')  # Order transactions by date

    return render(request, 'wallet/dashboard.html', {
        'wallets': wallets,
        'transactions': transactions
    })

def pay(request):
    if request.method == 'POST':
        # Handle the payment logic
        wallet_id = request.POST.get('wallet_id')  # Get the wallet_id from the form
        amount = request.POST.get('amount')  # Get the amount from the form
        
        # Ensure you have a valid wallet
        try:
            wallet = Wallet.objects.get(id=wallet_id)
        except Wallet.DoesNotExist:
            return HttpResponse("Wallet not found.", status=404)

        # Create a transaction (adjust the transaction_type as needed)
        transaction = Transaction.objects.create(
            wallet=wallet,
            amount=amount,
            transaction_type='payment'  # Example type, adjust as needed
        )

        # Redirect or render a success page
        return redirect('dashboard')  # Redirect to the dashboard after payment

    wallets = Wallet.objects.all()  # Get all wallets for the form
    return render(request, 'wallet/pay.html', {'wallets': wallets})

def request_money(request):
    if request.method == 'POST':
        # Handle the request money logic
        wallet_id = request.POST.get('wallet_id')  # Get the wallet_id from the form
        amount = request.POST.get('amount')  # Get the amount from the form
        
        # Ensure you have a valid wallet
        try:
            wallet = Wallet.objects.get(id=wallet_id)
        except Wallet.DoesNotExist:
            return HttpResponse("Wallet not found.", status=404)

        # Create a transaction for the money request
        transaction = Transaction.objects.create(
            wallet=wallet,
            amount=amount,
            transaction_type='request'  # Example type, adjust as needed
        )

        # Redirect or render a success page
        return redirect('dashboard')  # Redirect to the dashboard after requesting money

    wallets = Wallet.objects.all()  # Get all wallets for the form
    return render(request, 'wallet/request_money.html', {'wallets': wallets})

def transactions(request):
    transactions = Transaction.objects.all().order_by('-created_at')  # Fetch all transactions
    return render(request, 'wallet/transactions.html', {'transactions': transactions})

