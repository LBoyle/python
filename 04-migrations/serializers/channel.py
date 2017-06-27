from app import BASE_URL

def channelSerializer(c):
    return {'id': c.id, 'name': c.name, 'link': BASE_URL+'/channels/'+str(c.id), 'subscribers': [{'id': u.id, 'name': u.name, 'link': BASE_URL+'/users/'+str(u.id)} for u in c.subscribers]}
