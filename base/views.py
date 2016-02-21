#-*- coding: utf-8 -*-
""" Views for the base application """

from django.shortcuts import render,  get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf

import rpceth

from .models import EthAccount, Transaction
from django.contrib.auth.models import User
from .forms import PassForm

def home(request):
    """ Default view for the root """
    # if request.session['user_id'] is not None:
    #     c = {}
    #     c.update(csrf(request))    
    #     return render(request, 'base/home.html',c)	
    c = {}
    c.update(csrf(request))
    return render(request, 'base/home.html',c)

def login(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'base/login.html')

def auth_view(request):
    email = request.POST.get('email', '')
    password = request.POST.get('pass', '')
    user = auth.authenticate(username= email, password=password)
    print email
    print password
    print "hello, world!"
    if user is not None:
        auth.login(request, user)
        request.session['user_id']=email
        return HttpResponseRedirect('/wallet')
    else:
        return HttpResponseRedirect('/accounts/invalid')

def wallet(request):
    if request.method == "POST":
        form=PassForm(request.POST)
        if form.is_valid():
            acc=form.save(commit=False)
            acc.owner = User.objects.get(username=request.session['user_id'])
            acc.account_address = rpceth.newAccount(acc.account_password)
            acc.save()
            return redirect('base.views.wallet_detail', address=acc.account_address)
    else:
        user=User.objects.get(username=request.session['user_id'])
        ethAccounts = EthAccount.objects.filter(owner=user).order_by("created_date")
        #포린키 필터는 포린 오브렉트의 아이디(숫자)
        balance = sum([int(i.balance) for i in ethAccounts])/(10.0**18)
        form = PassForm()
    return render(request, 'base/wallet.html', {"email" : request.user.username, "accounts":ethAccounts, "balance": balance, "form":form})

def invalid_login(request):
    return render(request, 'base/home.html')

def logout(request):
    auth.logout(request)
    try:
    	del request.session['user_id']
    except KeyError:
    	pass
    return render(request, 'base/home.html')

def wallet_detail(request, address):
    ethAccount = get_object_or_404(EthAccount, account_address=address)
    ethAccount.balance=ethAccount.balance/(10**18)
    # ethAccount = EthAccount.objects.filter(account_address=address)
    return render(request, 'base/wallet_detail.html', {"ethAccount": ethAccount})

def wallet_add(request):
    if request.method == "POST":
        form=PassForm(request.POST)
        if form.is_valid():
            acc=form.save(commit=False)
            acc.owner = User.objects.get(username==request.session['user_id'])
            acc.account_address = rpceth.newAccount(acc.account_password)
            acc.save()
            return redirect('base.views.wallet_detail', address=acc.account_address)
        else:
            form=PassForm()
    return render(request, 'base/wallet.html', {'form': form})

def transaction_eth(request):
    return render(request, 'base/transaction.html', {})

