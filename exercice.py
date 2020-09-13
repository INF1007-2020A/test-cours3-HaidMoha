#!/usr/bin/env python
# -*- coding: utf-8 -*-
def capitaliser_pays(nom):
    print(nom.lower())
    print(nom.capitalize())
    f = print(nom.find('and'))
        print(f.lower())
    return nom


livre_empruntables = 0
# ne pas modifier la ligne ci-dessus

livre_prêt = 7
return livre_prêt
livre_empruntables = livre_prêt - 2
return livre_prêt 











if __name__ == '__main__':
    pays = [
        'AfghanIstan',
        'albania',
        'algeria',
        'AndorRa',
        'angolA',
        'antigua ANd barbuda',
        'argEntina',
        'Armenia',
        'austrAlia',
        'ausTria',
        'azerBaijaN'
    ]
    for i in range(len(pays)):
        pays[i] = capitaliser_pays(pays[i])

    print(pays)
