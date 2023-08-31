from base import query


def create_payload(text, target_language):
    payload = {
        "inputs": ">>" + str(target_language) + "<<" + str(text)
    }
    return payload


def translate(text, target_language=None):
    payload = create_payload(text,
                             target_language)
    response = query(payload)
    response = response[20:-3]
    return response


print(translate("Where are we", "nyn"))
