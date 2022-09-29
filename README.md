# Course-Scraper

A python script that scrapes course data from saved html files. Code is hacky and ugly, but as far as I know it works for the html files of https://handbook.uts.edu.au/courses/c09066.html https://handbook.uts.edu.au/courses/c09067.html https://handbook.uts.edu.au/courses/c10066.html https://handbook.uts.edu.au/courses/c10408.html. Repository also contains the data scraped from these courses.

## Output format

The first key/value is "subjects", in the form 
```
"subjects": {
  "<subject number>": {
    "name": "<subject name>",
    "credit points": "<number of credit points>"
  }
}
```
An example is 
```
"subjects": {
    "16263": {
      "name": "Design Team Management",
      "credit points": 6
    },
    "16314": {
      "name": "Construction Technology 3",
      "credit points": 6
    },
    "CBK91895": {
      "name": "Civil and Environmental Engineering choice",
      "credit points": 6
    },
    "CBK91781": {
      "name": "Electrical Engineering options",
      "credit points": 24
    }
}
``` 
Note that electives are not listed out.

The next keys/values are each individual course. The format is 
```
"<course name>" : {
  "<major name>": {
    "<year>" : {
      "<session name>" : [
        <subjects/data>
      ]
    }
  }
}
```

An example of this with a single subject is given
```
"C09066v6 Bachelor of Engineering (Honours)": {
    "Biomedical Engineering major, Autumn commencing": {
      "Year 1": {
        "Autumn session": [
          "33130",
          "48230",
          "68037",
          "Select 6 credit points from the following:",
          "48510",
          "41099"
        ],
        "Spring session": [
          "33230",
          "48023",
          "41160",
          "91400"
        ]
      },
      "Year 2": {
        "Autumn session": [
          "48240",
          "Select 6 credit points from the following:",
          "31250",
          "31061",
          "Select 6 credit points from the following:",
          "91148",
          "65111",
          "41162",
          "41035"
        ],
        "Spring session": [
          "Select 12 credit points of options ",
          "91161",
          "48250"
        ]
      },
      "Year 3": {
        "Autumn session": [
          "48260",
          "41163",
          "Select 6 credit points of options ",
          "41161"
        ],
        "Spring session": [
          "91705",
          "41028",
          "Select 6 credit points from the following:",
          "48270",
          "48210",
          "Select 6 credit points from the following:",
          "26101",
          "42026",
          "Select 6 credit points of options "
        ]
      },
      "Year 4": {
        "Autumn session": [
          "41055",
          "41029",
          "43021",
          "Select 6 credit points from the following:",
          "49261",
          "42001"
        ],
        "Spring session": [
          "41030",
          "43022",
          "Select 6 credit points from the following:",
          "42722",
          "42724"
        ]
      }
    }
}
```
Note that the text saying "Select X credit points from the following is still there". The subjects below are the options to select credit points from. Also note that only the subject number is given, the name is given in the "subjects" portion of the data.
