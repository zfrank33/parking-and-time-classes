from fcntl import F_GET_SEALS


class ParkingSim():
    def __init__ (self):
        self.ticket_name = input('Please enter your name... ')
        self.park_spaces = {}
        self.tickets = [1,2,3,4,5,6,7,8,9,10]
    def pick_ticket(self):
        if len(self.tickets) > 0:
            self.park_spaces[self.ticket_name] = self.tickets.pop()
            print(f'Your ticket number is {self.park_spaces[self.ticket_name]}')
            print(self.park_spaces)
        if len(self.tickets) == 0:
            print("Sorry, lot full")
    def pay_ticket(self):
        print(f'Your ticket is {self.park_spaces}. Payment amount is $5. Please insert payment amount.')
        payment = input("Please enter payment amount. ")
        if payment == '$5':
            self.park_spaces.clear()
            self.tickets = [1,2,3,4,5,6,7,8,9,10]
            print(self.park_spaces)
            print("Payment successful.")
        else:
            print("Payment failed. Please try again.")
    def leave_lot(self):
        prompt = input("Are you sure you would like to leave? ")
        if prompt.lower() == "yes":
            if len(self.park_spaces) == 0:
                print("Thank you for coming!")
            else:
                print("Error! Payment must be made. Try again!")
                main()
parking_sim = ParkingSim()
def main():
    while True:
        prompt = input("Thank you for choosing city parking! Please pick from the following options: ticket/pay/leave \n")
        if prompt.lower() == "ticket":
            parking_sim.pick_ticket()
        if prompt.lower() == "pay":
            parking_sim.pay_ticket()
        if prompt.lower() == "leave":
            parking_sim.leave_lot()
            break
main()        



