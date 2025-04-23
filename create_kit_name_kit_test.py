# Creación de un kit:
#   Success_response = code: 201
#   Negative_response_missing_parameters = code: 400, message: "No se han aprobado todos los parámetros requeridos"
#   Negative_response_bad_name = code:400, message: "El nombre debe contener sólo letras latino, un espacio y un guión. De 2 a 15 caracteres"

import sender_stand_request
import data

#PART 1: POST NEW USER

def post_new_user():

    user_response = sender_stand_request.post_new_user()

    #Verify new user response
    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""

    return user_response.json()["authToken"]

#PART 2: POST NEW KIT

def get_kit_header():

    current_header = data.kit_header.copy()
    current_header["Authorization"] = post_new_user()

    return current_header

def get_kit_body(kit_name):

    current_body = data.kit_body.copy()
    current_body["name"] = kit_name

    return current_body

def positive_assert(kit_name):

    # Get_kit_header
    kit_header = get_kit_header()

    # Get_kit_body
    kit_body = get_kit_body(kit_name)

    #Post kit
    kit_response = sender_stand_request.post_new_client_kit(kit_body, kit_header)

    #Show kit response
    print(f'\nDatos del kit: {kit_body}')
    print(f'\tStatus_code = {kit_response.status_code}')
    print(f'\tjson = {kit_response.json()}')

    #Verify kit response
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

    print('\nTEST_APPROVED')

def negative_assert_bad_name(kit_name):

    # Get_kit_header
    kit_header = get_kit_header()

    # Get_kit_body
    kit_body = get_kit_body(kit_name)

    # Post kit
    kit_response = sender_stand_request.post_new_client_kit(kit_body, kit_header)

    # Show kit response
    print(f'\nDatos del kit: {kit_body}')
    print(f'\tStatus_code = {kit_response.status_code}')
    print(f'\tjson = {kit_response.json()}')

    # Verify kit response
    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400
    assert kit_response.json()["message"] == "El nombre debe contener sólo letras latino, un espacio y un guión. De 2 a 15 caracteres"

    print('\nTEST_APPROVED')

def negative_assert_missing_parameters(current_body):

    # Get_kit_header
    kit_header = get_kit_header()

    # Post kit
    kit_response = sender_stand_request.post_new_client_kit(current_body, kit_header)

    # Show kit response
    print(f'\nDatos del kit: {current_body}')
    print(f'\tStatus_code = {kit_response.status_code}')
    print(f'\tjson = {kit_response.json()}')

    # Verify kit response
    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400
    assert kit_response.json()["message"] == "No se han aprobado todos los parámetros requeridos"

    print('\nTEST_APPROVED')

#PART 3: TESTS

def test_1_create_kit_1_letter_in_name_get_success_response():
    print('\n\tPRUEBA 1: El número permitido de caracteres (1)')
    positive_assert(data.one_letter)

def test_2_create_kit_511_letter_in_name_get_success_response():
    print('\n\tPRUEBA 2: El número permitido de caracteres (511)')
    positive_assert(data.letter_511)

def test_3_create_kit_0_letter_in_name_get_error_response():
    print('\n\tPRUEBA 3: El número de caracteres es menor que la cantidad permitida (0)')
    negative_assert_bad_name(data.zero_letter)

def test_4_create_kit_512_letter_in_name_get_error_response():
    print('\n\tPRUEBA 4: El número de caracteres es mayor que la cantidad permitida (512) ')
    negative_assert_bad_name(data.letter_512)

def test_5_create_kit_has_special_symbol_in_name_get_error_response():
    print('\n\tPRUEBA 5: Se permiten caracteres especiales ("№%@",)')
    positive_assert(data.special_symbol)

def test_6_create_kit_has_space_in_name_get_error_response():
    print('\n\tPRUEBA 6: Se permiten espacios (A Aaa)')
    positive_assert(data.space)

def test_7_create_kit_has_number_in_name_get_error_response():
    print('\n\tPRUEBA 7: Se permiten números (123)')
    positive_assert(data.number)

def test_8_create_kit_no_first_name_get_error_response():
    print('\n\tPRUEBA 8: El parámetro no se pasa en la solicitud')
    # Get_kit_body
    current_body = data.kit_body.copy()
    current_body.pop("name")
    negative_assert_missing_parameters(current_body)

def test_9_create_kit_number_type_first_name_get_error_response():
    print('\n\tPRUEBA 9: Se ha pasado un tipo de parámetro diferente (número)')
    # Get_kit_body
    current_body = data.kit_body.copy()
    current_body["name"] = data.number_type
    negative_assert_missing_parameters(current_body)