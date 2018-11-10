GATEWAY_FLAGS := -I. -I/usr/local/include -I$(GOPATH)/src -I$(GOPATH)/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis -I/usr/local/include

GRPC_FLAGS := --python_out=./endpoint/libs --grpc_python_out=./endpoint/libs

## setup
deps:
	go get -u google.golang.org/grpc
	go get -u github.com/grpc-ecosystem/grpc-gateway/protoc-gen-grpc-gateway
	go get -u github.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger
	go get -u github.com/golang/protobuf/protoc-gen-go

gitssl:
	git config --global http.sslVerify true

## build
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
	python ./endpoint/server/grpc_server.py