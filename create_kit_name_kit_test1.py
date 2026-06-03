import sender_stand_request
import data

# 1. Definimos las funciones de ayuda PRIMERO
def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = name
    return current_kit_body

def get_new_user_token():
    user_response = sender_stand_request.post_new_user(data.user_body)
    return user_response.json()["authToken"]

# 2. Luego las pruebas
def test_create_kit_1_char_in_name():
    kit_body = get_kit_body("a")
    kit_response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert kit_response.status_code == 201

def test_create_kit_511_chars_in_name():
    kit_body = get_kit_body("a" * 511)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert kit_response.status_code == 201

def test_create_kit_0_chars_in_name():
    kit_body = get_kit_body("")
    kit_response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert kit_response.status_code == 400

def test_create_kit_512_chars_in_name():
    kit_body = get_kit_body("a" * 512)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert kit_response.status_code == 400

def test_create_kit_special_chars_in_name():
    kit_body = get_kit_body("№%@")
    kit_response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert kit_response.status_code == 201

def test_create_kit_spaces_in_name():
    kit_body = get_kit_body(" A Aaa ")
    kit_response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert kit_response.status_code == 201

def test_create_kit_numbers_in_name():
    kit_body = get_kit_body("123")
    kit_response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert kit_response.status_code == 201

def test_create_kit_no_name_param():
    kit_response = sender_stand_request.post_new_client_kit({}, get_new_user_token())
    assert kit_response.status_code == 400

def test_create_kit_number_type_in_name():
    kit_body = get_kit_body(123)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert kit_response.status_code == 400