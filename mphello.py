import morepath

app = morepath.App(name='Hello')

@app.path(path='')
class Root(object):
    pass

@app.view(model=Root)
def hello_world(self, request):
    return "Hello world!"

if __name__ == '__main__':
    config = morepath.setup()
    config.scan()
    config.commit()
    morepath.run(app)
