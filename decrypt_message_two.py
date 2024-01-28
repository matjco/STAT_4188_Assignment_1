encrypted_file = open("encrypted_message_two.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write Code Here

encrypted_message_list = list(encrypted_message)
message = encrypted_message_list

i = 1
j = -i - 1

while i < j % len(encrypted_message):
    j = -i - 1

    #store the earlier character in the message
    temp = message[i]

    #assign the later character in the message to the earlier character
    message[i] = message[j]

    #assign the earlier character in the message to the later character
    message[j] = temp

    i += 2

message_str = "".join(message)

print(message_str)