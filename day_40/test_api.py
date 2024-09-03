import  requests
import os
TOKEN = os.getenv("TOKEN")
email = "jlcarcamosurbina@gmail.com"
id = 1
head = {"Authorization": TOKEN}
end_point = f'https://api.sheety.co/cd1a064e0f44ab9c6aca48b4624dcb9a/emails/respuestasDeFormulario1/{int(id)}'
params = {"respuestasDeFormulario1": {"confirm": 1, "email": email}}
put_results = requests.put(url=end_point, json=params, headers=head)
put_results.raise_for_status()

print (put_results.text)