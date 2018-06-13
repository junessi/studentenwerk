# This is django apps which provide the canteen meals via RESTful API.

The information of a canteen are constructed in json format, below is an example:

```json
{
  name: "Mensa WUEins",
  fullname: "Mensa WUEins“,
  address: "Wundt Straße 1, 01217 Dresden",
  week0: [
    {
      text: "Angebote am Montag, 4. Juni 2018",
      meals_of_mealdate: [
      {
        name: "Türkisches Hacksteak mit Tsatsiki und gebackenen Kartoffelecken",
        price0: "2,71€",
        price1: "4,46€"
      },
      {
        name: "Pilzschmarrn mit Schnittlauchrahm und Rote-Bete-Salat",
        price0: "2,25€",
        price1: "4,00€"
      }
      ]
    },
    {
      text: "Angebote am Dienstag, 5. Juni 2018",
      meals_of_mealdate: [
        {
          name: "Geschnetzelter Hähnchen-Reisauflauf mit Curry",
          price0: "2,25€",
          price1: "4,00€"
        }
      ]
    },
    ......
  ],
  week1: [
    ......
  ],
  week2: [
    ......
  ]
}
```
