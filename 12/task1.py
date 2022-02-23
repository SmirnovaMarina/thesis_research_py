# Seats booking simulator

SEATS_PER_ROOM = 10
TIME_SLOTS = ['10:00', '15:00', '20:00']
price = 10


class SeatingManager:
  def __init__(self):
    self.seats = [('_', None) for _ in range(SEATS_PER_ROOM)]

  def book(self, position: int, info: dict):
    if self.seats[position][0] == 'x':
      raise Exception('Seat already booked')
    self.seats[position] = ('x', info)

  def display(self):
    print('Seats:')
    for i, seat in enumerate(self.seats, 1):
      print(f'\t{i}: {seat[0]}')


schedule = {
  time: SeatingManager() for time in TIME_SLOTS
}

actions = {
  'q': 'Quit the program',
  '1': 'Book a ticket',
  '2': 'Display seating arrangement',
  '3': 'Check ticket price',
  '4': 'Change ticket price',
}


def prompt_main_action():
  print('Possible actions:')
  for key, description in actions.items():
    print(f'\t({key}): {description}')
  print('Please choose an action: ', end='')
  action = input()
  if action not in actions:
    raise Exception('Invalid action')
  if action == 'q':
    exit()
  return int(action)


def prompt_time_slot():
  print('Available time slots:')
  for i, time in enumerate(TIME_SLOTS, 1):
    print(f'\t({i}): {time}')
  print('Please select a time slot: ', end='')
  time_slot = int(input())
  if time_slot not in range(1, len(TIME_SLOTS) + 1):
    raise Exception('Invalid time slot')
  return TIME_SLOTS[time_slot]


def prompt_info():
  print('Please enter your information')
  print('\tFirst name: ', end='')
  first_name = input()
  print('\tLast name: ', end='')
  last_name = input()
  return {
    'first_name': first_name,
    'last_name': last_name,
  }


if __name__ == '__main__':
  while True:
    cmd = prompt_main_action()
    if cmd == 1:
      slot = prompt_time_slot()
      manager = schedule[slot]
      manager.display()
      print('Please select a seat: ', end='')
      seat = int(input()) - 1
      info = prompt_info()
      manager.book(seat, info)
    elif cmd == 2:
      slot = prompt_time_slot()
      manager = schedule[slot]
      manager.display()
    elif cmd == 3:
      print(f'The ticket price is ${price}')
    elif cmd == 4:
      print('Please enter the new price: ', end='')
      price = int(input())
    print()
