// Code generated by protoc-gen-grpc-gateway. DO NOT EDIT.
// source: protos/iris.proto

/*
Package protos is a reverse proxy.

It translates gRPC into RESTful JSON APIs.
*/
package protos

import (
	"io"
	"net/http"

	"github.com/golang/protobuf/proto"
	"github.com/grpc-ecosystem/grpc-gateway/runtime"
	"github.com/grpc-ecosystem/grpc-gateway/utilities"
	"golang.org/x/net/context"
	"google.golang.org/grpc"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/grpclog"
	"google.golang.org/grpc/status"
)

var _ codes.Code
var _ io.Reader
var _ status.Status
var _ = runtime.String
var _ = utilities.NewDoubleArray

func request_Iris_Predict_0(ctx context.Context, marshaler runtime.Marshaler, client IrisClient, req *http.Request, pathParams map[string]string) (proto.Message, runtime.ServerMetadata, error) {
	var protoReq IrisRequest
	var metadata runtime.ServerMetadata

	if err := marshaler.NewDecoder(req.Body).Decode(&protoReq); err != nil && err != io.EOF {
		return nil, metadata, status.Errorf(codes.InvalidArgument, "%v", err)
	}

	msg, err := client.Predict(ctx, &protoReq, grpc.Header(&metadata.HeaderMD), grpc.Trailer(&metadata.TrailerMD))
	return msg, metadata, err

}

// RegisterIrisHandlerFromEndpoint is same as RegisterIrisHandler but
// automatically dials to "endpoint" and closes the connection when "ctx" gets done.
func RegisterIrisHandlerFromEndpoint(ctx context.Context, mux *runtime.ServeMux, endpoint string, opts []grpc.DialOption) (err error) {
	conn, err := grpc.Dial(endpoint, opts...)
	if err != nil {
		return err
	}
	defer func() {
		if err != nil {
			if cerr := conn.Close(); cerr != nil {
				grpclog.Infof("Failed to close conn to %s: %v", endpoint, cerr)
			}
			return
		}
		go func() {
			<-ctx.Done()
			if cerr := conn.Close(); cerr != nil {
				grpclog.Infof("Failed to close conn to %s: %v", endpoint, cerr)
			}
		}()
	}()

	return RegisterIrisHandler(ctx, mux, conn)
}

// RegisterIrisHandler registers the http handlers for service Iris to "mux".
// The handlers forward requests to the grpc endpoint over "conn".
func RegisterIrisHandler(ctx context.Context, mux *runtime.ServeMux, conn *grpc.ClientConn) error {
	return RegisterIrisHandlerClient(ctx, mux, NewIrisClient(conn))
}

// RegisterIrisHandlerClient registers the http handlers for service Iris
// to "mux". The handlers forward requests to the grpc endpoint over the given implementation of "IrisClient".
// Note: the gRPC framework executes interceptors within the gRPC handler. If the passed in "IrisClient"
// doesn't go through the normal gRPC flow (creating a gRPC client etc.) then it will be up to the passed in
// "IrisClient" to call the correct interceptors.
func RegisterIrisHandlerClient(ctx context.Context, mux *runtime.ServeMux, client IrisClient) error {

	mux.Handle("POST", pattern_Iris_Predict_0, func(w http.ResponseWriter, req *http.Request, pathParams map[string]string) {
		ctx, cancel := context.WithCancel(req.Context())
		defer cancel()
		if cn, ok := w.(http.CloseNotifier); ok {
			go func(done <-chan struct{}, closed <-chan bool) {
				select {
				case <-done:
				case <-closed:
					cancel()
				}
			}(ctx.Done(), cn.CloseNotify())
		}
		inboundMarshaler, outboundMarshaler := runtime.MarshalerForRequest(mux, req)
		rctx, err := runtime.AnnotateContext(ctx, mux, req)
		if err != nil {
			runtime.HTTPError(ctx, mux, outboundMarshaler, w, req, err)
			return
		}
		resp, md, err := request_Iris_Predict_0(rctx, inboundMarshaler, client, req, pathParams)
		ctx = runtime.NewServerMetadataContext(ctx, md)
		if err != nil {
			runtime.HTTPError(ctx, mux, outboundMarshaler, w, req, err)
			return
		}

		forward_Iris_Predict_0(ctx, mux, outboundMarshaler, w, req, resp, mux.GetForwardResponseOptions()...)

	})

	return nil
}

var (
	pattern_Iris_Predict_0 = runtime.MustPattern(runtime.NewPattern(1, []int{2, 0}, []string{"iris"}, ""))
)

var (
	forward_Iris_Predict_0 = runtime.ForwardResponseMessage
)
