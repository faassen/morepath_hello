import morepath

app = morepath.App()

@app.root()
class Root(object):
    pass

@app.view(model=Root)
def hello_world(request, model):
    return "Hello world!"

if __name__ == '__main__':
    config = morepath.setup()
    config.scan()
    config.commit()
    app.run()
