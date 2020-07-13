class seats_bass:
    def __init__(self):
        file = open('seats.txt', 'w')
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
        seats = ''
        for i in arr:
            seats += '0'
        file.write(seats)

    def display_interface(self):
        choose = "1. Display status of all set.\n" \
                 "2. Reserve seats.\n" \
                 "3. Exit\n" \
                 "Please srlect your choice [1 , 2 , or 3] :"
        return choose
    def display_booking(self):
        file = open('seats.txt', 'r')
        seats_list = []
        cnt = 1
        for i in file.readline():
            if i == '0':
                seats_list.append(str(cnt))
            elif i == '1':
                seats_list.append('Reserved')
            cnt += 1
        file.close()
        display = ''
        cnt_done = 0
        cnt_available = 0
        done = '\n>>Number of none available = '
        available = '>>Number of available = '
        counter = 0
        for s in seats_list:
            if len(str(s)) > 2:
                display += " { " + str(s) + " } "
                counter += 1
            elif len(str(s)) > 1 and len(str(s)) < 3:
                display += " {    " + str(s) + "    } "
                counter += 1
            else:
                display += " {     " + str(s) + "    } "
                counter += 1
            if counter%4 == 0:
                display += '\n'
        for d in seats_list:
            if len(str(d)) > 3:
                cnt_done += 1
            else:
                cnt_available += 1
        done += str(cnt_done)
        available += str(cnt_available)
        display += done + "\n" + available
        return display ,cnt_available

    def bookings(self,set_new_seats):
        file = open('seats.txt', 'r')
        seats_list = []
        cnt = 1
        for i in file.readline():
            if i == '0':
                seats_list.append(str(cnt))
            else:
                seats_list.append('Reserved')
            cnt += 1
        file.close()

        file_new_bookings = open('seats.txt', 'w')
        cnt = 0
        for i in seats_list:
            for booking in set_new_seats:
                if i == str(booking):
                    seats_list[cnt] = "Reserved"
            cnt += 1
        set_seats = ''
        for d in seats_list:
            if len(str(d)) > 0 and len(str(d)) < 4:
                set_seats += "0"
            else:
                set_seats += "1"
        file_new_bookings.write(set_seats)


    def interface(self):
        stop = True
        while stop:
            print(self.display_interface())
            inputs = input()
            if inputs == '1':
                print(user.display_booking()[0])
            elif inputs == '2':
                try:
                    number_reserve = int(input("enter number reversed : "))
                except ValueError:
                    print("please inter number")
                    input("Press Enter to continue...")
                    user.interface()
                if self.display_booking()[1] == 0:
                    print("sorry is not avilable any seats")
                    input("Press Enter to continue...")
                    user.interface()
                elif number_reserve > self.display_booking()[1]:
                    print("sorry there are "+ str(self.display_booking()[1]) +" avilable.. enter less number")
                    input("Press Enter to continue...")
                    user.interface()
                elif number_reserve <= 0:
                    print("invalid number ..")
                    input("Press Enter to continue...")
                    user.interface()
                else:
                    reserves = []
                    for i in range(number_reserve):
                        try:
                            number = int(input("Enter seat number of required seat: "))
                            if number > 28:
                                print("please enter number less from 29")
                                input("Press Enter to continue...")
                                user.interface()
                            else:
                                reserves.append(number)
                        except ValueError:
                            print("please enter number")
                            input("Press Enter to continue...")
                            user.interface()

                    file = open('seats.txt', 'r')
                    seats_list = []
                    cnt = 0
                    for i in file.readline():
                        seats_list.append(i)
                    file.close()
                    while cnt < len(seats_list):
                        for booking in reserves:
                            if cnt+1 == booking:
                                if str(seats_list[cnt]) == '1':
                                    print("sorry this seat number ("+str(booking)+") is already taken")
                                    input("Press Enter to continue...")
                                    user.interface()

                        cnt +=1
                    user.bookings(reserves)
            elif inputs == '3':
                break
            else:
                print("Please Enter a number according to givin list")
                input("Press Enter to continue...")
                user.interface()

user = seats_bass()
user.interface()