"""
A list of streets
Each street is a dictionary including the name of street and list of point labels
"""


streets = [
    {
        'name': 'Stevenson St',
        'paths': [
            [1, 2, 3, 4, 91, 92, 89, 90, 180, 181, 182, 183, 184, 185],
            [135, 134, 102, 103, 133, 132, 130, 129, 120, 121, 122, 125],
            [186, 187, 188, 189, 190, 191, 192, 193, 194],
        ],
    },
    {
        'name': 'Boxer St',
        'paths': [[5, 6, 7, 8, 9, 10, 11]],
    },
    {
        'name': 'Herman St',
        'paths': [[12, 13, 14, 15, 16, 17, 18]],
    },
    {
        'name': 'Karluk St',
        'paths': [[19, 20, 21, 22, 23, 24, 25, 26, 27]],
    },
    {
        'name': 'Laura Madison St',
        'paths': [[97, 28, 29, 30, 31, 32, 33, 34, 35, 36, 86]],
    },
    {
        'name': 'North Star St',
        'paths': [
            [37, 38, 39, 40, 41],
            [42, 43, 44, 45, 46]
        ],
    },
    {
        'name': 'Transit St',
        'paths': [
            [47, 48],
            [49, 50, 51, 52, 53]
        ],
    },
    {
        'name': 'Saya St',
        'paths': [
            [58, 59, 60],
            [57, 63]]
        ,
    },
    {
        'name': 'Yugit St',
        'paths': [[56, 75, 76, 64, 65, 66, 67, 79]],
    },
    {
        'name': 'Sanatu St',
        'paths': [[68, 69, 80]],
    },
    {
        'name': 'Iigu St',
        'paths': [[70, 71]],
    },
    {
        'name': 'Ahgeak St',
        'paths': [[72, 73, 81]],
    },
    {
        'name': 'Tahak St',
        'paths': [[1, 12, 19, 28, 37]],
    },
    {
        'name': 'Okakok St',
        'paths': [[2, 5, 13, 20, 29, 38, 47]],
    },
    {
        'name': 'C Ave',
        'paths': [
            [4, 7],
            [8, 15, 23],
            [22, 31, 40],
            [41, 49]
        ],
    },
    {
        'name': 'B Ave',
        'paths': [[74, 9, 16, 24, 32, 42, 50, 57]],
    },
    {
        'name': 'A Ave',
        'paths': [[10, 17, 25, 33, 43, 51, 58, 63, 64]],
    },
    {
        'name': 'Ahmoagak Ave',
        'paths': [[91, 11, 18, 26, 34, 44, 52, 59, 65]],
    },
    {
        'name': 'Uula St',
        'paths': [[27, 35, 45, 53, 60, 66, 68, 70, 72]],
    },
    {
        'name': 'Qaiyaan St',
        'paths': [[36, 46, 55, 62, 67, 69, 71, 73]],
    },
    {
        'name': 'Utiqtuq St',
        'paths': [[77, 55, 54, 61, 62, 78]],
    },
    {
        'name': 'Kaleak St',
        'paths': [[82, 83]],
    },
    {
        'name': 'Sakeagak St',
        'paths': [[81, 82]],
    },
    {
        'name': 'Kignak St',
        'paths': [[77, 78, 79, 80]],
    },
    {
        'name': 'Cakeatter Rd',
        'paths': [[84, 83, 85, 86, 87, 88, 90]],
    },
    {
        'name': 'Brower Rd',
        'paths': [[1, 93, 94, 95, 96, 97]],
    },
    {
        'name': 'Eben Hopson St',
        'paths': [[97, 98, 100, 101, 102, 104]],
    },
    {
        'name': 'Kogiak St',
        'paths': [[103, 104, 105, 131, 106, 107, 108, 109, 110, 111]],
    },
    {
        'name': 'Aivik St',
        'paths': [[130, 131]],
    },
    {
        'name': 'Agvik St',
        'paths': [[132, 105, 145, 144, 142, 137, 136]],
    },
    {
        'name': 'Egasak St',
        'paths': [
            [129, 128, 127, 126, 121],
            [122, 123, 116, 113]
        ],
    },
    {
        'name': 'Nachik St',
        'paths': [[129, 107, 147]],
    },
    {
        'name': 'Kongek St',
        'paths': [[106, 146]],
    },
    {
        'name': 'Church St',
        'paths': [[102, 145]],
    },
    {
        'name': 'Cunningham St',
        'paths': [[119, 107]],
    },
    {
        'name': 'Kongosak St',
        'paths': [[120, 119, 118, 117, 112]],
    },
    {
        'name': 'Egasak St',
        'paths': [[122, 123, 116, 113]],
    },
    {
        'name': 'Ogrook St',
        'paths': [[115, 116, 117, 110]],
    },
    {
        'name': 'Apayauk St',
        'paths': [[125, 115, 114]],
    },
    {
        'name': 'Pisokak St',
        'paths': [[114, 113, 112, 111]],
    },
    {
        'name': 'Fire Ln',
        'paths': [
            [123, 124],
            [184, 188, 201, 207],
            [181, 196, 192],
        ],
    },
    {
        'name': 'Nanook St',
        'paths': [[108, 152]],
    },
    {
        'name': 'Okpik St',
        'paths': [[109, 153, 155, 159, 161, 162, 163, 164, 165, 166, 167]],
    },
    {
        'name': 'D St',
        'paths': [[167, 168, 169, 170]],
    },
    {
        'name': 'H St',
        'paths': [[166, 176, 177]],
    },
    {
        'name': 'Paniego St',
        'paths': [[173, 175, 165]],
    },
    {
        'name': 'Itta St',
        'paths': [[164, 174, 173, 172, 177, 168]],
    },
    {
        'name': 'Tapak St',
        'paths': [[158, 159, 160]],
    },
    {
        'name': 'Ahkovak St',
        'paths': [[3, 6, 14, 21, 30, 39, 48, 56, 178, 170, 171, 162, 179, 158, 154, 110],],
    },
    {
        'name': 'Momeganna St',
        'paths': [[144, 146, 147, 148, 152, 153, 154]],
    },
    {
        'name': '',
        'paths': [[134, 143, 142]],
    },
    {
        'name': '',
        'paths': [[137, 138, 139, 140, 141, 138]],
    },
    {
        'name': '',
        'paths': [[148, 149, 150, 151]],
    },
    {
        'name': '',
        'paths': [[155, 156, 157]],
    },
    {
        'name': '',
        'paths': [[180, 195, 194, 197]],
    },
    {
        'name': '',
        'paths': [[193, 198]],
    },
    {
        'name': '',
        'paths': [[182, 191]],
    },
    {
        'name': '',
        'paths': [[183, 190]],
    },
    {
        'name': '',
        'paths': [[197, 198, 199, 200, 201, 202, 203, 204, 186]],
    },
    {
        'name': '',
        'paths': [[189, 200, 206]],
    },
    {
        'name': '',
        'paths': [[199, 205]],
    },
    {
        'name': '',
        'paths': [[187, 203]],
    },
    {
        'name': '',
        'paths': [[205, 206, 207]],
    },
    {
        'name': '',
        'paths': [[195, 196]],
    },
    {
        'name': '',
        'paths': [[185, 186]],
    },
    {
        'name': '',
        'paths': [[88, 89]],
    },
]


if __name__ == "__main__":
    print(len(streets))