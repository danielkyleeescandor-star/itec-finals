
from string import Template

message = Template("Hello, $name! Welcome to $school.")

student = message.substitute(
    name="Daniel",
    school="LSPU"
)

print(student)
