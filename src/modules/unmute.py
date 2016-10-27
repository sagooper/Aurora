import src.permission as perm

async def unmute(client, message, arg):
    if await perm.have_access(message.author) == perm.Roles.Admin.Level:
        string = arg.split(' ')

        # Get the members ID
        member_id = string[0]
        member_id = member_id.replace('<', '')
        member_id = member_id.replace('@', '')
        member_id = member_id.replace('>', '')

        # Find the mute role
        for server in client.servers:
            # print(server)
            for roles in server.roles:
                # print(roles.name)
                if roles.name == 'Muted':
                    role = roles

                    # Find the member using the ID
                    members = client.get_all_members()
                    for member in members:
                        if member.id == member_id:
                            # Mute the member
                            await client.remove_roles(member, role)
                            break
    else:
        await client.send_message(message.channel, 'This command is only available for ' + perm.Roles.Admin.Name + 's')