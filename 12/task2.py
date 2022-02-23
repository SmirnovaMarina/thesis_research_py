# Coffee machine simulator

DEFAULT_ITEM_COUNT = 10


class ItemSupply:
  def __init__(self, name, amount = DEFAULT_ITEM_COUNT):
    self.name = name
    self.quantity = amount

  def use(self):
    if self.quantity <= 0:
      raise Exception(f'Ran out of {self.name}')
    self.quantity -= 1

  def refill(self, amount = DEFAULT_ITEM_COUNT):
    self.quantity = amount


class CoffeeMachine:
  def __init__(self):
    self.coffee = ItemSupply('coffee', 12)
    self.milk = ItemSupply('milk', 12)
    self.cups = ItemSupply('cups', 15)
    self.sugar = ItemSupply('sugar', 10)
    self.on = False

  def turn_on(self):
    self.on = True

  def turn_off(self):
    self.on = False

  def serve_cup(self, sugar=False):
    if not self.on:
      raise Exception('Machine is turned off')
    resources = [self.coffee, self.milk, self.cups]
    if sugar:
      resources.append(self.sugar)
    for item in resources:
      item.use()

  def display_supply(self):
    print('Remaining supplies:')
    for item in [self.coffee, self.milk, self.cups, self.sugar]:
      print(f'\t{item.name}: {item.quantity}')

  def reload_supplies(self):
    if self.on:
      raise Exception('Cannot reload supplies while machine is on')
    for item in [self.coffee, self.milk, self.cups, self.sugar]:
      item.refill(DEFAULT_ITEM_COUNT)


actions = {
  'q': 'Quit the program',
  '1': 'Brew a cup of coffee',
  '1': 'Brew a cup of coffee',
  '2': 'Display remaining supplies',
  '3': 'Turn the machine on',
  '4': 'Turn the machine off',
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
  print()
  return int(action)


def prompt_sugar():
  print('Do you want to add sugar? (y/n) ', end='')
  sugar = input()
  if sugar not in ['y', 'n']:
    raise Exception('Invalid answer')
  return sugar == 'y'

machine = CoffeeMachine()

if __name__ == '__main__':
  while True:
    print('Machine state: ', 'on ✅' if machine.on else 'off ❌')
    cmd = prompt_main_action()
    if cmd == 1:
      sugar = prompt_sugar()
      machine.serve_cup(sugar=sugar)
      print('Here is your coffee: ☕')
    elif cmd == 2:
      machine.display_supply()
    elif cmd == 3:
      machine.turn_on()
    elif cmd == 4:
      machine.turn_off()
    print()
