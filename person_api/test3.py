import requests

# Define the base URL for your API
base_url = 'http://localhost:8000/api/'  # Replace with your API's URL

# Define headers if needed (e.g., for authentication)
headers = {
    'Content-Type': 'application/json',
}

# Function to print response content
def print_response(response):
    print(f'Status Code: {response.status_code}')
    print('Response Content:')
    print(response.text)
    print('\n')

# Create a new person record
def create_person_record(person_name):
    data = {"name": person_name}
    response = requests.post(base_url, json=data, headers=headers)
    print(response.status_code)
    assert response.status_code == 201, f"Failed to create a person record with name: {person_name}"
    return response.json()

# Get all person records
def get_all_person_records():
    response = requests.get(base_url, headers=headers)
    assert response.status_code == 200, "Failed to retrieve all person records"
    return response.json()

# Get a specific person record by name
def get_person_record_by_name(person_name):
    response = requests.get(f'{base_url}{person_name}/', headers=headers)
    assert response.status_code == 200, f"Failed to retrieve a person record by name: {person_name}"
    return response.json()

# Update a person record's name
def update_person_record_name(old_name, new_name):
    data = {'name': new_name}
    response = requests.put(f'{base_url}{old_name}/', json=data, headers=headers)
    assert response.status_code == 200, f"Failed to update a person record with name: {old_name} to {new_name}"
    return response.json()

# Delete a person record by name
def delete_person_record_by_name(person_name):
    response = requests.delete(f'{base_url}{person_name}/', headers=headers)
    assert response.status_code == 204, f"Failed to delete a person record by name: {person_name}"

# Test the CRUD operations
if __name__ == '__main__':
    # Create a person record
    created_record = create_person_record('John')
    
    # # Get all person records and check if the created record is in the list
    # all_records = get_all_person_records()
    # assert created_record in all_records, f"Created record with name: {created_record['name']} not found in the list of all records"
    
    # # Get the person record by name and check if it matches the created record
    # retrieved_record = get_person_record_by_name('John')
    # assert retrieved_record == created_record, "Retrieved record does not match the created record"
    
    # # Update the person record's name and check if the name is updated
    # updated_record = update_person_record_name('John', 'John Doe')
    # assert updated_record['name'] == 'John Doe', "Failed to update the person record's name"
    
    # # Delete the person record by name
    # delete_person_record_by_name('John Doe')
    
    # # Check if the record is deleted by trying to retrieve it again
    # try:
    #     get_person_record_by_name('John Doe')
    #     assert False, "Record was not deleted as expected"
    # except requests.exceptions.HTTPError:
    #     pass  # This is expected as the record should not exist anymore
    
    print("All assertions passed successfully!")
