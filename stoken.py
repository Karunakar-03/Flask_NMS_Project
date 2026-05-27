from itsdangerous import URLSafeTimedSerializer
secret_key='karunakarv'
def endata(data):
    serializer=URLSafeTimedSerializer(secret_key)
    return serializer.dumps(data,salt='uppu')
def dndata(data):
    serializer=URLSafeTimedSerializer(secret_key)
    return serializer.loads(data,salt='uppu')

