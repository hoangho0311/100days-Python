import  requests
import html

reception = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
reception.raise_for_status()
data = reception.json()
print(data["results"])