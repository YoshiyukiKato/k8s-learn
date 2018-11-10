# ragoon
データ活用APIの基盤を作るぞい

## setup local
```sh
$ brew install hyperkit
$ brew install docker-machine-driver-hyperkit
$ brew cask install minikube
$ brew install helm-kubernetes
$ minikube start --memory=8192 --cpus=4 --vm-driver=hyperkit --kubernetes-version=v1.12.0
```

### install istio via helm
```sh
# download
$ cd ~
$ curl -L https://git.io/getLatestIstio | sh -
$ cd istio-1.0.3
$ echo "export PATH=$PWD/bin:\$PATH" >> ~/.bash_profile
# install to minikube
$ kubectl apply -f install/kubernetes/helm/helm-service-account.yaml
$ helm init --service-account tiller
$ helm install install/kubernetes/helm/istio --name istio --namespace istio-system # this will take a while...
```

### use docker on minikube vm
```sh
# use docker on minikube vm
$ eval $(minikube docker-env)
```

## usage (iris)
### build image
```sh
$ cd ./services/iris
$ source .env
$ docker build -t $IMAGE:$TAG ./
```

### deploy to k8s
```sh
# build config
$ kustomize build ./k8s/src/overlays/$STAGE > ./k8s/dist/$STAGE.yaml
# create|update|delete
$ kubectl {create|apply|delete} -f ./k8s/dist/$STAGE.yaml
```

### open url
```sh
$ open $(minikube ip)/iris
```

## trying protobuf and gRPC
お試し中。Request/Responseのスキーマ宣言としてprotobuf。ルータと各サービス間の通信をgRPCでやる
あんまり性能差が出ないならflaskで全然いいと思ってるけど、Request/Responseのスキーマ宣言は欲しいので悩みどころ

### setup local
```sh
$ pip install grpcio-tools googleapis-common-protos
```

### compile protobuf
```sh
$ cd ./services/iris
$ python -m grpc_tools.protoc -I protos --python_out=app/libs/grpc --grpc_python_out=app/libs/grpc protos/*.proto
```

### run gRPC server/client
```sh
$ python app/grpc/iris_server.py
```

```sh
$ python app/grpc/iris_client.py
```
