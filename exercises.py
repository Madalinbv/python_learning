
'''
    Pentru a putea modulariza codul si a ne asigura ca anumite bucati de cod merg,
    intotdeauna este bine sa folosim functii.
    Exista un principiu in programare, si anume DRY (do not repeat yourself), de care
    veti fi intrebati in interviuri aproape mereu. Daca avem de facut acelasi lucru in 10
    locuri intr-un proiect, nu vom scrie aceeasi bucata de 10 ori, in schimb o vom incapsula
    intr-o functie, care ne va da rezultatul.
'''
def say_hello_world():
    print("Hello, World!")

'''
    Sa presupunem ca "Hello, World!" nu e singurul lucru pe care vrem sa il spunem,
    in cazul asta, vom folosi o functie cu ARGUMENT. Argumentul, in cazul nostru, 
    trebuie sa fie un string, iar acel string va fi printat la consola, cand noi apelam
    functia folosind acest string ca si parametru de intrare. Stringurile in python sunt 
    bucati de text. Pentru a ii spune pythonului ca ceva anume este text, scriem intre 2 ghilimele duble
    exemplu: "ceva" --> string
             "ceva --> not string
             ceva" --> not string
             "altceva" --> string
             1 --> not string
'''
def say_something(something):
    print(something)

'''
    Asta e putin bonus si putin mai greu de inteles, o sa detaliem in lectiile ulterioare
    Avem aceeasi metoda ca mai sus cu conditia ca ii specificam functiei tipul de parametru
    pe care trebuie sa il primeasca, si anume string.
'''
def say_something_special(something: str):
    print(something)

'''
    O sa trecem acum la o functie care ne va intoarce un rezultat atunci cand o apelam
    si nu va printa nimic la consola. Ce vom face cu rezultatul este treaba noastra, ulterior.
    Pentru a putea folosi rezultatul trebuie sa il stocam intr-o variabila.
    Variabilele un python sunt folosite pentru a stoca anumite tipuri de date:
    int --> numere intregi
    float --> numere cu virgula
    string --> texte, stringuri
    etc.
    pentru a stoca ceva intr-o variabila, tot ce trebuie sa facem este sa scriem ceva de genul:
    variabila = "Hello world!"
'''
def give_me_a_string():
    return "I gave you this string!"

'''
    In continuare vom defini o functie care adauga doua numere, primite ca si parametrii
    Operatiile in python sunt: 
    scadere (-)
    adunare (+)
    inmultire (*)
    impartire (/)
    ridicare la putere (**)
'''
def add_two_numbers(a, b):
    return a + b

# impartire numere
def divide_numbers(a, b):
    return a / b

#ridicare la patrat
def square_up(a, b):
    return a ** 2

'''
    Acum, este randul vostru sa implementati 4 functii care sa faca scaderea a 2 numere, impartirea a 2 numere
    inmultirea a 2 numere si ridicarea la patrat a unui numar. Va voi scrie eu scheletul de functii pentru 2 din ele
    Pentru celelalte 2 il veti scrie voi.
    
    functiile pentru impartire si ridicare la putere se vor numi
        - divide_numbers()
        - square_up()
        
    !! ATENTIE, daca nu le numiti asa, veti primi eroare de la checker. !!
    
    Un lucru important:
        - incercati sa pastrati aceeasi nomenclatura pe care am folosit-o si eu, este best practice
        - functiile trebuie sa fie usor de inteles, sa aiba nume sugestive, la fel si variabilele, cand vom ajunge acolo
'''
def subtract_numbers(a, b):
    pass # remove this line when done
    return (a - b)

def multiply_numbers(a, b):
    pass # remove this line when done
    return (a * b)


# TODO: implement division
# TODO: implement power

if __name__ == '__main__':
    # folosind functia print(argument), putem printa orice in consola.
    # argumentul trebuie sa fie un numar, un text, orice variabila.
    # aici, de exemplu printam un text (in programare se numesc strings)
    print("Hello, World!")

    # aici o sa apelam prima metoda facuta de NOI, nu una deja existenta in python
    # si anume, say_hello_world()
    say_hello_world()

    # aici vom apela o functie care va printa orice ii dam noi ca input
    say_something("Salut, eu sunt Bogdan!")

    # aici vom apela functia care va printa orice STRING ii dam noi ca input
    # HINT: incercati sa ii dati un numar, fara sa fie intre " ", sa vedeti ce se intampla :)
    say_something_special("something special")

    # vom stoca rezultatul acestei functii in variabila result
    result = give_me_a_string()
    # in momentul de fata, in result, avem textul intors de functia noastra, hai sa il printam.
    # avand in vedere ca variabila noastra, result, poate fi folosita ca si parametru al unei functii
    # ce functie credeti ca ar trebui sa folosim ca sa printam result?
    # TODO: inlocuiti aceasta linie cu apelul functiei potrivite

    # haideti sa folosim si functia care aduna cele doua numere si sa printam rezultatul direct
    # putem sa printam direct rezultatul unei functii fara a il mai stoca intr-o variabila, daca
    # nu mai avem nevoie de el in continuare in cod.
    # Daca avem nevoie de acest rezultat in alte 2-3-4 locuri, atunci, vom folosi o variabila
    # pentru a nu apela functia de mai multe ori, stiind ca ne va da acelasi rezultat.
    # Cu cat mai putine apeluri de functii, cu atat mai bine.
    print(add_two_numbers(2, 3))


'''
    Dupa ce terminati de inteles, si incepeti sa implementati,
    Ca sa vedeti rezultatele, rulati checkerul. 
    Click dreapta pe fisierul checker.py si RUN (pentru cei cu pycharm)
    
    Orice intrebari, let me know. E destul de simplu, o luam usor. Maine vor veni alte exercitii + alte explicatii.
    
    Dati feedback. Nu am explicat bine, spuneti, nu ati inteles, intrebati.
    O sa mearga totul cum trebuie daca mereu stiu ce vreti de la mine.

    Good luck and hope you enjoy. ^_^
    
    BONUS: daca vreti sa intelegeti inainte sa explic eu foarte detaliat data types in python:
    https://www.w3schools.com/python/python_datatypes.asp
    
    Au un site bunicel, dar nu e neaparat foarte explicit. E fain ca poti testa tu sa vezi ce se intampla.
    Have a look, daca vreti, daca nu, urmatoarea lectie va fi exclusiv despre data types.
'''



