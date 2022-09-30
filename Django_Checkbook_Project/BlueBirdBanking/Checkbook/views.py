from django.shortcuts import render, redirect, get_object_or_404
from . forms import AccountForm, TransactionForm
from .models import Account, Transaction


# This function will render the Home page when requested
def home(request):
    form = TransactionForm(data=request.POST or None) # Retrieves the Transaction form
    # Checks if requested method is POST
    if request.method == 'POST':
        # if the form is submitted, retrieve which account the user wants to view
        pk = request.POST['account']
        # call balance function to render that accounts Balance Sheet
        return balance(request, pk)
        # Passes content to the template as a dictionary
    content = {'form': form}
        # adds content of form to page
    return render(request, 'checkbook/index.html', content)


# This function will render the Create New Account page when requested
def create_account(request):
    form = AccountForm(data=request.POST or None) # Retrieves the account form
    # Checks if requested method is POST
    if request.method == 'POST':
        # Check to see if the submitted form is valid and if so, saves the form
        if form.is_valid():
            # Saves new account
            form.save()
            # returns user back to the home page
            return redirect('index')
        # Saves content to the template as a dictionary
    content = {'form': form}
        # adds content of form to page
    return render(request, 'checkbook/CreateNewAccount.html', content)


# This function will render the Balance page when requested
def balance(request, pk):
    account = get_object_or_404(Account, pk=pk) # Retrieve the requested account using its primary key
    transactions = Transaction.Transactions.filter(account=pk) # Retrieve al of that accounts transactions
    current_total = account.initial_deposit # Creates account total variable, starting with initial deposit value
    table_contents = {} # Creates a dictionary into which transactions information will be placed
    for t in transactions: # Loop through transactions and determine which is a deposit or withdrawl
        if t.type == 'Deposit':
            current_total += t.amount # If deposit add amount to balance
            table_contents.update({t: current_total}) #Add transaction and total to the dictionary
        else:
            current_total -= t.amount # If withdrawl subtract amount from balance
            table_contents.update({t: current_total}) #Add transaction and total to the dictionary
    # Pass account, account total balance, and transaction information to the template
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)


# This function will render the Transaction page when requested
def transaction(request):
    form = TransactionForm(data=request.POST or None)  # Retrieves the Transaction form
    # Checks if requested method is POST
    if request.method == 'POST':
        # Check to see if the submitted form is valid and if so, saves the form
        if form.is_valid():
            # retreive which account the transaction was for
            pk = request.POST['account']
            # Saves transaction form
            form.save()
            # renders balance of the accounts Balance Sheet
            return balance(request, pk)
        # Pass content to the template as a dictionary
    content = {'form': form}
        # adds content of form to page
    return render(request, 'checkbook/AddTransaction.html', content)

