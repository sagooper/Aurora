import src.permission as perm
Helper = {
    '!sleave':{'Help':'!sleave', 'Description':'And the bot left the server', 'Type':'Admin'},
    '!fuckoff':{'Help':'!fuckoff', 'Description':'Yeah. The Bot is out!', 'Type':'Admin'}
}
async def sleave(client, message, *argument):
    if await perm.have_permission(message.author) == 2:
        await client.leave_server(message.server)
    else:
        await client.send_message(message.channel, 'This command is only available for ' + str(perm.Admin_Name) + 's')


async def fuckoff(client, message, arg):
    await _sleave(client, message, arg)
