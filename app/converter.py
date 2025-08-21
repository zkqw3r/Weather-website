async def wind_direction(degrees):
    """
    Function for getting information about wind direction (initially, 
    the API transmits wind direction degrees)
    """

    directions = ["С", "ССВ", "СВ", "ВСВ", "В", "ВЮВ", "ЮВ", "ЮЮВ",
                  "Ю", "ЮЮЗ", "ЮЗ", "ЗЮЗ", "З", "ЗСЗ", "СЗ", "ССЗ"]
    index = round(degrees/22.5) % 16
    return directions[index]


async def pressure_mmhg(hPa):
    return int(hPa*0.750062)


async def pick_icon(icon_id):
    """
    Function for selecting an image from the project folder, 
    due to the delay in loading the photo via the link via 
    url: https://openweathermap.org/img/wn/<id_icon>@2x.png, 
    it was decided to download all the icons and compare them 
    with the id that is passed to weather as the id parameter
    """
    group = {
        200:'icons/11d.png',
        201:'icons/11d.png',
        202:'icons/11d.png',
        210:'icons/11d.png',
        211:'icons/11d.png',
        212:'icons/11d.png',
        221:'icons/11d.png',
        230:'icons/11d.png',
        231:'icons/11d.png',
        232:'icons/11d.png',
        300:'icons/09d.png',
        301:'icons/09d.png',
        302:'icons/09d.png',
        310:'icons/09d.png',
        311:'icons/09d.png',
        312:'icons/09d.png',
        313:'icons/09d.png',
        314:'icons/09d.png',
        321:'icons/09d.png',
        500:'icons/10d.png',
        501:'icons/10d.png',
        502:'icons/10d.png',
        503:'icons/10d.png',
        504:'icons/10d.png',
        511:'icons/13d.png',
        520:'icons/09d.png',
        521:'icons/09d.png',
        522:'icons/09d.png',
        531:'icons/09d.png',
        600:'icons/13d.png',
        601:'icons/13d.png',
        602:'icons/13d.png',
        611:'icons/13d.png',
        612:'icons/13d.png',
        613:'icons/13d.png',
        615:'icons/13d.png',
        616:'icons/13d.png',
        620:'icons/13d.png',
        621:'icons/13d.png',
        622:'icons/13d.png',
        701:'icons/50d.png',
        711:'icons/50d.png',
        721:'icons/50d.png',
        731:'icons/50d.png',
        741:'icons/50d.png',
        751:'icons/50d.png',
        761:'icons/50d.png',
        762:'icons/50d.png',
        771:'icons/50d.png',
        781:'icons/50d.png',
        800:'icons/01d.png',
        801:'icons/02d.png',
        802:'icons/03d.png',
        803:'icons/04d.png',
        804:'icons/04d.png',
    }
    return group.get(icon_id)
