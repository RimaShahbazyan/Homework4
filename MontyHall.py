def MontyHall():
        import random
        n=100
        
        change_win=0
        change_count=0
        nochange_win=0
        doors=[1,2,3]
        changed=[True,False]
     
        for i in range(n):
                doors=[1,2,3]

                prize= random.choice(doors)
             
                choice=random.choice(doors)
                doors.remove(prize)
                if(prize!= choice):
                        doors.remove(choice)
                opened=doors[0]
                        

             
             
                print("""
             Prize is behind door {0}
             Contestant chooses door {1}
             Host opens door {2}""".format(prize,choice,opened))

             

                if random.choice(changed):
                        
                        change_count+=1
                        if (prize!=choice):
                                change_win +=1 
                                print("""
             Contestant switches the door from door {0} to door {1}
             Contestant  Won!""".format(choice,prize))
                        else:
                             print("""
             Contestant switches the door from door {0} to door {1}
             Contestant Lost""".format(choice,doors[1]))


                else:
                        print("""
               Contestant doesn't swtich the door""")
                        
                        if (prize==choice):
                               nochange_win += 1
                               print("""
               Contestant  Won!""")
                        else:
                               print("""
               Contestant  Lost!""")


        return [ change_win/change_count * 100 , nochange_win/(n-change_count)*100 ]

monty_hall=MontyHall()
print("Probability of winning when switching: {0}%".format(round(monty_hall[0],2)))
print("Probability of winning when NOT switching: {0}%".format(round(monty_hall[1],2)))


