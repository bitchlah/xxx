# Edit By @pikyus1
# @greyyvbss
# Terima kasih untuk semua creator yang membuat animasi gambarβ¨
# Maaf bagi creator yang belum dicantumkan atas kelalaian saya ππ»
# collect image animation by @punya_alby
# Modifikasi edit by @punya_alby
# Jangan Dihapus Credits nya bodoh
# DAH CAPE NIH NGUMPULIN ANIMASI GAMBAR SANA SINI
# βββββββββββββββββββββββββββββββββ
# βββββββββββββββββββββββββββββββββ
# βββββββββββββββββββββββ¦ββββββββββ
# βββββββββββββββββββββββββββββββββ
# βββββββββββββββββββββββ¦ββββββββββ
# βββββββββββββββββββββββββββββββββ
# PERSETAN DENGAN ORANG YANG HAPUS CREDIT

from time import sleep
from AyiinXd import bot
from AyiinXd.events import register
from telethon import events
import asyncio


@register(outgoing=True, pattern='^.huh(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n(\\_/)`"
                     "`\n(β_β)`"
                     "`\n />β€οΈ *Ini Buat Kamu`")
    sleep(3)
    await typew.edit("`\n(\\_/)`"
                     "`\n(β_β)`"
                     "`\n/>π  *Aku Ambil Lagi`")
    sleep(2)
    await typew.edit("`\n(\\_/)`"
                     "`\n(β_β)`"
                     "`\nπ<\\  *Terimakasih`")


@register(outgoing=True, pattern='^.huh2(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n(\\_/)`"
                     "`\n(β_β)`"
                     "`\n />β€οΈ *NIH AKU KASIH BUAT KAMU`")
    sleep(3)
    await typew.edit("`\n(\\_/)`"
                     "`\n(β_β)`"
                     "`\n/>π  *Eh GAK JADI DEH,UDAH DI KASIH GRATIS MALAH DIRUSAKIN`")
    sleep(2)
    await typew.edit("`\n(\\_/)`"
                     "`\n(β_β)`"
                     "`\nπ<\\  *Terimakasih sudah dirusak..`")
# CREDIT BY @PUNYA_ALBY


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 103)

    input_str = event.pattern_match.group(1)

    if input_str == "ceritacinta":

        await event.edit(input_str)

        animation_chars = [
            "`Cerita β€οΈ Cinta` ",
            "  π             π \n/π\\         <π\\ \n π               /|",
            "  π          π³ \n/π\\       /π\\ \n  π            /|",
            "  π            π \n/π\\         <π> \n  π             /|",
            "  π         βΊοΈ \n/π\\      /π\\ \n  π          /|",
            "  π          π \n/π\\       /π\\ \n  π           /|",
            "  π   π \n /π\\/π\\ \n   π   /|",
            " π³  π \n /|\\ /π\\ \n /     / |",
            "π    /π°\\ \n<|\\      π \n /π    / |",
            "π \n/(),βπ? \n /\\         _/\\/|",
            "π \n/\\_,__π« \n  //    //       \\",
            "π \n/\\_,π¦_π  \n  //         //        \\",
            "  π­      βΊοΈ \n  /|\\   /(πΆ)\\ \n  /!\\   / \\ ",
            "`TAMAT π`"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 103])


@register(outgoing=True, pattern='^.nah(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n(\\_/)`"
                     "`\n(β_β)`"
                     "`\n />π *Ini Buat Kamu`")
    sleep(2)
    await typew.edit("`\n(\\_/)`"
                     "`\n(β_β)`"
                     "`\nπ<\\  *Tapi Bo'ong Hiyahiyahiya`")


@register(outgoing=True, pattern='^.nah2(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n(\\_/)`"
                     "`\n(β_β)`"
                     "`\n />π *Ini Buat Kamu`")
    sleep(2)
    await typew.edit("`\n(\\_/)`"
                     "`\n(β_β)`"
                     "`\nπ<\\  *Tapi Bo'ong`")
    sleep(2)
    await typew.edit("`\n(\\_/)`"
                     "`\n(β_β)`"
                     "`\n />π *eh maaf nih beneran buat kamu`")
    sleep(2)
    await typew.edit("`\n(\\_/)`"
                     "`\n(β_β)`"
                     "`\n/>π  *KOK MALAH DIRUSAKIN SIH??`")
    sleep(2)
    await typew.edit("`\n(\\_/)`"
                     "`\n(β_β)`"
                     "`\nπ<\\  *Yaudah ku ambil lagi eumm`")
# CREDIT BY @PUNYA_ALBY


@register(outgoing=True, pattern=r"^\.nih$")
async def nih(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n(\\_/)`"
                     "`\n(β_β)`"
                     "`\n />π *Ini Buat Kamu`"
                     "\n                    \n"
                     r"`(\_/)`"
                     "`\n(β_β)`"
                     "`\nπ<\\  *Tapi Bo'ong`")


@register(outgoing=True, pattern=r"^\.tai$")
async def taco(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("\n{\\__/}"
                     "\n(β_β)"
                     "\n( >π© Mau Tai Ku?")


@register(outgoing=True, pattern="^.fuck$")
async def iqless(e):
    await e.edit("ππππππππ\nππππππππ\nππ\nππ\nππ\nππππππ\nππππππ\nππ\nππ\nππ\nππ\nππ")


@register(outgoing=True, pattern=r"^\.bulan2$")
async def moon(event):
    deq = deque(list("ππππππππ"))
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern="^.kiss(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("πππππ"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(117)

    input_str = event.pattern_match.group(1)

    if input_str == "bulan":

        await event.edit(input_str)

        animation_chars = [
            "π",
            "π",
            "π",
            "π",
            "π",
            "π",
            "π",
            "π",
            "π",
            "π",
            "π",
            "π",
            "π",
            "π",
            "π",
            "π",
            "π",
            "π",
            "π",
            "π",
            "π",
            "π",
            "π",
            "π",
            "π",
            "π",
            "π",
            "π",
            "π",
            "π",
            "π",
            f"π"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 32])


@register(outgoing=True, pattern=r"^\.bunga$")
async def moon(event):
    deq = deque(list("πΌπ»πΊπΉπΈπ·"))
    try:
        for x in range(35):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern=r"^\.waktu$")
async def moon(event):
    deq = deque(list("πππππππ"))
    try:
        for x in range(100):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern=r"^\.buah$")
async def moon(event):
    deq = deque(list("πππππππ"))
    try:
        for x in range(35):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern=r"^\.jam$")
async def clock(event):
    deq = deque(list("πππππππππππ"))
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern="^.hujan$")
async def rain(event):
    deq = deque(list("βοΈπ€βοΈπ₯βοΈπ§β"))
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern="^.love$")
async def love(event):
    deq = deque(list("β€οΈπ§‘πππππ€πππππππ"))
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern="^.bumi$")
async def earth(event):
    deq = deque(list("ππππππππ"))
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern="^.hati$")
async def earth(event):
    deq = deque(list("π€πππππ§‘β€οΈπ€"))
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern="^.monyet$")
async def earth(event):
    deq = deque(list("ππππππππ"))
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern="^.emo$")
async def earth(event):
    deq = deque(list("ππππππ€£π­π΅πππ"))
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern="^.gas$")
async def gas(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("___________________π")
        await e.edit("________________π___")
        await e.edit("______________π_____")
        await e.edit("___________π________")
        await e.edit("________π___________")
        await e.edit("_____π______________")
        await e.edit("__π_________________")
        await e.edit("π___________________")
        await e.edit("_____________________")
        await e.edit(choice(FACEREACTS))


@register(outgoing=True, pattern="^.sayang$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("I LOVEE YOUUU π")
        await e.edit("ππππ")
        await e.edit("ππππ")
        await e.edit("ππππ")
        await e.edit("ππππ")
        await e.edit("ππππ")
        await e.edit("ππππ")
        await e.edit("SAYANG KAMU πππ")
        await e.edit("ππππ")
        await e.edit("ππππ")
        await e.edit("ππππ")
        await e.edit("SAYANG")
        await e.edit("KAMU")
        await e.edit("SELAMANYA π")
        await e.edit("ππππ")
        await e.edit("SAYANG")
        await e.edit("KAMU")
        await e.edit("SAYANG")
        await e.edit("KAMU")
        await e.edit("I LOVE YOUUUU")
        await e.edit("MY BABY")
        await e.edit("ππππ")
        await e.edit("ππππ")
        await e.edit("SAYANG KAMUπ")


@register(outgoing=True, pattern='^.dino(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`DIN DINNN.....`")
    sleep(1)
    await typew.edit("`DINOOOOSAURUSSSSS!!`")
    sleep(1)
    await typew.edit("`π                        π¦`")
    await typew.edit("`π                       π¦`")
    await typew.edit("`π                      π¦`")
    await typew.edit("`π                     π¦`")
    await typew.edit("`π   `LARII`          π¦`")
    await typew.edit("`π                   π¦`")
    await typew.edit("`π                  π¦`")
    await typew.edit("`π                 π¦`")
    await typew.edit("`π                π¦`")
    await typew.edit("`π               π¦`")
    await typew.edit("`π              π¦`")
    await typew.edit("`π             π¦`")
    await typew.edit("`π            π¦`")
    await typew.edit("`π           π¦`")
    await typew.edit("`πWOARGH!   π¦`")
    await typew.edit("`π           π¦`")
    await typew.edit("`π            π¦`")
    await typew.edit("`π             π¦`")
    await typew.edit("`π              π¦`")
    await typew.edit("`π               π¦`")
    await typew.edit("`π                π¦`")
    await typew.edit("`π                 π¦`")
    await typew.edit("`π                  π¦`")
    await typew.edit("`π                   π¦`")
    await typew.edit("`π                    π¦`")
    await typew.edit("`π                     π¦`")
    await typew.edit("`π  Huh-Huh           π¦`")
    await typew.edit("`π                   π¦`")
    await typew.edit("`π                  π¦`")
    await typew.edit("`π                 π¦`")
    await typew.edit("`π                π¦`")
    await typew.edit("`π               π¦`")
    await typew.edit("`π              π¦`")
    await typew.edit("`π             π¦`")
    await typew.edit("`π            π¦`")
    await typew.edit("`π           π¦`")
    await typew.edit("`π          π¦`")
    await typew.edit("`π         π¦`")
    await typew.edit("`DIA SEMAKIN MENDEKAT!!!`")
    sleep(1)
    await typew.edit("`π       π¦`")
    await typew.edit("`π      π¦`")
    await typew.edit("`π     π¦`")
    await typew.edit("`π    π¦`")
    await typew.edit("`Dahlah Pasrah Aja`")
    sleep(1)
    await typew.edit("`π§π¦`")
    sleep(2)
    await typew.edit("`-TAMAT-`")


@register(outgoing=True, pattern="^.gabut2$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`Kawan kawan Aku mau cerita sedikit`")
        sleep(1)
        await e.edit("`Jadi Hari ini Aku lagi stressss anjing `")
        sleep(1)
        await e.edit("`GARA GARA GUA LIAT GRUP RAME`")
        sleep(1)
        await e.edit("`GILIRAN GUA NGETIK SEKETIKA SEPI`")
        sleep(1)
        await e.edit("`ANJING BANGET KAN YA`")
        sleep(1)
        await e.edit("`PADAHAL PAS GUA BLM DTG RAME BGT`")
        sleep(1)
        await e.edit("`PAS GUA MUNCUL SEPI BGT`")
        sleep(1)
        await e.edit("`ADA RASA INGIN KELUAR`")
        sleep(1)
        await e.edit("`TAPI KALIAN TEMAN AKU`")
        sleep(1)
        await e.edit("π₯Ί")
        await e.edit("π­")
        await e.edit("π")
        await e.edit("π")
        await e.edit("`TAI BANGET POKOK NYA`")
        await e.edit("π©")
        await e.edit("...........................π")
        await e.edit("..........................π.")
        await e.edit("..............πΊ.........π..")
        await e.edit("..............πΊ........π...")
        await e.edit("..............πΊ.......π....")
        await e.edit("..............πΊ......π.....")
        await e.edit("..............πΊ.....π......")
        await e.edit("..............πΊ....π.......")
        await e.edit("..............πΊ...π........")
        await e.edit("..............πΊ.π..........")
        await e.edit("..............πΊπ...........")
        await e.edit("............ππΊ.............")
        await e.edit("..........π...πΊ............")
        await e.edit(".........π.....πΊ...........")
        await e.edit("........π.......πΊ..........")
        await e.edit(".......π..........πΊ........")
        await e.edit("......π.............πΊ......")
        await e.edit(".....π...............πΊ.....")
        await e.edit("....π..................πΊ...")
        await e.edit("..π.....................πΊ..")
        await e.edit(".π........................πΊ")
        await e.edit("π...........................")
        await e.edit("...........................π")
        await e.edit("........π π‘ποΈ............π.")
        await e.edit("........ποΈπ‘π ...........π..")
        await e.edit("........ποΈπ‘π ..........π...")
        await e.edit("........ποΈπ‘π .........π....")
        await e.edit("........ποΈποΈποΈ........π.....")
        await e.edit("........π‘π π‘.......π......")
        await e.edit("........ποΈπ‘π ......π.......")
        await e.edit("........ποΈπ‘π .....π........")
        await e.edit("........ποΈπ‘π ....π.........")
        await e.edit("........ποΈπ‘π ...π..........")
        await e.edit("........ποΈπ‘π ..π...........")
        await e.edit("........ποΈπ‘π .π............")
        await e.edit("........ποΈπ‘π π.............")
        await e.edit("........ποΈπ‘ππ .............")
        await e.edit("........ποΈππ‘π .............")
        await e.edit("........ππ π‘ποΈ.............")
        await e.edit(".......π.π π‘π‘.............")
        await e.edit("......π..ποΈπ‘π .............")
        await e.edit(".....π...ποΈπ‘π .............")
        await e.edit("....π....ποΈπ π‘.............")
        await e.edit("...π.....π π‘ποΈ.............")
        await e.edit("..π......ποΈπ‘π .............")
        await e.edit(".π.......ποΈπ‘π .............")
        await e.edit("π........π π‘ποΈ.............")
        await e.edit("...........................π")
        await e.edit("............π............π.")
        await e.edit("............π...........π..")
        await e.edit("............π..........π...")
        await e.edit("............π.........π....")
        await e.edit("............π........π.....")
        await e.edit("............π.......π......")
        await e.edit("............π......π.......")
        await e.edit("............π.....π........")
        await e.edit("............π....π.........")
        await e.edit("............π...π..........")
        await e.edit("............π..π...........")
        await e.edit("............π.π............")
        await e.edit("............ππ.............")
        await e.edit("............ππ.............")
        await e.edit("...........π.π.............")
        await e.edit("..........π..π.............")
        await e.edit(".........π...π.............")
        await e.edit("........π....πα΄¬α΄Έα΄Έα΄¬α΄΄α΅ α΄¬α΄·α΄?α΄¬α΄ΏΒ²Λ£.")
        await e.edit("α΅α΄¬α΄΄ α΄¬α΄°αΆ»α΄¬α΄Ίπ....π.............")
        await e.edit("Λ’α΄΄α΄Όα΄Έα΄¬α΅ α΄¬α΄΄π....π.............")
        await e.edit(".........π...π............")
        await e.edit("...........π.π............")
        await e.edit("............ππ............")
        await e.edit("CERITANYA LAGI SHOLAT")
        await e.edit("KARNA SI UDIN TIDAK MAU CELAKA")
        await e.edit("SUNGGUH BERMANFAAT YAH GABUT NYA")
        await e.edit("KATA SI UDIN")
        await e.edit("SHOLAT LAH SEBELUM KAU DI SHOLATKAN")
        await e.edit("α΄¬α΄Έα΄΄α΄¬α΄Ήα΄°α΅α΄Έα΄΅α΄Έα΄Έα΄¬α΄΄ α΄°α΄΄ α΄·α΄±α΄Έα΄¬α΄Ώππ.............")
        await e.edit("α΄?α΄΅Λ’α΄Ήα΄΅α΄Έα΄Έα΄¬α΄΄..........π.π.............")
        await e.edit("...............π..π.............")
        await e.edit("..............π...π.............")
        await e.edit(".............π....π.............")
        await e.edit("............π.....π.............")
        await e.edit("...........π......π.............")
        await e.edit("..........π.......π.............")
        await e.edit("ποΈ.......π........π.............")
        await e.edit("ποΈ......π.........π.............")
        await e.edit("ποΈ.....π..........π.............")
        await e.edit("ποΈ....π...........π.............")
        await e.edit("ποΈ...π............π.............")
        await e.edit("ποΈ..π.............π.............")
        await e.edit("ποΈ.π..............π.............")
        await e.edit("ποΈπ...............π.............")
        await e.edit("..............................πποΈ")
        await e.edit(".............................π.ποΈ")
        await e.edit("............................π..ποΈ")
        await e.edit("...........................π...ποΈ")
        await e.edit("..........................π....ποΈ")
        await e.edit(".........................π.....ποΈ")
        await e.edit("........................π......ποΈ")
        await e.edit(".......................π.......ποΈ")
        await e.edit(".....................π.........ποΈ")
        await e.edit("....................π..........ποΈ")
        await e.edit("...................π...........ποΈ")
        await e.edit("..................π............ποΈ")
        await e.edit(".................π.............ποΈ")
        await e.edit("................π..............ποΈ")
        await e.edit("...............π...............ποΈ")
        await e.edit("..............π................ποΈ")
        await e.edit(".............π.................ποΈ")
        await e.edit("............π..................ποΈ")
        await e.edit("...........π...................ποΈ")
        await e.edit("..........π....................ποΈ")
        await e.edit(".........π.....................ποΈ")
        await e.edit("........π......................ποΈ")
        await e.edit(".......π.......................ποΈ")
        await e.edit("......π........................ποΈ")
        await e.edit(".....π.........................ποΈ")
        await e.edit("....π..........................ποΈ")
        await e.edit("...π...........................ποΈ")
        await e.edit("..π............................ποΈ")
        await e.edit(".π.............................ποΈ")
        await e.edit("π..............................ποΈ")
        await e.edit("π’                       πΆ")
        await e.edit("π’                      πΆ")
        await e.edit("π’                     πΆ")
        await e.edit("π’                    πΆ")
        await e.edit("π’                   πΆ")
        await e.edit("π’                  πΆ")
        await e.edit("π’                 πΆ")
        await e.edit("π’                πΆ")
        await e.edit("π’               πΆ")
        await e.edit("π’              πΆ")
        await e.edit("π’             πΆ")
        await e.edit("π’            πΆ")
        await e.edit("π’           πΆ")
        await e.edit("π’          πΆ")
        await e.edit("π’         πΆ")
        await e.edit("π’        πΆ")
        await e.edit("π’       πΆ")
        await e.edit("π’      πΆ")
        await e.edit("π’     πΆ")
        await e.edit("π’    πΆ")
        await e.edit("π’   πΆ")
        await e.edit("π’  πΆ")
        await e.edit("π’ πΆ")
        await e.edit("π’πΆ")
        await e.edit("πΆπ’")
        await e.edit("πΆ π’")
        await e.edit("πΆ  π’")
        await e.edit("πΆ   π’")
        await e.edit("πΆ    π’")
        await e.edit("πΆ     π’")
        await e.edit("πΆ      π’")
        await e.edit("πΆ       π’")
        await e.edit("πΆ        π’")
        await e.edit("πΆ         π’")
        await e.edit("πΆ          π’")
        await e.edit("πΆ           π’")
        await e.edit("πΆ            π’")
        await e.edit("πΆ             π’")
        await e.edit("πΆ              π’")
        await e.edit("πΆ               π’")
        await e.edit("πΆ                π’")
        await e.edit("πΆ                 π’")
        await e.edit("πΆ                  π’")
        await e.edit("πΆ                   π’")
        await e.edit("πΆ                    π’")
        await e.edit("πΆ                     π’")
        await e.edit("πΆ                      π’")
        await e.edit("πΆ                       π’")
        await e.edit("πΆ                        π’")
        await e.edit("πΆ                         π’")
        await e.edit("πΆ                          π’")
        await e.edit("πΆ                           π’")
        await e.edit("πΆ                            π’")
        await e.edit("πΆ                             π’")
        await e.edit("πΆ                              π’")
        await e.edit("πΆ                               π’")
        await e.edit("πΆ                                π’")
        await e.edit("π’                       πΆ")
        await e.edit("π’                      πΆ")
        await e.edit("π’                     πΆ")
        await e.edit("π’                    πΆ")
        await e.edit("π’                   πΆ")
        await e.edit("π’                  πΆ")
        await e.edit("π’                 πΆ")
        await e.edit("π’                πΆ")
        await e.edit("π’               πΆ")
        await e.edit("π’              πΆ")
        await e.edit("π’             πΆ")
        await e.edit("π’            πΆ")
        await e.edit("π’           πΆ")
        await e.edit("π’          πΆ")
        await e.edit("π’         πΆ")
        await e.edit("π’        πΆ")
        await e.edit("π’       πΆ")
        await e.edit("π’      πΆ")
        await e.edit("π’     πΆ")
        await e.edit("π’    πΆ")
        await e.edit("π’   πΆ")
        await e.edit("π’  πΆ")
        await e.edit("π’ πΆ")
        await e.edit("π’πΆ")
        await e.edit("πΆπ’")
        await e.edit("πΆ π’")
        await e.edit("πΆ  π’")
        await e.edit("πΆ   π’")
        await e.edit("πΆ    π’")
        await e.edit("πΆ     π’")
        await e.edit("πΆ      π’")
        await e.edit("πΆ       π’")
        await e.edit("πΆ        π’")
        await e.edit("πΆ         π’")
        await e.edit("πΆ          π’")
        await e.edit("πΆ           π’")
        await e.edit("πΆ            π’")
        await e.edit("πΆ             π’")
        await e.edit("πΆ              π’")
        await e.edit("πΆ               π’")
        await e.edit("πΆ                π’")
        await e.edit("πΆ                 π’")
        await e.edit("πΆ                  π’")
        await e.edit("πΆ                   π’")
        await e.edit("πΆ                    π’")
        await e.edit("πΆ                     π’")
        await e.edit("πΆ                      π’")
        await e.edit("πΆ                       π’")
        await e.edit("πΆ                        π’")
        await e.edit("πΆ                         π’")
        await e.edit("πΆ                          π’")
        await e.edit("πΆ                           π’")
        await e.edit("πΆ                            π’")
        await e.edit("πΆ                             π’")
        await e.edit("πΆ                              π’")
        await e.edit("πΆ                               π’")
        await e.edit("πΆ                                π’")
        await e.edit("`NGAPAIN DI LIAT?ππ‘`")


@register(outgoing=True, pattern="^.gabut$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`PERNAAHHHHH KAHHH KAUUU MENGIRA`")
        await e.edit("`SEPEEERTIIIII APAAAA BENTUKKKKKKK CINTAAAA`")
        await e.edit("`RAMBUUUT WARNAAA WARNII`")
        await e.edit("`BAGAI GULALI`")
        await e.edit("`IMUUUTTTTT LUCUUU`")
        await e.edit("`WALAAUUUU TAK TERLALU TINGGI`")
        await e.edit("`GW GABUUTTTT`")
        await e.edit("`EMMMM BACOTNYA`")
        await e.edit("`GABUTTTT WOI GABUT`")
        await e.edit("ππππ")
        await e.edit("ππππ")
        await e.edit("ππππ")
        await e.edit("ππππ")
        await e.edit("`CILUUUKKK BAAAAA`")
        await e.edit("ππππ")
        await e.edit("π’                       πΆ")
        await e.edit("π’                      πΆ")
        await e.edit("π’                     πΆ")
        await e.edit("π’                    πΆ")
        await e.edit("π’                   πΆ")
        await e.edit("π’                  πΆ")
        await e.edit("π’                 πΆ")
        await e.edit("π’                πΆ")
        await e.edit("π’               πΆ")
        await e.edit("π’              πΆ")
        await e.edit("π’             πΆ")
        await e.edit("π’            πΆ")
        await e.edit("π’           πΆ")
        await e.edit("π’          πΆ")
        await e.edit("π’         πΆ")
        await e.edit("π’        πΆ")
        await e.edit("π’       πΆ")
        await e.edit("π’      πΆ")
        await e.edit("π’     πΆ")
        await e.edit("π’    πΆ")
        await e.edit("π’   πΆ")
        await e.edit("π’  πΆ")
        await e.edit("π’ πΆ")
        await e.edit("π’πΆ")
        await e.edit("πΆπ’")
        await e.edit("πΆ π’")
        await e.edit("πΆ  π’")
        await e.edit("πΆ   π’")
        await e.edit("πΆ    π’")
        await e.edit("πΆ     π’")
        await e.edit("πΆ      π’")
        await e.edit("πΆ       π’")
        await e.edit("πΆ        π’")
        await e.edit("πΆ         π’")
        await e.edit("πΆ          π’")
        await e.edit("πΆ           π’")
        await e.edit("πΆ            π’")
        await e.edit("πΆ             π’")
        await e.edit("πΆ              π’")
        await e.edit("πΆ               π’")
        await e.edit("πΆ                π’")
        await e.edit("πΆ                 π’")
        await e.edit("πΆ                  π’")
        await e.edit("πΆ                   π’")
        await e.edit("πΆ                    π’")
        await e.edit("πΆ                     π’")
        await e.edit("πΆ                      π’")
        await e.edit("πΆ                       π’")
        await e.edit("πΆ                        π’")
        await e.edit("πΆ                         π’")
        await e.edit("πΆ                          π’")
        await e.edit("πΆ                           π’")
        await e.edit("πΆ                            π’")
        await e.edit("πΆ                             π’")
        await e.edit("πΆ                              π’")
        await e.edit("πΆ                               π’")
        await e.edit("πΆ                                π’")
        await e.edit("πΆ                                 π’")
        await e.edit("`AHHH MANTAP`")
        await e.edit("π")
        await e.edit("π")
        await e.edit("π")
        await e.edit("π")
        await e.edit("π")
        await e.edit("π")
        await e.edit("π’                       πΆ")
        await e.edit("π’                      πΆ")
        await e.edit("π’                     πΆ")
        await e.edit("π’                    πΆ")
        await e.edit("π’                   πΆ")
        await e.edit("π’                  πΆ")
        await e.edit("π’                 πΆ")
        await e.edit("π’                πΆ")
        await e.edit("π’               πΆ")
        await e.edit("π’              πΆ")
        await e.edit("π’             πΆ")
        await e.edit("π’            πΆ")
        await e.edit("π’           πΆ")
        await e.edit("π’          πΆ")
        await e.edit("π’         πΆ")
        await e.edit("π’        πΆ")
        await e.edit("π’       πΆ")
        await e.edit("π’      πΆ")
        await e.edit("π’     πΆ")
        await e.edit("π’    πΆ")
        await e.edit("π’   πΆ")
        await e.edit("π’  πΆ")
        await e.edit("π’ πΆ")
        await e.edit("π’πΆ")
        await e.edit("πΆπ’")
        await e.edit("πΆ π’")
        await e.edit("πΆ  π’")
        await e.edit("πΆ   π’")
        await e.edit("πΆ    π’")
        await e.edit("πΆ     π’")
        await e.edit("πΆ      π’")
        await e.edit("πΆ       π’")
        await e.edit("πΆ        π’")
        await e.edit("πΆ         π’")
        await e.edit("πΆ          π’")
        await e.edit("πΆ           π’")
        await e.edit("πΆ            π’")
        await e.edit("πΆ             π’")
        await e.edit("πΆ              π’")
        await e.edit("πΆ               π’")
        await e.edit("πΆ                π’")
        await e.edit("πΆ                 π’")
        await e.edit("πΆ                  π’")
        await e.edit("πΆ                   π’")
        await e.edit("πΆ                    π’")
        await e.edit("πΆ                     π’")
        await e.edit("πΆ                      π’")
        await e.edit("πΆ                       π’")
        await e.edit("πΆ                        π’")
        await e.edit("πΆ                         π’")
        await e.edit("πΆ                          π’")
        await e.edit("πΆ                           π’")
        await e.edit("πΆ                            π’")
        await e.edit("πΆ                             π’")
        await e.edit("πΆ                              π’")
        await e.edit("πΆ                               π’")
        await e.edit("πΆ                                π’")
        await e.edit("π’                       πΆ")
        await e.edit("π’                      πΆ")
        await e.edit("π’                     πΆ")
        await e.edit("π’                    πΆ")
        await e.edit("π’                   πΆ")
        await e.edit("π’                  πΆ")
        await e.edit("π’                 πΆ")
        await e.edit("π’                πΆ")
        await e.edit("π’               πΆ")
        await e.edit("π’              πΆ")
        await e.edit("π’             πΆ")
        await e.edit("π’            πΆ")
        await e.edit("π’           πΆ")
        await e.edit("π’          πΆ")
        await e.edit("π’         πΆ")
        await e.edit("π’        πΆ")
        await e.edit("π’       πΆ")
        await e.edit("π’      πΆ")
        await e.edit("π’     πΆ")
        await e.edit("π’    πΆ")
        await e.edit("π’   πΆ")
        await e.edit("π’  πΆ")
        await e.edit("π’ πΆ")
        await e.edit("π’πΆ")
        await e.edit("πΆπ’")
        await e.edit("πΆ π’")
        await e.edit("πΆ  π’")
        await e.edit("πΆ   π’")
        await e.edit("πΆ    π’")
        await e.edit("πΆ     π’")
        await e.edit("πΆ      π’")
        await e.edit("πΆ       π’")
        await e.edit("πΆ        π’")
        await e.edit("πΆ         π’")
        await e.edit("πΆ          π’")
        await e.edit("πΆ           π’")
        await e.edit("πΆ            π’")
        await e.edit("πΆ             π’")
        await e.edit("πΆ              π’")
        await e.edit("πΆ               π’")
        await e.edit("πΆ                π’")
        await e.edit("πΆ                 π’")
        await e.edit("πΆ                  π’")
        await e.edit("πΆ                   π’")
        await e.edit("πΆ                    π’")
        await e.edit("πΆ                     π’")
        await e.edit("πΆ                      π’")
        await e.edit("πΆ                       π’")
        await e.edit("πΆ                        π’")
        await e.edit("πΆ                         π’")
        await e.edit("πΆ                          π’")
        await e.edit("πΆ                           π’")
        await e.edit("πΆ                            π’")
        await e.edit("πΆ                             π’")
        await e.edit("πΆ                              π’")
        await e.edit("πΆ                               π’")
        await e.edit("πΆ                                π’")
        await e.edit("π’                       πΆ")
        await e.edit("π’                      πΆ")
        await e.edit("π’                     πΆ")
        await e.edit("π’                    πΆ")
        await e.edit("π’                   πΆ")
        await e.edit("π’                  πΆ")
        await e.edit("π’                 πΆ")
        await e.edit("π’                πΆ")
        await e.edit("π’               πΆ")
        await e.edit("π’              πΆ")
        await e.edit("π’             πΆ")
        await e.edit("π’            πΆ")
        await e.edit("π’           πΆ")
        await e.edit("π’          πΆ")
        await e.edit("π’         πΆ")
        await e.edit("π’        πΆ")
        await e.edit("π’       πΆ")
        await e.edit("π’      πΆ")
        await e.edit("π’     πΆ")
        await e.edit("π’    πΆ")
        await e.edit("π’   πΆ")
        await e.edit("π’  πΆ")
        await e.edit("π’ πΆ")
        await e.edit("π’πΆ")
        await e.edit("πΆπ’")
        await e.edit("πΆ π’")
        await e.edit("πΆ  π’")
        await e.edit("πΆ   π’")
        await e.edit("πΆ    π’")
        await e.edit("πΆ     π’")
        await e.edit("πΆ      π’")
        await e.edit("πΆ       π’")
        await e.edit("πΆ        π’")
        await e.edit("πΆ         π’")
        await e.edit("πΆ          π’")
        await e.edit("πΆ           π’")
        await e.edit("πΆ            π’")
        await e.edit("πΆ             π’")
        await e.edit("πΆ              π’")
        await e.edit("πΆ               π’")
        await e.edit("πΆ                π’")
        await e.edit("πΆ                 π’")
        await e.edit("πΆ                  π’")
        await e.edit("πΆ                   π’")
        await e.edit("πΆ                    π’")
        await e.edit("πΆ                     π’")
        await e.edit("πΆ                      π’")
        await e.edit("πΆ                       π’")
        await e.edit("πΆ                        π’")
        await e.edit("πΆ                         π’")
        await e.edit("πΆ                          π’")
        await e.edit("πΆ                           π’")
        await e.edit("πΆ                            π’")
        await e.edit("πΆ                             π’")
        await e.edit("πΆ                              π’")
        await e.edit("πΆ                               π’")
        await e.edit("πΆ                                π’")
        await e.edit("`GABUT`")


@register(outgoing=True, pattern="^.mf$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`maaf gak dulu` **γ(γ;_ _)γ=3** ")


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "cinta":

        await event.edit(input_str)

        animation_chars = [
            "`Connecting Ke Server Cinta`",
            "`Mencari Target Cinta`",
            "`Mengirim Cintaku.. 0%\nβββββββββββββββββββββββββ `",
            "`Mengirim Cintaku.. 4%\nβββββββββββββββββββββββββ `",
            "`Mengirim Cintaku.. 8%\nβββββββββββββββββββββββββ `",
            "`Mengirim Cintaku.. 20%\nβββββββββββββββββββββββββ `",
            "`Mengirim Cintaku.. 36%\nβββββββββββββββββββββββββ `",
            "`Mengirim Cintaku.. 52%\nβββββββββββββββββββββββββ `",
            "`Mengirim Cintaku.. 84%\nβββββββββββββββββββββββββ `",
            "`Mengirim Cintaku.. 100%\nβββββββββCINTAKUβββββββββββ `",
            f"`Cintaku Sekarang Sepenuhnya Terkirim Padamu, Dan Sekarang Aku Sangat Mencintai Mu, I Love You π`"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])


@register(outgoing=True, pattern="^.orgil(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`ANJING ADA ORANG GILA.....`")
    sleep(1)
    await typew.edit("`ORANG GILAAAAAA!!`")
    sleep(1)
    await typew.edit("`π                        π€Έ`")
    await typew.edit("`π                       π€Έ`")
    await typew.edit("`π                      π¨βπ¦½`")
    await typew.edit("`π                     βΉοΈ`")
    await typew.edit("`π   `LARII`          π€Ύ`")
    await typew.edit("`π                  π€Ύ`")
    await typew.edit("`π                  π€Ύ`")
    await typew.edit("`π                 π€Ύ`")
    await typew.edit("`π                π€Ύ`")
    await typew.edit("`π               π€Ί`")
    await typew.edit("`π              π`")
    await typew.edit("`π             π`")
    await typew.edit("`π            π`")
    await typew.edit("`π           π€Ύ`")
    await typew.edit("`πPULUPULU   π§`")
    await typew.edit("`π           βΉοΈ`")
    await typew.edit("`π            βΉοΈ`")
    await typew.edit("`π             π€Ί`")
    await typew.edit("`π              π₯΄`")
    await typew.edit("`π               π`")
    await typew.edit("`π                π`")
    await typew.edit("`π                 π€Έ`")
    await typew.edit("`π                  π€Έ`")
    await typew.edit("`π                   π€Έ`")
    await typew.edit("`π                    π€Έ`")
    await typew.edit("`π                     βΉοΈ`")
    await typew.edit("`π  Huh-Huh           π`")
    await typew.edit("`π                   π€`")
    await typew.edit("`π                  π`")
    await typew.edit("`π                 βΉοΈ`")
    await typew.edit("`π                π`")
    await typew.edit("`π               π€΄`")
    await typew.edit("`π              π`")
    await typew.edit("`π             π`")
    await typew.edit("`π            π₯΄`")
    await typew.edit("`π           π₯΄`")
    await typew.edit("`π          π€‘`")
    await typew.edit("`π         π€­`")
    await typew.edit("`CAPE BANGET ANJING!!!`")
    sleep(1)
    await typew.edit("`π       π`")
    await typew.edit("`π      π€Ύ`")
    await typew.edit("`π     π`")
    await typew.edit("`π    π`")
    await typew.edit("`Dahlah Pasrah Aja`")
    sleep(1)
    await typew.edit("`π§π`")
    sleep(2)
    await typew.edit("`-TAMAT-`")


@register(outgoing=True, pattern="^.pesawat(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return

    await event.edit("β-------------")
    await event.edit("-β------------")
    await event.edit("--β-----------")
    await event.edit("---β----------")
    await event.edit("----β---------")
    await event.edit("-----β--------")
    await event.edit("------β-------")
    await event.edit("-------β------")
    await event.edit("--------β-----")
    await event.edit("---------β----")
    await event.edit("----------β---")
    await event.edit("-----------β--")
    await event.edit("------------β-")
    await event.edit("-------------β")
    await asyncio.sleep(3)
    await event.delete()


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 9

    animation_ttl = range(0, 15)

    input_str = event.pattern_match.group(1)

    if input_str == "wupload":

        await event.edit(input_str)

        animation_chars = [
            "Uploading File From Telegram To Whatsapp...",
            " User Online: True\nTelegram API Access: True\nWhatsapp API Access: True\nRead Storage: True ",
            "DOWNLOADING STARTED... \n\n0% [ββββββββββββββββββββ]\n`Connecting To WhatsApp API...`\nETA: 0m, 20s",
            "DOWNLOADING... \n\n11.07% [ββββββββββββββββββββ]\n\nETA: 0m, 18s",
            "DOWNLOADING... \n\n20.63% [ββββββββββββββββββββ]\n\nETA: 0m, 16s",
            "FILE DOWNLOADED, UPLOADING TO ADMIN'S WHATSAPP GROUP [CHUTIYA GENG BOYS]... \n\n34.42% [ββββββββββββββββββββ]\n\nETA: 0m, 14s",
            "UPLOADING... \n\n42.17% [ββββββββββββββββββββ]\n\nETA: 0m, 12s",
            "UPLOADING... \n\n55.30% [ββββββββββββββββββββ]\n\nETA: 0m, 10s",
            "UPLOADING... \n\n64.86% [ββββββββββββββββββββ]\n\nETA: 0m, 08s",
            "UPLOADED TO ADMIN'S WHATSAPP GROUP SERVER ... \n\n74.02% [ββββββββββββββββββββ]\n\nETA: 0m, 06s",
            "SPLITTING FILE IN WHATSAPP SUPPORTED SIZE & UPLOADING IT ... 86.21% [ββββββββββββββββββββ]\n\nETA: 0m, 04s",
            "SPLITTING FILE IN WHATSAPP SUPPORTED SIZE & UPLOADING IT... 93.50% [ββββββββββββββββββββ]\n\nETA: 0m, 02s",
            "UPLOADING TO ADMIN'S WHATSAPP GROUP [CHUTIYA GANG BOYS]... 100% [ββββββββββββββββββββ]\n`Scanning file...`\nETA: 0m, 00s",
            "UPLOADING FILE TO WHATSAPP GROUP COMPLETED!\nFILE VERIFIED: β",
            "API TERMINATED UNTIL FURTHER USAGE..."]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 15])


@bot.on(events.NewMessage(pattern=r"\.bom", outgoing=True))
async def _(event):
    if event.fwd_from:
        return

    await event.edit("βͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \n")
    await asyncio.sleep(0.5)
    await event.edit("π£π£π£π£ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \n")
    await asyncio.sleep(0.5)
    await event.edit("βͺοΈβͺοΈβͺοΈβͺοΈ \nπ£π£π£π£ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \n")
    await asyncio.sleep(0.5)
    await event.edit("βͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nπ£π£π£π£ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \n")
    await asyncio.sleep(0.5)
    await event.edit("βͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nπ£π£π£π£ \nβͺοΈβͺοΈβͺοΈβͺοΈ \n")
    await asyncio.sleep(0.5)
    await event.edit("βͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nπ£π£π£π£ \n")
    await asyncio.sleep(1)
    await event.edit("βͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nπ₯π₯π₯π₯ \n")
    await asyncio.sleep(0.5)
    await event.edit("βͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nπ₯π₯π₯π₯ \nπ₯π₯π₯π₯ \n")
    await asyncio.sleep(0.5)
    await event.edit("βͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nβͺοΈβͺοΈβͺοΈβͺοΈ \nπ΅π΅π΅π΅ \n")
    await asyncio.sleep(0.5)
    await event.edit("MENINGGAL DUNIA...")
    await asyncio.sleep(2)
    await event.delete()


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 17)

    input_str = event.pattern_match.group(1)

    if input_str == "hadiah":

        await event.edit(input_str)

        animation_chars = [
            "β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬\nβ¬β¬β¬[π](https://github.com/sahyam2019/OpenUserBot)β¬",
            "β¬β¬β¬β¬β¬\nπβ¬β¬β¬β¬\nβ¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬\nβ¬β¬β¬[π](https://github.com/sahyam2019/OpenUserBot)β¬",
            "β¬β¬β¬β¬β¬\nβ¬πβ¬β¬β¬\nβ¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬\nβ¬β¬β¬[π](https://github.com/sahyam2019/OpenUserBot)β¬",
            "β¬β¬β¬β¬β¬\nβ¬β¬πβ¬β¬\nβ¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬\nβ¬β¬β¬[π](https://github.com/sahyam2019/OpenUserBot)β¬",
            "β¬β¬β¬β¬β¬\nβ¬β¬β¬πβ¬\nβ¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬\nβ¬β¬β¬[π](https://github.com/sahyam2019/OpenUserBot)β¬",
            "β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬\nβ¬β¬β¬πβ¬\nβ¬β¬β¬β¬β¬\nβ¬β¬β¬[π](https://github.com/sahyam2019/OpenUserBot)β¬",
            "β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬\nβ¬β¬β¬πβ¬\nβ¬β¬β¬[π](https://github.com/sahyam2019/OpenUserBot)β¬",
            "β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬\nβ¬β¬β¬πβ¬\nβ¬β¬β¬[π](https://github.com/sahyam2019/OpenUserBot)β¬\nβ¬β¬β¬β¬β¬",
            "β¬β¬β¬β¬β¬\nβ¬β¬β¬πβ¬\nβ¬β¬β¬[π](https://github.com/sahyam2019/OpenUserBot)β¬\nβ¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬",
            "β¬β¬β¬β¬β¬\nβ¬β¬πβ¬β¬\nβ¬β¬[π](https://github.com/sahyam2019/OpenUserBot)β¬β¬\nβ¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬",
            "β¬β¬β¬β¬β¬\nβ¬πβ¬β¬β¬\nβ¬[π](https://github.com/sahyam2019/OpenUserBot)β¬β¬β¬\nβ¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬",
            "β¬β¬β¬β¬β¬\nπβ¬β¬β¬β¬\n[π](https://github.com/sahyam2019/OpenUserBot)β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬",
            "β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬",
            "β¬β¬β¬β¬\nβ¬β¬β¬β¬\nβ¬β¬β¬β¬\nβ¬β¬β¬β¬",
            "β¬β¬β¬\nβ¬β¬β¬\nβ¬β¬β¬",
            "β¬β¬\nβ¬β¬",
            "[π](https://gifft.me/id/b#Y3A2pY80Bk09qUOi7ToH)"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 17])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 12)

    input_str = event.pattern_match.group(1)

    if input_str == "polisi":

        await event.edit(input_str)

        animation_chars = [

            "π΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅",
            "π΅π΅π΅β¬β¬β¬π΄π΄π΄\nπ΅π΅π΅β¬β¬β¬π΄π΄π΄\nπ΅π΅π΅β¬β¬β¬π΄π΄π΄",
            "π΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅",
            "π΅π΅π΅β¬β¬β¬π΄π΄π΄\nπ΅π΅π΅β¬β¬β¬π΄π΄π΄\nπ΅π΅π΅β¬β¬β¬π΄π΄π΄",
            "π΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅",
            "π΅π΅π΅β¬β¬β¬π΄π΄π΄\nπ΅π΅π΅β¬β¬β¬π΄π΄π΄\nπ΅π΅π΅β¬β¬β¬π΄π΄π΄",
            "π΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅",
            "π΅π΅π΅β¬β¬β¬π΄π΄π΄\nπ΅π΅π΅β¬β¬β¬π΄π΄π΄\nπ΅π΅π΅β¬β¬β¬π΄π΄π΄",
            "π΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅",
            "π΅π΅π΅β¬β¬β¬π΄π΄π΄\nπ΅π΅π΅β¬β¬β¬π΄π΄π΄\nπ΅π΅π΅β¬β¬β¬π΄π΄π΄",
            "π΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅",
            "OUB **Polisi sedang mengejarmu sekarang**"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 12])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_ttl = range(0, 103)

    input_str = event.pattern_match.group(1)

    if input_str == "kill":

        await event.edit(input_str)

        animation_chars = [

            "οΌ¦ο½ο½ο½ο½ο½ο½ο½",
            "(γο½₯ΰΈ΄Οο½₯ΰΈ΄)οΈ»γβδΈ-->",
            "---->____________β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β ",
            "------>__________β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β ",
            "-------->β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β _________",
            "---------->β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β _______",
            "------------>β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β _____",
            "-------------->β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β ____",
            "------------------>",
            "------>;(^γ^)γ",
            "(οΏ£γΌοΏ£) MENINGGAL",
            "**Mati aja kau PERSETAN π΅π΅**",
        ]

        for i in animation_ttl:

            await event.edit(animation_chars[i % 103])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "Macos":

        await event.edit(input_str)

        animation_chars = [

            "`Connecting To Hackintosh...`",
            "`Initiating Hackintosh Login.`",
            "`Loading Hackintosh... 0%\nβββββββββββββββββββββββββ `",
            "`Loading Hackintosh... 4%\nβββββββββββββββββββββββββ `",
            "`Loading Hackintosh... 8%\nβββββββββββββββββββββββββ `",
            "`Loading Hackintosh... 20%\nβββββββββββββββββββββββββ `",
            "`Loading Hackintosh... 36%\nβββββββββββββββββββββββββ `",
            "`Loading Hackintosh... 52%\nβββββββββββββββββββββββββ `",
            "`Loading Hackintosh... 84%\nβββββββββββββββββββββββββ `",
            "`Loading Hackintosh... 100%\nβββββββββββββββββββββββββ `",
            "`Welcome...\n\nStock OS: Symbian OS\nCurrent OS: Hackintosh`\n\n**Spesifikasi PC Saya:**\n\n **CPU:** __2.9GHz Intel Core i9-8950HK (hexa-core, 12MB cache, up to 4.8GHz)__\n\n**Graphics:** __Nvidia GeForce GTX 1080 OC (8GB GDDR5X)__\n\n**RAM:** __32GB DDR4 (2,666MHz)__\n\n**Screen:** __17.3-inch, QHD (2,560 x 1,440) 120Hz G-Sync__\n\n**Storage:** __512GB PCIe SSD, 1TB HDD (7,200 rpm)__\n\n**Ports:** __2 x USB 3.0, 1 x USB-C 3.0, 1 x USB-C (Thunderbolt 3), HDMI, mini DisplayPort, Ethernet, headphone jack, microphone jack__\n\n**Connectivity:** __Killer 1550 802.11ac Wi-Fi, Bluetooth 5.0__\n\n**Camera:** __Alienware FHD camera, Tobii IR Eye-tracking with Windows Hello__\n\n**Size:** __16.7 x 13.1 x 1.18 inches (42.4 x 33.2 x 2.99cm; W x D x H)__"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "Windows":

        await event.edit(input_str)

        animation_chars = [

            "`Connecting To Windows 10...`",
            "`Initiating Windows 10 Login.`",
            "`Loading Windows 10... 0%\nβββββββββββββββββββββββββ `",
            "`Loading Windows 10... 4%\nβββββββββββββββββββββββββ `",
            "`Loading Windows 10... 8%\nβββββββββββββββββββββββββ `",
            "`Loading Windows 10... 20%\nβββββββββββββββββββββββββ `",
            "`Loading Windows 10... 36%\nβββββββββββββββββββββββββ `",
            "`Loading Windows 10... 52%\nβββββββββββββββββββββββββ `",
            "`Loading Windows 10... 84%\nβββββββββββββββββββββββββ `",
            "`Loading Windows 10... 100%\nβββββββββββββββββββββββββ `",
            "`Welcome...\n\nStock OS: Symbian OS\nCurrent OS: Windows 10`\n\n**Spesifikasi PC Saya:**\n\n **CPU:** __2.9GHz Intel Core i9-8950HK (hexa-core, 12MB cache, up to 4.8GHz)__\n\n**Graphics:** __Nvidia GeForce GTX 1080 OC (8GB GDDR5X)__\n\n**RAM:** __32GB DDR4 (2,666MHz)__\n\n**Screen:** __17.3-inch, QHD (2,560 x 1,440) 120Hz G-Sync__\n\n**Storage:** __512GB PCIe SSD, 1TB HDD (7,200 rpm)__\n\n**Ports:** __2 x USB 3.0, 1 x USB-C 3.0, 1 x USB-C (Thunderbolt 3), HDMI, mini DisplayPort, Ethernet, headphone jack, microphone jack__\n\n**Connectivity:** __Killer 1550 802.11ac Wi-Fi, Bluetooth 5.0__\n\n**Camera:** __Alienware FHD camera, Tobii IR Eye-tracking with Windows Hello__\n\n**Size:** __16.7 x 13.1 x 1.18 inches (42.4 x 33.2 x 2.99cm; W x D x H)__"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "Linux":

        await event.edit(input_str)

        animation_chars = [

            "`Connecting To Linux...`",
            "`Initiating Linux Login.`",
            "`Loading Linux... 0%\nβββββββββββββββββββββββββ `",
            "`Loading Linux... 4%\nβββββββββββββββββββββββββ `",
            "`Loading Linux... 8%\nβββββββββββββββββββββββββ `",
            "`Loading Linux... 20%\nβββββββββββββββββββββββββ `",
            "`Loading Linux... 36%\nβββββββββββββββββββββββββ `",
            "`Loading Linux... 52%\nβββββββββββββββββββββββββ `",
            "`Loading Linux... 84%\nβββββββββββββββββββββββββ `",
            "`Loading Linux... 100%\nβββββββββββββββββββββββββ `",
            "`Welcome...\n\nStock OS: Symbian OS\nCurrent OS: Linux`\n\n**Spesifikasi PC Saya:**\n\n **CPU:** __2.9GHz Intel Core i9-8950HK (hexa-core, 12MB cache, up to 4.8GHz)__\n\n**Graphics:** __Nvidia GeForce GTX 1080 OC (8GB GDDR5X)__\n\n**RAM:** __32GB DDR4 (2,666MHz)__\n\n**Screen:** __17.3-inch, QHD (2,560 x 1,440) 120Hz G-Sync__\n\n**Storage:** __512GB PCIe SSD, 1TB HDD (7,200 rpm)__\n\n**Ports:** __2 x USB 3.0, 1 x USB-C 3.0, 1 x USB-C (Thunderbolt 3), HDMI, mini DisplayPort, Ethernet, headphone jack, microphone jack__\n\n**Connectivity:** __Killer 1550 802.11ac Wi-Fi, Bluetooth 5.0__\n\n**Camera:** __Alienware FHD camera, Tobii IR Eye-tracking with Windows Hello__\n\n**Size:** __16.7 x 13.1 x 1.18 inches (42.4 x 33.2 x 2.99cm; W x D x H)__"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "Stock":

        await event.edit(input_str)

        animation_chars = [

            "`Connecting To Symbian OS...`",
            "`Initiating Symbian OS Login.`",
            "`Loading Symbian OS... 0%\nβββββββββββββββββββββββββ `",
            "`Loading Symbian OS... 4%\nβββββββββββββββββββββββββ `",
            "`Loading Symbian OS... 8%\nβββββββββββββββββββββββββ `",
            "`Loading Symbian OS... 20%\nβββββββββββββββββββββββββ `",
            "`Loading Symbian OS... 36%\nβββββββββββββββββββββββββ `",
            "`Loading Symbian OS... 52%\nβββββββββββββββββββββββββ `",
            "`Loading Symbian OS... 84%\nβββββββββββββββββββββββββ `",
            "`Loading Symbian OS... 100%\nβββββββββββββββββββββββββ `",
            "`Welcome...\n\nStock OS: Symbian OS\nCurrent OS: Symbian OS`\n\n**Spesifikasi PC Saya:**\n\n **CPU:** __2.9GHz Intel Core i9-8950HK (hexa-core, 12MB cache, up to 4.8GHz)__\n\n**Graphics:** __Nvidia GeForce GTX 1080 OC (8GB GDDR5X)__\n\n**RAM:** __32GB DDR4 (2,666MHz)__\n\n**Screen:** __17.3-inch, QHD (2,560 x 1,440) 120Hz G-Sync__\n\n**Storage:** __512GB PCIe SSD, 1TB HDD (7,200 rpm)__\n\n**Ports:** __2 x USB 3.0, 1 x USB-C 3.0, 1 x USB-C (Thunderbolt 3), HDMI, mini DisplayPort, Ethernet, headphone jack, microphone jack__\n\n**Connectivity:** __Killer 1550 802.11ac Wi-Fi, Bluetooth 5.0__\n\n**Camera:** __Alienware FHD camera, Tobii IR Eye-tracking with Windows Hello__\n\n**Size:** __16.7 x 13.1 x 1.18 inches (42.4 x 33.2 x 2.99cm; W x D x H)__"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 7)

    input_str = event.pattern_match.group(1)

    if input_str == "os":

        await event.edit(input_str)

        animation_chars = [
            "`Scanning OS...`",
            "`Scanning OS......`",
            "__Current Loaded OS: CrDroid OS__\n\n**To Boot Other OS, Use The Following Trigger:**\nβοΈ `.Macos`\nβοΈ `.Windows`\nβοΈ `.Linux`\nβοΈ `.Stock`",
            "__Current Loaded OS: CrDroid OS__\n\n**To Boot Other OS, Use The Following Trigger:**\nβ `.Macos`\nβοΈ `.Windows`\nβοΈ `.Linux`\nβοΈ `.Stock`",
            "__Current Loaded OS: CrDroid OS__\n\n**To Boot Other OS, Use The Following Trigger:**\nβ `.Macos`\nβ `.Windows`\nβοΈ `.Linux`\nβοΈ `.Stock`",
            "__Current Loaded OS: CrDroid OS__\n\n**To Boot Other OS, Use The Following Trigger:**\nβ `.Macos`\nβ `.Windows`\nβ `.Linux`\nβοΈ `.Stock`",
            "__Current Loaded OS: CrDroid OS__\n\n**To Boot Other OS, Use The Following Trigger:**\nβ `.Macos`\nβ `.Windows`\nβ `.Linux`\nβ `.Stock`\n\n by @heyworld and others"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 7])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 24)

    input_str = event.pattern_match.group(1)

    if input_str == "sinyal":

        await event.edit(input_str)

        animation_chars = [

            "β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬",
            "β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nπβ¬β¬β¬β¬β¬",
            "β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬πβ¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬",
            "β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬πβ¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬",
            "β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬πβ¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬",
            "β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬πβ¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬",
            "β¬β¬β¬β¬β¬π\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬",
            "πΈβ¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬",
            "β¬β¬β¬β¬β¬β¬\nπΈβ¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬",
            "β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬πΈβ¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬",
            "β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬πΈβ¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬",
            "β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬πΈβ¬β¬β¬\nβ¬β¬β¬β¬β¬β¬",
            "β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬πΈβ¬β¬",
            "β¬β¬β¬πΈβ¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬",
            "β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬πΈβ¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬",
            "β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬πΈβ¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬",
            "β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬πΈβ¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬",
            "β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬πΈβ¬β¬\nβ¬β¬β¬β¬β¬β¬",
            "β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬πΈβ¬πΆββοΈ\nβ¬β¬β¬β¬β¬β¬",
            "β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬πΈπΆββοΈβ¬\nβ¬β¬β¬β¬β¬β¬",
            "β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nπ½β¬β¬πΈπΆββοΈβ¬\nβ¬β¬β¬β¬β¬β¬",
            "β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬π½β¬πΈπΆββοΈβ¬\nβ¬β¬β¬β¬β¬β¬",
            "β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬\nβ¬β¬π½πΈπΆββοΈβ¬\nβ¬β¬β¬β¬β¬β¬",
            "__Sinyal Hilang....__"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 24])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "hackfb":

        await event.edit(input_str)

        animation_chars = [
            "`Connecting To Hacked Private Server...`",
            "`Target Selected.`",
            "`Hacking... 0%\nβββββββββββββββββββββββββ `",
            "`Hacking... 4%\nβββββββββββββββββββββββββ `",
            "`Hacking... 8%\nβββββββββββββββββββββββββ `",
            "`Hacking... 20%\nβββββββββββββββββββββββββ `",
            "`Hacking... 36%\nβββββββββββββββββββββββββ `",
            "`Hacking... 52%\nβββββββββββββββββββββββββ `",
            "`Hacking... 84%\nβββββββββββββββββββββββββ `",
            "`Hacking... 100%\nβββββββββHACKEDβββββββββββ `",
            f"`Akun Target Diretas...\n\nBayar uang sebesar 1000$ terlebih dahulu Ke @{DEFAULTUSER} atau belikan mobil aja Untuk Menghapus Peretasan Ini`"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "hacktel":

        await event.edit(input_str)

        animation_chars = [
            "`Connecting To Hacked Private Server...`",
            "`Target Selected.`",
            "`Hacking... 0%\nβββββββββββββββββββββββββ `",
            "`Hacking... 4%\nβββββββββββββββββββββββββ `",
            "`Hacking... 8%\nβββββββββββββββββββββββββ `",
            "`Hacking... 20%\nβββββββββββββββββββββββββ `",
            "`Hacking... 36%\nβββββββββββββββββββββββββ `",
            "`Hacking... 52%\nβββββββββββββββββββββββββ `",
            "`Hacking... 84%\nβββββββββββββββββββββββββ `",
            "`Hacking... 100%\nβββββββββHACKEDβββββββββββ `",
            f"`Akun Target Diretas...\n\nBayar uang sebesar 9999$ terlebih dahulu Ke @{DEFAULTUSER} atau belikan pizza π aja Untuk Menghapus Peretasan Ini`"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 15)

    input_str = event.pattern_match.group(1)

    if input_str == "support2":

        await event.edit(input_str)

        animation_chars = [
            "β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬",
            "β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬",
            "β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬",
            "β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬",
            "β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬",
            "β¬β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬β¬",
            "β¬β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬β¬",
            "β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬",
            "β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬",
            "β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬",
            "β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬",
            "β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬",
            "β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬",
            "β¬β¬β¬\nβ¬β¬β¬\nβ¬β¬β¬",
            "[ππ΄π](t.me/ruangdiskusikami)"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 15])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 15)

    input_str = event.pattern_match.group(1)

    if input_str == "hackwa":

        await event.edit(input_str)

        animation_chars = [
            "Looking for WhatsApp databases in targeted person...",
            " User online: True\nTelegram access: True\nRead Storage: True ",
            "Hacking... 0%\n[ββββββββββββββββββββ]\n`Looking for WhatsApp...`\nETA: 0m, 20s",
            "Hacking... 11.07%\n[ββββββββββββββββββββ]\n`Looking for WhatsApp...`\nETA: 0m, 18s",
            "Hacking... 20.63%\n[ββββββββββββββββββββ]\n`Found folder C:/WhatsApp`\nETA: 0m, 16s",
            "Hacking... 34.42%\n[ββββββββββββββββββββ]\n`Found folder C:/WhatsApp`\nETA: 0m, 14s",
            "Hacking... 42.17%\n[ββββββββββββββββββββ]\n`Searching for databases`\nETA: 0m, 12s",
            "Hacking... 55.30%\n[ββββββββββββββββββββ]\n`Found msgstore.db.crypt12`\nETA: 0m, 10s",
            "Hacking... 64.86%\n[ββββββββββββββββββββ]\n`Found msgstore.db.crypt12`\nETA: 0m, 08s",
            "Hacking... 74.02%\n[ββββββββββββββββββββ]\n`Trying to Decrypt...`\nETA: 0m, 06s",
            "Hacking... 86.21%\n[ββββββββββββββββββββ]\n`Trying to Decrypt...`\nETA: 0m, 04s",
            "Hacking... 93.50%\n[ββββββββββββββββββββ]\n`Decryption successful!`\nETA: 0m, 02s",
            "Hacking... 100%\n[ββββββββββββββββββββ]\n`Scanning file...`\nETA: 0m, 00s",
            "Hacking complete!\nUploading file...",
            "Akun Target Diretas...!\n\n β File telah berhasil diunggah ke server saya.\nWhatsApp Database:\n`./DOWNLOADS/msgstore.db.crypt12`"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 15])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 27)

    input_str = event.pattern_match.group(1)

    if input_str == "ular3":

        await event.edit(input_str)

        animation_chars = [

            "βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ",

            "β»οΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ",

            "β»οΈβ»οΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ",

            "β»οΈβ»οΈβ»οΈοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ",

            "β»οΈβ»οΈβ»οΈβ»οΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ",

            "ββ»οΈβ»οΈβ»οΈβ»οΈβ»οΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ",

            "β»οΈβ»οΈβ»οΈβ»οΈβ»οΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ»οΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ",

            "β»οΈβ»οΈβ»οΈβ»οΈβ»οΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ»οΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ»οΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ",

            "β»οΈβ»οΈβ»οΈβ»οΈβ»οΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ»οΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ»οΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ»οΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ",

            "β»οΈβ»οΈβ»οΈβ»οΈβ»οΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ»οΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ»οΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ»οΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ»οΈ",

            "β»οΈβ»οΈβ»οΈβ»οΈβ»οΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ»οΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ»οΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ»οΈ\nβΌοΈβΌοΈβΌοΈβ»οΈβ»οΈ",

            "β»οΈβ»οΈβ»οΈβ»οΈβ»οΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ»οΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ»οΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ»οΈ\nβΌοΈβΌοΈβ»οΈβ»οΈβ»οΈ",

            "β»οΈβ»οΈβ»οΈβ»οΈβ»οΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ»οΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ»οΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ»οΈ\nβΌοΈβ»οΈβ»οΈβ»οΈβ»οΈ",

            "β»οΈβ»οΈβ»οΈβ»οΈβ»οΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ»οΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ»οΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ»οΈ\nβ»οΈβ»οΈβ»οΈβ»οΈβ»οΈ",

            "β»οΈβ»οΈβ»οΈβ»οΈβ»οΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ»οΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ»οΈ\nβ»οΈβΌοΈβΌοΈβΌοΈβ»οΈ\nβ»οΈβ»οΈβ»οΈβ»οΈβ»οΈ",

            "β»οΈβ»οΈβ»οΈβ»οΈβ»οΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ»οΈ\nβ»οΈβΌοΈβΌοΈβΌοΈβ»οΈ\nβ»οΈβΌοΈβΌοΈβΌοΈβ»οΈ\nβ»οΈβ»οΈβ»οΈβ»οΈβ»οΈ",

            "β»οΈβ»οΈβ»οΈβ»οΈβ»οΈ\nβ»οΈβΌοΈβΌοΈβΌοΈβ»οΈ\nβ»οΈβΌοΈβΌοΈβΌοΈβ»οΈ\nβ»οΈβΌοΈβΌοΈβΌοΈβ»οΈ\nβ»οΈβ»οΈβ»οΈβ»οΈβ»οΈ",

            "β»οΈβ»οΈβ»οΈβ»οΈβ»οΈ\nβ»οΈβ»οΈβΌοΈβΌοΈβ»οΈ\nβ»οΈβΌοΈβΌοΈβΌοΈβ»οΈ\nβ»οΈβΌοΈβΌοΈβΌοΈβ»οΈ\nβ»οΈβ»οΈβ»οΈβ»οΈβ»οΈ",

            "β»οΈβ»οΈβ»οΈβ»οΈβ»οΈ\nβ»οΈβ»οΈβ»οΈβΌοΈβ»οΈ\nβ»οΈβΌοΈβΌοΈβΌοΈβ»οΈ\nβ»οΈβΌοΈβΌοΈβΌοΈβ»οΈ\nβ»οΈβ»οΈβ»οΈβ»οΈβ»οΈ",

            "β»οΈβ»οΈβ»οΈβ»οΈβ»οΈ\nβ»οΈβ»οΈβ»οΈβ»οΈβ»οΈ\nβ»οΈβΌοΈβΌοΈβΌοΈβ»οΈ\nβ»οΈβΌοΈβΌοΈβΌοΈβ»οΈ\nβ»οΈβ»οΈβ»οΈβ»οΈβ»οΈ",

            "β»οΈβ»οΈβ»οΈβ»οΈβ»οΈ\nβ»οΈβ»οΈβ»οΈβ»οΈβ»οΈ\nβ»οΈβΌοΈβΌοΈβ»οΈβ»οΈ\nβ»οΈβΌοΈβΌοΈβΌοΈβ»οΈ\nβ»οΈβ»οΈβ»οΈβ»οΈβ»οΈ",

            "β»οΈβ»οΈβ»οΈβ»οΈβ»οΈ\nβ»οΈβ»οΈβ»οΈβ»οΈβ»οΈ\nβ»οΈβΌοΈβΌοΈβ»οΈβ»οΈ\nβ»οΈβΌοΈβΌοΈβ»οΈβ»οΈ\nβ»οΈβ»οΈβ»οΈβ»οΈβ»οΈ",

            "β»οΈβ»οΈβ»οΈβ»οΈβ»οΈ\nβ»οΈβ»οΈβ»οΈβ»οΈβ»οΈ\nβ»οΈβΌοΈβΌοΈβ»οΈβ»οΈ\nβ»οΈβΌοΈβ»οΈβ»οΈβ»οΈ\nβ»οΈβ»οΈβ»οΈβ»οΈβ»οΈ",

            "β»οΈβ»οΈβ»οΈβ»οΈβ»οΈ\nβ»οΈβ»οΈβ»οΈβ»οΈβ»οΈ\nβ»οΈβΌοΈβΌοΈβ»οΈβ»οΈ\nβ»οΈβ»οΈβ»οΈβ»οΈβ»οΈ\nβ»οΈβ»οΈβ»οΈβ»οΈβ»οΈ",

            "β»οΈβ»οΈβ»οΈβ»οΈβ»οΈ\nβ»οΈβ»οΈβ»οΈβ»οΈβ»οΈ\nβ»οΈβ»οΈβΌοΈβ»οΈβ»οΈ\nβ»οΈβ»οΈβ»οΈβ»οΈβ»οΈ\nβ»οΈβ»οΈβ»οΈβ»οΈβ»οΈ",

            "β»οΈβ»οΈβ»οΈβ»οΈβ»οΈ\nβ»οΈβ»οΈβ»οΈβ»οΈβ»οΈ\nβ»οΈβ»οΈβ»οΈβ»οΈβ»οΈ\nβ»οΈβ»οΈβ»οΈβ»οΈβ»οΈ\nβ»οΈβ»οΈβ»οΈβ»οΈβ»οΈ",

            "β»οΈβ»οΈβ»οΈβ»οΈβ»οΈ\nβ»οΈβΌοΈβ»οΈβΌοΈβ»οΈ\nβ»οΈβ»οΈβ»οΈβ»οΈβ»οΈ\nβ»οΈβΌοΈβΌοΈβΌοΈβ»οΈ\nβ»οΈβ»οΈβ»οΈβ»οΈβ»οΈ"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 27])


@register(outgoing=True, pattern="^.sange$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("SAYANGGGGGGGGG π")
        sleep(1)
        await e.edit("ππππ")
        sleep(1)
        await e.edit("ππππ")
        sleep(1)
        await e.edit("ππππ")
        sleep(1)
        await e.edit("ππππ")
        sleep(1)
        await e.edit("ππππ")
        sleep(1)
        await e.edit("ππππ")
        sleep(1)
        await e.edit("EMMMMMMπ₯Ίπ₯Ίπ₯Ί")
        sleep(1)
        await e.edit("ππππ")
        await e.edit("ππππ")
        await e.edit("ππππ")
        await e.edit("SAYANG")
        sleep(1)
        await e.edit("AKU ππ")
        sleep(1)
        await e.edit("SANGE ππ ππ")
        sleep(1)
        await e.edit("ππππ")
        sleep(1)
        await e.edit("SAYANG")
        sleep(1)
        await e.edit("AYO NGEWEπ€­π€­")
        sleep(1)
        await e.edit("PLISSπ₯Ίπ₯Ί")
        sleep(1)
        await e.edit("AKU SANGEππ")
        sleep(1)
        await e.edit("I LOVE YOUUUU")
        sleep(1)
        await e.edit("AH AH AH BEIBB")
        sleep(1)
        await e.edit("π¦π¦π¦π¦")
        sleep(1)
        await e.edit("OH BABY")
        sleep(1)
        await e.edit("AKU SAYANG KAMUπ")


@register(outgoing=True, pattern="^.koc$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("8β===D")
        await e.edit("8=β==D")
        await e.edit("8==β=D")
        await e.edit("8===βD")
        await e.edit("8==β=D")
        await e.edit("8=β==D")
        await e.edit("8β===D")
        await e.edit("8=β==D")
        await e.edit("8==β=D")
        await e.edit("8===βD")
        await e.edit("8==β=D")
        await e.edit("8=β==D")
        await e.edit("8β===D")
        await e.edit("8=β==D")
        await e.edit("8==β=D")
        await e.edit("8===βD")
        await e.edit("8==β=D")
        await e.edit("8=β==D")
        await e.edit("8===βDπ¦")
        await e.edit("8==β=Dπ¦π¦")
        await e.edit("8=β==Dπ¦π¦π¦")
        await e.edit("8β===Dπ¦π¦π¦π¦")
        await e.edit("8===βDπ¦π¦π¦π¦π¦")
        await e.edit("8==β=Dπ¦π¦π¦π¦π¦π¦")
        await e.edit("8=β==Dπ¦π¦π¦π¦π¦π¦π¦")
        await e.edit("8β===Dπ¦π¦π¦π¦π¦π¦π¦π¦")
        await e.edit("8===βDπ¦π¦π¦π¦π¦π¦π¦π¦π¦")
        await e.edit("8==β=Dπ¦π¦π¦π¦π¦π¦π¦π¦π¦π¦")
        await e.edit("8=β==D Lah Kok Habis?")
        await e.edit("π­π­π­π­")


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 549755813888)
    input_str = event.pattern_match.group(1)
    if input_str == "solar":
        await event.edit(input_str)
        animation_chars = [
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nπβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nπβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈπβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈββΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈπβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈββΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈπ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nββΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nββΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈπ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈββΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈπβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈββΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈπβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nπβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nπβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈπβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈββΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈπβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈββΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈπ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nββΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nββΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈπ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈββΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈπβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈββΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈπβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nπβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nπβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈπβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈββΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈπβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈββΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈπ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nββΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nββΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈπ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈββΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈπβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈββΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈπβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nπβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nπβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈπβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈββΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈπβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈββΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈπ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nββΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nββΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈπ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈββΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈπβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈββΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈπβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nπβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nπβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈπβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈββΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈπβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈββΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈπ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nββΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nββΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈπ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈββΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈπβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈββΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈπβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nπβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nπβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈπβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈββΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈπβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈββΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈπ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nββΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nββΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈπ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈββΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈπβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈββΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈπβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nπβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nπβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈπβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈββΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈπβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈββΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈπ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nββΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nββΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈπ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈββΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈπβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈββΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈπβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nπβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nπβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈπβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈββΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈπβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈββΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈπ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nββΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nββΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈπ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈββΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈπβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈββΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈπβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nπβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nπβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈπβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈββΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈπβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈββΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈπ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nββΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nββΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈπ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈββΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈπβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈββΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈπβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nπβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nπβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈπβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈββΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈπβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈββΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈπ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nββΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nββΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈπ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈββΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈπβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈββΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈπβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nπβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nπβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈπβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈββΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈπβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈββΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈπ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nββΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nββΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈπ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈββΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈπβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈββΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈπβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nπβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nπβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈπβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈββΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈπβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈββΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈπ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nββΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nββΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈπ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈββΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈπβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈββΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈπβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nπβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nπβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈπβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈββΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈπβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈββΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈπ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nββΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nββΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈπ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈββΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈπβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈββΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈπβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nπβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nπβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈπβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈββΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈπβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈββΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈπ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nββΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nββΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈπ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈββΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈπβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈββΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈπβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nπβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nπβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈπβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈββΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈπβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈββΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈπ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nββΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nββΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈπ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈββΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈπβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈββΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈπβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nπβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nπβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈπβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈββΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈπβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈββΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈπ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nββΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nββΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈπ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈββΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈπβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈββΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈπβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nπβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nπβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈπβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈββΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈπβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈββΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈπ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nββΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nββΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈπ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈββΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈπβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈββΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈπβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nπβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nπβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈπβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈββΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈπβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈββΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈπ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nββΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nββΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈπ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
            "`βΌοΈββΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈπβΌοΈ`",
            "`βΌοΈβΌοΈβΌοΈββΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈπβΌοΈβΌοΈβΌοΈ`",
        ]

        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 549755813888])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 549755813888)
    input_str = event.pattern_match.group(1)
    if input_str == "human":
        await event.edit(input_str)
        animation_chars = [
            "β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nπ²π²π²π²π²π²π²",
            "β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬π\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nπ²π²π²π²π²π²π²",
            "β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬πβ¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nπ²π²π²π²π²π²π²",
            "β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬πβ¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nπ²π²π²π²π²π²π²",
            "β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬πβ¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nπ²π²π²π²π²π²π²",
            "β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬πβ¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nπ²π²π²π²π²π²π²",
            "β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬πβ¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nπ²π²π²π²π²π²π²",
            "β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nπβ¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nπ²π²π²π²π²π²π²",
            "β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nπ²π²π²π²π²π²π²",
            "β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬πβ¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nπ²π²π²π²π²π²π²",
            "β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬πβ¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nπ²π²π²π²π²π²π²",
            "β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬πβ¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nπ²π²π²π²π²π²π²",
            "β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬πβ¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nπ²π²π²π²π²π²π²",
            "β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬πβ¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nπ²π²π²π²π²π²π²",
            "β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬πβ¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nπ²π²π²π²π²π²π²",
            "β¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nβ¬β¬β¬πβ¬β¬β¬\nβ¬β¬β¬β¬β¬β¬β¬\nπ²π²π²π²π²π²π²"]

        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 549755813888])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 549755813888)
    input_str = event.pattern_match.group(1)
    if input_str == "albyuserbot":
        await event.edit(input_str)
        animation_chars = [
            "β«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈ\nβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈ\nβ«οΈβͺοΈβ«οΈ..**α΄ΚΚΚ α΄κ±α΄ΚΚα΄α΄**..β«οΈβͺοΈβ«οΈ\nβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈ\nβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈ\n",
            "βͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈ\nβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈ\nβͺοΈβ«οΈβͺοΈ..**α΄ΚΚΚ α΄κ±α΄ΚΚα΄α΄**..βͺοΈβ«οΈβͺοΈ\nβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈ\nβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈ\n",
            "β«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈ\nβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈ\nβ«οΈβͺοΈβ«οΈ..**α΄ΚΚΚ α΄κ±α΄ΚΚα΄α΄**..β«οΈβͺοΈβ«οΈ\nβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈ\nβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈ\n",
            "βͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈ\nβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈ\nβͺοΈβ«οΈβͺοΈ..**α΄ΚΚΚ α΄κ±α΄ΚΚα΄α΄**..βͺοΈβ«οΈβͺοΈ\nβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈ\nβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈ\n",
            "β«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈ\nβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈ\nβ«οΈβͺοΈβ«οΈ..**α΄ΚΚΚ α΄κ±α΄ΚΚα΄α΄**..β«οΈβͺοΈβ«οΈ\nβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈ\nβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈ\n",
            "βͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈ\nβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈ\nβͺοΈβ«οΈβͺοΈ..**α΄ΚΚΚ α΄κ±α΄ΚΚα΄α΄**..βͺοΈβ«οΈβͺοΈ\nβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈ\nβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈ\n",
            "β«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈ\nβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈ\nβ«οΈβͺοΈβ«οΈ..**α΄ΚΚΚ α΄κ±α΄ΚΚα΄α΄**..β«οΈβͺοΈβ«οΈ\nβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈ\nβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈ\n",
            "βͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈ\nβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈ\nβͺοΈβ«οΈβͺοΈ..**α΄ΚΚΚ α΄κ±α΄ΚΚα΄α΄**..βͺοΈβ«οΈβͺοΈ\nβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈ\nβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈ\n",
            "β«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈ\nβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈ\nβ«οΈβͺοΈβ«οΈ..**α΄ΚΚΚ α΄κ±α΄ΚΚα΄α΄**..β«οΈβͺοΈβ«οΈ\nβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈ\nβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈ\n",
            "βͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈ\nβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈ\nβͺοΈβ«οΈβͺοΈ..**α΄ΚΚΚ α΄κ±α΄ΚΚα΄α΄**..βͺοΈβ«οΈβͺοΈ\nβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈ\nβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈ\n",
            "βͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈ\nβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈ\nβͺοΈβ«οΈβͺοΈ..**α΄ΚΚΚ α΄κ±α΄ΚΚα΄α΄**..βͺοΈβ«οΈβͺοΈ\nβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈ\nβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈβ«οΈβͺοΈ\n",
        ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)


@register(outgoing=True, pattern='^.city(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        """ββπ      β           β
       β  β         β    π    β    β        β          β     β   β
π¬π¨π«π’π€π₯π¦πͺπ«
              π²/     lπ\\π³π­
           π³/  π l  π \\π΄ π¬                       π¬  π΄/            l  π    \\π²
      π²/   π     l               \
   π³/πΆ           |   π         \\ π΄π΄π΄
π΄/                    |                     \\π²"""
    )

# created by @greyyvbss


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 549755813888)
    input_str = event.pattern_match.group(1)
    if input_str == "kereta":
        await event.edit(input_str)
        animation_chars = [
            "**r**",
            "**ra**",
            "**rap**",
            "**rape**",
            "**rape_**",
            "**rape_t**",
            "**rape_tr**",
            "**rape_tra**",
            "**rape_trai**",
            "**rape_train**",
            "**ape_trainπ**",
            "**pe_trainπππ**",
            "**e_trainππππ**",
            "**_trainπππππ**",
            "**trainππππππ**",
            "**rainπππππππ**",
            "**ainππππππππ**",
            "**inπππππππππ**",
            "**nππππππππππ**",
            "ππππππππππ",
            "πππππππππ",
            "ππππππππ",
            "πππππππ",
            "ππππππ",
            "πππππ",
            "ππππ",
            "πππ",
            "ππ",
            "π",
            "**rApEd**",
        ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)

# created by @greyyvbss
