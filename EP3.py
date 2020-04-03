# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 10:20:51 2020

@author: lucas
"""
from random import randint

bag = 100

game= True
while game:
    if bag<0:
        print('GAME OVER')
        game = False
    bet = int(input('valor da aposta?:'))
    if bet > 12:
        print('aposta inválida')
        break
    print('as apostas possíveis são:')
    print('pass line bet')
    print('field')
    print('any craps')
    print('twelve')
    jogo = input('qual aposta?: ')
    if jogo == 'pass line bet':
        dado1=randint(1,6)
        dado2=randint(1,6)
        print(dado1)
        print(dado2)
        summy = dado1 + dado2
        print('o resultado é', summy)
        passline = True
        while passline:
            if summy == 7:
                bag = bag + bet
                print('valor da bag é', bag)
                break
            if summy == 11:
                bag = bag + bet
                print('valor da bag é', bag)
                break
            if summy == 2:
                bag = bag - bet
                print('valor da bag é', bag)
                break
            if summy == 3:
                bag = bag - bet
                print('valor da bag é', bag)
                break
            if summy == 12:
                bag = bag - bet
                print('valor da bag é', bag)
                break
            else:
                point=True
                while point:
                    dado1=randint(1,6)
                    dado2=randint(1,6)
                    print(dado1)
                    print(dado2)
                    summy = dado1 + dado2
                    print('o resultado do point é', summy)
                    if summy == bet:
                        bag = bag + bet
                        print('valor da bag é', bag)
                        point = False
                        passline = False                  
                    elif summy == 7:
                        bag = 0
                        print('GAME OVER')
                        point = False
                        passline = False
                        game = False

    if jogo == 'field':
        dado1=randint(1,6)
        dado2=randint(1,6)
        print(dado1)
        print(dado2)
        summy = dado1 + dado2
        print('o resultado é', summy)
        if summy == 5:
            bag = 0
            print('GAME OVER')
            game = False
        if summy == 6:
            bag = 0
            print('GAME OVER')
            game = False
        if summy == 7:
            bag = 0
            print('GAME OVER')
            game = False
        if summy == 8:
            bag = 0
            print('GAME OVER')
            game = False
        if summy == 2:
            bag = bag + 2*bet
            print('valor da bag é', bag)
        if summy == 12:
            bag = bag + 3*bet
            print('valor da bag é', bag)
        else:
            print('valor da bag é', bag)
        
        
    if jogo == 'any craps':
        dado1=randint(1,6)
        dado2=randint(1,6)
        print(dado1)
        print(dado2)
        summy = dado1 + dado2
        print('o resultado é', summy)
        if summy == 2:
            bag = bag + 7*bet
            print('valor da bag é', bag)
        if summy == 3:
            bag = bag + 7*bet
            print('valor da bag é', bag)            
        if summy == 12:
            bag = bag + 7*bet
            print('valor da bag é', bag)    
        else:
            bag = bag - bet
            print('você perdeu a aposta')
            print('valor da bag é', bag)
            
    if jogo == 'twelve':
        dado1=randint(1,6)
        dado2=randint(1,6)
        print(dado1)
        print(dado2)
        summy = dado1 + dado2
        print('o resultado é', summy)
        if summy == 12:
            print('você ganhou a aposta')
            bag = bag + 30*bet
            print('valor da bag é', bag)
        else:
            bag = bag - bet
            print('você perdeu a aposta')
            print('valor da bag é', bag)
        
            

        
        

                
                
            
































