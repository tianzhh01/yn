from cele import app
from datetime import datetime


@app.task
def math_add(x, y):
    return 10 * x + y


if __name__ == '__main__':
    # t = datetime(2020, 9, 15, 14, 58, 58)
    # math_add.apply_async(args=(1, 8), eta=t)
    # print(t)
    r = math_add.delay(3, 5)
    print(r.get())
