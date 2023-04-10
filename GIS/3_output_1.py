import requests
import time

person_ids = [89, 170, 340, 400, 622, 624, 646, 647, 935, 936, 937, 1474, 1692, 2043, 1285, 1286, 1288]

print("personid\tAddrName")
for person_id in person_ids:
    url = f"https://cbdb.fas.harvard.edu/cbdbapi/person.php?id={person_id}&o=json"
    response = requests.get(url)
    data = response.json()
    addresses = data['Package']['PersonAuthority']['PersonInfo']['Person']['PersonAddresses']['Address']
    if isinstance(addresses, list):
        addr_name = None
        for address in addresses:
            if address['AddrType'] == '籍貫(基本地址)':
                addr_name = address['AddrName']
                break
    elif isinstance(addresses, dict):
        if addresses['AddrType'] == '籍貫(基本地址)':
            addr_name = addresses['AddrName']
        else:
            addr_name = None
    else:
        addr_name = None
    print(f"{person_id}\t{addr_name}")
    time.sleep(0.5)
