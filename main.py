# This program will help me get unstuck when I am overwhelmed by choice.
# The focus here will be to select a task to do next.  
# There will be an option for me to input guidelines, or just have the
# program pick something itself.

# Functions defined here:
from random import randint

# Merge lists
def pick_random(list):
  n=len(list)
  i=randint(2,n-1)
  return list[i]

def pick_random_final(list):
  n=len(list)
  i=randint(0,n-1)
  return list[i]
 

# Lists of options
rescue=["i","p","do 5 minutes of restorative breathing","wrap up in a cosy blanket","write in your journal","talk to Deryk","make a hot chocolate","do a grounding activity","write in your bujo","use Autumn/Christmas visualisation distraction","listen to Christmas music","take a nap"]

passive_rest=["i","p","watch Thor Ragnarok","watch Loki","watch Ant-Man","watch Spiderman","watch The Good Place","watch Parks and Rec","watch Brooklyn 99","watch a new series","watch a new movie","scroll through Netflix and make a to-watch list","watch Harry Potter","make a Sugar and Sloth wishlist","scroll through Instagram for project ideas","do a guided meditation in the office"]

routine_chores=["i","g","wash the dishes", "clean the bathroom","tidy the office","complete one step of laundry","change the sheets","change the towels","dust"]

household_chores=["i","g","organise paperwork in the office","deep clean the kitchen","go through my wardrobe for donations","go through the kitchen cabinets and fridge","tidy the medicine shelf"]

creative_relaxed=["i","r","mend something","work on your granny squares","work on an embroidery project","organise your craft resources","make a craft project and craft supply wishlist"]

creative_goal=["i","g","work on your miniature library","create something miniature from polymer clay","create earrings from polymer clay","code something","plan Instagram posts"]

bujo=["i","r","make a holiday activity wishlist","make a do more/less list","revisit your resolutions and goals","make a calendar for the upcoming season","make pages for your work planner","make pages for your lesson palnner","make a weekly bujo layout to encourage daily journalling"]

read=["i","r","read my current book","re-read a Harry Potter book","read a new book from Mieke","read a new book from Deryk","read a new Rick Riordan book"]

learn=["i","g","meet your three daily goals on Duolingo","work on 'Python the Hard Way'","work on your French books"]

work_fun=["i","g","make Mathematician posters","work on data analysis","work through a week of lesson in the Y10 computing course","read Computer Science pedagogy resources"]

inside_movement=["i","r","do Beyonce sit-ups","do a Zumba class","do a Nike workout program","do a Nike yoga class"]

outside_adventure=["o","g","go to the V&A","go to the Science Museum","go into Chinatown and find a new ingredient","go to Chelsea and walk around","find day tickets to the theatre","visit Kew Gardens","visit Chiswick House","take the train somewhere new","walk along the South Bank"]

outside_rest=["o","p","listen to a podcast in the park","lay outside and soak up the sun","listen to a podcast in the garden","do a guided meditation in the garden"]

outside_walk=["o","r","walk to pick up boba","pick up groceries for a nice meal today","pick up pastries from Cut the Mustard","go for a walk around Tooting Common","go for a walk around Furzedown Park"]

master_list=[passive_rest,outside_walk,outside_adventure,inside_movement,work_fun,learn,read,bujo,creative_goal,creative_relaxed,household_chores,routine_chores,outside_rest]

easy_list=[learn,read,bujo,creative_relaxed,routine_chores,passive_rest]

today_list=[]


# Ask if I have capacity to answer any questions
print("Hello there!  Let's start with a check in.")
capacity=int(input("On a scale from 1 = super anxious to 9 = just indecisive, how are you feeling? "))


# Select an item from the rescue list
# Then give a follow up activity from passive rest
if capacity<2:
  activity_rescue=pick_random(rescue)
  activity_passive_rest=pick_random(passive_rest)
  print("\nFirst you should {}. \nThen just {}.  \nLater, if you're feeling up to something a bit more active, come back here for more advice.".format(activity_rescue,activity_passive_rest))

# Select an activity from the passive rest
elif capacity<5:
  activity_passive_rest=pick_random(passive_rest)
  print("\nSounds like some passive rest is the best choice. \nI recommend you {}.".format(activity_passive_rest))

# Filter by how much influence I want to have in the choice 
else:
  influence=input("\nHow involved in the decision process do you want to be? \n(a) I'll pick the categories, you make the final choice \n(b) I'll give a few parameters \n(c) No more choices, please\n").lower()
  if influence=="c":
    print("\nLet me take care of this for you.")
    today_list=easy_list

  elif influence=="b":
    print("\nLet's narrow down our options.")
    location=input("Where do you want to be? \n (a) inside\n (b) outside\n (c) not bothered\n").lower()
    energy=input("Do you want to be \n (a) passive\n (b) relaxed\n (c) goal-oriented\n (d) not bothered\n").lower()
  
    # Filter by location
    if location=="a":
      for index in range(len(master_list)):
        if master_list[index][0]=="i":
          today_list.append(master_list[index])

    elif location=="b":
      for index in range(len(master_list)):
        if master_list[index][0]=="o":
          today_list.append(master_list[index])

    else:
      today_list=master_list

  
    # Filter by energy         
    if energy=="a":
      to_remove=[]
      for index in range(len(today_list)):
        if today_list[index][1]=="r" or today_list[index][1]=="g":
          to_remove.append(today_list[index])
      for list in to_remove:
        today_list.remove(list)

    elif energy=="b":
      to_remove=[]
      for index in range(len(today_list)):
        if today_list[index][1]=="p" or today_list[index][1]=="g":
          to_remove.append(today_list[index])
      for list in to_remove:
       today_list.remove(list)

    elif energy=="c":
      to_remove=[]
      for index in range(len(today_list)):
        if today_list[index][1]=="p" or today_list[index][1]=="r":
          to_remove.append(today_list[index])
      for list in to_remove:
       today_list.remove(list)


  elif influence=="a":
    chores=input("Include chores? Y/N\n").lower()
    if chores=="y":
      today_list.append(routine_chores)
      today_list.append(household_chores)
    creative=input("Include creative activities? Y/N\n").lower()
    if creative=="y":
      today_list.append(creative_relaxed)
      today_list.append(creative_goal)
      today_list.append(bujo)
    thinking=input("Include reading and learning? Y/N\n").lower()
    if thinking=="y":
      today_list.append(read)
      today_list.append(learn)
    work=input("Include work fun? Y/N\n").lower()
    if work=="y":
      today_list.append(work_fun)
    out_sit=input("Include outside relaxing? Y/N\n").lower()
    if out_sit=="y":
      today_list.append(outside_sitspot)
      today_list.append(outside_rest)
    out_active=input("Include active outside activities? Y/N\n").lower()
    if out_active=="y":
      today_list.append(outside_adventure)
      today_list.append(outside_walk)
    

  # Create list of options, select at random, display result
  if len(today_list)==0:
    today_list=easy_list
  options=[]
  for i in range(0,len(today_list)):
    options+=today_list[i][2:]

  print("\nToday you should {}.".format(pick_random_final(options)))
  reroll=input("\nIf you would like one re-roll of your options, type RR: ").lower()
  if reroll=="rr":
    print("\nYou should {}.".format(pick_random_final(options)))
