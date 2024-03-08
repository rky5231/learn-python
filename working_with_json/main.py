book = {}
book['tom'] = {
    'name': 'tom',
    'address': '1 read street, NY',
    'phone': 1234567890
}
book['bob'] = {
    'name': 'bob',
    'address': '1 green street, NY',
    'phone': '0987654321'
}

import json
s = json.dumps(book)
with open("book.txt", 'w') as file:
    file.write(s)