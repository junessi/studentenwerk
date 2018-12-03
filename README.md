# This is a set of django apps which provide the canteen information and meals via RESTful API.

## To retrieve the information of a canteen, use the following api:
```
GET /<canteen_name>
```
For example:
```
# Get details about canteen WUEins
$ curl http://example.com/wueins
{
    name: "Mensa WUEins",
    fullname: "Mensa WUeins / Sportsbar",
    address: "Wundtstraße 1, 01217 Dresden",
    city: "Dresden",
    detail: "Zwei Gerichte stehen zur Auswahl, eines davon vegetarisch. Es gibt täglich ein frisches Salatbuffet, Desserts und Eis sind ebenfalls im Angebot.",
    opentimes: "10302130|10302130|10302130|10302130|10302130|closed|closed",
    contact: "",
    logourl: "https://www.studentenwerk-dresden.de/images/mensen/logos/mensa-wueins-sportsbar.png",
}
```

## There are several apis that can get meals of a canteen by using a pattern to set range of dates.
The following patterns can be used to get meals of yesterday, today and tomorrow, and the meals of last, this and next week.
```
GET /<canteen_name>/(yesterday|today|tomorrow)
GET /<canteen_name>/(last|this|next)week
```
For example:
```
curl http://example.com/wueins/today
curl http://example.com/wueins/tomorrow
```
We can even get the meals of last/next N weeks:
```
GET /<canteen_name>/(last|next)[N]weeks
```
For example:
```
curl http://example.com/wueins/last3weeks
curl http://example.com/wueins/next2weeks
```
The following api can get the meals of a canteen by using keywords "**from**" and "**to**" to set range of the dates:
```
GET /<canteen_name>/from[DATE_START]to[DATE_END]
```
For example:
```
curl http://example.com/wueins/from20181101to20181103
```
Further more, we can use square brackets([ and ]) to set a relative range of dates. The following api gets the meals from **the date of M days relative to today** to **the date of N days relative to day**, in which M and N are _**signed integer**_:
```
GET /<canteen_name>/[M, N]
```
For example:
```
# from 2 day before today to 3 days after today
curl http://example.com/wueins/[-2,3]
# from tomorrow to 3 days after today
curl http://example.com/wueins/[1,3]
# from today to tomorrow
curl http://example.com/wueins/[0,1]
```
