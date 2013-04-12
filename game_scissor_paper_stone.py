#!/usr/bin/python2.7
import random
comp_wins=(1,2,-3,-4)
user_wins=(-1,-2,3,4)
play='y'
while (play=='y'):

	s={1:'Rock',2:'Spock',3:'Paper',4:'Lizard',5:'Scissor'}
	for k, v in s.items(): print 'Enter', k, 'for', v

	# taking input from user
	user_choice=int(raw_input('Enter your choice\t:'))
	while (user_choice) not in range(1,6):
		user_choice=int(raw_input('Enter choice between 1 to 5\t:'))
	print 'You choosed :',s[(user_choice)]

	# computer's choice

	comp_choice = random.randint(1,5)
	print 'Computer choosed :',s[comp_choice]

	if (comp_choice-user_choice in comp_wins):
		print 'Computer wins the game ! :('
	elif(comp_choice-user_choice in user_wins):
		print '!! HURRAY !! You win the game ! :)'
	else:
		print 'There is a tie ! \n '
		
	play=raw_input('Want to play again ? (y/n)' )	
	while play not in ('y','n'):
		play=raw_input('Enter the CORRECT choice. (y/n)' )

print 'Thank you for playing the game. \n Have a nice Day. '
