import requests

# URL API endpoint
url = "http://localhost:5054/api/Event"

# Dữ liệu mẫu
data = [
  {
        "event": {
            "eventid": 22898,
            "eventname": "2024 JIN YOUNG FAN MEETING IN VIETNAM <Love Letter>",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/18/3a/7a/488621ad9d789a7a1c8228209a2f546d.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 1500000,
            "starttime": "2024-09-28T11:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22897,
            "eventname": "2024 CHANYEOL LIVE TOUR: 都市風景 (City-scape) in HO CHI MINH",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/c9/5b/a3/4bf339980eafce491ff81ce1814ff7d1.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 2000000,
            "starttime": "2024-09-28T12:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 23002,
            "eventname": "Giai Điệu Mùa Thu",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/4d/d5/47/0fb24723a602b269c1ef471823df8ac5.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 50000,
            "starttime": "2024-09-28T12:30:39Z"
        }
    },
    {
        "event": {
            "eventid": 22947,
            "eventname": "DeloDelo Show : Liveshow \"Người Đang Yêu\"",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/ec/a4/15/7bdf0c75bc6e160083620b6b231e3b2a.jpeg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 550000,
            "starttime": "2024-09-28T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22649,
            "eventname": "[HCM] SUNGHA JUNG LIVE IN VIETNAM 2024",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/e4/7c/f2/c5a96abce15ad0e195cf4012bc5f3af2.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 700000,
            "starttime": "2024-10-04T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22903,
            "eventname": "LIVE CONCERT ĐỨC TRÍ - CÓ ĐÔI LẦN",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/ba/f5/84/ae0b8e22f3e1b1422bebe9afe36ed56c.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 1000000,
            "starttime": "2024-10-05T12:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22651,
            "eventname": "[ĐÀ NẴNG] SUNGHA JUNG LIVE IN VIETNAM 2024",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/27/d3/b5/053995945064a4d799fe0e3a3ecf506f.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 700000,
            "starttime": "2024-10-05T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 23102,
            "eventname": "HỒ CHÍ MINH - THE MUSIC OF ABBA | ARRIVAL FROM SWEDEN",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/eb/33/cd/ed8d18132e6666716e18328b200db382.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 1250000,
            "starttime": "2024-10-05T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22650,
            "eventname": "[HÀ NỘI] SUNGHA JUNG LIVE IN VIETNAM 2024",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/e4/7c/f2/ac2c5e7b45b2b560c452cf6c1ca98a6b.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 700000,
            "starttime": "2024-10-06T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 23095,
            "eventname": "[BẾN THÀNH] Đêm nhạc Lam Trường - Cẩm Ly",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/09/a6/06/c1890fa91b9334f9e4c5ff90e96ef5d1.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2024-10-06T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 23103,
            "eventname": "HỘI AN - THE MUSIC OF ABBA | ARRIVAL FROM SWEDEN",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/eb/33/cd/352a812b3d182ef9f383957ea789cbdf.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 600000,
            "starttime": "2024-10-08T12:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 23104,
            "eventname": "ĐÀ NẴNG - THE MUSIC OF ABBA | ARRIVAL FROM SWEDEN",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/eb/33/cd/6c537645e6b40499bfaaa9ea0afbc062.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 900000,
            "starttime": "2024-10-09T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22908,
            "eventname": "[TP.HCM] Vũ. - \"Bảo Tàng của Nuối Tiếc\" Live Concert 2024",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/44/e2/90/76fb84dbfdcd86e99f720aca467ffd04.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 599000,
            "starttime": "2024-10-12T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 23094,
            "eventname": "[BẾN THÀNH] Đêm nhạc Thùy Dung - KM: Nguyễn Đình Tuấn Dũng",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/75/3a/99/33b75f01cd382f58be53d4d564842dd5.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 300000,
            "starttime": "2024-10-12T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 23072,
            "eventname": "(Hà Nội) Funk, R'n\"B & City Pop - Nhóm nghệ sĩ Pháp FUNKINDUSTRY",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/a3/74/b6/60060c8342d1d745343c1922c44b6114.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 200000,
            "starttime": "2024-10-19T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22976,
            "eventname": "LULULOLA SHOW VŨ CÁT TƯỜNG | TỪNG LÀ",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/06/c8/2b/907245a444785aa567dc0136ed83c0cd.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 550000,
            "starttime": "2024-10-26T10:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22907,
            "eventname": "[Hà Nội] Vũ. - \"Bảo Tàng của Nuối Tiếc\" Live Concert 2024",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/38/f6/ef/afb1d3c8ef2492054ae52fee6e5aa30c.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 599000,
            "starttime": "2024-10-26T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22780,
            "eventname": "Ho Chi Minh City - The Bootleg Beatles",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/9d/48/e1/cbeea4fadb33c2ce2fc11f791de32f4e.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 1500000,
            "starttime": "2024-10-31T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22781,
            "eventname": "Hanoi - The Bootleg Beatles",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/dd/e0/38/a7da5503aeb91097712b8ca45bb9828c.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 1500000,
            "starttime": "2024-11-02T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 23091,
            "eventname": "YÊU HOÀ BÌNH 2024",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/f1/4a/c8/89538579ad36c711a125d59b92319d3f.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 490000,
            "starttime": "2024-11-30T06:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22981,
            "eventname": "[Đà Nẵng] Những Thành Phố Mơ Màng Year End 2024",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/2c/c7/b7/91caf2ee355252776fe11773bf223068.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 599000,
            "starttime": "2024-11-30T08:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22879,
            "eventname": "(Hà Nội) Piano | Olivier Moulin - Kỷ niệm 100 năm ngày mất của Gabriel Fauré",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/6e/a4/62/8697b312e05783e1309f61caec56ee6d.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 250000,
            "starttime": "2024-12-07T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22982,
            "eventname": "[TP.HCM] Những Thành Phố Mơ Màng Year End 2024",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/41/05/9f/c747749b3725747674cbeaab5340e5d0.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 599000,
            "starttime": "2024-12-08T08:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22983,
            "eventname": "[Hà Nội] Những Thành Phố Mơ Màng Year End 2024",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/63/16/63/e1b2ad0f15703886e705b66a1c2f09f5.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 599000,
            "starttime": "2024-12-21T08:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 831,
            "eventname": "YÊN ẤM MERCHANDISE_HOÀNG DŨNG_YÊN CONCERT",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/4c/1a/37/33e9975cec90506ae11a9dd491f6d07e.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 49000,
            "starttime": "2024-12-30T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 1279,
            "eventname": "The “Traditional Water Puppet Show”",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/03/21/08/2aff26681043246ebef537f075e2f861.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 300000,
            "starttime": "2024-09-24T11:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22969,
            "eventname": "[BẾN THÀNH] Đêm nhạc Lâm Bảo Ngọc - Phạm Anh Duy",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/55/66/1b/bd504bcc4965ecd06e773f0f75c99fd7.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 150000,
            "starttime": "2024-09-22T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22967,
            "eventname": "[BẾN THÀNH] Đêm nhạc Trung Quân - Văn Mai Hương",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/74/dc/6b/dac51e37825b7e93e7fbc875bc1e20ad.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 900000,
            "starttime": "2024-09-21T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22968,
            "eventname": "[BẾN THÀNH] Đêm nhạc Thái Đinh - Nam Kun",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/8e/c1/4b/f11558d7a5d7084898294d7680a47ee5.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 150000,
            "starttime": "2024-09-20T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22966,
            "eventname": "[BẾN THÀNH] Đêm nhạc Hà Nhi - Mai Tiến Dũng",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/76/16/78/b88c2a641b8d36d414fb3a05801745d8.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2024-09-19T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22824,
            "eventname": "[SG] CHỐN... TÌM SHOW VŨ CÁT TƯỜNG | \"TỪNG LÀ\"...\"NGƯỜI BÌNH THƯỜNG\"",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/c4/ae/b1/899236fe0e960ec5b772d19abc582213.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 550000,
            "starttime": "2024-09-19T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 23001,
            "eventname": "Hội Trăng Rằm Vạn Phúc City",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/5a/4f/e3/53f088dbf43be9f6ea44ba11d1bfbf95.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 50000,
            "starttime": "2024-09-15T12:20:00Z"
        }
    },
    {
        "event": {
            "eventid": 22888,
            "eventname": "Từ Nay...Từ Đây music show x Tăng Phúc (Chapter Hà Nội) ",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/79/1e/f2/43b816dcc2b2b70d1a7a0e6ccfa714c1.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 800000,
            "starttime": "2024-09-14T13:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22950,
            "eventname": "Ecstatic Dance & Contact Improv",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/20/ac/98/5bd1c3ced68185e4889ba6360c138403.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 150000,
            "starttime": "2024-09-14T11:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22798,
            "eventname": "20TH ANNIVERSARY 2024 KIM JAE JOONG ASIA TOUR CONCERT \"FLOWER GARDEN\" IN VIETNAM",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/15/fa/c8/4c10f840ae4686d82944ccdb34a617f0.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 2000000,
            "starttime": "2024-09-14T11:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22965,
            "eventname": "[BẾN THÀNH] Đêm nhạc Nguyễn Kiều Oanh - Dickson - KM: JINJU",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/06/a6/36/9a87fcc7ae1450e4e2e6043069c797e9.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 300000,
            "starttime": "2024-09-12T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22868,
            "eventname": "BOLLYWOOD NIGHT @ BENARAS HERITAGE ",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/3c/42/8f/6071d96edd0e4f1f34f990b0864905dc.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 289000,
            "starttime": "2024-09-07T12:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22943,
            "eventname": "[BẾN THÀNH] Đêm nhạc Phan Mạnh Quỳnh - Nguyên Hà. Special guest: Vy Vy",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/41/e2/4a/5e5ce2097b6b659792b4412c6d849ab7.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2024-09-06T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22931,
            "eventname": "[BẾN THÀNH] Đêm nhạc Mỹ Linh - Hoàng Hải",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/fe/9e/83/6f05248e113d15660b8b178bb9d9ca14.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2024-09-05T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22837,
            "eventname": "Van Phuc Water Show \"Love's Melody\"",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/8c/41/a3/e138f8331ab011e543ed63d6942ff1ed.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 280000,
            "starttime": "2024-09-02T11:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22864,
            "eventname": "LULULOLA SHOW THÙY CHI & VƯƠNG ANH TÚ | HẾT THƯƠNG CẠN NHỚ",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/59/55/ce/1ae8c45c2b6c1176de856629ad6235c4.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 450000,
            "starttime": "2024-09-01T10:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22829,
            "eventname": "TỪ ĐÂY...TỪ NAY... Music show x TĂNG PHÚC (Chapter Đà Lạt)",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/5f/f9/3f/ae7c9aa247bfc78212aa42ee523c633d.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 800000,
            "starttime": "2024-09-01T10:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22863,
            "eventname": "[MĂNG ĐEN TREEHOUSE VILLAGE - KON TUM] CHỐN...TÌM SHOW BẰNG KIỀU - PHƯỢNG VŨ | NƠI MÙA THU BẮT ĐẦU",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/0d/9a/e1/e90581077da9c00e26e636bdb9bacf49.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 450000,
            "starttime": "2024-09-01T10:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22818,
            "eventname": "Saigon International Guitar Festival 2024",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/90/88/2c/04e5e344e83979947bc71189651149ec.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 240000,
            "starttime": "2024-09-01T10:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22765,
            "eventname": "[HẢI PHÒNG] LÊ HIẾU & VICKY NHUNG",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/70/c6/eb/659930148c7f550bdf4e5230f7225c69.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 350000,
            "starttime": "2024-08-31T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22876,
            "eventname": "Tom Chat : Mini show \"Hãy yêu khi ta còn bên nhau\"",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/7a/68/8d/8b36e24844de31c7c5d877be594566d7.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2024-08-31T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22860,
            "eventname": "SỐNG D'ART - SONG D'ART LIVE CONCERT",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/92/41/a4/a438e8099bcef67611a4ac864cd14288.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 2000000,
            "starttime": "2024-08-31T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22771,
            "eventname": "DeloDelo Show : Trót Yêu",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/65/8d/31/a66178fa7a541f4b1cf750bb2e8baff1.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2024-08-31T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22941,
            "eventname": "31.08 | HỒ MÂY SHOW | PHAN HOÀNG YẾN | MINI LIVE SHOW | SÂN KHẤU TRÊN ĐỈNH NÚI",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/75/3f/46/bad06bf49f4c202186343f29453cbdc0.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 300000,
            "starttime": "2024-08-31T12:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22854,
            "eventname": "THE NEXT Live Concert",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/b7/f9/8d/101e33f85cb890be52e374186064cf5f.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 199000,
            "starttime": "2024-08-31T11:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22858,
            "eventname": "LULULOLA SHOW HỒ NGỌC HÀ | CÔ ĐƠN TRÊN SOFA",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/34/d5/cb/8e98dadf39aa082791175b3477a7c684.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 600000,
            "starttime": "2024-08-31T10:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 13047,
            "eventname": "WHITE PARTY VIETNAM 2024",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/02/22/BF092B.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 2200000,
            "starttime": "2024-08-30T09:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22811,
            "eventname": "Đêm nhạc Acoustic & Ballad gây quỹ từ thiện",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/78/38/0e/b17210de60198e5459ec5ff59d469aff.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 169000,
            "starttime": "2024-08-28T12:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22877,
            "eventname": "Tom Chat : Mini show Quang Linh \"Tình ca Bolero\"",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/92/ee/c6/4cb00dc460b4dee421674ac1c822cb23.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 300000,
            "starttime": "2024-08-24T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22738,
            "eventname": "THÁNG 8 CHÀO THU VI VU XEM NHẠC NƯỚC",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/d0/02/04/a31d12da65b72869920d95a7c35c2066.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 50000,
            "starttime": "2024-08-24T12:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22537,
            "eventname": "[HN] Hà Trần: Thiên Hà Tinh Khôi",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/9b/f9/1d/d9025f1b0696423a5382aaa72df3ebbe.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 1200000,
            "starttime": "2024-08-24T12:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22865,
            "eventname": "LULULOLA SHOW HÀ NHI | CHƯA QUÊN NGƯỜI YÊU CŨ",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/79/bc/c7/147059954a70e3229912017267cfa389.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2024-08-24T10:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22906,
            "eventname": "24.08 XUÂN NGHI THE VOICE | ĐÊM NHẠC TRÊN ĐỈNH NÚI ",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/44/77/28/f2567063fe5d389eb64260026e4111b5.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 250000,
            "starttime": "2024-08-24T10:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22924,
            "eventname": "TẮM ÂM THANH VỚI CHUÔNG XOAY VÀ GONG",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/28/e2/b2/9edf35787ee8a50466bcdd4f7d5cb106.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 350000,
            "starttime": "2024-08-24T10:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22848,
            "eventname": "[BẾN THÀNH] Đêm nhạc Lân Nhã - KM: Tiêu Châu Như Quỳnh",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/2c/91/07/6dc5cd050b5149bd0392057ca89afe05.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2024-08-18T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22862,
            "eventname": "LULULOLA SHOW VĂN MAI HƯƠNG & QUINN HIỀN MAI | ĐẠI MINH TINH",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/82/fb/b9/fdd2192806df8dca250d36272cf8e053.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 450000,
            "starttime": "2024-08-18T10:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22831,
            "eventname": "[BẾN THÀNH] Đêm nhạc Thái Đinh - Vinh Khuất",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/e5/c6/c4/199fcb70d4cab2b0539928b2a6b96b09.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 150000,
            "starttime": "2024-08-17T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22870,
            "eventname": "Tom Chat : Minishow Jimmii Nguyễn: \"Nhớ vể em\"",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/fe/ed/1c/fa60e2fb06727b5b942b0a10847ff41d.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2024-08-17T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22789,
            "eventname": "[THANH HÓA] CHỐN... TÌM SHOW HƯƠNG TRÀM - MARS ANH TÚ | DUYÊN MÌNH LỠ",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/27/ff/e3/1bec6a263f1df069c69d8710b73e4531.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 450000,
            "starttime": "2024-08-17T12:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22731,
            "eventname": "Tom Chat - Live Show No.15 : Chuyện Tình Yêu",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/91/8a/b4/c6ab9f36649b9f04f08314b32081e90d.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 200000,
            "starttime": "2024-08-16T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22894,
            "eventname": "[BẾN THÀNH] Đêm nhạc Trung Quân - Hiền Thục",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/b8/4a/b8/e36882ad455e0da861ac3e76195fef51.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 1000000,
            "starttime": "2024-08-14T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22814,
            "eventname": "1900 The Tunnel #28: Locked In",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/62/fe/6e/1a33b5765218eb6a987c5f412160f2b6.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 150000,
            "starttime": "2024-08-11T14:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22847,
            "eventname": "[BẾN THÀNH] Đêm nhạc Tuấn Ngọc",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/f1/72/1d/e1cccecf94daec245a759109447d4425.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2024-08-11T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22758,
            "eventname": "[SG] CHỐN... TÌM SHOW HƯƠNG TRÀM - MARS ANH TÚ | DUYÊN MÌNH LỠ",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/f8/25/7e/67f1022b0251257bb8b40634e5e8796f.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 700000,
            "starttime": "2024-08-10T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22538,
            "eventname": "[HCM] Hà Trần: Thiên Hà Tinh Khôi",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/f7/76/e8/96d3b14074c06dfa68a5b01767b79a75.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 1200000,
            "starttime": "2024-08-10T12:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22603,
            "eventname": "LULULOLA SHOW VŨ CÁT TƯỜNG | NGƯỜI BÌNH THƯỜNG",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/06/c8/2b/37ebab3a02b580b0189cd3632123b14c.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2024-08-10T10:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22845,
            "eventname": "[BẾN THÀNH] Đêm nhạc Bùi Lan Hương",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/50/84/3e/abaa859d955b048be0769d3185874001.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2024-08-09T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22830,
            "eventname": "[BẾN THÀNH] Đêm nhạc Văn Mai Hương - Hà An Huy",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/74/f1/a1/85f7e39e9cc31b1f2a576cffc6febf3e.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2024-08-05T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22729,
            "eventname": "TỪ ĐÂY... TỪ NAY Music Tour x Tăng Phúc (Sài Gòn)",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/7e/30/a8/65175c6c81f8dbe8c3a63418c3308d59.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 800000,
            "starttime": "2024-08-04T12:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22732,
            "eventname": "Tom Chat - Minishow : Cho em một lần yêu",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/44/5d/55/716f79f25b3ee86bbb28c91897e210e1.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2024-08-03T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22503,
            "eventname": "Liveshow Cẩm Ly - Kỷ niệm 30 năm ca hát - Tự tình quê hương 6",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/d5/6a/b4/6a9816189b5148a5750113f782e5be94.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 400000,
            "starttime": "2024-08-03T12:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22630,
            "eventname": "LULULOLA SHOW PHAN MẠNH QUỲNH | BIẾT ƠN ĐỂ ĐANG Ở LẠI",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/57/04/b1/39315e2c790f67ecc938701754816d15.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 450000,
            "starttime": "2024-08-02T10:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22762,
            "eventname": "[BẾN THÀNH] Đêm nhạc Vũ - Nguyên Hà",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/96/a0/2f/645eababa0bb48c96794436614cff1de.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2024-07-30T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22203,
            "eventname": "[HN] TRUNG QUÂN  1689 - More than 1589",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/97/da/27/688b1023838b78769de811921c861e46.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 1000000,
            "starttime": "2024-07-29T12:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22763,
            "eventname": "[BẾN THÀNH] Đêm nhạc Vương Anh Tú - Nguyễn Kiều Oanh. KM: Thành Đạt",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/a8/95/59/4258deed792c51ee797121074da82efb.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 300000,
            "starttime": "2024-07-28T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22484,
            "eventname": "2024 SUPER JUNIOR <SUPER SHOW SPIN-OFF: Halftime> in HO CHI MINH",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/c2/4b/79/43aa7f8fbf384caa5ddceb011498dbd7.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 3000000,
            "starttime": "2024-07-28T10:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22761,
            "eventname": "[BẾN THÀNH] Đêm nhạc Bạch Công Khanh - Tuấn Nghĩa",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/f1/15/31/03676d3fdb917725ea73fb644afa4137.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 150000,
            "starttime": "2024-07-27T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22683,
            "eventname": "SAY HI THÁNG 7 CÙNG VAN PHUC WATER SHOW",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/bb/73/32/e3018dbae9ad106cd87b5698b2d16b21.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 50000,
            "starttime": "2024-07-27T12:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22652,
            "eventname": "LULULOLA SHOW THÙY CHI & MAI TIẾN DŨNG | NGƯỜI NHƯ ANH HƠN EM CHỖ NÀO",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/e9/fb/9b/4501e2de06f2b5f454dc35b119d24217.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 450000,
            "starttime": "2024-07-27T10:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22760,
            "eventname": "[BẾN THÀNH] Đêm nhạc Phương Anh - Phương Ý. KM: Thanh Vinh",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/6e/38/91/627dfc4784d4151ac2436c85e9ee8f44.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 300000,
            "starttime": "2024-07-20T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22755,
            "eventname": "20.07 MINAKO BAND | LIVE BAND AT HỒ MÂY SHOW",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/6b/1e/5a/f714d983d91cb4aa5c4c42f9467a2593.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 200000,
            "starttime": "2024-07-20T12:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22706,
            "eventname": "[BẾN THÀNH] Đêm nhạc Thuỳ Dung - KM: Nguyễn Đình Tuấn Nghĩa",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/45/8a/ca/d2e4a4844120e3e9075098be0307efa3.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 300000,
            "starttime": "2024-07-19T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22670,
            "eventname": "LULULOLA SHOW HOÀNG DŨNG KM LÂM PHÚC & MR BOTT BAND | ĐÔI LỜI TÌNH CA",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/b1/08/4f/15a974b605c705c9890cb9e3ca4a4b74.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 450000,
            "starttime": "2024-07-19T10:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22204,
            "eventname": "[HCM] TRUNG QUÂN  1689 - More than 1589",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/bb/e2/49/34560b519e0293e77d1b16bbaaefcf1c.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 1000000,
            "starttime": "2024-07-13T12:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22600,
            "eventname": "LULULOLA SHOW LÂN NHÃ KM BÙI LAN HƯƠNG",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/ff/c1/fe/5c11b48e9101d920e6a6a8bff33b712c.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 450000,
            "starttime": "2024-07-13T10:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22737,
            "eventname": "1900 Hip Hop Party: Coldzy & Friends - MEDICINE: Exclusive Album Listening Party",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/26/84/3b/189e79daa65d770306cd60aff8b3d1de.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 350000,
            "starttime": "2024-07-12T14:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22656,
            "eventname": "[HẢI PHÒNG] LÊ HIẾU & VICKY NHUNG",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/4c/d7/fb/96ea174734ad3f98c1a51a2642885f63.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 400000,
            "starttime": "2024-07-12T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22705,
            "eventname": "[BẾN THÀNH] Đêm nhạc Hoàng Hải - Myra Trần",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/1a/cf/0a/dd89be01b53f00f260e91370a58fcc86.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2024-07-11T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22703,
            "eventname": "[BẾN THÀNH] Đêm nhạc Lê Hiếu - Lâm Bảo Ngọc",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/2a/a4/da/b2b855dff68707d70acbaddd818ab613.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 400000,
            "starttime": "2024-07-10T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22671,
            "eventname": "LULULOLA SHOW HOÀNG HẢI & THÙY CHI | NHẮN GIÓ MÂY RẰNG ANH YÊU EM",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/65/82/1e/23f76562706705c61e292b609df38ea1.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 450000,
            "starttime": "2024-07-07T10:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22633,
            "eventname": "MINI SHOW 06.07 TRƯƠNG THẢO NHI | SÂN KHẤU HỒ MÂY SHOW ",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/94/91/ed/498fbfe1c94828f08af4c888e2a25a8e.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 200000,
            "starttime": "2024-07-06T11:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22631,
            "eventname": "LULULOLA SHOW ƯNG HOÀNG PHÚC - NGUYỄN KIỀU OANH | NẾU TA CÒN YÊU NHAU",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/83/9b/e7/d87f0b648d52d24bf4ba4509c1c3f957.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 400000,
            "starttime": "2024-07-06T10:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22402,
            "eventname": "[Hà Nội] Những Thành Phố Mơ Màng Summer Tour 2024",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/a0/37/5e/2db1319230e01ee3e519dbd1a34c6fcf.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 389000,
            "starttime": "2024-07-06T08:19:00Z"
        }
    },
    {
        "event": {
            "eventid": 22702,
            "eventname": "[BẾN THÀNH] Đêm nhạc Quang Dũng",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/59/82/57/f23e2c79d382700c8d1675feda151e7d.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2024-07-05T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22660,
            "eventname": "CHƯƠNG TRÌNH BIỂU DIỄN PIANO CỔ ĐIỂN \"THE WORLD'S CLASSIC\"",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/86/f4/18/725d523c61602a8a3b0bd3559caaa3b6.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2024-06-30T12:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22602,
            "eventname": "HCM Piano Concerto cùng nghệ sĩ Bích Trà, nhạc trưởng Trần Nhật Minh, và hoạ sĩ ",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/f6/68/a0/f366a33b8adcc4e2f5401f80c3a98966.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 800000,
            "starttime": "2024-06-30T11:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22601,
            "eventname": "LULULOLA SHOW VĂN MAI HƯƠNG KM TAMA | MƯA THÁNG SÁU",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/d5/04/0f/db899d69ab93db592f0cefe60c7333d7.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 450000,
            "starttime": "2024-06-30T10:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22635,
            "eventname": "[HBSO] A NIGHT OF PYOTR TCHAINKOVSKY & RICHARD  STRAUSS",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/92/38/ec/e4708456f62b18262765e600db1357f4.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 550000,
            "starttime": "2024-06-29T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22569,
            "eventname": "DeloDelo Show : Vì Em Thương Anh",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/b4/be/58/94aaaf104e2108b89d21aa0ba043c6bf.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 450000,
            "starttime": "2024-06-29T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22673,
            "eventname": "VUI HÈ CÙNG CON VỚI VẠN PHÚC WATER SHOW",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/44/24/ba/cd2a0840d9e3ed5676a1115d15814386.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 50000,
            "starttime": "2024-06-29T12:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22556,
            "eventname": "HARMONY SHOW | TÌNH EM LÀ ĐẠI DƯƠNG | DUY MẠNH - LƯƠNG BÍCH HỮU",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/9b/02/e3/0ff09a9e80a056240dd45a5dbce7022c.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2024-06-29T12:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22599,
            "eventname": "LULULOLA SHOW LÊ HIẾU - TĂNG PHÚC - HỒ TIẾN ĐẠT - NS NGUYỄN MINH CƯỜNG",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/14/29/83/21b4cfe7e192377e5a3a3db1208db2b9.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 450000,
            "starttime": "2024-06-29T10:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22568,
            "eventname": "Nhịp Thời Gian : Hạt Mầm Yêu Thương",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/58/c5/bb/e32afc0f999b9a549a803fe37037705f.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 600000,
            "starttime": "2024-06-28T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22620,
            "eventname": "[BẾN THÀNH] Đêm nhạc Lương Bích Hữu - Tăng Phúc",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/59/ec/82/4c3539f36d49022c7f22ddd3b815760f.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 150000,
            "starttime": "2024-06-28T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22619,
            "eventname": "[BẾN THÀNH] Đêm nhạc Lân Nhã - Phương Linh",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/59/8d/92/252f4ade60ff649baff5d83ea2f379d7.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2024-06-27T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22468,
            "eventname": "Les danses",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/f2/7e/14/35186a5aea8b2a053afb1df3600afb42.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 100000,
            "starttime": "2024-06-26T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22618,
            "eventname": "[BẾN THÀNH] Đêm nhạc Nguyên Hà - Hà An Huy",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/e8/93/83/3dfc53c8772f50884d12c84799e500a3.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 300000,
            "starttime": "2024-06-23T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22435,
            "eventname": "(Hà Nội) Piano solo - David Greilsammer | Du hành cùng Satie ",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/f0/38/15/f009dd87ed00495db2377515923b910f.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 250000,
            "starttime": "2024-06-22T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22617,
            "eventname": "[BẾN THÀNH] Đêm nhạc Văn Mai Hương - Hoàng Dũng",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/fb/d8/51/0b832deb11bb399a6fd8837a70db6cd0.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2024-06-22T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22589,
            "eventname": "VUI HÈ CÙNG CON VỚI VAN PHUC WATER SHOW",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/f7/c2/29/18edda93cf928ed72924eaf4d7cdf08c.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 50000,
            "starttime": "2024-06-22T12:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22595,
            "eventname": "LULULOLA SHOW TĂNG PHÚC - NGUYÊN HÀ | CHỜ NGÀN LỜI HỨA",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/4c/40/db/ec3bbdb145f4bb505038e5ae8972b4bc.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 400000,
            "starttime": "2024-06-22T10:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22577,
            "eventname": "[BẾN THÀNH] Đêm nhạc Julie Thanh Nguyên - Thục Đoan - Nguyễn Đức",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/cc/ef/70/5d4757b5c3d450f5ddaae21afe7d89d0.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 150000,
            "starttime": "2024-06-21T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22594,
            "eventname": "LULULOLA SHOW MYRA TRẦN - MAI TIẾN DŨNG | CẦU VỒNG LẤP LÁNH",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/c6/fd/e1/ffaa102e8b270450205cf3646228b641.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 450000,
            "starttime": "2024-06-21T10:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22418,
            "eventname": "Automechanika Ho Chi Minh City",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/5e/14/06/c6110f4f83794f33063ba2de893d2259.jpeg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 149000,
            "starttime": "2024-06-21T10:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22561,
            "eventname": "[BẾN THÀNH] Đêm nhạc Phạm Quỳnh Anh - Myra Trần",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/9e/60/50/1f27f43203f97b6698659704c579ab17.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2024-06-20T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22578,
            "eventname": "[BẾN THÀNH] Đêm nhạc Mai Tiến Dũng - Lâm Bảo Ngọc",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/66/0d/01/4825f68fbbd99091b17a232a23d75498.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 300000,
            "starttime": "2024-06-19T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22560,
            "eventname": "[BẾN THÀNH] Đêm nhạc Phương Phương Thảo - Nguyễn Kiều Oanh",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/d3/23/34/74394c5a92719e252fc82feb722c1de0.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 300000,
            "starttime": "2024-06-16T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22559,
            "eventname": "[BẾN THÀNH] Đêm nhạc Nguyễn Đình Tuấn Dũng - Phương Phương Thảo - Viễn Trinh",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/af/d8/69/312a602b2b23557a2de058b13e0fc1b9.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 300000,
            "starttime": "2024-06-15T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 21859,
            "eventname": "[LULULOLA SHOW] BẰNG KIỀU | LẠI GẦN HÔN ANH",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/05/08/AB4869.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2024-06-15T10:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 14824,
            "eventname": "[NEW] VIETNAM COCKTAIL FESTIVAL 2024",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/03/01/996979.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 1000000,
            "starttime": "2024-06-15T08:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 15104,
            "eventname": "[Sài Gòn] Những Thành Phố Mơ Màng Summer Tour 2024",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/9f/0b/d4/f19a8a171d730418077d310ff82e7224.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 550000,
            "starttime": "2024-06-15T07:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22558,
            "eventname": "[BẾN THÀNH] Đêm nhạc Phan Mạnh Quỳnh - Bùi Lan Hương",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/97/5d/06/f166d17ccecc6dc26fe775acfda26ba0.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2024-06-14T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22462,
            "eventname": "MEMORY SHOW 5 | CHỦ ĐỀ: \"DUYÊN MÌNH LỠ\" - HƯƠNG TRÀM",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/6f/2b/d4/720556478b3b1eea0cb13867d0333106.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 400000,
            "starttime": "2024-06-09T12:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 21840,
            "eventname": "[LULULOLA SHOW] PHAN MẠNH QUỲNH - KM HELLEN | NGÀY CHƯA GIÔNG BÃO",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/57/04/b1/821b5e71ce786b82aca489bfbce354e5.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 450000,
            "starttime": "2024-06-07T10:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22447,
            "eventname": "WESTLIFE THE HITS TOUR 2024 LIVE IN HANOI",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/1a/52/a2/4303c4da7ba6e5806b06e9d40a91d0c5.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 850000,
            "starttime": "2024-06-05T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22557,
            "eventname": "[BẾN THÀNH] Đêm nhạc Đức Tuấn",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/4c/a8/73/4d2287d40fb9d8edd05ae47ba904fa6e.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 300000,
            "starttime": "2024-06-02T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22440,
            "eventname": "VUI TẾT THIẾU NHI CÙNG NHẠC NƯỚC VAN PHUC WATER SHOW",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/56/86/2d/64e4e64d5266efad159c33377d2cbb29.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 50000,
            "starttime": "2024-06-01T12:30:15Z"
        }
    },
    {
        "event": {
            "eventid": 22477,
            "eventname": "THE FOUNTAIN FESTIVAL",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/58/80/9b/b79b1b89e3668298fd44e2e626530729.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 350000,
            "starttime": "2024-06-01T11:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22464,
            "eventname": "LULULOLA SHOW VŨ CÁT TƯỜNG | TỪNG LÀ",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/23/a1/82/2d03b36411a1c7e4069cefa5c0b09c24.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2024-06-01T10:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22461,
            "eventname": "[DeloDelo Show] Liveshow Nhớ Về Em - Giấc Mơ Có Thật",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/2c/3c/60/56c0ebe388f4d2eb81ad944a4d85e534.jpeg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 550000,
            "starttime": "2024-05-31T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22423,
            "eventname": "Retro- Giao Hòa Cảm Xúc",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/27/95/45/67530f6eae5aaa9731b0297db58cd278.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 1500000,
            "starttime": "2024-05-31T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22459,
            "eventname": "HARMONY SHOW | MƯA THÁNG SÁU - DÀNH CHO EM | VĂN MAI HƯƠNG - HOÀNG TÔN",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/4b/12/67/d7c3f0f79227bd3a72e1124a48d28437.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 650000,
            "starttime": "2024-05-31T11:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22457,
            "eventname": "[BẾN THÀNH] Đêm nhạc Vũ - Orange",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/66/ba/57/b88e16bcd9f8d6049f219f62c7a72390.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 700000,
            "starttime": "2024-05-30T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22446,
            "eventname": "[HCM] NHÂM NHI GHITA cùng HOÀNG HẢI - QUANG TRUNG - ALI HOÀNG DƯƠNG",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/75/e3/41/60737a41d28c8edbb66f3b1b35a647a8.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 800000,
            "starttime": "2024-05-29T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22453,
            "eventname": "[BẾN THÀNH] Đêm nhạc Quốc Thiên - Phương Phương Thảo",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/b2/e5/91/c2e0fde72df43c2d618f0e8e34eb676a.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2024-05-26T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22466,
            "eventname": "LULULOLA SHOW THÙY CHI & LÊ HIẾU ",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/13/f1/fe/d8ca454bef955420bb80be540084bc75.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 400000,
            "starttime": "2024-05-25T10:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22491,
            "eventname": "LUNAS DEBUT SHOWCASE - OFFLINE FAN MEETING",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/e8/60/2a/c80d33a955fc8f36a98fcbc1f120c750.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 0,
            "starttime": "2024-05-25T08:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22438,
            "eventname": "Tom Chat Liveshow No.13 - Dạ Khúc Tháng Năm",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/8f/51/22/1227f0f17e6926ca8fd107df341b9146.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 600000,
            "starttime": "2024-05-24T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22451,
            "eventname": "[BẾN THÀNH] Đêm nhạc Thái Đinh - Phạm Hồng Phước - Phượng Vũ",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/3d/9f/b1/bbd86508d00cdef89fe20704d30b27f2.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 150000,
            "starttime": "2024-05-24T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22450,
            "eventname": "[BẾN THÀNH] Đêm nhạc Đan Trường - Lương Bích Hữu",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/3c/68/2f/cb3468fecedbd7c784c1cedc8c2ae104.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2024-05-19T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22448,
            "eventname": "[BẾN THÀNH] Đêm nhạc Quang - Nguyễn Kiều Oanh",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/d3/ae/5f/be82d1c75fa004f259622a9f5164a69d.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2024-05-18T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22465,
            "eventname": "LULULOLA SHOW HƯƠNG TRÀM & HOÀNG HẢI | CHO EM GẦN ANH",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/f7/ec/a5/af90e09020de64b37e3394a7a05682c3.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 450000,
            "starttime": "2024-05-18T10:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 15107,
            "eventname": "[Đà Nẵng] Những Thành Phố Mơ Màng Summer Tour 2024",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/f2/8d/0e/d1f556a40c9447add5f5d691d2cfb8c5.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 550000,
            "starttime": "2024-05-18T08:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 21999,
            "eventname": "ĐÊM CHUNG KẾT MISS & MISTER FITNESS SUPERMODEL WORLD 2024",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/6b/ff/7a/8b2400b82753028fa2964d370b13c047.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 400000,
            "starttime": "2024-05-18T08:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22458,
            "eventname": "[BẾN THÀNH] Đêm nhạc Hà Trần - Thuỳ Chi",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/11/38/47/d6aeebf9723c92de6f3f4fa96394162b.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 1000000,
            "starttime": "2024-05-17T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 18257,
            "eventname": "[LULULOLA SHOW] MYRA TRẦN • VƯƠNG ANH TÚ | ANH CHƯA THƯƠNG EM ĐẾN VẬY ĐÂU",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/f2/64/f8/6472faaba08a07f1ce6c184060c15e70.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 400000,
            "starttime": "2024-05-17T10:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 21468,
            "eventname": "[HẢI PHÒNG] TÌNH THÔI XÓT XA - LAM TRƯỜNG",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/04/17/925DE7.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 350000,
            "starttime": "2024-05-17T00:45:00Z"
        }
    },
    {
        "event": {
            "eventid": 22195,
            "eventname": "[Bến Thành] ĐÊM NHẠC VĂN MAI HƯƠNG - HOÀNG HẢI",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/04/25/07E84D.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2024-05-12T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22192,
            "eventname": "[Bến Thành] ĐÊM NHẠC QUANG DŨNG",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/04/25/CCC1F6.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2024-05-11T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 19885,
            "eventname": "SAIGON SOUL REVIVAL - New Album Tour",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/04/01/1A4D25.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 100000,
            "starttime": "2024-05-11T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 21060,
            "eventname": "SHE IN SHINE | HÀ NHI CONCERT 2024",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/40/a0/12/262d4adc48df842fb906543ab1965012.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 600000,
            "starttime": "2024-05-11T10:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22189,
            "eventname": "[Bến Thành] ĐÊM NHẠC MYRA  TRẦN - TĂNG PHÚC",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/04/25/64CC03.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2024-05-10T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22183,
            "eventname": "[Bến Thành] ĐÊM NHẠC THANH HÀ - NGUYỄN HÀ",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/04/25/A435FF.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2024-05-09T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22373,
            "eventname": "CONCERT: THE LOVE WITHIN [NHAC VIEN HCM]",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/04/29/C1A455.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 350000,
            "starttime": "2024-05-06T12:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 22180,
            "eventname": "[Bến Thành] ĐÊM NHẠC THÙY DUNG - special guest: NGUYỄN ĐÌNH TUẤN DŨNG",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/04/25/6B200E.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 300000,
            "starttime": "2024-05-03T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 21498,
            "eventname": "CHƯƠNG TRÌNH NHẠC NƯỚC ĐẶC BIỆT LỄ 1/5: KỂ TÍCH XƯA CÙNG VAN PHUC WATER SHOW",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/04/19/3F2DAA.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 50000,
            "starttime": "2024-05-01T12:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 20877,
            "eventname": "THE FOUNTAIN FESTIVAL",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/04/10/086652.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 350000,
            "starttime": "2024-05-01T11:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 21311,
            "eventname": "LULULOLA SHOW QUỐC THIÊN & THÀNH ĐẠT | NGÀY MAI NGƯỜI TA LẤY CHỒNG",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/50/8b/5f/1706eff1c1fb2a8ebdebe3aadf499199.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 400000,
            "starttime": "2024-05-01T10:15:00Z"
        }
    },
    {
        "event": {
            "eventid": 20757,
            "eventname": "HARMONY SHOW | SÓNG TÌNH | MTV BAND",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/04/09/4893BC.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 600000,
            "starttime": "2024-04-30T12:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 21686,
            "eventname": "THE FOUNTAIN FESTIVAL",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/04/10/086652.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 350000,
            "starttime": "2024-04-30T11:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 18932,
            "eventname": "LULULOLA SHOW VĂN MAI HƯƠNG | MƯA THÁNG SÁU",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/d6/00/0a/d7e3df5a45b393504d09267902a75286.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 450000,
            "starttime": "2024-04-30T10:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 20176,
            "eventname": "[NEW][Bến Thành] ĐÊM NHẠC VŨ - NGUYÊN HÀ",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/04/03/7F13AD.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2024-04-28T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 20628,
            "eventname": "LULULOLA SHOW THÙY CHI • MAI TIẾN DŨNG  | CON ĐƯỜNG HẠNH PHÚC",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/ab/03/aa/4b229dfc6fad92518edcf3f8bb631526.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 400000,
            "starttime": "2024-04-28T10:15:00Z"
        }
    },
    {
        "event": {
            "eventid": 19555,
            "eventname": "2024 KIM JAE JOONG SPECIAL J-PARTY FAN CONCERT [I’M TWENTY] IN VIETNAM",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/6e/88/05/b810a62b12cd32623bf3a271cc371b25.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 1500000,
            "starttime": "2024-04-27T11:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 16164,
            "eventname": "[NEW] [LULULOLA SHOW] ANH TÚ VOI BẢN ĐÔN & BẢO ANH",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/ae/22/dd/7b8fdacfe6b5e2e4e0176bad9fc242f9.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 450000,
            "starttime": "2024-04-27T10:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 20179,
            "eventname": "[NEW][Bến Thành] ĐÊM NHẠC BẠCH CÔNG KHANH - VIỄN TRINH",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/04/03/682FCD.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 250000,
            "starttime": "2024-04-26T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 21083,
            "eventname": "LULULOLA SHOW] HIỀN HỒ & VƯƠNG ANH TÚ | | GẶP NHƯNG KHÔNG Ở LẠI",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/27/51/6b/f5c44d8fdc309a5b35a4a18228504272.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 450000,
            "starttime": "2024-04-21T10:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 15100,
            "eventname": "[Hà Nội] Những Thành Phố Mơ Màng Summer Tour 2024",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/04/12/1D7EE3.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 550000,
            "starttime": "2024-04-20T08:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 20169,
            "eventname": "[NEW][Bến Thành] ĐÊM NHẠC VICKY NHUNG - NGUYỄN KIỀU OANH",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/04/03/B7993C.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 300000,
            "starttime": "2024-04-19T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 19463,
            "eventname": "[NEW][Bến Thành] ĐÊM NHẠC MỸ LINH - NGUYÊN HÀ",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/03/28/75F2FA.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2024-04-18T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 20172,
            "eventname": "[NEW][Bến Thành] ĐÊM NHẠC ĐỨC TUẤN - ĐỒNG LAN",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/04/03/7AFAFB.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 150000,
            "starttime": "2024-04-17T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 19466,
            "eventname": "[NEW][Bến Thành] ĐÊM NHẠC THÁI ĐINH - LÂM BẢO NGỌC",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/03/28/B13FAE.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 150000,
            "starttime": "2024-04-14T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 17563,
            "eventname": "[NEW] Hà Nội - Tuấn Hưng  : Show GỬI NGÀN LỜI YÊU - DeloDeloShow",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/03/18/7ECC2E.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2024-04-14T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 15566,
            "eventname": "[NEW] Hà Nội - Trung Quân  : Show TRÓT YÊU - DeloDeloShow",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/03/06/457014.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 600000,
            "starttime": "2024-04-13T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 17037,
            "eventname": "SPECIAL MEMORY SHOW: Birthday Night|Quốc Thiên",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/03/13/BA412D.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 600000,
            "starttime": "2024-04-13T12:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 17727,
            "eventname": "SAU NÀY CỦA CHÚNG TA - LÊ HIẾU - NGUYÊN HÀ",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/4e/7a/43/12f8d6a034885fb6dd4cd70889f2b90f.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 600000,
            "starttime": "2024-04-13T12:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 13921,
            "eventname": "[NEW] [LULULOLA SHOW] PHAN MẠNH QUỲNH - KM NGUYỄN KIỀU OANH | SAU LỜI TỪ KHƯỚC",
            "baner_url": "https://images.tkbcdn.com/2/608/332/ts/ds/cc/91/69/9f1be613b4389eaabb0a61bcf6c32efe.png",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 400000,
            "starttime": "2024-04-13T10:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 20284,
            "eventname": "INFiNITY Pool Party w/ Stelios Vasilloudis",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/04/03/8A9541.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 100000,
            "starttime": "2024-04-13T09:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 21043,
            "eventname": "Múa Hip-hop: The Roots",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2019/03/14/933123.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 100000,
            "starttime": "2024-04-11T17:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 19458,
            "eventname": "[NEW][Bến Thành] ĐÊM NHẠC QUỐC THIÊN - KM: UYÊN LINH - PHƯƠNG LINH",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/03/28/E6C3D7.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2024-04-08T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 13495,
            "eventname": "2024 BAEKHYUN [Lonsdaleite] IN HO CHI MINH",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/03/13/359E79.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 2500000,
            "starttime": "2024-04-07T17:07:00Z"
        }
    },
    {
        "event": {
            "eventid": 20163,
            "eventname": "THE FOUNTAIN FESTIVAL",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/04/03/3E212C.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 350000,
            "starttime": "2024-04-06T11:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 17404,
            "eventname": "[Bến Thành] ĐÊM NHẠC LÂN NHÃ - KM:  Lâm Bảo Ngọc - Guitarist Dũng dAlAt, nghệ sĩ Flute Hoàng Yến",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/03/18/65EDE4.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 850000,
            "starttime": "2024-03-31T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 15050,
            "eventname": "Classical Masterpieces Reimagined",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/03/12/EAF252.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 400000,
            "starttime": "2024-03-31T11:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 13721,
            "eventname": "HIMITSU MARCH WORKSHOP - NẾN THƠM (MAKE YOUR OWN CANDLE)",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/02/21/EAD2E5.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 400000,
            "starttime": "2024-03-31T08:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 14464,
            "eventname": "[NEW] [LULULOLA SHOW] TRUNG QUÂN | NGƯỜI ĐANG YÊU",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/04/28/73F878.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 450000,
            "starttime": "2024-03-30T10:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 16782,
            "eventname": "ROMANTIC NIGHT 3 - FROM WEST TO EAST",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/03/12/73AA0C.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2024-03-29T12:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 10105,
            "eventname": "SUPER JUNIOR-L.S.S. THE SHOW : Th3ee Guys in HO CHI MINH",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/03/15/74D423.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 1800000,
            "starttime": "2024-03-24T17:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 13743,
            "eventname": "HIMITSU MARCH WORKSHOP - TRỒNG CÂY (KOKEDAMA + TERRARIUM)",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/02/21/CC167B.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 700000,
            "starttime": "2024-03-24T03:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 16615,
            "eventname": "WORKSHOP DIY TRANH CHÂN DUNG ĐẤT SÉT",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/03/11/23F198.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 149000,
            "starttime": "2024-03-17T09:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 13752,
            "eventname": "THE SPONGEBOB MUSICAL: YOUTH EDITION",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/02/22/F6AC27.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 120000,
            "starttime": "2024-03-16T11:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 13855,
            "eventname": "HIMITSU MARCH WORKSHOP - PERFUME BY YOU (NƯỚC HOA ĐỘC BẢN)",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/02/21/0B8F77.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 600000,
            "starttime": "2024-03-16T11:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 10646,
            "eventname": "Open Air Cinema Club | Baby Driver",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/01/18/5C72BB.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 50000,
            "starttime": "2024-03-14T11:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 14449,
            "eventname": "[9/3 ] - MINISHOW - CÂU TRẢ LỜI DUY NHẤT -HOÀNG HẢI",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/02/25/29CBC6.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 350000,
            "starttime": "2024-03-09T10:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 11645,
            "eventname": "VỞ HÀI KỊCH \"XUÂN...DỮ CHƯA\"",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/02/02/866873.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 200000,
            "starttime": "2024-02-14T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 8891,
            "eventname": "[HAPPY VALENTINE'S DAY] - NGUYỄN TRẦN TRUNG QUÂN  -  NHẬT PHÁT - MINH SU - BINH VAN BAND",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/01/04/24686A.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 356000,
            "starttime": "2024-02-14T10:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 10835,
            "eventname": "LỄ HỘI TẾT - LỄ HỘI XUÂN TUẦN CHÂU - HẠ LONG",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/01/19/617E7C.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 139000,
            "starttime": "2024-02-12T00:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 8773,
            "eventname": "[THE GREENERY ART] ART WORKSHOP \"TRANG TRÍ LỊCH TẾT - DECORATE NEW YEAR CALENDAR\"",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/01/02/D76032.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 385000,
            "starttime": "2024-01-28T10:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 7048,
            "eventname": "[LOVE BY THE BAY] LAM TRƯỜNG | TÌNH THÔI XÓT XA",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/12/18/BE837D.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 540000,
            "starttime": "2024-01-13T13:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 9401,
            "eventname": "[ ITS x Thiên Đăng ] DISNEY 101: THE ULTIMATE SHOWDOWN - ĐẠI NHAC - KỊCH HỘI DISNEY TẠI SÂN KHẤU THIÊN ĐĂNG",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/01/10/5E410D.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 600000,
            "starttime": "2024-01-13T12:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 970,
            "eventname": "ĐÊM CHUNG KẾT CUỘC THI HOA HẬU HOÀN VŨ VIỆT NAM 2023",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/11/30/8E7D60.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 600000,
            "starttime": "2023-12-31T10:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 1010,
            "eventname": "[ HOA BAY- SHOW GALA 2023 ĐẶC BIỆT ] - BỐ GẤU HOÀNG HẢI - JIMMII NGUYỄN - NGỌC PHẠM - JIMMII BAND",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/12/01/8E8D21.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 390000,
            "starttime": "2023-12-30T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 72,
            "eventname": "ĐÊM BÁN KẾT & TRÌNH DIỄN TRANG PHỤC DÂN TỘC CUỘC THI HOA HẬU HOÀN VŨ VIỆT NAM 2023",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/11/27/BF25AA.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 300000,
            "starttime": "2023-12-26T11:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 940,
            "eventname": "[THE GREENERY ART] ART WORKSHOP \"VẼ TÚI VẢI 2023\"",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/11/30/ADC89F.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 385000,
            "starttime": "2023-12-26T10:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 70,
            "eventname": "[Lucteam Theatre] Kịch Búp Bê",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/11/29/1F68DD.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 300000,
            "starttime": "2023-12-23T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 5152,
            "eventname": "THE CHILL FEST - WHITE X'MAS",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/12/07/ECC920.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 299000,
            "starttime": "2023-12-22T10:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 186,
            "eventname": "Fintastic! Christmas Celebration",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/11/08/03B6D1.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 100000,
            "starttime": "2023-12-17T11:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 1447,
            "eventname": "I’ll be there: A Friendship Dance Story",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/12/10/B22A51.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 150000,
            "starttime": "2023-12-10T08:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 1337,
            "eventname": "Goatee The Goat",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/11/17/5FE9AB.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 120000,
            "starttime": "2023-12-09T08:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 1277,
            "eventname": "Miracle Christmas",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/11/21/C8993B.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 100000,
            "starttime": "2023-12-09T03:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 1164,
            "eventname": "Open Air Cinema Club | The Polar Express",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/11/10/72CC41.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 60000,
            "starttime": "2023-12-07T11:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 117,
            "eventname": "PEPSI presents RAVOLUTION Music Festival (RAVO-X Edition)",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/11/16/247724.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 999000,
            "starttime": "2023-12-03T08:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 130,
            "eventname": "Hanoi Christmas Market 2023",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/09/28/51EECC.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 127000,
            "starttime": "2023-12-02T04:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 1417,
            "eventname": "Sân Khấu Quốc Thảo- Nhạc kịch: \"Những Kẻ dị mộng mơ\"",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/11/02/3240A7.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 100000,
            "starttime": "2023-11-26T12:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 906,
            "eventname": "[HỒ CHÍ MINH] OPERA: Paysage dans l'oubli | Khung cảnh lãng quên -                                Olivier Dhénin Hữu & Benjamin Attahir",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/11/21/679F3B.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 100000,
            "starttime": "2023-11-26T09:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 604,
            "eventname": "Chương trình Múa Rối Nước Cổ Truyền",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/11/14/9D0E78.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 100000,
            "starttime": "2023-11-26T02:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 790,
            "eventname": "THE CURIOUS INCIDENT OF THE DOG IN THE NIGHT TIME",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/10/30/956CEF.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 120000,
            "starttime": "2023-11-25T07:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 1402,
            "eventname": "WESTLIFE - The Wild Dreams Tour",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/11/17/8588C8.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 600000,
            "starttime": "2023-11-22T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 1137,
            "eventname": "TWO X 30 Performance - Directed by Michael Caldwell",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/11/06/1F57A5.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 100000,
            "starttime": "2023-11-18T08:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 900,
            "eventname": "Sân Khấu Kịch Quốc Thảo - Kịch Ma : \"Mặt Nạ\"",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/01/31/7A46FB.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 100000,
            "starttime": "2023-11-12T12:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 1298,
            "eventname": "Vở Kịch \" Khách sạn 18.9Hz”",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/10/31/645319.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 150000,
            "starttime": "2023-11-12T12:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 1287,
            "eventname": "MY SCHOOL PRESIDENT FAN MEETING IN VIETNAM",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/10/03/D42B7E.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 1000000,
            "starttime": "2023-11-12T11:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 1275,
            "eventname": "TÁI TẠO NĂNG LƯỢNG VỚI CHUÔNG XOAY VÀ YOGA",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/10/20/C46AA4.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 1900000,
            "starttime": "2023-11-11T01:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 626,
            "eventname": "Trải Nghiệm Làm Gốm - Cảm nhận bình yên giữa lòng Sài Gòn",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/11/10/03DCCB.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 100000,
            "starttime": "2023-11-10T02:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 114,
            "eventname": "LIVE SYMPHONIC ORCHESTRA TO ZANARKAND",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/10/13/0DDFB3.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 440000,
            "starttime": "2023-10-28T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 554,
            "eventname": "Happy Halloween - Van Phuc Water Show",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/10/18/CAABF5.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 150000,
            "starttime": "2023-10-28T12:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 750,
            "eventname": "GIN FESTIVAL SAIGON 2023",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/09/11/9BFB69",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 1300000,
            "starttime": "2023-10-28T08:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 871,
            "eventname": "[HỒ CHÍ MINH] Fergessen (TP.HCM)",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/10/04/323F3F.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 100000,
            "starttime": "2023-10-26T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 96,
            "eventname": "MISS GRAND INTERNATIONAL 2023 - FINAL NIGHT",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/09/23/D46CC6.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 4000000,
            "starttime": "2023-10-25T12:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 1139,
            "eventname": "MISS GRAND INTERNATIONAL 2023 - SEMI-FINAL NIGHT",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/09/23/1520F8.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 1500000,
            "starttime": "2023-10-22T12:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 1364,
            "eventname": "Miss Grand International 2023 - National Costume",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/10/02/596BAA.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 1000000,
            "starttime": "2023-10-20T12:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 764,
            "eventname": "CHUNG KẾT CHƯƠNG TRÌNH THE NEW MENTOR - NGƯỜI MẪU TOÀN NĂNG",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/09/24/249704.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2023-10-15T11:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 896,
            "eventname": "Sân Khấu Kịch Quốc Thảo - Nhạc Kịch : \"Kỹ Nữ\"",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/02/28/D88DE3.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 100000,
            "starttime": "2023-10-14T12:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 311,
            "eventname": "\"Giấc Mơ Phù Đổng\" - Chương trình nghệ thuật truyền cảm hứng",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/10/13/4EA18C.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 300000,
            "starttime": "2023-10-13T12:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 1244,
            "eventname": "WORKSHOP LÀM BÁNH TRUNG THU",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/08/29/271ACC",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 450000,
            "starttime": "2023-09-30T07:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 1303,
            "eventname": "Nhạc kịch hài: AI LÀ HUNG THỦ?",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/04/02/907791.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 150000,
            "starttime": "2023-09-29T12:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 487,
            "eventname": "HAY GLAMPING MUSIC FESTIVAL 2023",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/09/18/1129F4.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 890000,
            "starttime": "2023-09-29T07:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 586,
            "eventname": "(Hà Nội) Duo piano & violon : Maxime Zecchini & Chương Vũ",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/08/31/52ABC3",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 250000,
            "starttime": "2023-09-22T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 250,
            "eventname": "[HỒ CHÍ MINH] Duo piano & violon : Maxime Zecchini & Chương Vũ",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/08/31/B2196D",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 250000,
            "starttime": "2023-09-15T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 1463,
            "eventname": "CHUNG KẾT TOÀN QUỐC MISS GRAND VIETNAM 2023",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/08/04/2BFDF0.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2023-08-27T12:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 956,
            "eventname": "CHA MẸ ĐỜI THẦM THIÊNG - NHỮNG HOÁ THÂN 3",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/07/18/2AB58F.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 110000,
            "starttime": "2023-08-26T09:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 1193,
            "eventname": "CHUNG KHẢO TOÀN QUỐC MISS GRAND VIETNAM 2023",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/08/04/43106D.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 200000,
            "starttime": "2023-08-23T12:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 1132,
            "eventname": "Sân Khấu Kịch Quốc Thảo - NHẠC KỊCH  : \"Siêu Thú Tranh Tài\"",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/05/19/6C506D.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 120000,
            "starttime": "2023-08-20T09:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 763,
            "eventname": "Nhạc Kịch : \"Công chúa kiêu kỳ và ba bà tiên \"",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/06/13/0AECC2.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 120000,
            "starttime": "2023-08-13T09:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 347,
            "eventname": "[Kịch] MÌNH NÓI CHUYỆN MÌNH - NSND Kim Xuân, Hồng Ánh, Đoàn Khoa, Quang Thảo, Huỳnh Ly",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/08/02/14BD48.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 250000,
            "starttime": "2023-08-12T12:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 1352,
            "eventname": "Hài kịch: Yêu Ông Thầy",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/03/28/40FF76.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 120000,
            "starttime": "2023-08-12T12:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 1253,
            "eventname": "[LOVE BY THE BAY] ĐÀM VĨNH HƯNG | BIỂN TÌNH",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/08/08/4AC776.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 600000,
            "starttime": "2023-08-12T10:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 1209,
            "eventname": "Sân Khấu Kịch Quốc Thảo - Nhạc Kịch: \"Vùng Đất Diệu Kỳ\"",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/05/29/AFF3F5.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 120000,
            "starttime": "2023-08-06T09:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 1090,
            "eventname": "Nhạc Nước - Van Phuc Water Show",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/07/13/3CE1AF.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 150000,
            "starttime": "2023-08-05T12:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 121,
            "eventname": "CLEAR presents WATERA FESTIVAL 2023 - Sat 29.07.2023",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/06/15/E62945.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 699000,
            "starttime": "2023-07-29T08:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 1216,
            "eventname": "MANGA COMIC CON Việt Nam 2023",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/06/30/2AC128.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 99000,
            "starttime": "2023-07-29T00:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 777,
            "eventname": "Vở diễn 'Hiu Hiu Gió Bấc'",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/06/19/FA1AF2.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 250000,
            "starttime": "2023-07-15T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 243,
            "eventname": "TRỌNG HIẾU - DANCE YOUR ENERGY UP MINISHOW",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/05/23/7CCE31.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 850000,
            "starttime": "2023-07-15T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 669,
            "eventname": "Chương trình âm nhạc thính phòng \"Tuyển tập âm nhạc Pháp\"",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/07/04/5D290F.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 100000,
            "starttime": "2023-07-12T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 717,
            "eventname": "[HÀ NỘI] OPERA - VIETNAM'S 2ND INTERNATIONAL CLASSICAL MUSIC FESTIVAL",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/06/29/2E2467.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2023-07-08T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 704,
            "eventname": "Danang Electronic Carnival- Let your Color glow 07/07/2023",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/06/24/F84983.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 450000,
            "starttime": "2023-07-07T09:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 383,
            "eventname": "Nhạc Trong Rừng #5: Hơi Thở Của Rừng by TAYNGUYENSOUND",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/05/23/21013B.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 399000,
            "starttime": "2023-06-30T12:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 177,
            "eventname": "Ca Nhạc Hài Kịch : Đêm Của Cười 3",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/06/14/C7E944.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 340000,
            "starttime": "2023-06-24T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 726,
            "eventname": "(Hà Nội) Pop - rock : The Rodeo & Mạc and the odd stones",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/05/18/750119.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 100000,
            "starttime": "2023-06-21T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 105,
            "eventname": "[HỒ CHÍ MINH] POP FRANÇAISE - THE RODEO",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/05/19/0486CA.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 150000,
            "starttime": "2023-06-16T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 1320,
            "eventname": "Nhạc Trong Rừng #3: Khởi Đầu Mới by Phạm Nguyên Ngọc, Vanh, Ca Ca và Võ Lê Vy",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/05/20/493754.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 499000,
            "starttime": "2023-06-03T12:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 1135,
            "eventname": "DANCENTER RECITALS & SHOW",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/05/27/E7DA1F.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 100000,
            "starttime": "2023-05-28T11:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 226,
            "eventname": "Hoà nhạc kèn gỗ: MAGIC IN THE WIND",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/04/14/88BAE1.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2023-05-20T12:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 221,
            "eventname": "Amazing Show: Trung Quân - Khách mời Miina (20/05/2023)",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/05/04/F90EDC.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 200000,
            "starttime": "2023-05-20T09:45:00Z"
        }
    },
    {
        "event": {
            "eventid": 1236,
            "eventname": "Amazing Show: Hoàng Dũng - Lê Hiếu (13/05/2023)",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/05/04/D6F48B.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 400000,
            "starttime": "2023-05-12T21:45:00Z"
        }
    },
    {
        "event": {
            "eventid": 214,
            "eventname": "Amazing Show:  Hồ Văn Cường - Danh ca Ngọc Sơn (30/04/2023)",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/04/14/D37A4F.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 800000,
            "starttime": "2023-04-30T09:45:00Z"
        }
    },
    {
        "event": {
            "eventid": 277,
            "eventname": "Love Story - SantaEarth Fanmeet In VietNam",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/02/24/51356D.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 1800000,
            "starttime": "2023-04-30T08:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 587,
            "eventname": "Amazing Show: VĂN MAI HƯƠNG - TRUNG QUÂN - MYRA TRẦN",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/03/06/A75A9C.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 800000,
            "starttime": "2023-04-22T09:45:00Z"
        }
    },
    {
        "event": {
            "eventid": 1336,
            "eventname": "[HÀ NỘI] OPERA - CAVALLERIA RUSTICANA",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/03/31/492ED0.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2023-04-16T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 522,
            "eventname": "[KROSSING OVER] FINAL SHOW: GIỮA NGÀN TINH TÚ | Dance x Live Music",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/04/15/939CE0.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 180000,
            "starttime": "2023-04-15T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 916,
            "eventname": "[KROSSING OVER] CÓ THỂ NGHE THẤY TÔI KHÔNG? | Dance x Talk",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/03/21/22FA55.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 400000,
            "starttime": "2023-04-14T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 183,
            "eventname": "[KROSSING OVER] HÀNH TRÌNH / JOURNAL | Dance x Live Music",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/03/30/CD7CA6.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 180000,
            "starttime": "2023-04-13T12:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 1150,
            "eventname": "[KROSSING OVER] VƯỢT QUA - CROSS/OVER | Dance x Film Screening x Live Music x Poetry",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/03/21/B070D7.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 400000,
            "starttime": "2023-04-12T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 621,
            "eventname": "[KROSSING OVER] WHEN FILM MEETS DANCE |  Film Screening",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/03/21/DB3F20.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 200000,
            "starttime": "2023-04-08T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 318,
            "eventname": "[SÀI GÒN] - TALENTED YOUTH",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/03/11/2E2D60.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 350000,
            "starttime": "2023-04-01T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 1210,
            "eventname": "Kịch: TRÁI TIM OAN KHUẤT - HOÀNG THÁI THANH",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2022/12/08/04C9EA.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 230000,
            "starttime": "2023-03-26T08:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 1134,
            "eventname": "Amazing Show:  TRUNG QUÂN - THUỲ CHI",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/03/06/B48BB3.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 700000,
            "starttime": "2023-03-25T09:45:00Z"
        }
    },
    {
        "event": {
            "eventid": 164,
            "eventname": "APPASSIONATA : Classical Music Concert",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/03/07/205EEC.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2023-03-19T11:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 268,
            "eventname": "St. Patrick's Day Fun Fair: Support Tree-Planting for a Greener Tomorrow",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/03/10/788799.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 50000,
            "starttime": "2023-03-19T07:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 640,
            "eventname": "Shooting Stars In VietNam",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2022/12/19/C787CB.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 1800000,
            "starttime": "2023-03-04T11:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 783,
            "eventname": "AMAZING SHOW: Văn Mai Hương - Tăng Phúc - Trương Thảo Nhi (04/03/2023)",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/02/06/E02564.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 600000,
            "starttime": "2023-03-04T09:45:00Z"
        }
    },
    {
        "event": {
            "eventid": 735,
            "eventname": "NHÓM KỊCH NNCK: Kịch Thiếu Nhi - RA ĐẢO LẤY VÀNG",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/02/09/E6B6C8.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 200000,
            "starttime": "2023-02-26T09:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 97,
            "eventname": "NHÓM KỊCH NNCK: Kịch Thiếu Nhi - BẠCH TUYẾT",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2022/12/12/9D0DF3.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 200000,
            "starttime": "2023-02-26T09:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 911,
            "eventname": "NHÓM KỊCH NNCK: THỊ HẾN LẮM CHIÊU...THỊ NGHÊU LẮM TRÒ",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/01/10/427203.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 200000,
            "starttime": "2023-02-24T17:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 672,
            "eventname": "NHÓM KỊCH NNCK: SÀN NHẢY PHI CÔNG (18+)",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2022/04/16/6368FB.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 200000,
            "starttime": "2023-02-18T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 1024,
            "eventname": "Amazing Show: Trịnh Thăng Bình - Liz Kim Cương - Khách mời Hà Nhi (18/02/2023)",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/02/06/E12D0B.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 600000,
            "starttime": "2023-02-18T10:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 1348,
            "eventname": "[ 1st FAN MEETING ]  OHM NANON IN VIETNAM",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/01/06/A258F2.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 1800000,
            "starttime": "2023-02-18T07:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 405,
            "eventname": "Chung kết Miss Charm 2023",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/02/08/456D6A.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2023-02-16T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 932,
            "eventname": "VALENTINE CONCERT - FROM ITALY WITH LOVE",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2022/12/30/C35992.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 300000,
            "starttime": "2023-02-12T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 167,
            "eventname": "NHÓM KỊCH NNCK: SÀI GÒN CÒN NGƯỜI TỐT KHÔNG ?",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/01/10/951768.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 200000,
            "starttime": "2023-02-11T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 509,
            "eventname": "Open Air Cinema Club | Mad Max: Fury Road",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/02/01/A41648.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 50000,
            "starttime": "2023-02-10T12:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 264,
            "eventname": "Amazing Show: DALAB - MIU LÊ",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2022/11/22/EE9A65.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 800000,
            "starttime": "2023-02-05T09:45:00Z"
        }
    },
    {
        "event": {
            "eventid": 1229,
            "eventname": "Amazing Show: Trung Quân Idol - Phạm Quỳnh Anh",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/02/01/43A70F.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 600000,
            "starttime": "2023-02-04T09:45:00Z"
        }
    },
    {
        "event": {
            "eventid": 870,
            "eventname": "Kịch: MÙI CỦA HẠNH PHÚC - HOÀNG THÁI THANH",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2022/08/17/50E89D.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 210000,
            "starttime": "2023-01-29T12:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 253,
            "eventname": "Hài kịch: ĐẢO THOÁT Ế",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/01/03/D27C42.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 150000,
            "starttime": "2023-01-28T12:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 788,
            "eventname": "Amazing Show: TRUNG QUÂN IDOL - MYRA TRẦN",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2022/12/26/2100C1.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 800000,
            "starttime": "2023-01-25T10:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 131,
            "eventname": "[ DA LAT BY NIGH ] LƯƠNG BÍCH HỮU - ƯNG HOÀNG PHÚC 25.1.2023 (Mùng 4 tết)",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/01/03/DB7641.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 800000,
            "starttime": "2023-01-25T09:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 123,
            "eventname": "Amazing Show: ANH TÚ - LYLY",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2022/12/26/1EC999.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 700000,
            "starttime": "2023-01-24T10:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 184,
            "eventname": "THE PIANIST: VOICE OF THE NEW GENERATION",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/01/06/51A496.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 400000,
            "starttime": "2023-01-15T12:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 1338,
            "eventname": "[ Dalat by night] TRUNG QUÂN - UYÊN LINH",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/01/03/6BD651.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 800000,
            "starttime": "2023-01-14T09:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 643,
            "eventname": "[ Amazing show] TRUNG QUÂN - UYÊN LINH",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2023/01/03/6BD651.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 800000,
            "starttime": "2023-01-14T09:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 858,
            "eventname": "Cải lương: BẠCH LONG - 55 Năm \"Ăn Cơm Tổ, Khổ Vẫn Cười!\"",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2022/12/12/22D4EA.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 220000,
            "starttime": "2023-01-08T12:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 497,
            "eventname": "Vở cải lương \"Loạn Thế Anh Hùng\"",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2022/12/28/1DF1D1.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 200000,
            "starttime": "2023-01-07T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 1172,
            "eventname": "Amazing Show: NAM EM - VƯƠNG ANH TÚ",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2022/12/26/B7073C.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2023-01-01T10:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 1976,
            "eventname": "INTOART Forest 2022",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2022/11/29/A312CF.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ho Chi Minh City"
        },
        "listing": {
            "priceperticket": 1400000,
            "starttime": "2022-12-31T07:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 453,
            "eventname": "NHÓM KỊCH NNCK: CHỒNG CHUNG CHUNG CHỒNG (YÊU AI AI YÊU?)",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2022/10/14/93E351.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 200000,
            "starttime": "2022-10-21T13:00:00Z"
        }
    },
    {
        "event": {
            "eventid": 22386,
            "eventname": "ĐÊM NHẠC TRỊNH CÔNG SƠN: NHỚ ÁNH THÊ THIẾT",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2022/07/28/D49C03.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Ha Noi Capital"
        },
        "listing": {
            "priceperticket": 250000,
            "starttime": "2022-08-01T13:30:00Z"
        }
    },
    {
        "event": {
            "eventid": 18009,
            "eventname": "SỰ KIỆN CHUNG KẾT HOA HẬU HOÀN VŨ VIỆT NAM 2022",
            "baner_url": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2022/06/14/7F229B.jpg",
            "description": ""
        },
        "venue": {
            "venuecity": "Da Nang City"
        },
        "listing": {
            "priceperticket": 500000,
            "starttime": "2022-06-25T11:00:00Z"
        }
    }
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
        "catId": 1  # Assuming a default category ID
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