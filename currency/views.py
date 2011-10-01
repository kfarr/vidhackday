from currency.models import Currency, Transaction, Holding

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

def index_view(request):
	if request.user.is_authenticated():
		return dashboard_view(request)
	return render_to_response('index.html', {}, context_instance=RequestContext(request))

@login_required
def currency_view(request, short_symbol = None):
	from currency.forms import CurrencyForm

	currency = None
	if short_symbol: currency = get_object_or_404(Currency, short_symbol = short_symbol)
	# if currency == if exists

	if request.method == 'POST':
		form = CurrencyForm(request.POST)
		if currency: form = CurrencyForm(request.POST, instance=currency)

		if form.is_valid():
			instance = form.save()
			messages.success(request, "This currency has been saved.")
			instance.owner = request.user
			instance.save()
			return HttpResponseRedirect(reverse('currency.views.dashboard_view', ))
	else:
		form = CurrencyForm()
		if currency: form = CurrencyForm(instance = currency)

	return render_to_response('currency.html', {'form': form, 'short_symbol': short_symbol}, context_instance=RequestContext(request))

@login_required
def transaction_view(request, transaction_id = None):
	from currency.forms import TransactionForm

	transaction = None
	if transaction_id: transaction = get_object_or_404(Transaction, id = transaction_id)

	if request.method == 'POST':
		form = TransactionForm(request.POST)
		if transaction: form = TransactionForm(request.POST, instance = transaction)

		if form.is_valid():
			instance = form.save()
			messages.success(request, "This transaction has been saved.")

#- on transaction create
#  - verify that transaction is legal
#     1. for from_currency (if any)
#       - make sure it exists
#       - make sure from_user has a large enough holding in that currency
#       - make sure to_user is in can_receive for from_currency or from_currency allows free trade
#     2. for to_currency (if any)
#       - make sure it exists
#       - make sure to_user has a large enough holding in that currency
#       - make sure from_user is in can_receive for to_currency or to_currency allows free trade
#     3. save transaction with state=requested
#	step 3.5 -- email user notification --
#     4. redirect back to /dashboard


#- on transaction approve
#   1. verify that from_user has a large enough holding in from_currency (if any)
#   2. verify that to_user has a large enough holding in to_currency (if any)
#   3. perform transaction
#       - set status to done or whatever
#       - reduce from_users holding in from_currency (if any) by from_amount
#       - increase to_users holding in from_currency by from_amount
#       - reduce to_users holding in to_currency by to_amount
#       - increase from_users holding in to_currency (if any) by to_amount
#   4. redirect to /dashboard
   
#- on transaction deny
#   1. set status to denied
#   2. redirect to /dashboard


			return HttpResponseRedirect(reverse('currency.views.transaction_view', args=[instance.id],))
	else:
		form = TransactionForm()
		if transaction: form = TransactionForm(instance = transaction)

	return render_to_response('transaction.html', {'form': form, 'transaction_id': transaction_id}, context_instance=RequestContext(request))

@login_required
def dashboard_view(request):
	currencies = Currency.objects.filter(owner = request.user)
	holdings = Holding.objects.filter(userprofile = request.user.userprofile)

	from django.db.models import Q
	transactions = Transaction.objects.filter(from_user = request.user)

	return render_to_response('dashboard.html', {'currencies': currencies, 'holdings': holdings, 'transactions': transactions}, context_instance=RequestContext(request))
