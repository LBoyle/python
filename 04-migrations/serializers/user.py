from app import BASE_URL

def userSerializer(u):
    return {'id': u.id,'name': u.name, 'link': BASE_URL+'/users/'+str(u.id), 'subscriptions': [{'id': c.id, 'name': c.name, 'link': BASE_URL+'/channels/'+str(c.id)} for c in u.subscriptions]}
