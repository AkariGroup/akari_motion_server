from grpc.tools import protoc

pyPath = "../lib/grpc"

protoc.main(
    (
        "",
        "-I.",
        "--python_out=../lib/grpc",
        "--grpc_python_out=../lib/grpc",
        "motion_server.proto",
    )
)
