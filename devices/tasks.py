from bigbrother.celery import app

@app.task
def set_light_brightness():
    pass

@app.task
def send_rc_signal():
    pass


#body = json.loads(request.body.decode('utf-8'))