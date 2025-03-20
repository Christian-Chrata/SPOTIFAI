from tabulate import tabulate

music = [
    {'MUSICID': '1', 'NAME': 'item of the Stars', 'GENRE': 'Pop', 'ARTIST': 'John Doe', 'YEAR': '2023', 'DURATION': 225},
    {'MUSICID': '2', 'NAME': 'Waves of Love', 'GENRE': 'Rock', 'ARTIST': 'The Ocean Band', 'YEAR': '2021', 'DURATION': 240},
    {'MUSICID': '3', 'NAME': 'Echoes in Time', 'GENRE': 'Jazz', 'ARTIST': 'Jane Smith', 'YEAR': '2022', 'DURATION': 312},
    {'MUSICID': '4', 'NAME': 'Under the Moonlight', 'GENRE': 'Pop', 'ARTIST': 'Tom Johnson', 'YEAR': '2020', 'DURATION': 210},
    {'MUSICID': '5', 'NAME': 'Rolling Hills', 'GENRE': 'Folk', 'ARTIST': 'The Woodworkers', 'YEAR': '2019', 'DURATION': 230},
    {'MUSICID': '6', 'NAME': 'Midnight Drive', 'GENRE': 'Electronic', 'ARTIST': 'DJ Flash', 'YEAR': '2023', 'DURATION': 260},
    {'MUSICID': '7', 'NAME': 'Dancing Shadows', 'GENRE': 'Pop', 'ARTIST': 'Anna Grace', 'YEAR': '2021', 'DURATION': 215},
    {'MUSICID': '8', 'NAME': 'Dreamscape', 'GENRE': 'Ambient', 'ARTIST': 'The Tranquils', 'YEAR': '2022', 'DURATION': 370},
    {'MUSICID': '9', 'NAME': 'Desert Sunrise', 'GENRE': 'Rock', 'ARTIST': 'Rock Nomads', 'YEAR': '2020', 'DURATION': 300},
    {'MUSICID': '10', 'NAME': 'City Lights', 'GENRE': 'Pop', 'ARTIST': 'The Night Crew', 'YEAR': '2023', 'DURATION': 245},
    {'MUSICID': '11', 'NAME': 'Golden Horizons', 'GENRE': 'Folk', 'ARTIST': 'Sarah and the Winds', 'YEAR': '2019', 'DURATION': 225},
    {'MUSICID': '12', 'NAME': 'Electric Pulse', 'GENRE': 'Electronic', 'ARTIST': 'Luna Waves', 'YEAR': '2022', 'DURATION': 255},
    {'MUSICID': '13', 'NAME': 'Tides of Emotion', 'GENRE': 'Jazz', 'ARTIST': 'The Velvet Jazz', 'YEAR': '2021', 'DURATION': 325},
    {'MUSICID': '14', 'NAME': 'After the Storm', 'GENRE': 'Rock', 'ARTIST': 'The Stormchasers', 'YEAR': '2020', 'DURATION': 290},
    {'MUSICID': '15', 'NAME': 'Summer Breeze', 'GENRE': 'Pop', 'ARTIST': 'Lily Parker', 'YEAR': '2023', 'DURATION': 200},
    {'MUSICID': '16', 'NAME': 'Silent Nights', 'GENRE': 'Classical', 'ARTIST': 'The Symphony Orchestra', 'YEAR': '2022', 'DURATION': 360},
    {'MUSICID': '17', 'NAME': 'Heartbeats', 'GENRE': 'Pop', 'ARTIST': 'Nina Rose', 'YEAR': '2021', 'DURATION': 250},
    {'MUSICID': '18', 'NAME': 'Lost in Time', 'GENRE': 'Electronic', 'ARTIST': 'Echo Chamber', 'YEAR': '2023', 'DURATION': 330},
    {'MUSICID': '20', 'NAME': 'Whispers of the Wind', 'GENRE': 'Ambient', 'ARTIST': 'Sonic Dreams', 'YEAR': '2020', 'DURATION': 425},
    {'MUSICID': '19', 'NAME': 'Crystal Dreams', 'GENRE': 'Folk', 'ARTIST': 'Crystal River Band', 'YEAR': '2021', 'DURATION': 265}
]

# ================================================================================
# Menu Section
# ================================================================================

def adminLogin():
    user = input('Please enter the password: ')
    if user == "CAPSTONE": return True
    return False

def exit(type='customer'):
    text = ''
    
    if type == 'customer':
        text = 'Are you sure you want to exit the application 🥺(Y/N)? '
    elif type == 'admin':
        text = 'Are you sure you want to exit admin mode (Y/N)? '
        
    user = input(text).upper()
    if (user == 'Y') or (user == 'YES'): return True
    return False

def mainMenu(type='customer'):
    if type == 'customer':
        while True:
            print(60*'\n')
            print('''
[\033[1mSPOTIFAI\033[0m]

[1] Search music
[2] Exit
[0] Admin mode
        ''')
            user = (input('Select menu: '))
            
            if user == '1': # Search music
                searchMenu()
            elif user == '2': # Exit
                if exit('customer'):
                    break
            elif user == '0': # Admin mode
                if adminLogin(): mainMenu('admin')
            else:
                print(f'The option "{user}" is not valid 🙏')
                input('Press enter... ')
    elif type == 'admin':
        while True:
            print(60*'\n')
            print('''
[\033[1mADMIN SPOTIFAI\033[0m]

[1] Search music
[2] Add music
[3] Edit music
[4] Delete music
[5] Exit admin mode
        ''')
            user = (input('Select menu: '))
            
            if user == '1': # Search music
                searchMenu('admin')
            elif user == '2': # Add music
                createMenu()
            elif user == '3': # Edit music
                updateMenu()
            elif user == '4': # Delete music
                deleteMenu()
            elif user == '5': # Admin mode
                if exit('admin'): break
            else:
                print(f'The option "{user}" is not valid 🙏')
                input('Press enter... ')
            

# ================================================================================
# READ Section
# ================================================================================

def show(type='customer', data=[]):
    print(60*'\n')
    print('Music list:')
    if type == 'customer': # NAME | GENRE | ARTIST | YEAR | DURATION
        print(tabulate(
            data, 
            headers=['Music name', 'Music genre', 'Artist', 'Release year', 'Song duration'], 
            tablefmt='heavy_grid'
            ))
    elif type == 'admin': # Music ID | Name | Genre | Artist | Year | Duration
        print(tabulate(
            data, 
            headers=['Music ID', 'Music name', 'Music genre', 'Artist', 'Release year', 'Song duration'], 
            tablefmt='heavy_grid'
            ))

def read(type='customerShowAll'):
    data = []
    
    if type == 'customerShowAll': # Customer show all music list
        for item in music:
            _DURATUION = f'{item['DURATION']//60}:{item['DURATION']%60}'
            data.append([
                item['NAME'], 
                item['GENRE'],
                item['ARTIST'], 
                item['YEAR'],
                _DURATUION
            ])
            
        if len(data) > 0:
            show('customer', data)
        else: print('There are no music items 🙏')
    
    elif type == 'customerShowKeyword': # Customer filter by keyword name, genre, and artist
        user = input('Enter a music keyword: ')
        
        for item in music:
            text = f'{item['NAME']}{item['GENRE']}{item['ARTIST']}'
            if user.lower() in text.lower():
                _DURATUION = f'{item['DURATION']//60}:{item['DURATION']%60}'
                data.append([
                    item['NAME'], 
                    item['GENRE'],
                    item['ARTIST'], 
                    item['YEAR'],
                    _DURATUION
                ])
        
        if len(data) > 0:
            show('customer', data)
        else: print(f'There are no music items with the keyword "{user}" 🙏')
        
    elif type == 'customerSortGenre': # Customer sort by genre
        for item in music:
            _DURATUION = f'{item['DURATION']//60}:{item['DURATION']%60}'
            data.append([
                item['NAME'], 
                item['GENRE'],
                item['ARTIST'], 
                item['YEAR'],
                _DURATUION
            ])
        
        for i in range(len(data)):
            for j in range(i + 1, len(data)):
                if data[i][1] > data[j][1]: data[i], data[j] = data[j], data[i]
                    
        if len(data) > 0:
            show('customer', data)
        else: print(f'There are no music items 🙏')

    elif type == 'adminShowAll': # Admin show all music list
        for item in music:
            _DURATUION = f'{item['DURATION']//60}:{item['DURATION']%60}'
            data.append([
                item['MUSICID'],
                item['NAME'], 
                item['GENRE'],
                item['ARTIST'], 
                item['YEAR'],
                _DURATUION
            ])
            
        if len(data) > 0:
            show('admin', data)
        else: print('There are no music items 🙏')
        
    elif type == 'adminShowKeyword': # admin filter by keyword id, name, genre, and artist
        user = input('Enter a music keyword: ')
        
        for item in music:
            text = f'{item['MUSICID']}{item['NAME']}{item['GENRE']}{item['ARTIST']}'
            if user.lower() in text.lower():
                _DURATUION = f'{item['DURATION']//60}:{item['DURATION']%60}'
                data.append([
                    item['MUSICID'],
                    item['NAME'], 
                    item['GENRE'],
                    item['ARTIST'], 
                    item['YEAR'],
                    _DURATUION
                ])
        
        if len(data) > 0:
            show('admin', data)
        else: print(f'There are no music items with the keyword "{user}" 🙏')
        
    elif type == 'adminSortGenre': # Admin sort by genre
        for item in music:
            _DURATUION = f'{item['DURATION']//60}:{item['DURATION']%60}'
            data.append([
                item['MUSICID'],
                item['NAME'], 
                item['GENRE'],
                item['ARTIST'], 
                item['YEAR'],
                _DURATUION
            ])
        
        for i in range(len(data)):
            for j in range(i + 1, len(data)):
                if data[i][2] > data[j][2]: data[i], data[j] = data[j], data[i]
                    
        if len(data) > 0:
            show('admin', data)
        else: print(f'There are no music items 🙏')
    input('Press enter... ')

def searchMenu(type='customer'):
    while True:
        print(60*'\n')
        print('''
[\033[1mSearch Music\033[0m]

[1] Show all music
[2] Search music by keyword
[3] Sort by genre
[4] Back to main menu
    ''')
        user = (input('Select menu: '))
        
        if user == '1': # Show all music
            if type=='admin': read('adminShowAll')
            else: read('customerShowAll')
        elif user == '2': # Search music by keyword
            if type=='admin': read('adminShowKeyword')
            else: read('customerShowKeyword')
        elif user == '3': # Sort by genre
            if type=='admin': read('adminSortGenre')
            else: read('customerSortGenre')
        elif user == '4': # Back to main menu
            break
        else:
            print(f'The option "{user}" is not valid 🙏')
            input('Press enter... ')

# ================================================================================
# CREATE Section
# ================================================================================

def create(type='createSingle'):
    print(60*'\n')
    data=[]
    
    if type == 'createSingle':
        _dict={
            'MUSICID': None,
            'NAME': None,
            'GENRE': None,
            'ARTIST': None,
            'YEAR': None,
            'DURATION': None,
        }
        
        user=input('Enter the music id: ')
        
        if user.isdigit():
            _dict['MUSICID'] = user
            
            for item in music:
                if item['MUSICID'] == user: 
                    print('The music ID already exists!')
                    _dict['MUSICID'] = None
                    break
                
        else: print('The music ID must be numeric!')
        
        if _dict['MUSICID'] != None:
            _dict['NAME']=input('Enter the music name: ') # Name
            
            while True: # Genre
                print('Genre list: Ambient, Classical, Electronic, Folk, Jazz, Pop and Rock')
                user=input('Enter the music genre: ').capitalize()
                
                if (user=='Ambient') or (user=='Classical') or (user=='Electronic') or (user=='Folk') or (user=='Jazz') or (user=='Pop') or (user=='Rock'):
                    _dict['GENRE'] = user 
                else: 
                    print(f'The music genre {user} doesnt exists!')
                    
                if _dict['GENRE'] != None: break
                
            _dict['ARTIST']=input('Enter the artist name: ').title() # Artist
            
            while True: # Year
                user=input('Enter the year the music was released: ')
                
                if user.isdigit() == False:
                    print('The year must be a number (e.g., 2000).')
                else: _dict['YEAR'] = user 
                
                if _dict['YEAR'] != None: break
                
            while True: # Song duration
                user=input('Enter the duration of the song in seconds: ')
                
                if user.isdigit() == False:
                    print('The duration of the song must be in seconds (e.g., 185).')
                else: _dict['DURATION'] = int(user)
                
                if _dict['DURATION'] != None: break
            
            data.append(_dict)
        
    elif type == 'createBatch':
        while True:
            _dict={
                'MUSICID': '0',
                'NAME': None,
                'GENRE': None,
                'ARTIST': None,
                'YEAR': None,
                'DURATION': None,
            }
            
            if len(data) > 0:
                for item in data:
                    if _dict['MUSICID'] <= item['MUSICID']:
                        _dict['MUSICID'] = f'{int(item['MUSICID']) + 1}'
            else:
                for item in music:
                    if _dict['MUSICID'] <= item['MUSICID']:
                        _dict['MUSICID'] = f'{int(item['MUSICID']) + 1}'
            
            _dict['NAME']=input('Enter the music name: ') # Name
            
            while True: # Genre
                print('Genre list: Ambient, Classical, Electronic, Folk, Jazz, Pop and Rock')
                user=input('Enter the music genre: ').capitalize()
                
                if (user=='Ambient') or (user=='Classical') or (user=='Electronic') or (user=='Folk') or (user=='Jazz') or (user=='Pop') or (user=='Rock'):
                    _dict['GENRE'] = user 
                else: 
                    print(f'The music genre {user} doesnt exists!')
                    
                if _dict['GENRE'] != None: break
                
            _dict['ARTIST']=input('Enter the artist name: ').title() # Artist
            
            while True: # Year
                user=input('Enter the year the music was released: ')
                
                if user.isdigit() == False:
                    print('The year must be a number (e.g., 2000).')
                else: _dict['YEAR'] = user 
                
                if _dict['YEAR'] != None: break
                
            while True: # Song duration
                user=input('Enter the duration of the song in seconds: ')
                
                if user.isdigit() == False:
                    print('The duration of the song must be in seconds (e.g., 185).')
                else: _dict['DURATION'] = int(user)
                
                if _dict['DURATION'] != None: break
            
            data.append(_dict)
            
            user = input('\nDo you want to add another music? (Y/N) ').upper()
            if (user == 'Y') or (user == 'YES'):
                continue
            else: break
    
    if len(data) > 0:
        _data = []
        for item in data:
            _DURATUION = f'{item['DURATION']//60}:{item['DURATION']%60}'
            _data.append(
                [
                    item['MUSICID'],
                    item['NAME'],
                    item['GENRE'],
                    item['ARTIST'],
                    item['YEAR'],
                    _DURATUION
                ]
            )
            
        show('admin', _data)
        user = input('Are you sure you want to add the music above (Y/N): ').upper()
        if (user == 'Y') or (user == 'YES'):
            music.extend(data)
            print('The music has been successfully saved.')
        else: print('The process has been canceled')
        
    input('Press enter... ')
    
def createMenu():
    while True:
        print(60*'\n')
        print('''
[\033[1mAdd Music\033[0m]

[1] Add music
[2] Add music batches
[3] Back to main menu
    ''')
        user = (input('Select menu: '))
        
        if user == '1': # Add music
            create('createSingle')
        elif user == '2': # Add music batches
            create('createBatch')
        elif user == '3': # Back to main menu
            break
        else:
            print(f'The option "{user}" is not valid 🙏')
            input('Press enter... ')

# ================================================================================
# UPDATE Section
# ================================================================================

def update(type='updateNormal'):
    print(60*'\n')
    _BEFORE={
        'MUSICID': None,
        'NAME': None,
        'GENRE': None,
        'ARTIST': None,
        'YEAR': None,
        'DURATION': None,
    }
    
    _AFTER={
        'MUSICID': None,
        'NAME': None,
        'GENRE': None,
        'ARTIST': None,
        'YEAR': None,
        'DURATION': None,
    }
    
    _data = []
    for item in music:
        _DURATUION = f'{item['DURATION']//60}:{item['DURATION']%60}'
        _data.append(
            [
                item['MUSICID'],
                item['NAME'],
                item['GENRE'],
                item['ARTIST'],
                item['YEAR'],
                _DURATUION
            ]
        )
    show('admin', _data)
    
    if type == 'updateNormal': # Normal update
        user = input('Enter the music id: ')
        for item in music:
            if item['MUSICID'] == user:
                _BEFORE = item
                _AFTER['MUSICID'] = item['MUSICID']
                break
        
        if _AFTER['MUSICID'] != None:
            _DURATUION = f'{_BEFORE['DURATION']//60}:{_BEFORE['DURATION']%60}'
            _data = []
            _data.append(
                [
                    _BEFORE['MUSICID'],
                    _BEFORE['NAME'],
                    _BEFORE['GENRE'],
                    _BEFORE['ARTIST'],
                    _BEFORE['YEAR'],
                    _DURATUION
                ]
            )
            show('admin', _data)
            user = input('Do you want to update the music above? (Y/N) ').upper()
            if (user == 'Y') or (user == 'YES'):
                _AFTER['NAME']=input('Enter the music name: ') # Name
                
                while True: # Genre
                    print('Genre list: Ambient, Classical, Electronic, Folk, Jazz, Pop and Rock')
                    user=input('Enter the music genre: ').capitalize()
                    
                    if (user=='Ambient') or (user=='Classical') or (user=='Electronic') or (user=='Folk') or (user=='Jazz') or (user=='Pop') or (user=='Rock'):
                        _AFTER['GENRE'] = user 
                    else: 
                        print(f'The music genre {user} doesnt exists!')
                        
                    if _AFTER['GENRE'] != None: break
                    
                _AFTER['ARTIST']=input('Enter the artist name: ').title() # Artist
                
                while True: # Year
                    user=input('Enter the year the music was released: ')
                    
                    if user.isdigit() == False:
                        print('The year must be a number (e.g., 2000).')
                    else: _AFTER['YEAR'] = user 
                    
                    if _AFTER['YEAR'] != None: break
                    
                while True: # Song duration
                    user=input('Enter the duration of the song in seconds: ')
                    
                    if user.isdigit() == False:
                        print('The duration of the song must be in seconds (e.g., 185).')
                    else: _AFTER['DURATION'] = int(user)
                    
                    if _AFTER['DURATION'] != None: break
                
                _data = []
                _data.append(
                    [
                        'Before',
                        _BEFORE['MUSICID'],
                        _BEFORE['NAME'],
                        _BEFORE['GENRE'],
                        _BEFORE['ARTIST'],
                        _BEFORE['YEAR'],
                        f'{_BEFORE['DURATION']//60}:{_BEFORE['DURATION']%60}'
                    ]
                )
                _data.append(
                    [
                        'After',
                        _AFTER['MUSICID'],
                        _AFTER['NAME'],
                        _AFTER['GENRE'],
                        _AFTER['ARTIST'],
                        _AFTER['YEAR'],
                        f'{_AFTER['DURATION']//60}:{_AFTER['DURATION']%60}'
                    ]
                )
                show('admin', _data)
                
                user = input('Are you sure you want to make changes? (Y/N) ').upper()
                if (user == 'Y') or (user == 'YES'):
                    for item in music:
                        if item == _BEFORE:
                            item['MUSICID'] =  _AFTER['MUSICID']
                            item['NAME'] =  _AFTER['NAME']
                            item['GENRE'] =  _AFTER['GENRE']
                            item['ARTIST'] =  _AFTER['ARTIST']
                            item['YEAR'] =  _AFTER['YEAR']
                            item['DURATION'] =  _AFTER['DURATION']
                    print('The music item has been updated successfully.')
                else: print('The process has been canceled')
            else: print('The process has been canceled')
        else: print('There are no music items 🙏')
        
    # user = input('Are you sure you want to add the music above (Y/N): ').upper()
    # if (user == 'Y') or (user == 'YES'):
    #     music.extend(data)
    #     print('The music has been successfully saved.')
    # else: print('The process has been canceled')
        
    input('Press enter... ')

def updateMenu():
    while True:
        print(60*'\n')
        print('''
[\033[1mEdit Music\033[0m]

[1] Edit music by music id
[2] Back to main menu
    ''')
        user = (input('Select menu: '))
        
        if user == '1': # Edit music by music id
            update('updateNormal')
        elif user == '2': # Back to main menu
            break
        else:
            print(f'The option "{user}" is not valid 🙏')
            input('Press enter... ')

# ================================================================================
# DELETE Section
# ================================================================================
    
recycle = []

def delete(type='deleteMusicID'):
    data=[]
    if type == 'deleteMusicID':
        _data=[]
        for item in music:
            _DURATUION = f'{item['DURATION']//60}:{item['DURATION']%60}'
            _data.append([
                item['MUSICID'],
                item['NAME'], 
                item['GENRE'],
                item['ARTIST'], 
                item['YEAR'],
                _DURATUION
            ])
            
        if len(_data) > 0:
            show('admin', _data)
            user = input('Please provide the music ID you would like to delete: ')
            
            for item in music:
                if item['MUSICID'] == user:
                    data.append([
                        item['MUSICID'],
                        item['NAME'], 
                        item['GENRE'],
                        item['ARTIST'], 
                        item['YEAR'],
                        item['DURATION']
                    ])
                    break
                
    elif type == 'deleteAllMusic':
        _data=[]
        for item in music:
            _data.append([
                item['MUSICID'],
                item['NAME'], 
                item['GENRE'],
                item['ARTIST'], 
                item['YEAR'],
                item['DURATION']
            ])
            
        if len(_data) > 0:
            show('admin', _data)
            
            data = _data
        
    elif type == 'restoreDeletedMusic':
        _data=[]
        for item in recycle:
            _DURATUION = f'{item['DURATION']//60}:{item['DURATION']%60}'
            _data.append([
                item['MUSICID'],
                item['NAME'], 
                item['GENRE'],
                item['ARTIST'], 
                item['YEAR'],
                item['DURATION']
            ])
            
        if len(_data) > 0:
            show('admin', _data)
            user = input('Please provide the music ID you would like to restore: ')
            
            for item in recycle:
                if item['MUSICID'] == user:
                    data.append([
                        item['MUSICID'],
                        item['NAME'], 
                        item['GENRE'],
                        item['ARTIST'], 
                        item['YEAR'],
                        item['DURATION']
                    ])
                    break
    
    if len(data) > 0: 
        show('admin', data)
        if type == 'restoreDeletedMusic':
            user = input('Are you sure you want to restore the music listed above (Y/N): ').upper()
            if (user == 'Y') or (user == 'YES'):
                for item in data:
                    recycle.remove(
                        {
                            'MUSICID': item[0],
                            'NAME': item[1], 
                            'GENRE': item[2], 
                            'ARTIST': item[3], 
                            'YEAR': item[4], 
                            'DURATION': item[5]
                        }
                    )
                    
                    music.append(
                        {
                            'MUSICID': item[0],
                            'NAME': item[1], 
                            'GENRE': item[2], 
                            'ARTIST': item[3], 
                            'YEAR': item[4], 
                            'DURATION': item[5]
                        }
                    )
                print('The music item has been restored successfully.')
            else: print('The process has been canceled')
        else:
            user = input('Are you sure you want to delete the music listed above (Y/N): ').upper()
            if (user == 'Y') or (user == 'YES'):
                for item in data:
                    music.remove(
                        {
                            'MUSICID': item[0],
                            'NAME': item[1], 
                            'GENRE': item[2], 
                            'ARTIST': item[3], 
                            'YEAR': item[4], 
                            'DURATION': item[5]
                        }
                    )
                    
                    recycle.append(
                        {
                            'MUSICID': item[0],
                            'NAME': item[1], 
                            'GENRE': item[2], 
                            'ARTIST': item[3], 
                            'YEAR': item[4], 
                            'DURATION': item[5]
                        }
                    )
                print('The music item has been deleted successfully.')
            else: print('The process has been canceled')
    else: print('There are no music items 🙏')
        
    input('Press enter... ')
    
def deleteMenu():
    while True:
        print(60*'\n')
        print('''
[\033[1mDelete Music\033[0m]

[1] Delete by MusicID
[2] Delete all music
[3] Restore deleted music
[4] Back to main menu
    ''')
        user = (input('Select menu: '))
        
        if user == '1': # Delete by MusicID
            delete('deleteMusicID')
        elif user == '2': # Delete all music
            delete('deleteAllMusic')
        elif user == '3': # Restore deleted music
            delete('restoreDeletedMusic')
        elif user == '4': # Back to main menu
            break
        else:
            print(f'The option "{user}" is not valid 🙏')
            input('Press enter... ')

# ================================================================================
    
mainMenu('customer')