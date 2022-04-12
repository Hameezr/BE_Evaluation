import re

class Error(Exception):
    pass
class NegativeAge(Error):
    pass
class UnderAgeError(Error):
    pass
class DuplicateUsername(Error):
    pass
class InvalidEmail(Error):
    pass

def main():
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    data = [('hameezr', 'hameezr@gmail.com', 24),
            ('Jon', 'jon@snow.com', 28),
            ('tyrion', 'tyrion@lannister.com', 25),
            ('cersie', 'cersie@lannister.com', 24),
            ('tommy', 'tommy@baratehon.com', 13),
            ('cersie', 'cersie@lannister.co', 17),
            ('joffrey', 'joffrey@baratehon.com', -2),
            ('Sansa', 'sansastark.com', 29)]
    user_dict = dict()
    for user in data:
        try:
            if user[2] < 0:
                raise NegativeAge()
            elif user[2] < 16:
                raise UnderAgeError()
            elif user[0] in user_dict:
                raise DuplicateUsername()
            elif not(re.fullmatch(regex, user[1])):
                raise InvalidEmail()
            else:
                user_dict.update({user[0]: user[1]})
        except NegativeAge:
            print('couldn\'t add', user[0], 'since invalid age is entered')
        except UnderAgeError:
            print('couldn\'t add', user[0], 'since they are under 16 years of age')
        except DuplicateUsername:
            print('couldn\'t add', user[0], 'since this username has already been used')
        except InvalidEmail:
            print('couldn\'t add', user[0], 'since this email is not valid')        
    
    print(user_dict)

main()
