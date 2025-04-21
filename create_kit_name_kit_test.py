# Creación de usuario:
#   Success_response = code: 201
#   Negative_response_bad_data_1 = code:400, message: "No se han aprobado todos los parámetros requeridos. Parámetros requeridos: nombre, teléfono, dirección"
#   Negative_response_bad_name = code:400, message: "Has introducido un nombre de usuario no válido. El nombre solo puede contener letras latinas, la longitud debe ser de 2 a 15 caracteres."
#   Negative_response_bad_phone = code:400, message: "Has introducido un número de teléfono de usuario no válido. El número de teléfono solo puede contener números y un signo +"
#   Negative_response_bad_address = code:400, message: "Has introducido una dirección no válida. La dirección solo puede contener caracteres del alfabeto latino y signos de puntuación, la longitud de la dirección debe tener de 5 a 50 caracteres"
# Creación de un kit:
#   Success_response = code: 201
#   Negative_response_missing_parameters = code: 400, message: "No se han aprobado todos los parámetros requeridos"
#   Negative_response_bad_name = code:400, message: "El nombre debe contener sólo letras latino, un espacio y un guión. De 2 a 15 caracteres"

import sender_stand_request
import data

#PART 1: POST NEW USER

def post_new_user():

    user_body = data.user_body.copy()
    user_response = sender_stand_request.post_new_user()

    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""

    print(f'\nDatos del usuario enviados: {user_body}')
    print(f'\tPost new user: Status_code = {user_response.status_code}')
    print(f'\tPost new user: json = {user_response.json()}')

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

    #Verify kit response
    #assert kit_response.status_code == 201
    #assert kit_response.json()["name"] != ""

    #Show kit response
    print(f'\nDatos del kit enviado: {kit_body}')
    print(f'\tPost new kit: Status_code = {kit_response.status_code}')
    print(f'\tPost new kit: json = {kit_response.json()}')

    if kit_response.status_code == 201:
        print('\nTEST_APPROVED')
    else:
        print('\nTEST_FAILED')
        print('\tCode_expected: 201')

def negative_assert_bad_name(kit_name):

    # Get_kit_header
    kit_header = get_kit_header()

    # Get_kit_body
    kit_body = get_kit_body(kit_name)

    # Post kit
    kit_response = sender_stand_request.post_new_client_kit(kit_body, kit_header)

    # Verify kit response
    #assert kit_response.status_code == 400
    #assert kit_response.json()["code"] == 400
    #assert kit_response.json()["message"] == "El nombre debe contener sólo letras latino, un espacio y un guión. De 2 a 15 caracteres"

    # Show kit response
    print(f'\nDatos del kit enviado: {kit_body}')
    print(f'\tPost new kit: Status_code = {kit_response.status_code}')
    print(f'\tPost new kit: json = {kit_response.json()}')

    if (kit_response.status_code == 400
            and kit_response.json()["code"] == 400
            and kit_response.json()["message"] == "El nombre debe contener sólo letras latino, un espacio y un guión. De 2 a 15 caracteres"):
        print('\nTEST_APPROVED')
    else:
        print('\nTEST_FAILED')
        print('\tCode_expected: 400 \n\tMessage_expected: "El nombre debe contener sólo letras latino, un espacio y un guión. De 2 a 15 caracteres"')

def negative_assert_missing_parameters(current_body):

    # Get_kit_header
    kit_header = get_kit_header()

    # Post kit
    kit_response = sender_stand_request.post_new_client_kit(current_body, kit_header)

    # Verify kit response
    #assert kit_response.status_code == 400
    #assert kit_response.json()["code"] == 400
    #assert kit_response.json()["message"] == "No se han aprobado todos los parámetros requeridos"

    # Show kit response
    print(f'\nDatos del kit enviado: {current_body}')
    print(f'\tPost new kit: Status_code = {kit_response.status_code}')
    print(f'\tPost new kit: json = {kit_response.json()}')

    if (kit_response.status_code == 400
            and kit_response.json()["code"] == 400
            and kit_response.json()["message"] == "No se han aprobado todos los parámetros requeridos"):
        print('\nTEST_APPROVED')
    else:
        print('\nTEST_FAILED')
        print('\tCode_expected: 400 \n\tMessage_expected: "No se han aprobado todos los parámetros requeridos"')

#PART 3: TESTS

def test_1_create_kit_1_letter_in_name_get_success_response():
    print('\n\tPRUEBA 1: El número permitido de caracteres (1):')
    positive_assert("a")

def test_2_create_kit_511_letter_in_name_get_success_response():
    print('\n\tPRUEBA 2: El número permitido de caracteres (511):')
    positive_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcd"
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                    "abcdabcdabcdabcdabcdabcdabcdabcdabC")

def test_3_create_kit_0_letter_in_name_get_error_response():
    print('\n\tPRUEBA 3: El número de caracteres es menor que la cantidad permitida (0):')
    negative_assert_bad_name("")

def test_4_create_kit_512_letter_in_name_get_error_response():
    print('\n\tPRUEBA 4: El número de caracteres es mayor que la cantidad permitida (512): ')
    negative_assert_bad_name("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                             "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                             "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                             "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                             "abcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                             "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                             "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                             "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                             "abcdabcdabcdabcdabcdabcdabcdabcD")

def test_5_create_kit_has_special_symbol_in_name_get_error_response():
    print('\n\tPRUEBA 5: Se permiten caracteres especiales ("№%@",):')
    positive_assert("\"№%@\",")

def test_6_create_kit_has_space_in_name_get_error_response():
    print('\n\tPRUEBA 6: Se permiten espacios (A Aaa):')
    positive_assert("A Aaa")

def test_7_create_kit_has_number_in_name_get_error_response():
    print('\n\tPRUEBA 7: Se permiten números (123):')
    positive_assert("123")

def test_8_create_kit_no_first_name_get_error_response():
    print('\n\tPRUEBA 8: El parámetro no se pasa en la solicitud:')
    # Get_kit_body
    current_body = data.kit_body.copy()
    current_body.pop("name")
    negative_assert_missing_parameters(current_body)

def test_9_create_kit_number_type_first_name_get_error_response():
    print('\n\tPRUEBA 9: Se ha pasado un tipo de parámetro diferente (número):')
    # Get_kit_body
    current_body = data.kit_body.copy()
    current_body["name"] = 123
    negative_assert_missing_parameters(current_body)

test_1_create_kit_1_letter_in_name_get_success_response()
test_2_create_kit_511_letter_in_name_get_success_response()
test_3_create_kit_0_letter_in_name_get_error_response()
test_4_create_kit_512_letter_in_name_get_error_response()
test_5_create_kit_has_special_symbol_in_name_get_error_response()
test_6_create_kit_has_space_in_name_get_error_response()
test_7_create_kit_has_number_in_name_get_error_response()
test_8_create_kit_no_first_name_get_error_response()
test_9_create_kit_number_type_first_name_get_error_response()