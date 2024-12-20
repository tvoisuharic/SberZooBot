from gigachat import GigaChat

def get_animal_description(animal: str) -> str:
  if animal == "" or animal is None:
    return "Не знаю такого зверя"
  with GigaChat(credentials="OWVmZDViNmYtODdlNy00ZGI4LWI1NmUtMDkxOTIxMDMxZTM1OmQxODJiZDRlLTRhZjgtNGUwYS05ZTMxLWM2YzJmYmUxZDRiYw==", verify_ssl_certs=False) as giga:
    response = giga.chat(f"Ты экскурсовод в зоопарке. Расскажи мне на русском вкратце о животном {animal} в интересном формате. Приведи несколько интересных фактов о жизни и привычках этого существа. Не используй особую разметку")
    return response.choices[0].message.content