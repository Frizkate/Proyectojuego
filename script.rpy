init:
    $ inventory = []

define luis = Character("Luis")
define ente = Character("???")

default llavecabana = False
default llaveauto = False
default llavepieza = False
default casaexplorada = False

label start:
    image pantallanegra = "pantallanegra.jpg"
    scene pantallanegra
    luis "¿Qué sucede? ¿Dónde estoy?"

    image cabanainterior = "cabanainterior.jpg"
    scene cabanainterior
    with fade
    luis "¿Me encuentro en una cabaña?" 
    luis "Tengo que explorar para encontrar una manera de salir."
    jump quehacercabana

label quehacercabana:
    menu:
        "Salir de la cabaña":
            jump salircabana
        "Explorar la cabaña":
            jump explorarcabana

label explorarcabana:
    if llavecabana:
        luis "Ya he explorado todo. No he encontrado nada más que me sea útil."
        jump quehacercabana
    else:
        luis "Hay dos literas y mesas de luz a su lado. En la mesa de la derecha, veo una llave."

        menu:
            "Tomar la llave":
                $ llavecabana = True
                luis "Parece que con esto puedo abrir la puerta."
                jump quehacercabana

label salircabana:
    if llavecabana:
        image cabanaexterior = "cabanaexterior.jpeg"
        scene cabanaexterior
        "Logras salir de la cabaña."
        luis "¿Estoy acaso en el campamento al que fuí de niño?"
        luis "Todo se ve más siniestro de lo que recuerdo. ¿Qué está pasando?"
        "Decides echar un vistazo a tu alrededor"

        image bosque = "bosque.jpg"
        scene bosque
        with fade
        image ente = "screamer1.png"
        show ente at truecenter
        "En el bosque, veo una figura de una mujer. Parece estar observándome."
        menu:
            "Investigar la figura":
                jump investigate_figure
    else:
        luis "La puerta está cerrada. Necesito una llave."
        jump quehacercabana

label investigate_figure:
    luis "¿Hola?"
    ente "¿Por qué?"
    hide ente
    with dissolve
    luis "¿Cómo?"
    luis "¡Pará! ¡Volvé!"
    luis "..."
    luis "Tengo que salir de acá. Voy a seguir explorando."

label quehacerbosque:
    menu:
        "Ir al auto":
            jump escenaauto
        "Examinar la cerca":
            jump escenacerca
        "Adentrarme en el bosque":
            jump escenabosque

label escenaauto:
    if llaveauto:
        luis "Ya no queda nada que hacer acá."
        jump quehacerbosque
    else:
        image auto = "autoexterior.jpg"
        scene auto
        with fade
        luis "¡Éste es mi auto! ¡¿Qué le pasó?!"
        luis "No hay tiempo. Capás hay algo adentro"
        "Revisás adentro del auto"
        image autointerior ="autointerior.jpg"
        scene autointerior
        with fade
        "En la guantera encontrás una llave."
        $ llaveauto = True
        luis "Excelente. PArece ser la llave de una habitación."
        luis "De momento, ya hice todo lo que podía hacer acá. Perdón, viejo amigo."
        jump quehacerbosque

label escenacerca:
    image cerca = "cerca.png"
    scene cerca
    with fade
    luis "La cerca está cerrada con un candado. No puedo forzarla."
    if llaveauto:
        menu:
            "Probar llave del auto":
                "Esto no funciona acá. Mejor me vuelvo."
                jump quehacerbosque
            "Volver":
                jump quehacerbosque
    else:
        menu:
            "Volver":
                jump quehacerbosque

label escenabosque:
    image bosquecamino = "bosquecamino.png"
    scene bosquecamino
    with fade
    "Te adentras en el bosque."
    luis "Siento un frío escalofriante."
    luis "La oscuridad es intensa, pero la luz de la luna me guía."

    image casaexterior = "casaexterior.jpg"
    scene casaexterior 
    with fade
    "Ves una casa al fondo."
    "Tal vez encuentre ayuda allí."
    menu:
        "Acercarme a la casa":
            jump escenacasa

label escenacasa:
    if casaexplorada:
        jump casaquehacer
    else:
        image casa = "casainterior.jpg"
        scene casa
        with fade
        luis "La casa se parece a la mía, pero algo impactó la pared derecha."
        luis "Incluso está decorada como la mía, pero las fotos son diferentes."
        "Las imágenes muestran a dos personas en la oscuridad."
        "En las paredes hay trozos de papel que dicen '¿Por qué?'"
        menu:
            "Explorar la casa":
                jump explorarcasa

label explorarcasa:
    "Intento abrir varias habitaciones una por una sin éxito."
    luis "Solo queda una. La que comparto con la jabru."
    $ casaexplorada = True
    jump casaquehacer

label casaquehacer:
    if llaveauto:
        menu:
            "Probar llave":
                jump escenahabitacion
    else:
        luis "No hay caso. Necesito una llave o algo."
        luis "Mejor me vuelvo al inicio. Capás me perdí de algo"
        jump quehacerbosque

label escenahabitacion:
    image habitacion = "habitacion.png"
    scene habitacion
    with fade
    luis "Entré."
    luis "Siento una sensación de revelación."
    menu:
        "Explorar habitación":
            "Revolviendo todo, encontrás una llave en la mesa de luz"
            "Vamo' los pi'. Esta seguro funciona en la cerca."
            jump cercafinal

label cercafinal:
    scene cerca
    with fade
    "Usando la llave, abro la cerca y todo se vuelve claro."
    image pantallablanca = "pantallablanca.jpg"
    scene pantallablanca
    "De repente, todo se volvió blanco."
    "El insonorizante ruido de un pitido es luego calmado y reemplazado por murmuros."
    "Soy informado de lo que sucedió. Un accidente. Estando alcoholizado choqué contra mi propia casa y herí a mi propia esposa de gravedad."
    "Me dicen que no tiene salvación y esperan a que les de el sí y la desconecten"
    image final = "final.png"
    scene final
    with fade
    luis "No puedo creerlo."
    luis "¿Por qué?"
    scene pantallanegra
    "Fin demo"
    return
