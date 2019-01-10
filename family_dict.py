# Instructions
# Define a dictionary that contains information about several members of your family. Use the following example as a template.

# my_family = {
#     'sister': {
#         'name': 'Krista',
#         'age': 42
#     },
#     'mother': {
#         'name': 'Cathie',
#         'age': 70
#     }
# }
# Using a dictionary comprehension, produce output that looks like the following example.

# Krista is my sister and is 42 years old
# Helpful hint: To convert an integer into a string in Python, it's str(integer_value)

my_family = {
    'brother': {
        'name': 'Peter',
        'age': 40
    },
    'brother': {
        'name': 'Nathan',
        'age': 37
    },
    'sister': {
        'name': 'Emily',
        'age': 35
    },
    'mother': {
        'name': 'Julie',
        'age': 64
    },
    'father' :{
        'name': 'Andy',
        'age': 66
    }
}


list_my_family = {f'My {relation}, {relation_vals["name"]} is {str(relation_vals["age"])} years old.' for relation, relation_vals in my_family.items()}

print(list_my_family)