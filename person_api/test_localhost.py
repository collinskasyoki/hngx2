import requests

base_url = 'http://localhost:8000/api/' # Update this as necessary if running in a public facing server

# Function to print response content
def print_response(response):
    print(f'Status Code: {response.status_code}')
    print('Response Content:')
    print(response.text)
    print('\n')

def create_person_record(person_name):
    data = {'name': person_name}
    response = requests.post(base_url, json=data)
    print(f'Creating a person record with name: {person_name}')
    print_response(response)

def get_all_person_records():
    response = requests.get(base_url)
    print('Getting all person records')
    print_response(response)

def get_person_record_by_name(person_name):
    response = requests.get(f'{base_url}{person_name}/')
    print(f'Getting a person record by name: {person_name}')
    print_response(response)

def update_person_record_name(old_name, new_name):
    data = {'name': new_name}
    response = requests.put(f'{base_url}{old_name}/', json=data)
    print(f'Updating a person record with name: {old_name} to {new_name}')
    print_response(response)

def delete_person_record_by_name(person_name):
    response = requests.delete(f'{base_url}{person_name}/')
    print(f'Deleting a person record by name: {person_name}')
    print_response(response)

# Test the CRUD operations
if __name__ == '__main__':
    # Deleting test names if they already exist
    requests.delete(f'{base_url}John/')
    requests.delete(f'{base_url}Alice/')

    create_person_record('John')
    create_person_record('Alice')
    get_all_person_records()
    get_person_record_by_name('John')
    update_person_record_name('John', 'John Doe')
    get_person_record_by_name('John Doe')
    delete_person_record_by_name('John Doe')
    delete_person_record_by_name('Alice')
    get_all_person_records()

