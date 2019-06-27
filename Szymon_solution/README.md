# Idea

My idea is to create pod with two containers.
One container writes variables to files and other one reads these variables and serves it as http server.

Containers share one volume where the variables are located.

### Vars:
magic - random word changed every 2 seconds
time - time float read with time.time() [updated every 2 seconds]
const - constant value {'devop_sig_no': 8}

# Running demo
In order to run this demo use:
```bash
kubectl apply -f pod-app.yml
```

Afterwards forward port:
```bash
kubectl port-forward myapp 8080:8080
```

With complete setup use curl or web browser to reach addresses:
```
127.0.0.1:8080/magic
127.0.0.1:8080/const
127.0.0.1:8080/time
```

# Containers
Pod requires two container images
Both are pushed to docker hub.
However, if you want to build them manually then:
Dockerfile is the main container with https server and listener for variables.
put.dockerfile is container for writing new variables every 2 seconds.

# Extra
`cluster.yml` file is config file to build 1 master 1 worker cluster with KIND.
Run `kind create cluster --config cluster.yml` to get my cluster setup.

