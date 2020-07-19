import complex.complex_pb2 as complex_pb2

complex_message = complex_pb2.ComplexMessage()

# one_dummy_message = complex_pb2.DummyMessage()
#
# one_dummy_message.id = 124;
# one_dummy_message.name = "First dummy message"
# complex_message.one_dummy = one_dummy_message

complex_message.one_dummy.id = 123
complex_message.one_dummy.name = "first dummy message"

first_multiple_dummy = complex_message.multiple_dummy.add()
first_multiple_dummy.id = 234
first_multiple_dummy.name = "I am the first dummy message on the array"
# it's better
complex_message.multiple_dummy.add(id=1394934, name="Second element in the array")
# Be careful this does copy
third_dummy_message = complex_pb2.DummyMessage()
third_dummy_message.id = 12
third_dummy_message.name = "Third dummy message"

complex_message.multiple_dummy.extend([third_dummy_message])
print(complex_message)

# Protocol buffer generated buffer

