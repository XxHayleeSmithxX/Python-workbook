#message = open('315-message.txt','w')
#message.write('Testing file for player configuration\n')
#message.write('Testing file for player score\n')
#message.close()

#message = open('315-message.txt','a')
#message.write('spencer\n')
#message.close()

with open('318-message.text', 'w') as message:
    message.write('Testing file for player configuration\n')
    message.write('Testing file for player score\n')
    print('file created')
    print(message.read())