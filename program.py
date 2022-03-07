
from calendar import c
from re import S
# from this import d
from KeycapSet import KeycapSet
from KeycapsRepository import KeycapsRepository
from KitRepository import KitRepository
from prettytable import PrettyTable

def update_sub_menu():
    name_input = input('What is the name of the set you would like to update?\n'\
                                '---> ')
    repo = KeycapsRepository()
    set_info = repo.get_set(name_input)
    keycap_id = set_info.id
    print()
    print(f'Returned Keycap set ID: {set_info.id}')
    print()
    update_menu =  f'WHAT WOULD YOU LIKE TO UPDATE FOR {keycap_id}?\n' \
                    '(n) Keycap Name (NYI)\n' \
                    '(c) Color\n' \
                    '(p) Printing (NYI)\n' \
                    '(u) Manufacturer\n' \
                    '(k) Kitting (NYI)\n' \
                    '(m) Material \n' \
                    '(v) Vendor (NYI)\n'\
                    '(x) Quit / finished udating'
    print(update_menu)
    choice = input('---> ')
    while choice.lower() != 'x':
        if choice == 'n':
            print()
            print('+---------------------------------+')
            print('|       NOT YET IMPLIMENTED       |')
            print('+---------------------------------+')
            print()
            print(update_menu)
            choice = input('---> ')

        elif choice == 'c':
            print()
            try:
                updated_info = repo.update_color(keycap_id)

                print()
                print('+---------------------------------+')
                print('|          COLOR UPDATED          |')
                print('+---------------------------------+')
                print()
                print(update_menu)
                choice = input('---> ')
            except:
                print('Color ID does not exist - color not updated')

        elif choice == 'p':
            print()
            print('+---------------------------------+')
            print('|       NOT YET IMPLIMENTED       |')
            print('+---------------------------------+')
            print()
            print(update_menu)
            choice = input('---> ')

        elif choice == 'u':
            print()
            updated_info = repo.update_manu(keycap_id)

            t = PrettyTable(['Set ID', \
                                'Set Name', \
                                'Manufacturer', \
                                'Material', \
                                'Printing Method', \
                                'Profile'])
            t.title = f'KeycapSet TABLE ROW FOR: "{updated_info.keycapName}"'
            t.add_row([updated_info.id, \
                    updated_info.keycapName, \
                    updated_info.manu, \
                    updated_info.material, \
                    updated_info.printingMethod, \
                    updated_info.profile])
            print(t)
            print()
            print(update_menu)
            choice = input('---> ')

        elif choice == 'm':
            print()
            updated_info = repo.update_material(keycap_id)

            t = PrettyTable(['Set ID', \
                                'Set Name', \
                                'Manufacturer', \
                                'Material', \
                                'Printing Method', \
                                'Profile'])
            t.title = f'KeycapSet TABLE ROW FOR: "{updated_info.keycapName}"'
            t.add_row([updated_info.id, \
                    updated_info.keycapName, \
                    updated_info.manu, \
                    updated_info.material, \
                    updated_info.printingMethod, \
                    updated_info.profile])
            print(t)
            print()
            print(update_menu)
            choice = input('---> ')

        elif choice == 'k':
            print()
            print('+---------------------------------+')
            print('|       NOT YET IMPLIMENTED       |')
            print('+---------------------------------+')
            print()
            print(update_menu)
            choice = input('---> ')

        elif choice == 'v':
            print()
            print('+---------------------------------+')
            print('|       NOT YET IMPLIMENTED       |')
            print('+---------------------------------+')
            print()
        
        elif choice == 'x':
            print()
            quit()

        else:
            print()
            print('+---------------------------+')
            print('|       INVALID INPUT       |')
            print('+---------------------------+')
            print()
            print(update_menu)
            choice = input('---> ')

def no_results_found(search_term):
    print('+--------------------------------------------------------------------------------------+')
    print(f'   Hey, homeslice.  "{search_term}" yielded no results...                              ')
    print("   ....that or something really bad happebed that I haven't coded a fix for...          ")
    print("   Don't worry though, it's probably the former.                                        ")
    print('+--------------------------------------------------------------------------------------+')

def delete_sub_menu():
    #prints the search
    print()    
    d_menu =  str('DELETE OPTIONS\n' \
        '(s) Delete keycap set\n' \
        '(k) Delete kit \n' \
        '(b) Back to main menu\n')
    print(d_menu)
    choice = input('---> ')
    while choice.lower() != 'b':
        if choice == 's':
            print()
            delete_candidate = input('What is the name of the keycap set you wish to delete from the database? \n'\
                                    '---> ')
            repo = KeycapsRepository()
            try:
                delete_candidate_row = repo.get_set(delete_candidate)
            

                t = PrettyTable(['Set ID', \
                                'Set Name', \
                                'Manufacturer', \
                                'Material', \
                                'Printing Method', \
                                'Profile'])
                t.title = 'SELECTED KyecapSet ROW'
                t.add_row([delete_candidate_row.id, \
                        delete_candidate_row.keycapName, \
                        delete_candidate_row.manu, \
                        delete_candidate_row.material, \
                        delete_candidate_row.printingMethod, \
                        delete_candidate_row.profile])
                print(t)
            except:
                no_results_found(delete_candidate)

            confirm = input('if you would like to delete this row, type in the Set ID exactly as it is written, otherwise with deletion will be cancelled\n'
                            'type anything else if you\'d like to cancel the delete operation\n'
                            '---> ')

            # if confirm == delete_candidate_row.id:
            #         repo.delete_set(delete_candidate_row.id)
            try:
                if confirm == delete_candidate_row.id:
                    repo.delete_set(delete_candidate_row.id)
                else:
                    print('Delete operation cancelled.')
                    quit()
            
            except:
                no_results_found(confirm)

            print(d_menu)
            choice = input('---> ')
        
        elif choice == 'k':
            print()
            print('+---------------------------------+')
            print('|       NOT YET IMPLIMENTED       |')
            print('+---------------------------------+')
            print()
            print(d_menu)
            choice = input('---> ')

        elif choice.lower() == 'b':
            return 'b'
        else:
            print()
            print('+---------------------------+')
            print('|       INVALID INPUT       |')
            print('+---------------------------+')
            print()
            print(d_menu)
            choice = input('---> ')


def insert_sub_menu():
    #prints the search
    print()
    i_menu =  str('INSERT OPTIONS\n' \
        '(s) Add keycap set\n' \
        '(k) Add kit \n' \
        '(v) Add vendor\n' \
        '(c) Add color\n' \
        '(b) Back to main menu\n')
    print(i_menu)
    choice = input('---> ')
    while choice.lower() != 'b':
        if choice == 's':
            print()
            repo = KeycapsRepository()

            set_name = input('Name of set: ')
            manu = input('Manufacturer: ' )
            mats = input('Material:  ')
            printing = input('Printing method: ')
            profile = input('profile: ')

            set_to_be_added = KeycapSet(set_name, manu, mats, printing, profile, id='')

            new_row = repo.add_set(set_to_be_added)

            t = PrettyTable(['Set ID', \
                            'Set Name', \
                            'Manufacturer', \
                            'Material', \
                            'Printing Method', \
                            'Profile'])
            t.title = 'INSERTED ROW'
            t.add_row([new_row.id, \
                       new_row.keycapName, \
                       new_row.manu, \
                       new_row.material, \
                       new_row.printingMethod, \
                       new_row.profile])
            print(t)

            print()
            print(i_menu)
            choice = input('---> ')
        
        elif choice == 'k':
            print()
            print('+---------------------------------+')
            print('|       NOT YET IMPLIMENTED       |')
            print('+---------------------------------+')
            print()
            print(i_menu)
            choice = input('---> ')

        elif choice == 'v':
            print()
            print('+---------------------------------+')
            print('|       NOT YET IMPLIMENTED       |')
            print('+---------------------------------+')
            print()
            print(i_menu)
            choice = input('---> ')

        elif choice == 'c':
            print()
            print('+---------------------------------+')
            print('|       NOT YET IMPLIMENTED       |')
            print('+---------------------------------+')
            print()
            print(i_menu)
            choice = input('---> ')

        elif choice.lower() == 'b':
            return 'b'
        else:
            print()
            print('+---------------------------+')
            print('|       INVALID INPUT       |')
            print('+---------------------------+')
            print()
            print(i_menu)
            choice = input('---> ')




def search_sub_menu():
    #prints the search
    print()
    s_menu =  str('SEARCH OPTIONS\n' \
        '(c) Search for a color family\n' \
        '(m) Search for a manufacturer\n' \
        '(n) Search for kit and vendor information for a specific keycap set\n' \
        '(b) Back to main menu\n')
    print(s_menu)
    choice = input('---> ')
    while choice.lower() != 'b':
        if choice == 'c':
            print()
            search_term = input('What color would you like to search? (you may enter any number of color family names or type "all")\n' \
                                '---> ')
            try:
                if search_term.lower() == 'all':
                    repo = KeycapsRepository()
                    t = PrettyTable(['Set ID', \
                                     'Manufacturer', \
                                     'Set Name', \
                                     'Material', \
                                     'Printing Method', \
                                     'Profile', \
                                     'Number Of Kits', \
                                     'Color Family', \
                                     'Classes Matching Color'])
                    t.title = 'ALL COLOR FAMILIES'

                    for set in repo.view_all_color():
                        t.add_row([set.keycapSetID, \
                                   set.manu, \
                                   set.keycapName, \
                                   set.material, \
                                   set.printingMethod, \
                                   set.profile, \
                                   set.numberOfKits, \
                                   set.colorFam, \
                                   set.classesMatchingColor])
                    t.align = "l"
                    print(t)
                
                else:
                    repo = KeycapsRepository()
                    t = PrettyTable(['Set ID', \
                                    'Manufacturer', \
                                    'Set Name', \
                                    'Material', \
                                    'Printing Method', \
                                    'Profile', \
                                    'Number Of Kits', \
                                    'Color Family', \
                                    'Classes Matching Color'])
                    t.title = f'RESULT FOR COLOR: {search_term.upper()}'

                    for set in repo.search_color(search_term):
                        t.add_row([set.keycapSetID, \
                                   set.manu, \
                                   set.keycapName, \
                                   set.material, \
                                   set.printingMethod, \
                                   set.profile, \
                                   set.numberOfKits, \
                                   set.colorFam, \
                                   set.classesMatchingColor])
                    t.align = "l"
                    print(t)
            except:
                print()
                no_results_found(search_term)
            print()
            print(s_menu)
            choice = input('---> ')

        elif choice == 'm':
            print()
            search_term = input('What Manufacturer would you like to search for?\n' \
                                '---> ')
            try:
                repo = KeycapsRepository()
                t = PrettyTable(['Set ID', \
                                'Manu', \
                                'Set Name', \
                                'Colors Used', \
                                'Profile', \
                                '# of Kits in Set', \
                                'Vedor Regions'])
                t.title = f'RESULT FOR MANUFACTURER: {search_term}'

                for set in repo.search_manu(search_term):
                    t.add_row([set.id, \
                               set.manu, \
                               set.keycapName, \
                               set.colors, \
                               set.profile, \
                               set.numberOfKits, \
                            set.regionList])
                t.align = "l"
                print(t)
            except:
                print()
                no_results_found(search_term)
            print()
            print(s_menu)
            choice = input('---> ')    

        elif choice == 'n':  # takes care of searching for kits as well - possibly even vendor 
            print()
            search_term = input('Type in the name of the keycap set you whish to search for\n' \
                                '---> ')
            try:
                repo = KitRepository()
                t = PrettyTable(['Set ID', \
                                'Manufacturer', \
                                'Set Name', \
                                'Set Colors', \
                                'Kit ID', \
                                'Kit Name', \
                                'Legend Char', \
                                'Sublegend Char', \
                                'Number of Keys', \
                                'Tsangan Support', \
                                'ISO Support'])
                t.title = f'GENERAL INFORMAT FOR "{search_term.upper()}"'

                for set in repo.get_list_of_kits(search_term):
                    t.add_row([set.keycapSetID, \
                               set.manu, \
                               set.keycapName, \
                               set.setColors, \
                               set.kitID, \
                               set.kitName, \
                               set.legendChar, \
                               set.sublegendChar,\
                               set.numberOfKeys, \
                               set.tsangan, \
                               set.iso])
                t.align = "l"
                print(t)
                print()
                vendor_prompt = input('Would you like to see a list of vendors associated with this keycap set? (y/n)\n'\
                                      '...> ')
                while (vendor_prompt.lower() not in ['n', 'b', 'x']):
                    if vendor_prompt == 'y':
                        vendor_repo = KeycapsRepository()
                        v = PrettyTable(['Vendor ID', \
                                         'Vendor Name', \
                                         'Region', \
                                         'Vendor Website', \
                                         'Manufacturer', \
                                         'Keycap Set'])
                        v.title = f'VENDOR LIST FOR "{search_term.upper()}"'

                        for vendor in vendor_repo.search_vendor(search_term):
                            v.add_row([vendor.vendorID,\
                                       vendor.vendorName,\
                                       vendor.region,\
                                       vendor.vendorWebsite,\
                                       vendor.manu,\
                                       vendor.keycapName])
                            v.align = "l"
                            vendor_prompt = 'b'
                            print()
                        print(v)
                    else:
                        print()
                        print('+---------------------------+')
                        print('|       INVALID INPUT       |')
                        print('+---------------------------+')
                        print()
                        vendor_prompt = input('Would you like to see a list of vendors associated with this keycap set? (y/n)\n'\
                                              '...> ')
            except:
                print()
                no_results_found(search_term)
            print()
            print(s_menu)
            choice = input('---> ')  

        elif choice.lower() == 'b':
            return 'b'
        else:
            print()
            print('+---------------------------+')
            print('|       INVALID INPUT       |')
            print('+---------------------------+')
            print()
            print(s_menu)
            choice = input('---> ')

def main_menu():
    #prints the main menu options
    print()
    menu =  str('MAIN MENU\n'
        '(k) Quick view\n'
        '(s) Search database\n'
        '(i) Insert entries\n'
        '(u) Update entries\n'
        '(d) Delete entries\n'
        '(x) Quit')
    print(menu)
    choice = input('---> ')
    while choice.lower() != 'x':
        if choice == 'k':
            print()
            repo = KeycapsRepository()
            t = PrettyTable(['Set ID', \
                            'Manu', \
                            'Set Name', \
                            'Colors Used', \
                            'Material', \
                            'Profile', \
                            '# of Kits in Set', \
                            'Vedor Regions'])
            t.title = 'QUICK VIEW'
            for set in repo.get_agg_of_sets():
                t.add_row([set.id, \
                           set.manu, \
                           set.keycapName, \
                           set.colors, \
                           set.material, \
                           set.profile, \
                           set.numberOfKits, \
                           set.regionList])
            t.align = "l"
            print(t)
            print()
            print(menu)
            choice = input('---> ')

        elif choice == 's':
            print()
            search_sub_menu()
            print(menu)
            choice = input('---> ')  

        elif choice == 'i':
            print()
            insert_sub_menu()
            print()
            print(menu)
            choice = input('---> ')

        elif choice == 'u':
            print()
            update_sub_menu()
            print(menu)
            choice = input('---> ')

        elif choice == 'd':
            print()
            delete_sub_menu()
            print()
            print(menu)
            choice = input('---> ') 

        elif choice.lower() == 'x':
            return 'x'
        else:
            print()
            print('+---------------------------+')
            print('|       INVALID INPUT       |')
            print('+---------------------------+')
            print()
            print(menu)
            choice = input('---> ')


print()
print('  .#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@J '  )                                           
print('  :@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@J'   )                                       
print('  #Y@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?   ')                                         
print('  ,5@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@7   ' )                                       
print('  :G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@!   ' )                                      
print('  |B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&~   ')                            
print('  .#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&^             ')                           
print('  :&@@P5P@@@@@P5G@@@@@@@@@@@@@@@@@@@@@&77!J@@@@@@@@@@@@@@@@#^             .^^:  .^::        ')        
print('  ^@@P  5@@@@P  5@@@@@@@@@@@@@@@@@@@@@#.  ^@@@@@@@@@@@@@@@@@#:            Y@@#: ?@@&:              ') 
print('  !@&: !@@@@&: !@@GGG#&G55G&@#G55P#@@@#.  ~@@#GGPG&@@@#GP55P#B:       .:: Y@@&: ?@@&: ::.          ') 
print('  7@? .#@@@@7 :#@@^  ^..   :!..   .J@@#.  ~@P:  ^P@@5^.  .. Y@G.   .?G&&&##@@&: ?@@&G#&@#G7         ')
print('  JG  5@@@@P  5@@@^   5&B:   5##~   B@#.  ^7  ^P@@@?   ?B&&#@@@P.  P@@#7~7#@@&: ?@@@5~~Y@@@J        ')
print('  J^ !@@@@&^ !@@@@^  :@@@~  :&@@J   B@#.      :P@@&.  :@@@@@@@@@P ^@@@?   Y@@&: ?@@&.   #@@G        ')
print('  : :#@@@@? :#@@@@^  :@@@~  :&@@J   B@&.  ^B?   7#@?   !PBBG&@@@@5.G@@#7~7#@@&: ?@@@5~~Y@@@7        ')
print('    7GGGG5  7GGGGG:  :PGG^  .PGG!   YG5.  ^GG!   :5G7       7GGGGG!.JB&@&#5#&#: J&&GG&&@#P!    ')
print('+--------------------------------------------------------------------------------------------+')
print('|                  M O C K E Y C A P     D A T A B A S E    ( v 0.7 - beta)                  |')
print('+--------------------------------------------------------------------------------------------+')
print()
main_menu()

