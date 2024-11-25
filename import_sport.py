import requests

# URL API endpoint
url = "http://localhost:5054/api/Event"

# Dữ liệu mẫu
data = [
    {
        "event": {
            "eventid": 23077,
            "eventname": "VBA 2024 - FINALS GAME 1 - SAIGON HEAT vs CANTHO CATFISH",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/9b/70/96/4d368a40fbbe70184a6278a0f3361506.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 250000,
            "starttime": "2024-09-24T12:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22977,
            "eventname": "VBA 2024 PLAYOFFS GAME 1 - SAIGON HEAT VS NHA TRANG DOLPHINS",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/9b/70/96/3169bdd0e15cb9fba7c362f62462c4ed.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 250000,
            "starttime": "2024-09-15T12:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22936,
            "eventname": "Lion Championship 17 - 2024",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/b2/9e/9a/08564ab0ca80e401a0f64ff48ab87ee1.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 200000,
            "starttime": "2024-09-08T07:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22711,
            "eventname": "VBA  2024 - SAIGON HEAT VS CAN THO CATFISH - AUG 31",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/9b/70/96/bc9b81311df14f239d727191f6712132.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 200000,
            "starttime": "2024-08-31T12:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22896,
            "eventname": "VIEWING PARTY: CKTG VALORANT CHAMPIONS 2024",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/d7/73/6e/ddea48a734752d1999d70a9f97876c03.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 169000,
            "starttime": "2024-08-25T03:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22861,
            "eventname": "THẦN VÕ VIỆT NAM: VÒNG TỨ KẾT",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/45/7f/4c/dbe82f46c4050ae1a7edc77298c39a24.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 350000,
            "starttime": "2024-08-24T12:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22866,
            "eventname": "Sự kiện Offline Vòng Chung kết Giải đấu VCS 2024 MÙA HÈ",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/13/2a/40/55c178ad60dfba08e582a26a0c4d6b9f.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 249000,
            "starttime": "2024-08-18T08:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22890,
            "eventname": "ARENA OF FIGHTERS ",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/84/69/10/3231d05f7094f6d96d94588ead29af77.jpeg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2024-08-17T12:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22574,
            "eventname": "LEAD Professional Boxing | WBA Asia Vietnam Tournament | Quarter-finals",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/9e/bd/a0/da48c19d673397411bd9118e576077d4.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 300000,
            "starttime": "2024-08-11T11:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22710,
            "eventname": "VBA  2024 - SAIGON HEAT VS NHA TRANG DOLPHINS - AUG 10",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/9b/70/96/faf7434e7629fb90c46441b1b4e74404.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 200000,
            "starttime": "2024-08-10T12:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22806,
            "eventname": "Lion Championship 16 - 2024",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/4c/42/31/a881d1e1cf4ad2b30e05fb6672d9f95b.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 200000,
            "starttime": "2024-08-10T11:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22812,
            "eventname": "ĐẤU TRƯỜNG HỖN CHIẾN",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/e9/8a/d5/06fd5352c9a0788b6da76bb67a685713.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 199000,
            "starttime": "2024-08-10T02:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22709,
            "eventname": "VBA  2024 - SAIGON HEAT VS NHA TRANG DOLPHINS - AUG 07",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/9b/70/96/d5fcba94a5390448be39e32f22519b31.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 200000,
            "starttime": "2024-08-07T12:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22708,
            "eventname": "VBA  2024 - SAIGON HEAT VS DANANG DRAGONS - JUL 28",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/9b/70/96/73042ae6ca1adea02103d5eda99264fc.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 200000,
            "starttime": "2024-07-28T12:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22754,
            "eventname": "Chung kết giải đấu VALORANT CHAMPIONS TOUR 2024: CHALLENGERS VIETNAM SPLIT 2",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/48/3b/69/af1f4d104e01ba72504cb217b2599b19.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 129000,
            "starttime": "2024-07-25T07:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22570,
            "eventname": "Muay Thai Rampage x Road To ONE: Vietnam - SEMI-FINAL ROUND/ VÒNG BÁN KẾT",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/26/57/6f/4640e05173bc98583fe3117ea0a29172.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 300000,
            "starttime": "2024-07-21T11:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22704,
            "eventname": "VBA  2024 - SAIGON HEAT VS HO CHI MINH CITY WINGS - JUL 19",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/9b/70/96/086c7352a3a7caa5e150e5dc22dbe424.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 200000,
            "starttime": "2024-07-19T12:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22701,
            "eventname": "VBA  2024 - SAIGON HEAT VS CANTHO CATFISH - JUL 17",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/9b/70/96/c5709e986a5d39ebbdfb73e2a11b8d00.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 200000,
            "starttime": "2024-07-17T12:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22700,
            "eventname": "VBA 2024 - SAIGON HEAT VS DANANG DRAGONS - JUL 14",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/9b/70/96/5133b985ec3f90d08ee604ca129e6920.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 200000,
            "starttime": "2024-07-14T12:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22681,
            "eventname": "Lion Championship 15 - 2024",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/16/80/7e/44d46d5e87b1ff7c207251ee6e4ad5df.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 200000,
            "starttime": "2024-07-13T07:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22698,
            "eventname": "VBA  2024 - SAIGON HEAT VS HANOI BUFFALOES - JUL 07",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/9b/70/96/57edbec5b30f821eadb74bdabef9c565.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 200000,
            "starttime": "2024-07-07T12:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22677,
            "eventname": "VBA 2024 - SAIGON HEAT VS HANOI BUFFALOES- JUNE 30",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/9b/70/96/a348aaf8011d4cb464f33f7a4d29eda6.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 200000,
            "starttime": "2024-06-30T12:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22676,
            "eventname": "VBA  2024 - SAIGON HEAT VS HO CHI MINH WINGS - JUNE 28",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/9b/70/96/2dd7c9300a46215dcc8df0cb5b83aac6.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 200000,
            "starttime": "2024-06-28T12:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22552,
            "eventname": "Lion Championship 14 - 2024",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/ee/f4/b3/2c2c4b30ec43fa6a526f6be777203dfa.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 200000,
            "starttime": "2024-06-15T11:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 14124,
            "eventname": "MuayThai Rampage x Road to One - ELIMINATION",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/5e/d6/a3/b03f1c63cf18affcd298bc2252f8dba5.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 300000,
            "starttime": "2024-05-19T11:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22483,
            "eventname": "VIEWING PARTY - CHUNG KẾT TỔNG MSI 2024 | TPHCM & HÀ NỘI",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/a1/11/1e/61860cba92c1153a0e5a21190d7bea8b.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 129000,
            "starttime": "2024-05-19T08:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22421,
            "eventname": "Lion Championship 13 - 2024",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/d7/47/bb/96e77130a842e86eef4b59b79469b7e9.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 200000,
            "starttime": "2024-05-18T11:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 17374,
            "eventname": "BRAZIL VIETNAM FOOTBALL FESTIVAL 2024",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/04/22/B17195.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 600000,
            "starttime": "2024-04-27T10:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 18839,
            "eventname": "Lion Championship 12 - 2024",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/03/25/96AFC5.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 200000,
            "starttime": "2024-04-13T08:00:00Z"
        }
    },
]

# # Hàm thêm từng sự kiện
# def add_event(event):
#     # Chuyển đổi dữ liệu cho phù hợp với API
#     payload = {
#         "eveName": event["event"]["eventname"],
#         "eveDesc": event["event"].get("description", ""),
#         "eveCity": event["venue"]["venuecity"],
#         "eveTimestart": event["listing"]["starttime"],
#         "eveTimeend": event["listing"]["starttime"],  # Assuming end time is same as start
#         "eveThumb": event["event"]["baner_url"],
#         "catId": 2  # Assuming a default category ID
#     }
    
#     try:
#         # Gửi POST request
#         response = requests.post(url, json=payload)
#         # Kiểm tra phản hồi
#         if response.status_code == 201:
#             print(f"Sự kiện '{event['event']['eventname']}' đã được thêm thành công!")
#         else:
#             print(f"Lỗi khi thêm sự kiện '{event['event']['eventname']}': {response.text}")
#     except Exception as e:
#         print(f"Lỗi kết nối khi thêm sự kiện '{event['event']['eventname']}': {str(e)}")

type_url = "http://localhost:5054/api/type"
event_url = "http://localhost:5054/api/Event"
ticket_url = "http://localhost:5054/api/Ticket"

# Hàm thêm sự kiện
def add_event(event):
    payload = {
        "eveName": event["event"]["eventname"],
        "eveDesc": event["event"].get("description", ""),
        "eveCity": "Hanoi",  # Default city
        "eveTimestart": "2024-12-01T09:00:00.000Z",
        "eveTimeend": "2024-12-01T18:00:00.000Z",
        "eveThumb": event["event"]["baner_url"],
        "catId": 2  # Assuming a default category ID
    }
    try:
        response = requests.post(event_url, json=payload)
        if response.status_code == 201:
            event_data = response.json()
            print(f"Sự kiện '{payload['eveName']}' đã được thêm thành công với ID {event_data['eveId']}!")
            return event_data["eveId"]  # Trả về ID sự kiện vừa được thêm
        else:
            print(f"Lỗi khi thêm sự kiện '{event['event']['eventname']}': {response.text}")
            return None
    except Exception as e:
        print(f"Lỗi kết nối khi thêm sự kiện '{event['event']['eventname']}': {str(e)}")
        return None

# Hàm thêm Type cho sự kiện
def add_type(event_id):
    payload = {
        "typeName": "Standard",
        "typeDesc": f"Default type for Event {event_id}",
        "eventId": event_id
    }
    try:
        response = requests.post(type_url, json=payload)
        if response.status_code == 201:  # Nếu API trả về 201 (Created)
            type_data = response.json()
            print(f"Type 'Standard' đã được thêm cho sự kiện ID {event_id} với ID {type_data['typeId']}!")
            return type_data["typeId"]
        elif response.status_code == 200:  # Nếu trả về 200 (OK)
            type_data = response.json()
            print(f"Type có thể đã tồn tại: {type_data}")
            return type_data.get("typeId")  # Trả về typeId nếu có
        else:
            print(f"Lỗi khi thêm Type cho sự kiện ID {event_id}: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"Lỗi kết nối khi thêm Type cho sự kiện ID {event_id}: {str(e)}")
        return None

# Hàm thêm Ticket cho sự kiện
def add_ticket(event_id, type_id, ticket_price, ticket_qty=100):
    payload = {
        "eveId": event_id,
        "typeId": type_id,
        "ticketPrice": ticket_price,
        "ticketQty": ticket_qty
    }
    try:
        response = requests.post(ticket_url, json=payload)
        if response.status_code == 200:
            ticket_data = response.json()
            print(f"Ticket đã được thêm cho sự kiện ID {event_id} với Type ID {type_id}: {ticket_data}")
        else:
            print(f"Lỗi khi thêm Ticket cho sự kiện ID {event_id}: {response.text}")
    except Exception as e:
        print(f"Lỗi kết nối khi thêm Ticket cho sự kiện ID {event_id}: {str(e)}")

# Thêm sự kiện, Type và Ticket
for event in data:
    created_event_id = add_event(event)  # Thêm sự kiện
    if created_event_id:
        created_type_id = add_type(created_event_id)  # Thêm Type
        if created_type_id:
            ticket_price = event["listing"]["priceperticket"]  # Lấy giá vé từ dữ liệu
            add_ticket(created_event_id, created_type_id, ticket_price=ticket_price, ticket_qty=100)  # Thêm Ticket