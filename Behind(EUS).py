import folium

# 지도 중심 (Stevenson Ranch 근처)
m = folium.Map(location=[34.3860, -118.5735], zoom_start=14)

# Stevenson Ranch 주변 카페 리스트 (예시 좌표 포함)
cafes = [
    {
        "name": "Tous Les Jours Stevenson Ranch",
        "address": "24935 Pico Canyon Rd",
        "lat": 34.3839,
        "lon": -118.5738,
        "year": 2020
    },
    {
        "name": "Urbane Cafe",
        "address": "25916 The Old Rd",
        "lat": 34.3875,
        "lon": -118.5735,
        "year": 2012
    },
    {
        "name": "Wushiland Boba Valencia",
        "address": "25914 The Old Rd",
        "lat": 34.3873,
        "lon": -118.5732,
        "year": 2023
    },
    {
        "name": "San Fernando Coffee Company",
        "address": "24921 Pico Canyon Rd",
        "lat": 34.3837,
        "lon": -118.5735,
        "year": 2021
    },
    {
        "name": "Starbucks (Westridge Village Center)",
        "address": "25720 The Old Rd",
        "lat": 34.3848,
        "lon": -118.5718,
        "year": 2018
    },
    {
        "name": "Starbucks (25289 The Old Rd)",
        "address": "25289 The Old Rd",
        "lat": 34.3815,
        "lon": -118.5730,
        "year": 2016
    },
    {
        "name": "Starbucks (Inside Vons)",
        "address": "25850 The Old Rd",
        "lat": 34.3860,
        "lon": -118.5742,
        "year": 2015
    }
]

# 연도별 색상 설정
colors = {
    2012: "purple",
    2015: "red",
    2016: "orange",
    2018: "blue",
    2020: "green",
    2021: "pink",
    2023: "brown"
}

# 카페 마커 추가
for cafe in cafes:
    folium.CircleMarker(
        location=[cafe["lat"], cafe["lon"]],
        radius=8,
        popup=f"{cafe['name']}<br>{cafe['address']}<br>Opened: {cafe['year']}",
        color=colors.get(cafe["year"], "gray"),
        fill=True,
        fill_color=colors.get(cafe["year"], "gray"),
        fill_opacity=0.7,
        weight=2
    ).add_to(m)

# 지도 저장
m.save("cafe_map.html")
print(" cafe_map.html created successfully.")