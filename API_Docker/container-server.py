from flask import Flask, Response, request, jsonify
import os

app = Flask(__name__)


@app.route("/")
def index():
    return """
Available API endpoints:

GET /containers                     List all containers
GET /containers?state=running      List running containers (only)
GET /containers/<id>                Inspect a specific container
GET /containers/<id>/logs           Dump specific container logs
GET /images                         List all images

POST /images                        Create a new image
POST /containers                    Create a new container

DELETE /containers/<id>             Delete a specific container
DELETE /images/<id>                 Delete a specific image
DELETE /containers                  Delete all containers (including running)
DELETE /images                      Delete all images

PATCH /containers/<id>              Change a container's state
PATCH /images/<id>                  Change a specific image's attributes

"""
#GET METHODS
@app.route('/containers', methods=['GET'])
def containers_index():

    s = os.popen('docker ps -a').read()

    resp = '' + s

    return Response(response=resp, mimetype="application/json")

@app.route('/containers?state=running', methods=['GET'])
def containers_running():

    s = os.popen('docker ps').read()
    resp = '' + s
    return Response(response=resp, mimetype="application/json")


@app.route('/containers/<id>', methods=['GET'])
def containers_show(id):
    """
    Inspect specific container

    """
    dockerCMD = 'docker inspect ' + id
    s = os.popen(dockerCMD).read()
    resp = '' + s

    return Response(response=resp, mimetype="application/json")



@app.route('/containers/<id>/logs', methods=['GET'])
def containers_log(id):
    """
    Dump specific container logs

    """
    dockerCMD = 'docker logs ' + id
    s = os.popen(dockerCMD).read()
    resp = '' + s
    return Response(response=resp, mimetype="application/json")




@app.route('/images', methods=['GET'])
def images_index():
    s = os.popen('docker images').read()
    resp = '' + s
    return Response(response=resp, mimetype="application/json")

#################################################################
# POST METHODS

@app.route('/images', methods=['POST'])
def image_create():
    """
    Create container (from existing image using id or name)

    """
    body = request.get_json(force=True)
    image = body['image']

    print(image)

    if (image == 'whalesay'):
        dockerBuild = 'docker build -t ' + image + ' ./dockerfiles/whalesay/. '
    elif (image == 'ssh'):
        dockerBuild = 'docker build -t ' + image + ' ./dockerfiles/ssh/. '
    else:
        dockerBuild = 'docker build -t ' + image + ' ./dockerfiles/'+image+'/. '



    s = os.popen(dockerBuild).read()
    print(s)
    resp = '' + s


    return Response(resp, mimetype="application/json")


@app.route('/containers', methods=['POST'])
def container_create():
    """
    Create image (from uploaded Dockerfile)

    """

    body = request.get_json(force=True)
    image = body['image']
    name = body['name']

    dockercmd = 'docker images -q ' + image
    #gets the id of the image
    id = os.popen(dockercmd).read()
    print(id)

    dockerContainer = 'docker run --name ' + name + ' ' + id
    s = os.popen(dockerContainer).read()
    print(s)
    resp = '' + s

    return Response(response=resp, mimetype="application/json")


###########################DELETE#######################

@app.route('/images/<id>', methods=['DELETE'])
def images_remove(id):
    """
    Delete a specific image
    """
    dockerCMD = 'docker rmi ' + id
    s = os.popen(dockerCMD).read()

    resp = '' + s
    return Response(response=resp, mimetype="application/json")

@app.route('/containers/<id>', methods=['DELETE'])
def containers_remove(id):
    """
    Delete a specific container - must be already stopped/killed

    """
    dockerCMD = 'docker rm ' + id
    s = os.popen(dockerCMD).read()
    resp = '' + s
    return Response(response=resp, mimetype="application/json")

@app.route('/containers', methods=['DELETE'])
def containers_remove_all():
    """
    Force remove all containers - dangrous!

    """
    dockerCMD1 = 'docker kill $(docker ps -q) '
    s = os.popen(dockerCMD1).read()

    print('stoped all containers...')
    dockerCMD2 = 'docker rm $(docker ps -a -q) '
    s = os.popen(dockerCMD2).read()
    print('deleting all containers...')
    resp = '' + s
    return Response(response=resp, mimetype="application/json")

@app.route('/images', methods=['DELETE'])
def images_remove_all():
    """
    Force remove all images - dangrous!

    """
    dockerCMD1 = 'docker rmi $(docker images -q) '
    s = os.popen(dockerCMD1).read()
    print('deleting all images...')
 
    resp = ''
    return Response(response=resp, mimetype="application/json")



#######################PATCH#########################

@app.route('/containers/<id>', methods=['PATCH'])
def containers_update(id):
    """
    Update container attributes (support: state=running|stopped)

    curl -X PATCH -H 'Content-Type: application/json' http://localhost:8080/containers/b6cd8ea512c8 -d '{"state": "running"}'
    curl -X PATCH -H 'Content-Type: application/json' http://localhost:8080/containers/b6cd8ea512c8 -d '{"state": "stopped"}'

    """
    body = request.get_json(force=True)
    try:
        state = body['state']
        if state == 'running':
           # docker('restart', id)
            pass
    except:
        pass

    resp = '{"id": "%s"}' % id
    return Response(response=resp, mimetype="application/json")

@app.route('/images/<id>', methods=['PATCH'])
def images_update(id):
    """
    Update image attributes (support: name[:tag])  tag name should be lowercase only

    curl -s -X PATCH -H 'Content-Type: application/json' http://localhost:8080/images/7f2619ed1768 -d '{"tag": "test:1.0"}'

    """
    resp = ''
    return Response(response=resp, mimetype="application/json")


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080, debug=True)
