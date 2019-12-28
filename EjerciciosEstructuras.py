"""

Dado un diccionario, el cual almacena las calificaciones de un alumno, siendo las llaves los nombres de las materia y los valores las calificación, mostrar en pantalla el promedio del alumno.

Ejemplo: calificaciones = {calculo:10, dibujo:5}

"""

calificaciones = {'calculo':10, 'dibujo':5, 'españosl': 9}
promedio = sum(list(calificaciones.values()))/len(list(calificaciones.values()))
print(promedio)

"""

A partir del diccionario del ejercicio anterior, mostrar en pantalla la materia con mejor promedio.

"""
mayor = 0
for materia in calificaciones:
	if calificaciones[materia] > mayor:
		mayor = calificaciones[materia]
		materia_mayor = materia
print("La materia con la calificación más alta es ", materia_mayor)

"""

Crear una lista la cual almacene 10 números positivos ingresados por el usuario, mostrar en pantalla: la suma de todos los números, el promedio, el número mayor y el número menor.

"""
"""
lista = []
for i in range(10):
	#print("Hola")
	valor_ingresdo = int(input("Ingrese un dato "))
	lista.append(valor_ingresdo)

print("La suma de sus números es: ", sum(lista))
print("El número mayor es: ", max(lista))
print("El número menor es: ", min(lista))
"""

"""

Dado una lista de frases ingresadas por el usuario, mostrar en pantalla todas aquellas que sean palíndromo.

"""

palabras = ["Hola Mundo", "Anita Laba la tina", "Radar", "Ingresar"]
palabras = ",".join(palabras)
palabras = palabras.lower()
palabras = palabras.replace(" ", "")
palabras = palabras.split(",")

for palabra in palabras:
	if palabra == palabra[::-1]:
		print("La palabra: ", palabra, " es un palindromo")


"""

Mostrar en pantalla la palabra que más se repita junto con la cantidad de veces que lo hace del capituló número uno de Frankenstein

"""

capitulo1 = """ Soy ginebrino de nacimiento, y mi familia es una de las más distinguidas de esa república. Durante muchos años mis antepa­sados habían sido consejeros y jueces, y mi padre había ocupado con gran honor y buena reputación diversos cargos públicos. Todos los que lo conocían lo respetaban por su integridad e infatigable dedicación. Pasó su juventud dedicado por completo a los asuntos de su país, y sólo al final de su vida pensó en el matrimonio y así dar al Estado unos hijos que pudieran perpetuar su nombre y sus virtudes.

Puesto que las circunstancias de su matrimonio reflejan su personalidad, no puedo dejar de referirme a ellas. Uno de sus más íntimos amigos era un comerciante, que, debido a numerosos contratiempos, cayó en la miseria tras gozar de una muy desahogada situación. Este hombre, de nombre Beaufort, era de carácter orgulloso y altivo y se resistía a vivir en la pobreza y el olvido en el mismo país en el que, con anterioridad, se le distinguiera por su categoría y riqueza. Habiendo, pues, saldado sus deudas en la forma más honrosa, se retiró a la ciudad de Lucerna con su hija, donde vivió sumido en el anonimato y la desdicha. Mi padre profesaba a Beaufort una auténtica amistad, y su reclusión en estas desgraciadas circunstancias le afligió mucho. También sentía íntimamente la ausencia de su compañía, y se propuso encontrarlo y persuadirlo de que, con su crédito y ayuda, empezara de nuevo.

Beaufort había tomado medidas eficaces para esconderse, y mi padre tardó diez meses en descubrir su paradero. Entusiasmado con el descubrimiento, mi padre se apresuró hacia su casa situada en una humilde calle cerca del Reuss. Pero al llegar sólo encon­tró miseria y desesperación. Beaufort no había logrado salvar más que una pequeña cantidad de dinero de los despojos de su fortuna. Era suficiente para sustentarlo durante algunos meses y, mientras tanto, esperaba encontrar un trabajo respetable con algún comerciante. Así pues, pasó el intervalo inactivo; y, con tanto tiempo para reflexionar sobre su dolor, se hizo más profundo y amargo y, al fin, se apoderó de tal forma de él, que tres meses después estaba enfermo en cama, incapaz de realizar cualquier esfuerzo.

Su hija lo cuidaba con el máximo cariño, pero veía con desazón que su pequeño capital disminuía con rapidez y que no había otras perspectivas de sustento. Pero Caroline Beaufort estaba dotada de una inteligencia poco común; y su valor vino en su ayuda en la adversidad. Empezó a hacer labores sencillas; trenzaba paja, y de diversas maneras consiguió ganar una miseria que apenas le bastaba para sustentarse.

Así pasaron varios meses. Su padre empeoró, y ella cada vez tenía que emplear más tiempo en atenderlo; sus medios de sustento menguaban. A los diez meses murió su padre dejándola huérfana e indigente. Este golpe final fue demasiado para ella. Al entrar en la casa mi padre, la encontró arrodillada junto al ataúd, llorando amargamente; llegó como un espíritu protector para la pobre criatura, que se encomendó a él. Tras el entierro de su amigo, mi padre la llevó a Ginebra, confiándola al cuidado de un pariente; y dos años después se casó con ella.

Cuando mi padre se convirtió en esposo y padre, las obligaciones de su nueva situación le ocupaban tanto tiempo que dejó varios de sus trabajos públicos y se dedicó por entero a la educación de sus hijos. Yo era el mayor y el destinado a heredar todos sus derechos y obligaciones. Nadie puede haber tenido padres más tiernos que yo. Mi salud y desarrollo eran su constante ocupación, ya que fui hijo único durante varios años. Pero, antes de proseguir mi narración, debo contar un incidente que tuvo lugar cuando yo tenía cuatro años.

Mi padre tenía una hermana a quien amaba tiernamente y que se había casado muy joven con un caballero italiano. Poco después de su boda, había acompañado a su marido a su país natal, y durante algunos años mi padre tuvo muy poca relación con ella. Murió alrededor de la época de la que hablo, y pocos meses después mi padre recibió una carta de su cuñado haciéndole saber que tenía la intención de casarse con una dama italiana y pidiéndole que se hiciera cargo de la pequeña Elizabeth, la única hija de su difunta hermana.

Es mi deseo ––dijo–– que la consideres como hija tuya y que como a tal la eduques. Es la heredera de la fortuna de su madre, y te enviaré los documentos que así lo demuestran. Reflexiona sobre esta propuesta y decide si preferirías educar a tu sobrina tú mismo o que lo haga una madrastra.

Mi padre no dudó un instante, y de inmediato se puso en camino hacia Italia con el fin de acompañar a la pequeña Elizabeth hasta su futuro hogar. A menudo he oído a mi madre decir que era la criatura más preciosa que jamás había visto, e incluso ya entonces mostraba síntomas de un carácter dulce y afectuoso.

Estas características y el deseo de afianzar los lazos del amor familiar hicieron que mi madre considerara a Elizabeth como mi futura esposa, plan del cual nunca encontró razón para arrepentirse.

A partir de este momento, Elizabeth Lavenza se convirtió en mi compañera de juegos y, a medida que crecíamos, en una amiga. Era dócil y de buen carácter, a la vez que alegre y ju­guetona como un insecto de verano. A pesar de que era vivaz y animada, tenía fuertes y profundos sentimientos y era desacostumbradamente afectuosa. Nadie podía disfrutar mejor de la libertad ni podía plegarse con más gracia que ella a la sumisión o lanzarse al capricho. Su imaginación era exuberante, pero tenía una gran capacidad para aplicarla. Su persona era el reflejo de su mente, sus ojos de color avellana, aunque vivos como los de un pájaro, poseían una atractiva dulzura. Su figura era ligera y airosa y, aunque era capaz de soportar gran fatiga, parecía la criatura más frágil del mundo. A pesar de que me cautivaba su compren­sión y fantasía, me deleitaba cuidarla como a un animalillo predilecto. Nunca vi más gracia, tanto personal como mental, ligada a mayor modestia.

Todos querían a Elizabeth. Si los criados tenían que pedir algo, siempre lo hacían a través de ella. No conocíamos ni la desunión ni las peleas, pues aunque éramos muy diferentes de carácter, incluso en esa diferencia había armonía. Yo era más tranquilo y filosófico que mi compañera, pero menos dócil. Mi capacidad de concentración era mayor, pero no tan firme. Yo me deleitaba investigando los hechos relativos al mundo en sí, ella prefería las aéreas creaciones de los poetas. Para mí el mundo era un secreto que anhelaba descubrir, para ella era un vacío que se afanaba por poblar con imaginaciones personales.

Mis hermanos eran mucho más jóvenes que yo; pero tenía un amigo entre mis compañeros del colegio, que compensaba esta deficiencia. Henry Clerval era hijo de un comerciante de Ginebra, íntimo amigo de mi padre, y un chico de excepcional talento e imaginación. Recuerdo que, cuando tenía nueve años, escribió un cuento que fue la delicia y el asombro de todos sus compañeros. Su tema de estudio favorito eran los libros de caballería y romances, y recuerdo que de muy jóvenes solíamos representar obras escritas por él, inspiradas en estos sus libros predilectos, siendo los principales personajes Orlando, Robin Hood, Amadís y San Jorge.

Juventud más feliz que la mía no puede haber existido. Mis padres eran indulgentes y mis compañeros amables. Para nosotros los estudios nunca fueron una imposición; siempre teníamos una meta a la vista que nos espoleaba a proseguirlos. Esta era el método, y no la emulación, que nos inducía a aplicarnos. Con el fin de que sus compañeras no la dejaran atrás, a Elizabeth no se la orientaba hacia el dibujo. Sin embargo, se dedicaba a él motivada por el deseo de agradar a su tía, representando alguna escena favorita dibujada por ella misma. Aprendimos inglés y latín para poder leer lo que en esas lenguas se había escrito. Tan lejos estaba el estudio de resultarnos odioso a consecuencia de los castigos, que disfrutábamos con él, y nuestros entretenimientos constituían lo que para otros niños hubieran sido pesadas tareas. Quizá no leímos tantos libros ni aprendimos lenguas tan rápidamente como aquellos a quienes se les educaba conforme a los métodos habituales, pero lo que aprendimos se nos fijó en la memoria con mayor profundidad.

Incluyo a Henry Clerval en esta descripción de nuestro círculo doméstico, pues estaba con nosotros continuamente.

Iba al colegio conmigo, y solía pasar la tarde con nosotros; pues, siendo hijo único y encontrándose solo en su casa, a su padre le complacía que tuviera amigos en la nuestra. Por otro lado nosotros tampoco estábamos del todo felices cuando Clerval estaba ausente.

Siento placer al evocar mi infancia, antes de que la desgracia me empañara la mente y cambiara esta alegre visión de utilidad universal por tristes y mezquinas reflexiones personales. Pero al esbozar el cuadro de mi niñez, no debo omitir aquellos acontecimientos que me llevaron, con paso inconsciente, a mi ulte­rior infortunio. Cuando quiero explicarme a mí mismo el origen de aquella pasión que posteriormente regiría mi destino, veo que arranca, como riachuelo de montaña, de fuentes poco no­bles y casi olvidadas, engrosándose poco a poco hasta que se convierte en el torrente que ha arrasado todas mis esperanzas y alegrías.

La filosofía natural es lo que ha forjado mi destino. Deseo, pues, en esta narración explicar las causas que me llevaron a la predilección por esa ciencia. Cuando tenía trece años fui de excursión con mi familia a un balneario que hay cerca de Thonon. La inclemencia del tiempo nos obligó a permanecer todo un día encerrados en la posada, y allí, casualmente, encontré un volumen de las obras de Cornelius Agrippa. Lo abrí con aburrimiento, pero la teoría que intentaba demostrar y los maravillosos hechos que relataba pronto tornaron mi indiferencia en entusiasmo. Una nueva luz pareció iluminar mi mente, y lleno de alegría le comuniqué a mi padre el descubrimiento. No puedo dejar de comentar aquí las múltiples oportunidades de que disponen los educadores para orientar la atención de sus alumnos hacia conocimientos prácticos, y que desaprovechan lamentablemente. Mi padre ojeó distraídamente la portada del libro y dijo:

¡Ah, Cornelius Agrippa! Víctor, hijo mío, no pierdas el tiempo con esto, son tonterías. Si en vez de hacer este comentario, mi padre se hubiera molestado en explicarme que los principios de Agrippa estaban totalmente superados, que existía una concepción científica moderna con posibilidades mucho mayores que la antigua, puesto que eran reales y prácticas mientras que las de aquélla eran quiméricas, tengo la seguridad de que hubiera perdido el interés por Agrippa. Probablemente, sensibilizada como tenía la imaginación, me hubiera dedicado a la química, teoría más racional y pro­ducto de descubrimientos modernos. Es incluso posible que mi pensamiento no hubiera recibido el impulso fatal que me llevó a la ruina. Pero la indiferente ojeada de mi padre al volumen que leía en modo alguno me indicó que él estuviera familiarizado con el contenido del mismo, y proseguí mi lectura con mayor avidez.

Mi primera preocupación al regresar a casa fue hacerme con la obra completa de este autor y, después, con la de Paracelso y Alberto Magno. Leí y estudié con gusto las locas fantasías de estos escritores. Me parecían tesoros que, salvo yo, pocos conocían. Aunque a menudo hubiera querido comunicarle a mi padre estas secretas reservas de mi sabiduría, me lo impedía su imprecisa desaprobación de mi querido Agrippa. Por tanto, y bajo promesa de absoluto secreto, le comuniqué mis descubrimientos a Elizabeth, pero el tema no le interesó y me vi obligado á continuar solo.

Puede parecer extraño que en el siglo XVIII surja un discípulo de Alberto Magno, pero nuestra familia no era científica, y yo no había asistido a ninguna de las clases que se daban en la universidad de Ginebra.

Así pues, mis sueños no se veían turbados por la realidad, y me lancé con enorme diligencia a la búsqueda de la piedra filosofal y el elixir de la vida. Pero era esto último lo que recibía mi más completa atención: la riqueza era un objetivo inferior; pero ¡qué fama rodearía al descubrimiento si yo pudiera eliminar de la humanidad toda enfermedad y hacer invulnerables a los hombres a todo salvo a la muerte violenta!

No eran éstos mis únicos pensamientos. Provocar la aparición de fantasmas y demonios era algo que mis autores predilectos prometían que era fácil, cumplimiento que yo ansiaba fervorosamente conseguir. Atribuía el que mis hechizos jamás tuvieran éxito más a mi inexperiencia y error que a la falta de habilidad o veracidad por parte de mis instructores.

Los fenómenos naturales que a diario tienen lugar no escapaban a mi observación. La destilación y los maravillosos efectos del vapor, procesos que mis autores favoritos desconocían por completo, provocaban mi asombro. Pero mi mayor sorpresa la suscitaron unos experimentos con una bomba de aire que empleaba un caballero al cual solíamos visitar.

El desconocimiento de los antiguos filósofos sobre éste y varios otros temas disminuyeron mi fe en ellos, pero no podía desecharlos por completo sin que algún otro sistema ocupara su lugar en mi mente.

Tenía alrededor de quince años cuando, habiéndonos retirado a la casa que teníamos cerca de Belrive, presenciamos una terrible y violenta tormenta. Había surgido detrás de las montañas del Jura, y los truenos estallaban al unísono desde varios puntos del cielo con increíble estruendo. Mientras duró la tormenta, observé el proceso con curiosidad y deleite. De pronto, desde el dintel de la puerta, vi emanar un haz de fuego de un precioso y viejo roble que se alzaba a unos quince metros de la casa; en cuanto se desvaneció el resplandor, el roble había desaparecido y no quedaba nada más que un tronco destrozado. Al acercarnos a la mañana siguiente, encontramos el árbol insólitamente destruido. No estaba astillado por la sacudida; se encontraba reducido por completo a pequeñas virutas de madera. Nunca había visto nada tan deshecho.

La catástrofe de este árbol avivó mi curiosidad, y con enorme interés le pregunté a mi padre acerca del origen y naturaleza de los truenos y los relámpagos.

Es la electricidad, me contestó, a la vez que me describía los diversos efectos de esa energía.

Construyó una pequeña máquina eléctrica y realizó algunos experimentos. También hizo una cometa con cable y cuerda, que arrancaba de las nubes ese fluido. Esto último acabó de destruir a Cornelius Agrippa, Alberto Magno y Paracelso, que durante tanto tiempo habían reinado como dueños de mi imaginación. Pero, por alguna fatalidad, no me sentí inclinado a empezar el estudio de los sistemas modernos, desinclinación que se vio influida por la siguiente circunstancia.

Mi padre expresó el deseo de que asistiera a un curso sobre filosofía natural. Gustosamente asentí a esto, pero algún motivo me impidió ir hasta que el curso estuvo casi terminado. Por tanto, al ser ésta una de las últimas clases, me resultó totalmente incomprensible. El profesor disertaba con la mayor locuacidad sobre el potasio y el boro, los sulfatos y óxidos, términos que yo no podía asociar a ninguna idea. Empecé a aborrecer la ciencia de la filosofía natural, aunque seguí leyendo a Plinio y Buffon con deleite, autores, a mi juicio, de similar interés y utilidad.

A esta edad las matemáticas y la mayoría de las ramas cercanas a esa ciencia constituían mi principal ocupación. También me afanaba por aprender lenguas; el latín ya me era familiar, y sin ayuda del diccionario empecé a leer algunos de los autores griegos más asequibles. También entendía inglés y alemán perfectamente.

Este era mi bagaje cultural a los diecisiete años, además de las muchas horas empleadas en la adquisición y conservación del conocimiento de la vasta literatura.

También recayó sobre mí la obligación de instruir a mis hermanos. Ernest, seis años menor que yo, era mi principal alumno. Desde la infancia había sido enfermizo, y Elizabeth y yo lo habíamos cuidado constantemente; era de disposición dócil, pero incapaz de cualquier prolongado esfuerzo mental. William, el benjamín de la familia, era todavía un niño y la criatura más preciosa del mundo; tenía los ojos vivos y azules, hoyuelos en las mejillas y modales zalameros, e inspiraba la mayor ternura.

Tal era nuestro ambiente familiar, en el cual el dolor y la inquietud no parecían tener cabida. Mi padre dirigía nuestros estudios, y mi madre participaba de nuestros entretenimientos. Ninguno de nosotros gozaba de más influencia que el otro; la voz de la autoridad no se oía en nuestro hogar, pero nuestro mutuo afecto nos obligaba a obedecer y satisfacer el más mínimo deseo del otro. """

capitulo1_lista = capitulo1.split(" ")
numero_palabra = {}

for palabra in capitulo1_lista:
	numero_palabra[palabra] = capitulo1_lista.count(palabra)

mayor = 0
for palabra in numero_palabra:
	if numero_palabra[palabra] > mayor:
		mayor = numero_palabra[palabra]
		palabra_repetida = palabra
print("La palabra que más se repite el el capítulo 1 de Frankenstain es '", palabra_repetida, "' con ", mayor, " veces")


"""

Remplazar cada letra de una frase dada por el usuario por la posición que le corresponde en el abecedario y mostrar el nuevo string en pantalla. (Los espacios no se remplazan) . Ejemplo: frase : 'Hola' salida : 815121 H(8) o(15) l(12) a(1)

"""

frase = "Hola mundo"
frase = frase.lower()
frase = frase.replace(" ", "")
lista_frase = []
for letra in frase:
	lista_frase.append(str(ord(letra)-96))

print(" ".join(lista_frase))

"""

Mostrar en pantalla la cantidad de vocales que existe en una frase dada por el usuario.

"""

contador = 0
for letra in frase:
	if letra in ["a", "e", "i", "o", "u"]:
		contador+=1

print(contador)


"""

Mostrar en pantalla la frecuencia de aparición de vocales en una frase dada por el usuario.

"""
vocales = {}
for letra in frase:
	if letra in ["a", "e", "i", "o", "u"]:
		vocales[letra] = frase.count(letra)

print(vocales)

"""

Eliminar todas las vocales de una frase dado por el usuario y mostrar el nuevo string en pantalla.

"""
for vocal in ["a", "e", "i", "o", "u"]:
	frase = frase.replace(letra, "")

print(frase)

"""

Listar todos los números pares del 0 al 100

"""

for numero in range(101):
	if numero%2 == 0:
		print(numero)