#!/usr/bin/env python3
"""Genera las páginas de la web de Febas Studio.

Uso: python3 construir.py
El correo y la fecha se cambian aquí arriba y se vuelven a generar las páginas.
"""
from pathlib import Path

CORREO = "febasstudio@gmail.com"  # Oficial (decidido el 2026-11-16).
FECHA_ES = "16 de noviembre de 2026"
FECHA_EN = "16 November 2026"
ANIO = 2026
RAIZ = Path(__file__).parent


def pagina(ruta, titulo, cabecera, cuerpo, idioma="es", nivel=0, otro_idioma=None, icono=False):
    sube = "../" * nivel
    cambio = ""
    if otro_idioma:
        texto, enlace = otro_idioma
        cambio = f'<p class="idioma"><a href="{enlace}">{texto}</a></p>'
    imagen = f'<img class="icono" src="{sube}englimals/icono.png" alt="">' if icono else ""
    estudio = "Febas Studio"
    html = f"""<!doctype html>
<html lang="{idioma}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fredoka:wght@600&family=Nunito:wght@400;700&display=swap">
<link rel="stylesheet" href="{sube}estilo.css">
</head>
<body>
<header>
<a class="estudio" href="{sube}index.html">{estudio}</a>
{imagen}
<h1>{cabecera}</h1>
</header>
<main>
{cambio}
{cuerpo}
</main>
<footer>© {ANIO} Febas Studio</footer>
</body>
</html>
"""
    destino = RAIZ / ruta
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(html, encoding="utf-8")


correo = f'<a href="mailto:{CORREO}">{CORREO}</a>'

# ---------------------------------------------------------------- Estudio
pagina(
    "index.html",
    "Febas Studio",
    "Febas Studio",
    f"""<div class="tarjeta">
<h2>Nuestras apps</h2>
<ul class="enlaces">
<li><a href="englimals/index.html">Englimals: inglés con mascotas</a></li>
</ul>
</div>
<div class="tarjeta">
<h2>Contacto</h2>
<p>{correo}</p>
</div>""",
)

# ---------------------------------------------------------------- Englimals (es)
pagina(
    "englimals/index.html",
    "Englimals: inglés con mascotas",
    "Englimals",
    f"""<div class="tarjeta">
<p>Aprende inglés cuidando a tus mascotas: lecciones cortas de cero a C2, con vocabulario, gramática, escucha y habla. Para personas de 13 años o más.</p>
</div>
<div class="tarjeta">
<h2>Ayuda y contacto</h2>
<p>Si tienes un problema, una duda o una idea, escríbenos a {correo}. Cuéntanos qué móvil tienes y la versión de la app (sale al final de Ajustes).</p>
<h3>Cambié de móvil, ¿cómo recupero mi partida?</h3>
<p>En el móvil antiguo, entra en Ajustes, «Copia en la nube», y entra con tu cuenta de Google. En el nuevo, pulsa «Ya tengo partida» al empezar, o entra con la misma cuenta desde Ajustes.</p>
<h3>¿Cómo borro mi copia en la nube?</h3>
<p>Mira <a href="borrar-cuenta.html">cómo borrar tu cuenta y tus datos</a>.</p>
</div>
<div class="tarjeta">
<h2>Información legal</h2>
<ul class="enlaces">
<li><a href="privacidad.html">Política de privacidad</a></li>
<li><a href="terminos.html">Términos de uso</a></li>
<li><a href="borrar-cuenta.html">Borrar tu cuenta y tus datos</a></li>
</ul>
</div>""",
    nivel=1,
    otro_idioma=("English", "en/index.html"),
    icono=True,
)

pagina(
    "englimals/privacidad.html",
    "Política de privacidad · Englimals",
    "Política de privacidad",
    f"""<div class="tarjeta">
<p class="fecha">Última actualización: {FECHA_ES}</p>
<p>Esta política explica qué datos usa la app Englimals, para qué y qué puedes hacer con ellos. Englimals es para personas de 13 años o más.</p>

<h2>1. Quién es el responsable</h2>
<p>Febas Studio, el estudio que publica Englimals. Contacto: {correo}.</p>

<h2>2. Datos que se quedan en tu móvil</h2>
<p>Tus mascotas, monedas, objetos, progreso en las lecciones, fallos para repasar y tus ajustes se guardan solo en tu móvil. No salen de él salvo que actives la copia en la nube o el ranking. Si borras la app, se borran.</p>

<h2>3. Copia en la nube (opcional)</h2>
<p>Si entras con tu cuenta de Google en Ajustes, «Copia en la nube», guardamos:</p>
<ul>
<li>el identificador de tu cuenta y tu correo electrónico, para saber de quién es la copia;</li>
<li>una copia de tu partida (lo del punto 2) y un resumen (nombres de las mascotas, nivel, monedas y fecha), para enseñártelo al recuperarla.</li>
</ul>
<p>Lo usamos solo para guardar y devolverte tu partida. La base legal es que tú nos lo pides al activar la copia (ejecución del servicio). La copia se guarda en Google Firebase (Google Ireland Ltd.), en servidores de la Unión Europea; Google actúa como encargado del tratamiento y puede tratar datos de la cuenta fuera de la UE con las garantías previstas por la ley (Marco de Privacidad de Datos UE-EE. UU. y cláusulas contractuales tipo). Cada cuenta solo puede leer su propia copia y la conexión va cifrada.</p>
<p>La copia se guarda hasta que la borres. Puedes cerrar sesión cuando quieras y borrar la copia y la cuenta desde la app (ver <a href="borrar-cuenta.html">cómo borrar tu cuenta</a>).</p>

<h2>4. Ranking del modo sin fin (opcional)</h2>
<p>Si entras en el ranking (botón «Ranking» del modo sin fin), guardamos en Google Firebase, a la vista de los demás jugadores:</p>
<ul>
<li>el identificador de tu cuenta: el de una cuenta anónima de Google Firebase (sin nombre ni correo) que se crea al entrar o, si has entrado con Google, el de tu cuenta de Google (entonces no se crea ninguna anónima). Ese identificador se ve en los datos del ranking, pero no es un nombre ni un correo;</li>
<li>un apodo inventado por la app (por ejemplo, «Panda Veloz 482»; no se puede escribir texto propio);</li>
<li>la especie de la mascota con la que jugaste;</li>
<li>tus mejores aciertos por nivel, de la semana y de siempre, y la fecha en que los conseguiste.</li>
</ul>
<p>Mientras juegas una partida guardamos también su nivel y la hora a la que empezó, para comprobar que el resultado es posible; se borran al terminarla. Lo usamos solo para enseñar el ranking. La base legal es que tú lo pides al entrar (ejecución del servicio). Se guarda en Google Firebase, como la copia del punto 3. Si después entras con tu cuenta de Google, el ranking pasa a esa cuenta.</p>
<p>Puedes salir cuando quieras en Ajustes, «Ranking», «Salir del ranking»: se borran tus puestos en todos los niveles y la cuenta anónima; si has entrado con Google, se borran los puestos de esa cuenta. Si cierras la sesión de Google, sales del ranking en ese móvil, pero tus puestos se quedan con tu cuenta de Google, como la copia: se borran con «Salir del ranking» mientras estés dentro con ella, o con «Borrar mi copia».</p>

<h2>5. Micrófono</h2>
<p>Solo se usa mientras pulsas el botón del micrófono en los ejercicios de hablar. Reconoce tu voz el sistema de tu móvil (Google o Apple), en el propio móvil cuando se puede. Englimals no guarda ni envía tu voz.</p>

<h2>6. Avisos</h2>
<p>Los recordatorios de tus mascotas los programa el propio móvil. No enviamos nada a ningún servidor para ellos. Puedes apagarlos en Ajustes.</p>

<h2>7. Anuncios y compras</h2>
<p>Ahora la app no tiene anuncios ni compras. Si se añaden, los gestionarán Google AdMob y la tienda de tu móvil; antes actualizaremos esta política y te pediremos permiso cuando la ley lo exija.</p>

<h2>8. Lo que no hacemos</h2>
<p>No vendemos tus datos, no los compartimos con nadie para publicidad y no los usamos para nada más que hacer funcionar la app.</p>

<h2>9. Menores</h2>
<p>Englimals no está pensada para menores de 13 años. Si sabemos que un menor de esa edad nos ha dado datos, los borraremos.</p>

<h2>10. Tus derechos</h2>
<p>Puedes pedirnos ver, corregir, borrar, limitar u oponerte al uso de tus datos, y recibir una copia de ellos, escribiendo a {correo}. Te responderemos en un mes como máximo. Si no estás de acuerdo con nuestra respuesta, puedes reclamar ante la Agencia Española de Protección de Datos (<a href="https://www.aepd.es">www.aepd.es</a>).</p>

<h2>11. Cambios</h2>
<p>Si cambiamos esta política, actualizaremos la fecha de arriba y, si el cambio es importante, te avisaremos en la app.</p>
</div>""",
    nivel=1,
    otro_idioma=("English", "en/privacy.html"),
)

pagina(
    "englimals/terminos.html",
    "Términos de uso · Englimals",
    "Términos de uso",
    f"""<div class="tarjeta">
<p class="fecha">Última actualización: {FECHA_ES}</p>
<ol>
<li>Englimals se ofrece tal cual, para uso personal. Hacemos lo posible para que el contenido sea correcto, pero puede tener errores.</li>
<li>Las lecciones son siempre gratis.</li>
<li>Las monedas, los tickets y los objetos del juego no tienen valor fuera de él ni se pueden cambiar por dinero.</li>
<li>Si en el futuro hay compras, se regirán por las condiciones de la tienda de tu móvil.</li>
<li>Podemos actualizar la app, su contenido y estos términos. Si el cambio es importante, te avisaremos en la app.</li>
<li>Las mascotas, el arte, los textos y el código de Englimals son de sus autores. Los recursos de otros están en la app, en Ajustes, «Créditos y licencias».</li>
<li>Para cualquier duda: {correo}.</li>
</ol>
</div>""",
    nivel=1,
    otro_idioma=("English", "en/terms.html"),
)

pagina(
    "englimals/borrar-cuenta.html",
    "Borrar tu cuenta · Englimals",
    "Borrar tu cuenta y tus datos",
    f"""<div class="tarjeta">
<p>Englimals solo guarda datos fuera de tu móvil si activaste la copia en la nube o entraste en el ranking. Así puedes borrarlos:</p>
<h2>Desde la app (al momento)</h2>
<ol>
<li>Abre Englimals y entra en Ajustes.</li>
<li>En «Copia en la nube», pulsa «Borrar mi copia».</li>
<li>Confirma con «Borrar».</li>
</ol>
<p>Se borran tu copia en la nube y tu cuenta de Englimals en la nube. La partida de tu móvil no se toca.</p>
<p>Para el ranking: en Ajustes, «Ranking», pulsa «Salir del ranking» y confirma. Se borran tus puestos en todos los niveles y, si no entraste con Google, la cuenta anónima. Si entraste con Google, se borran los puestos de esa cuenta: hazlo con la sesión abierta (si la cerraste, vuelve a entrar con ella) o usa «Borrar mi copia», que también los borra.</p>
<h2>Sin la app</h2>
<p>Escríbenos a {correo} desde el correo de la cuenta de Google con la que entraste, con el asunto «Borrar mi cuenta de Englimals». La borraremos en 30 días como máximo y te avisaremos.</p>
<h2>Qué se borra</h2>
<p>La copia de tu partida, su resumen, el identificador de tu cuenta y tu correo. No guardamos nada después. Si estabas en el ranking, también tus puestos, tu apodo y la especie de tu mascota.</p>
<h2>Los datos de tu móvil</h2>
<p>Se borran al desinstalar la app.</p>
</div>""",
    nivel=1,
    otro_idioma=("English", "en/delete-account.html"),
)

# ---------------------------------------------------------------- Englimals (en)
pagina(
    "englimals/en/index.html",
    "Englimals",
    "Englimals",
    f"""<div class="tarjeta">
<p>Learn English by looking after your pets: short lessons from beginner to C2. The lessons are explained in Spanish. For people aged 13 or over.</p>
</div>
<div class="tarjeta">
<h2>Help and contact</h2>
<p>If you have a problem, a question or an idea, write to us at {correo}. Tell us your phone model and the app version (shown at the bottom of Settings).</p>
</div>
<div class="tarjeta">
<h2>Legal</h2>
<ul class="enlaces">
<li><a href="privacy.html">Privacy policy</a></li>
<li><a href="terms.html">Terms of use</a></li>
<li><a href="delete-account.html">Delete your account and data</a></li>
</ul>
</div>""",
    idioma="en",
    nivel=2,
    otro_idioma=("Español", "../index.html"),
    icono=True,
)

pagina(
    "englimals/en/privacy.html",
    "Privacy policy · Englimals",
    "Privacy policy",
    f"""<div class="tarjeta">
<p class="fecha">Last updated: {FECHA_EN}</p>
<p>This policy explains what data the Englimals app uses, what for, and what you can do about it. Englimals is for people aged 13 or over.</p>

<h2>1. Who is responsible</h2>
<p>Febas Studio, the studio that publishes Englimals. Contact: {correo}.</p>

<h2>2. Data that stays on your phone</h2>
<p>Your pets, coins, items, lesson progress, mistakes to review and settings are stored only on your phone. They never leave it unless you turn on the cloud backup or join the leaderboard. If you delete the app, they are deleted.</p>

<h2>3. Cloud backup (optional)</h2>
<p>If you sign in with your Google account in Settings, “Cloud backup”, we store:</p>
<ul>
<li>your account ID and email address, to know whose backup it is;</li>
<li>a copy of your game (the data in point 2) and a summary (pet names, level, coins and date), to show you when restoring it.</li>
</ul>
<p>We only use it to store your game and give it back to you. The legal basis is that you ask us to when you turn the backup on (performance of the service). The backup is stored in Google Firebase (Google Ireland Ltd.), on servers in the European Union; Google acts as our processor and may process account data outside the EU with the safeguards required by law (EU-US Data Privacy Framework and standard contractual clauses). Each account can only read its own backup and the connection is encrypted.</p>
<p>The backup is kept until you delete it. You can sign out at any time and delete the backup and the account from the app (see <a href="delete-account.html">how to delete your account</a>).</p>

<h2>4. Endless mode leaderboard (optional)</h2>
<p>If you join the leaderboard (the “Leaderboard” button in endless mode), we store in Google Firebase, visible to other players:</p>
<ul>
<li>your account ID: that of an anonymous Google Firebase account (no name or email) created when you join or, if you have signed in with Google, that of your Google account (then no anonymous account is created). That ID is visible in the leaderboard data, but it is not a name or an email;</li>
<li>a nickname made up by the app (for example, “Swift Panda 482”; you can't type your own text);</li>
<li>the species of the pet you played with;</li>
<li>your best scores per level, for the week and all time, and the date you got them.</li>
</ul>
<p>While you play a game we also store its level and the time it started, to check that the result is possible; they are deleted when the game ends. We only use this to show the leaderboard. The legal basis is that you ask for it when joining (performance of the service). It is stored in Google Firebase, like the backup in point 3. If you later sign in with your Google account, the leaderboard moves to that account.</p>
<p>You can leave at any time in Settings, “Leaderboard”, “Leave the leaderboard”: your positions in all levels and the anonymous account are deleted; if you have signed in with Google, that account's positions are deleted. If you sign out of Google, you leave the leaderboard on that phone, but your positions stay with your Google account, like the backup: they are deleted with “Leave the leaderboard” while you are signed in with it, or with “Delete my backup”.</p>

<h2>5. Microphone</h2>
<p>It is only used while you press the microphone button in the speaking exercises. Your phone's system (Google or Apple) recognises your speech, on the phone itself whenever possible. Englimals never stores or sends your voice.</p>

<h2>6. Reminders</h2>
<p>Your pets' reminders are scheduled by the phone itself. We don't send anything to any server for them. You can turn them off in Settings.</p>

<h2>7. Ads and purchases</h2>
<p>The app has no ads or purchases right now. If they are added, Google AdMob and your phone's store will handle them; we will update this policy first and ask for your consent when the law requires it.</p>

<h2>8. What we don't do</h2>
<p>We don't sell your data, share it with anyone for advertising, or use it for anything other than making the app work.</p>

<h2>9. Children</h2>
<p>Englimals is not meant for children under 13. If we learn that a child under that age has given us data, we will delete it.</p>

<h2>10. Your rights</h2>
<p>You can ask us to access, correct, delete, restrict or object to the use of your data, and to receive a copy of it, by writing to {correo}. We will reply within one month. If you disagree with our answer, you can complain to the Spanish Data Protection Agency (<a href="https://www.aepd.es">www.aepd.es</a>) or your local authority.</p>

<h2>11. Changes</h2>
<p>If we change this policy, we will update the date above and, if the change is important, let you know in the app.</p>
</div>""",
    idioma="en",
    nivel=2,
    otro_idioma=("Español", "../privacidad.html"),
)

pagina(
    "englimals/en/terms.html",
    "Terms of use · Englimals",
    "Terms of use",
    f"""<div class="tarjeta">
<p class="fecha">Last updated: {FECHA_EN}</p>
<ol>
<li>Englimals is provided as is, for personal use. We do our best to keep the content correct, but it may contain mistakes.</li>
<li>The lessons are always free.</li>
<li>Coins, tickets and in-game items have no value outside the game and cannot be exchanged for money.</li>
<li>If there are purchases in the future, they will be governed by the terms of your phone's store.</li>
<li>We may update the app, its content and these terms. If a change is important, we will let you know in the app.</li>
<li>The pets, art, texts and code of Englimals belong to their authors. Third-party resources are listed in the app, in Settings, “Credits and licences”.</li>
<li>For any question: {correo}.</li>
</ol>
</div>""",
    idioma="en",
    nivel=2,
    otro_idioma=("Español", "../terminos.html"),
)

pagina(
    "englimals/en/delete-account.html",
    "Delete your account · Englimals",
    "Delete your account and data",
    f"""<div class="tarjeta">
<p>Englimals only stores data outside your phone if you turned on the cloud backup or joined the leaderboard. This is how to delete it:</p>
<h2>From the app (immediately)</h2>
<ol>
<li>Open Englimals and go to Settings.</li>
<li>Under “Cloud backup”, tap “Delete my backup”.</li>
<li>Confirm with “Delete”.</li>
</ol>
<p>Your cloud backup and your Englimals cloud account are deleted. The game on your phone is not touched.</p>
<p>For the leaderboard: in Settings, “Leaderboard”, tap “Leave the leaderboard” and confirm. Your positions in all levels are deleted and, if you didn't sign in with Google, the anonymous account too. If you signed in with Google, that account's positions are deleted: do it while signed in (if you signed out, sign in with it again) or use “Delete my backup”, which also deletes them.</p>
<h2>Without the app</h2>
<p>Write to {correo} from the email of the Google account you signed in with, with the subject “Delete my Englimals account”. We will delete it within 30 days and let you know.</p>
<h2>What is deleted</h2>
<p>Your game backup, its summary, your account ID and your email. We keep nothing afterwards. If you were on the leaderboard, also your positions, your nickname and your pet's species.</p>
<h2>Data on your phone</h2>
<p>It is deleted when you uninstall the app.</p>
</div>""",
    idioma="en",
    nivel=2,
    otro_idioma=("Español", "../borrar-cuenta.html"),
)

print("Páginas generadas.")
