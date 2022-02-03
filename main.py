# import random
# import discord_bot

# discord_bot.run()

import hikari
import hidden
import opensimplex
import random
import map_maker


def run():
    bot = hikari.GatewayBot(token=hidden.token)

    @bot.listen()
    async def ping(event: hikari.GuildMessageCreateEvent) -> None:
        # If a non-bot user sends a message "hk.ping", respond with "Pong!"
        # We check there is actually content first, if no message content exists,
        # we would get `None' here.

        w, h = 12, 12
        matrix = [[0 for x in range(w)] for y in range(h)]

        if event.is_bot or not event.content:
            return

        if event.content.startswith("!genOpen"):
            opensimplex.seed(random.randint(0, 2000))
            s = ""
            for i in range(w):
                for i1 in range(h):
                    v = opensimplex.noise2(i, i1) * 10
                    if v < 0:
                        v = v * -1

                    if v > 10:
                        v = v / 10
                        v = int(v)

                    v = v + 1
                    matrix[i][i1] = int(v)

                    s = s + str(matrix[i][i1])

                # await event.message.respond(s)
                s = ""

            # await event.message.respond("Done!")
            await event.message.respond(map_maker.arr_to_map(matrix, w, h))

        elif event.content.startswith("!genRand"):
            s = ""
            for i in range(w):
                for i1 in range(h):
                    matrix[i][i1] = random.randint(1, 5)
                    s = s + str(matrix[i][i1])

                # await event.message.respond(s)
                s = ""

            # await event.message.respond("Done!")
            await event.message.respond(map_maker.arr_to_map(matrix, w, h))

        elif event.content.startswith("!imgTest"):
            await event.message.respond("🟩🟦🟨⬜⬛⁉")

    bot.run()


run()
