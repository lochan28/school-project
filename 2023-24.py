import time as t
import os
import colorama
import pickle as p
from colorama import Fore
colorama.init(autoreset=True)
def movie_input():
    movies={}
    while True:                                    #movie loop
        timing={}
        movie_name=input("enter name of movie:")
        royal_price=int(input("enter cost of royal seats:"))
        comfirt_price=int(input("enter cost of comirt seats:"))
        economy_price=int(input("enter cost of economy seats:"))
        seat={"seating":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50],"pricing":[royal_price,comfirt_price,economy_price]}
        while True:                                                               #timing loop
            os.system("cls")
            movie_timing=input("enter HH:MM AM/PM:")
            timing[movie_timing]=seat
            t.sleep(0.5)
            print(Fore.GREEN+"timing succesfully added....\n\n")
            while True:                                                           #ask loop
                add=input("enter y/Y to add more movie timings \nelse enter n/N:")
                if add in "YesyesYES":
                    check=0
                    os.system("cls")
                    break
                elif add in "noNoNO":
                    check=1
                    break
                else:
                    print(Fore.RED+"invalid entery please try aggain")
                    continue
            if check==0:
                continue
            else:
                break
        movies[movie_name]=timing
        print(Fore.GREEN+"movie succesfully added....")
        while True:                                                                 #ask loop
            os.system("cls")
            add=input("enter y/Y to add more movie name \nelse enter n/N:")
            if add in "YesyesYES":
                check=0
                os.system("cls")
                break
            elif add in "noNoNO":
                check=1
                break
            else:
                print(Fore.RED+"invalid entery please try aggain")
                continue
        if check==0:
            continue
        else:
            break
    print(Fore.GREEN+"movies succesfully added....")
    t.sleep(1)
    os.system("cls")
    with open('movie.dat','rb') as f:
        file=p.load(f)
        if file!={}:
            movies.update(file)
    with open('movie.dat','wb') as f:
        p.dump(movies,f)
def movie_output():
    cost=0
    with open('movie.dat', 'rb') as f:
        moviedict=p.load(f)
        if moviedict!={}:
            t.sleep(1)
            print(Fore.BLUE+"list of movies:\n")
            movie_names=list(moviedict.keys())
            while True:                                                                #movie sellection
                for i in range (1,len(movie_names)+1):
                    t.sleep(0.5)
                    print(Fore.LIGHTGREEN_EX+str(i),Fore.LIGHTGREEN_EX+")",movie_names[i-1],"\n")
                select_movie=int(input(Fore.LIGHTGREEN_EX+"enter the number of movie you would like to see:"))
                os.system("cls")
                if 0<select_movie<=len(movie_names):
                    break
                else:
                    print(Fore.RED+"movie not avaliable try aggain....")
                    continue
            timings=moviedict[movie_names[select_movie-1]]
            time=list(timings.keys())
            print(Fore.BLUE+"sellect timing;\n")
            while True:                                                                #time sellection
                for i in range (1,len(time)+1):
                    print(Fore.CYAN+str(i),Fore.CYAN+")",time[i-1],"\n")
                select_timing=int(input(Fore.YELLOW+"enter the number of timing you would like to see:"))
                os.system("cls")
                if 0<select_timing<=len(time):
                    break
                else:
                    print(Fore.RED+"movie not avaliable try aggain....")
                    continue
            seat_price=timings[time[select_timing-1]]
            seates_booked=[]                                                            #seat sellection
            seat=list(seat_price['seating'])
            print(Fore.LIGHTYELLOW_EX+"royal:")
            for i in range(1,11):
                if i in seat:
                    print(Fore.GREEN+str(i),end=" ")
                else:
                    print(Fore.RED+str(i),end=" ")
                if i==10:
                    print("\n")
            print(Fore.LIGHTYELLOW_EX+"comfort:")
            for i in range(11,31):
                if i==21:
                    print("\n")
                if i in seat:
                    print(Fore.GREEN+str(i),end=" ")
                else:
                    print(Fore.RED+str(i),end=" ")
                if i==30:
                    print("\n")
            print(Fore.LIGHTYELLOW_EX+"economy:")
            for i in range(31,51):
                if i==41:
                    print("\n")
                if i in seat:
                    print(Fore.GREEN+str(i),end=" ")
                else:
                    print(Fore.RED+str(i),end=" ")
                if i==50:
                    print("\n")
            price=list(seat_price["pricing"])
            t.sleep(1)
            print(Fore.LIGHTYELLOW_EX+"prices:\n")
            t.sleep(0.5)
            print(" royal=",price[0],"\n comfort=",price[1],"\n economy=",price[2])
            t.sleep(0.5)
            print(Fore.GREEN+" green","=seat acalable\n",Fore.RED+"red","  =seat seat booked")
            t.sleep(0.5)
            select_seat=(input(Fore.YELLOW+"\nenter no. of seats you want to book:"))
            check=1
            while check<=int(select_seat):
                booking=int(input(Fore.YELLOW+"enter seat number that you want to book:"))
                if booking in seat:
                    seat.remove(booking)
                    seates_booked.append(booking)
                    if 0<booking<=10:
                        cost+=price[0]
                        check+=1
                    elif 10<booking<=30:
                        cost+=price[1]
                        check+=1
                    elif 30<booking<=50:
                        cost+=price[2]
                        check+=1
                    else:
                        print(Fore.RED+"invalid entry ,try again...")
                else:
                    print(Fore.RED+"invalid entery...")
                    continue
            new_seats={"seating":seat,"pricing":price}
            timings[time[select_timing-1]]=new_seats
            moviedict[movie_names[select_movie-1]]=timings
            with open('movie.dat', 'wb') as f:
                p.dump(moviedict,f)
            return movie_names[select_movie-1],time[select_timing-1],seates_booked,cost
        else:
            print(Fore.RED+"terre id no movie scheduled....")
            pass
def addloop(name,time,seat,cost_seat):
    while True:
        os.system("cls")
        addon=input(Fore.YELLOW+"food and beverages y/n:")
        os.system("cls")
        cost_food=cost_seat
        if addon in "yesYesYES":
            print(Fore.WHITE+"Press 1 for ",Fore.YELLOW+"Popcorn","=100/-")
            t.sleep(0.5)
            print("Press 2 for ",Fore.YELLOW+"Samosa","=50/-")
            t.sleep(0.5)
            print("Press 3 for ",Fore.YELLOW+"Cold Drink","=80/-")
            t.sleep(0.5)
            print("Press 0 to ",Fore.RED+"exit")
            while True:
                FB=(input(Fore.YELLOW+"\nEnter snak Number Between 1-3 or enter 0 for final bill:"))
                if FB=="1":
                    q=int(input(Fore.YELLOW+"Enter Quantity:"))
                    cost_food+=100*q
                    continue
                elif FB=="2":
                    q=int(input(Fore.YELLOW+"Enter Quantity:"))
                    cost_food+=50*q
                    continue
                elif FB=="3":
                    q=int(input(Fore.YELLOW+"Enter Quantity:"))
                    cost_food+=80*q
                    continue
                elif FB=="0":
                    print(Fore.GREEN+"itens successfully added")
                    break
                else:
                    print(Fore.RED+"invalid entery")
                    continue
            total=cost_seat+cost_food
            discount=cost_food*15//100
            os.system("cls")
            print(Fore.BLUE+"------",Fore.LIGHTMAGENTA_EX+"final bill",Fore.BLUE+"------")
            t.sleep(0.5)
            print("\n","\n","movie:",name,"\n","show time:",time,"\n","number of seats",seat,"\n","\n","cost of seats:","₹",cost_seat,"\n","Food and Beverages cost:","+","₹",cost_food,"\n","combo discount 15%:","-","₹",discount,"\n","final Food and Beverages cost:","₹",cost_food-discount)
            print()
            print(" total cost:","₹",total-discount)
            total_scalls(cost_seat,cost_food)
            exit=input(Fore.YELLOW+"\npress enter to takre another booking")
            if exit=="":
                os.system("cls")
                break
            break
        elif addon in "noNoNO":
            os.system("cls")
            print("You Haven't Taken any Addon")
            print()
            print(Fore.BLUE+"------",Fore.LIGHTMAGENTA_EX+"final bill",Fore.BLUE+"------")
            t.sleep(0.5)
            print("\n","\n","movie:",name,"\n","show time:",time,"\n","number of seats",seat,"\n","\n","cost of seats:","₹",cost_seat,"\n","Food and Beverages cost:","+","₹","0","\n","combo discount 5%:","-","₹","0","\n","final Food and Beverages cost:","₹","0")
            print()
            print(" total cost:","₹",cost_seat)
            total_scalls(cost_seat)
            exit=input(Fore.YELLOW+"\npress enter to take another order")
            if exit=="":
                os.system("cls")
                break
            break
        else:
            os.system("cls")
            print(Fore.RED+"invalid entery","\n","try again")
            continue
def starting():
    while True:
        print("\t",Fore.BLUE+"------",Fore.LIGHTMAGENTA_EX+"welcome",Fore.BLUE+"------","\n\n")
        t.sleep(0.5)
        print("to scheduled a movie- \t\t enter:1\nto take booking- \t\t enter:2\nto exit- \t\t\t enter:0\n ")
        t.sleep(0.5)
        selection_initial=(input(Fore.YELLOW+"select what you choice:"))
        if int(selection_initial)==1:
            os.system("cls")
            movie_input()
            continue
        elif int(selection_initial)==2:
            os.system("cls")
            name,time,seat,cost_seat=movie_output()
            addloop(name,time,seat,cost_seat)
            continue
        elif int(selection_initial)==0:
            with open('movie_sails.dat', 'rb') as f:
                dict=p.load(f)
                food=dict["sails_f"]
                seat=dict["sails_s"]
                os.system("cls")
                print(Fore.BLUE+"\t....",Fore.LIGHTMAGENTA_EX+"total sails",Fore.BLUE+"....","\nfrom seetd = ",seat,"\tfrom food and beverages = ",food)
            while True:
                print(Fore.GREEN+"enter 1","for clearing todays data else",Fore.GREEN+"press enter","key to pass:",end=" ")
                clear=input("")
                if clear=="1":
                    with open('movie_sails.dat', 'wb') as f:
                        d={"sails_f":0,"sails_s":0}
                        p.dump(d,f)
                    with open('movie.dat', 'wb') as f:
                        dict={}
                        p.dump(dict,f)
                    break
                elif clear=="":
                    break
                else:
                    continue
            break
        else:
            os.system("cls")
            print(Fore.RED+"invalit entery, please try again....")
            continue
def total_scalls(sails_seat=0,sails_food=0):
    with open('movie_sails.dat','rb') as f:
        dict=p.load(f)
        food=dict["sails_f"]+sails_food
        seat=dict["sails_s"]+sails_seat
    with open('movie_sails.dat', 'wb') as f:
        dict={"sails_f":food,"sails_s":seat}
        p.dump(dict,f)
os.system("cls")
starting()