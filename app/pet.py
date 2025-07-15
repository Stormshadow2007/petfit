pet_status = {
    'name': 'Fluffy',
    'strength': 5,
    'speed': 5,
    'level': 1
}

def update_pet(action):
    if action == 'workout':
        pet_status['strength'] += 1
    elif action == 'run':
        pet_status['speed'] += 1
    
    # Simple leveling system
    total = pet_status['strength'] + pet_status['speed']
    pet_status['level'] = total // 5