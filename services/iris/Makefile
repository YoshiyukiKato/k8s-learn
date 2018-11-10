GATEWAY_FLAGS := -I. -I/usr/local/include -I$(GOPATH)/src -I$(GOPATH)/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis -I/usr/local/include

GRPC_FLAGS := --python_out=./endpoint --grpc_python_out=./endpoint

## setup
deps:
	go get -u google.golang.org/grpc
	go get -u github.com/grpc-ecosystem/grpc-gateway/protoc-gen-grpc-gateway
	go get -u github.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger
	go get -u github.com/golang/protobuf/protoc-gen-go

gitssl:
	git config --global http.sslVerify true

## build app
ep:
	python -m grpc_tools.protoc $(GRPC_FLAGS) $(GATEWAY_FLAGS) protos/*.proto

gw:
	protoc $(GATEWAY_FLAGS) \
		--go_out=plugins=grpc:./gateway \
		--grpc-gateway_out=logtostderr=true:./gateway \
		--swagger_out=logtostderr=true:./docs \
		protos/*.proto

## run
rungw:
	go run ./gateway/main.go
runep:
	cd endpoint && python ./grpc_server.py

## build docker images
images:
	docker build -t iris/endpoint:0.0.1 -f ./dockerfiles/endpoint.dockerfile .
	docker build -t iris/gateway:0.0.1 -f ./dockerfiles/gateway.dockerfile .

## helm
up:
	helm upgrade --install --namespace iris iris ./k8s/iris
down:
	helm delete --purge iris
