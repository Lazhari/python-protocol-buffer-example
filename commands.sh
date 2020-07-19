protoc -I=simple/ --python_out=simple/ simple/simple.proto
protoc -I=enum/ --python_out=enum/ enum/enum.proto
protoc -I=complex/ --python_out=complex/ complex/complex.proto
