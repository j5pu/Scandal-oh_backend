# -*- coding: utf-8 -*-
username = {
    'existing': 'paco33',
    'existing_facebook': 'paco33_facebook',
    'another': 'capitancock',
    'another_facebook': 'capitancock_facebook',
    'invalid': 'capitañooo',
    }
email = {
    'existing': 'manitobueno@example.com',
    'existing_facebook': 'manitobueno_facebook@example.com',
    'another': 'yupi@yo.com',
    'another_facebook': 'yupi_facebook@yo.com',
    'invalid': 'yupi@.com',
    }
password = 'manito666'
# password bien escrita en formulario, pero que no existe para ningún registro
password_fail = 'manito666@@@@@'
# password mal escrita en formulario
password_invalid = 'mani'


username_list = {
    'valids': (
        'bizeuuu',
    ),
    'invalids': (
        'bizeuuuñño',
        'bizeuá sdf',
    )
}

email_list = {
    'valids': (
        'bizeuuu@example.com',
    ),
    'invalids': (
        'bizeuuu@?',
    )
}

password_list = {
    'valids': (
        'eñaaaÁ2710',
    ),
    'invalids': (
        '',
        '____________________________12fdsgsdgs12fdsgsdgs12fdsgsdgs12fdsgsdgs12fdsgsdgs12fdsgsdgs12fdsgsdgs12fdsgsdgs12fdsgsdgs12fdsgsdgs12fdsgsdgs12fdsgsdgss12fdsgsdgs12fdsgsdgs12fdsgsdgs12fdsgsdgs12fdsgss12fdsgsdgs12fdsgsdgs12dgs12fdsgsdgs12',
    )
}

# para logueo
username_email_list = {
    'valids': username_list['valids'] + email_list['valids'],
    'invalids': username_list['invalids'] + email_list['invalids'],
}