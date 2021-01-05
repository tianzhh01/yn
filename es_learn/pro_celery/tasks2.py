from cele import app


@app.task
def multi(x, y):
    return x + y
